import threading
import time
import random
import grpc
from concurrent import futures
import books_pb2 as pb
import books_pb2_grpc as pb_grpc

class ProcessThread(threading.Thread):
    def __init__(self, nodes, process_id):
        super(ProcessThread, self).__init__()
        self.nodes = nodes
        self.process_id = process_id
        self.head = None
        self.tail = None
        self.stopped = threading.Event()
        self.books = {}  # {book_name: price, status}
        self.successor = None
        self.predecessor = None
        self.update_queue = [] # [(book_name, price, time)]
        self.timeout = 0  # in seconds
        
    def setTimeout(self, timeout):
        self.timeout = timeout
        
    def getSuccessorAddress(self):
        if self.successor:
            node = int(self.successor.split("-")[0][-1])
            return self.nodes[node]
        else:
            return None
        
    def getPrecursorAddress(self):
        if self.predecessor:
            node = int(self.predecessor.split("-")[0][-1])
            return self.nodes[node]
        else:
            return None

    def run(self):
        while not self.stopped.wait(1):
            if self.tail != self.process_id:
                for book_name, price, queued_time in self.update_queue.copy():
                    if queued_time < time.time() - self.timeout:
                        channel = grpc.insecure_channel(self.getSuccessorAddress())
                        stub = pb_grpc.BookStoreStub(channel)
                        response = stub.UpdateBook(pb.UpdateBookRequest(book_name=book_name, price=price, process_id=self.successor))
                        if response.success:
                            self.update_queue.remove((book_name, price, queued_time))
                            
    def stop(self):
        self.stopped.set()
        
    def writeOp(self, book_name, price):
        print("Write op.", self.process_id)
        status = "dirty"
        self.books[book_name] = (price, status)
        if self.tail == self.process_id:
            return self.setClean(book_name, price)
        self.update_queue.append((book_name, price, time.time()))
        return True
    
    def setClean(self, book_name, price):
        if book_name in self.books and self.books[book_name][0] == price:
            self.books[book_name] = (self.books[book_name][0], "clean")
            if self.head != self.process_id:
                channel = grpc.insecure_channel(self.getPrecursorAddress())
                stub = pb_grpc.BookStoreStub(channel)
                response = stub.SetClean(pb.SetCleanRequest(book_name=book_name, price=price, process_id=self.predecessor))
                if not response.success:
                    return False
            return True
        else:
            return False
    
    def readOp(self, book_name):
        if book_name in self.books:
            return str(self.books[book_name][0]) + " EUR"
        else:
            return False
        
    def listBooks(self):
        books = []
        for i, (book_name, (price, status)) in enumerate(self.books.items()):
            books.append(str(i + 1) + ") " +  book_name + " = " + str(price) + " EUR")
        return books
    
    def dataStatus(self):
        statuses = []
        for i, (book_name, (price, status)) in enumerate(self.books.items()):
            statuses.append(str(i + 1) + ") " + book_name + " - " + status)
        return statuses

