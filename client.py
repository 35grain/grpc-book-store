import grpc
import books_pb2 as pb
import books_pb2_grpc as pb_grpc

# Will assume the code below is self-explanatory

def createStore(stub, node_id):
    num_processes = int(input(f"Node {node_id}> Number of processes: "))
    response = stub.CreateStorePS(pb.CreateStorePSRequest(num_processes=num_processes))
    print("Created processes:", ", ".join(response.process_ids))
    
def createChain(stub, node_id):
    response = stub.CreateChain(pb.CreateChainRequest())
    if response.success:
        print(f"Node {node_id}> Chain created. List with 'List-chain'.")
    else:
        print(f"Node {node_id}> {response.message}")
        
def resetChain(stub, node_id):
    response = stub.ResetChain(pb.ResetChainRequest())
    if response.success:
        print(f"Node {node_id}> Chain reset. List with 'List-chain'.")
    else:
        print(f"Node {node_id}> {response.message}")
    
def listChain(stub, node_id):
    response = stub.ListChain(pb.ListChainRequest())
    response.chain[0] += " (HEAD)"
    response.chain[-1] += " (TAIL)"
    print(f"Node {node_id}>\nChain: {' -> '.join(response.chain)}")
    
def writeOp(stub, node_id):
    book_name = input(f"Node {node_id}> Book name: ")
    price = float(input(f"Node {node_id}> Price: "))
    response = stub.WriteOperation(pb.WriteOperationRequest(book_name=book_name, price=price))
    if response.success:
        print(f"Node {node_id}> Successful write! List with 'List-books'.")
    else:
        print(f"Node {node_id}> {response.message}")
    
def readOp(stub, node_id):
    book_name = input(f"Node {node_id}> Book name: ")
    response = stub.ReadOperation(pb.ReadOperationRequest(book_name=book_name))
    if response.success:
        print(f"Node {node_id}> Price: {response.price}")
    else:
        print(f"Node {node_id}> {response.message}")
        
def listBooks(stub, node_id):
    response = stub.ListBooks(pb.ListBooksRequest())
    if response.success:
        if len(response.books):
            for book in response.books:
                print("\t" + book)
        else:
            print(f"Node {node_id}> No books in stock.")
    else:
        print(f"Node {node_id}> {response.message}")
        
def dataStatus(stub, node_id):
    response = stub.DataStatus(pb.DataStatusRequest())
    if response.success:
        if len(response.statuses):
            for status in response.statuses:
                print("\t" + status)
        else:
            print(f"Node {node_id}> No books in stock.")
    else:
        print(f"Node {node_id}> {response.message}")
    
def removeHead(stub, node_id):
    response = stub.RemoveHead(pb.RemoveHeadRequest())
    print(f"Node {node_id}> {response.message}")
    
def restoreHead(stub, node_id):
    response = stub.RestoreHead(pb.RestoreHeadRequest())
    print(f"Node {node_id}> {response.message}")
    
def setTimeout(stub, node_id):
    timeout = int(input(f"Node {node_id}> Timeout duration: "))
    
    response = stub.SetTimeout(pb.SetTimeoutRequest(time=timeout))
    print(f"Node {node_id}> {response.message}")

def terminal(nodes, node_id, quit_event):
    address = nodes[node_id]
    with grpc.insecure_channel(address) as channel:
        stub = pb_grpc.BookStoreStub(channel)
        print(f"Node {node_id}> Enter 'Local-store-ps' to get started or 'Quit' to abort.")
        while not quit_event.is_set():
            command = input(f"Node {node_id}> ").lower()
            if command == 'local-store-ps':
                createStore(stub, node_id)
            elif command == 'create-chain':
                createChain(stub, node_id)
            elif command == 'list-chain':
                listChain(stub, node_id)
            elif command == 'write-operation':
                writeOp(stub, node_id)
            elif command == 'read-operation':
                readOp(stub, node_id)
            elif command == 'list-books':
                listBooks(stub, node_id)
            elif command == 'data-status':
                dataStatus(stub, node_id)
            elif command == 'remove-head':
                removeHead(stub, node_id)
            elif command == 'restore-head':
                restoreHead(stub, node_id)
            elif command == 'time-out':
                setTimeout(stub, node_id)
            elif command == 'reset-chain':
                resetChain(stub, node_id)
            elif command == 'quit':
                # Exit all threads
                quit_event.set()
            elif len(command):
                print(f"Node {node_id}> Unknown command. Please try again!")
            else:
                continue