class BookStoreServicer(pb_grpc.BookStoreServicer):
    def __init__(self, nodes, node_id):
        self.nodes = nodes
        self.node_id = node_id
        self.processes = {}  # {process_id: process_thread}
        self.replication_chain = []
        self.timeout = 60  # in seconds
        
    def getHeadAddress(self):
        if self.replication_chain:
            node = int(self.replication_chain[0].split("-")[0][-1])
            return self.nodes[node]
        else:
            return None

    def CreateStorePS(self, request, context):
        node_id = self.node_id
        num_processes = request.num_processes

        process_ids = []
        for i in range(1, num_processes + 1):
            process_id = f"Node{node_id}-PS{i}"
            process_thread = ProcessThread(self.nodes, process_id)
            process_thread.start()
            self.processes[process_id] = process_thread
            process_ids.append(process_id)

        return pb.CreateStorePSResponse(process_ids=process_ids)

    def CreateChain(self, request, context):
        if len(self.processes) == 0:
            return pb.CreateChainResponse(success=False, message="Processes not created yet! Use `Local-store-ps`.")
        
        if self.replication_chain:
            return pb.CreateChainResponse(success=False, message="Chain already exists!")

        process_ids = list(self.processes.keys())
        for id, addr in self.nodes.items():
            if id != self.node_id:
                channel = grpc.insecure_channel(addr)
                stub = pb_grpc.BookStoreStub(channel)
                response = stub.GetProcesses(pb.GetProcessesRequest())
                if response.success:
                    process_ids.extend(response.process_ids)
                else:
                    return pb.CreateChainResponse(success=False, message=response.message)
        
        random.shuffle(process_ids)
        head = process_ids[0]
        tail = process_ids[-1]
        self.head = head
        self.tail = tail
        self.replication_chain = process_ids

        # Update successor and predecessor references
        for i, process_id in enumerate(process_ids):
            if process_id in self.processes:
                process = self.processes[process_id]
                process.head = head
                process.tail = tail
                process.successor = process_ids[(i + 1) % len(process_ids)]
                process.predecessor = process_ids[(i - 1) % len(process_ids)]
            
        success = self.propagateChain(process_ids)
        return pb.CreateChainResponse(success=success)
    
    def GetProcesses(self, request, context):
        if len(self.processes) == 0:
            return pb.GetProcessesResponse(success=False, message=f"Node {self.node_id} processes have not been created yet!")
        return pb.GetProcessesResponse(success=True, process_ids=list(self.processes.keys()))
    
    def PropagateChain(self, request, context):
        process_ids = request.chain

        if self.replication_chain:
            return pb.PropagateChainResponse(success=False, message="Chain already exists!")

        self.replication_chain = process_ids

        # Update successor and predecessor references
        for i, process_id in enumerate(process_ids):
            if process_id in self.processes:
                process = self.processes[process_id]
                process.head = process_ids[0]
                process.tail = process_ids[-1]
                process.successor = process_ids[(i + 1) % len(process_ids)]
                process.predecessor = process_ids[(i - 1) % len(process_ids)]

        return pb.PropagateChainResponse(success=True, message="Chain created.")
    
    def propagateChain(self, process_ids):
        for id, addr in self.nodes.items():
            if id != self.node_id:
                channel = grpc.insecure_channel(addr)
                stub = pb_grpc.BookStoreStub(channel)
                response = stub.PropagateChain(pb.PropagateChainRequest(chain=process_ids))
                if not response.success:
                    return False
        return True

    def ListChain(self, request, context):
        if not self.replication_chain:
            return pb.ListChainResponse(message="Chain does not exist.")

        return pb.ListChainResponse(chain=self.replication_chain)
    
    def UpdateBook(self, request, context):
        if not self.replication_chain:
            return pb.UpdateBookResponse(success=False, message="Chain does not exist!")

        book_name = request.book_name
        price = request.price
        process_id = request.process_id
        
        if process_id in self.processes:
            success = self.processes[process_id].writeOp(book_name, price)
            if success:
                return pb.UpdateBookResponse(success=success, message="Write successful.")
        else:
            return pb.UpdateBookResponse(success=False, message="Invalid process ID.")
        

    def WriteOperation(self, request, context):
        if not self.replication_chain:
            return pb.WriteOperationResponse(success=False, message="Chain does not exist!")
        
        book_name = request.book_name
        price = request.price

        # Write data to the head process
        head_process = self.replication_chain[0]
        if head_process in self.processes:
            success = self.processes[head_process].writeOp(book_name, price)
            if success:
                return pb.WriteOperationResponse(success=success, message="Write successful.")
            else:
                return pb.WriteOperationResponse(success=False, message="Write failed.")
        else:
            address = self.getHeadAddress()
            channel = grpc.insecure_channel(address)
            stub = pb_grpc.BookStoreStub(channel)
            return stub.WriteOperation(pb.WriteOperationRequest(book_name=book_name, price=price))
        
    def ReadOperation(self, request, context):
        if not self.replication_chain:
            return pb.ReadOperationResponse(success=False, message="Chain does not exist!")
        
        book_name = request.book_name

        # Read data from the head process
        head_process = self.replication_chain[0]
        if head_process in self.processes:
            price = self.processes[head_process].readOp(book_name)
            if price:
                return pb.ReadOperationResponse(success=True, price=price)
            else:
                return pb.ReadOperationResponse(success=False, message="Book not found.")
        else:
            address = self.getHeadAddress()
            channel = grpc.insecure_channel(address)
            stub = pb_grpc.BookStoreStub(channel)
            return stub.ReadOperation(pb.ReadOperationRequest(book_name=book_name))
        
    def ListBooks(self, request, context):
        if not self.replication_chain:
            return pb.ListBooksResponse(success=False, message="Chain does not exist!")
        
        head_process = self.replication_chain[0]
        if head_process in self.processes:
            books = self.processes[head_process].listBooks()
            if books:
                return pb.ListBooksResponse(success=True, books=books)
            return pb.ListBooksResponse(success=False, message="No books found.")
        else:
            address = self.getHeadAddress()
            channel = grpc.insecure_channel(address)
            stub = pb_grpc.BookStoreStub(channel)
            return stub.ListBooks(pb.ListBooksRequest())
        
    def DataStatus(self, request, context):
        if not self.replication_chain:
            return pb.DataStatusResponse(success=False, message="Chain does not exist!")
        
        head_process = self.replication_chain[0]
        if head_process in self.processes:
            statuses = self.processes[head_process].dataStatus()
            if statuses:
                return pb.DataStatusResponse(success=True, statuses=statuses)
            return pb.DataStatusResponse(success=False, message="Failed to get data status.")
        else:
            address = self.getHeadAddress()
            channel = grpc.insecure_channel(address)
            stub = pb_grpc.BookStoreStub(channel)
            return stub.DataStatus(pb.DataStatusRequest())
        
    def SetClean(self, request, context):
        if not self.replication_chain:
            return pb.SetCleanResponse(success=False, message="Chain does not exist!")
        
        book_name = request.book_name
        price = request.price
        process_id = request.process_id
        if process_id in self.processes:
            success = self.processes[process_id].setClean(book_name=book_name, price=price)
            if success:
                return pb.SetCleanResponse(success=success)
        return pb.SetCleanResponse(success=False, message="Set clean failed.")
    
    # Not clear if this is supposed to be node specific or for all nodes and whether it should be updated along the chain
    # Current implementation sets a new timeout immediately for all nodes
    def SetTimeout(self, request, context):
        if not self.replication_chain:
            return pb.SetTimeoutResponse(success=False, message="Chain does not exist! Use `Time-out` to create a chain first.")
        
        timeout = request.time
        for addr in self.nodes.values():
                channel = grpc.insecure_channel(addr)
                stub = pb_grpc.BookStoreStub(channel)
                response = stub.PropagateTimeout(pb.SetTimeoutRequest(time=timeout))
                if not response.success:
                    return pb.SetTimeoutResponse(success=False, message=response.message)
            
        return pb.SetTimeoutResponse(success=True, message=f"Timeout set to {timeout} seconds.")
    
    def PropagateTimeout(self, request, context):
        if not self.replication_chain:
            return pb.PropagateTimeoutResponse(success=False, message=f"Node {self.node_id} chain does not exist!")
        
        timeout = request.time
        for process_thread in self.processes.values():
            process_thread.setTimeout(timeout)
        
        return pb.PropagateTimeoutResponse(success=True, message=f"Timeout set to {timeout} seconds.")
    

    def stop_processes(self):
        for process_thread in self.processes.values():
            process_thread.stop()
            process_thread.join()
            
def serve(nodes, node_id, quit_event):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    book_store_servicer = BookStoreServicer(nodes, node_id)
    pb_grpc.add_BookStoreServicer_to_server(book_store_servicer, server)
    server.add_insecure_port(nodes[node_id])
    server.start()
    
    try:
        while not quit_event.is_set():
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        book_store_servicer.stop_processes()
        server.stop(0)