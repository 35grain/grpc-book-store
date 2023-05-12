import client
import server
import threading

def main():
    # Prepare data
    num_nodes = int(input("Enter number of participating nodes: "))
    print("Enter participating node addresses (in the format ip:port):")
    nodes = {}
    for i in range(1, num_nodes + 1):
        address = input(f"Node {i} address: ")
        nodes[i] = address
    print("Which of the nodes are you (select number)?")
    for id, addr in nodes.items():
        print(f"({id}) {addr}")
    node_id = int(input("I am: "))
    
    # Start server and client threads
    quit_event = threading.Event()
    server_thread = threading.Thread(target=server.serve, args=(nodes, node_id, quit_event))
    client_thread = threading.Thread(target=client.terminal, args=(nodes, node_id, quit_event))
    server_thread.start()
    client_thread.start()
    
    # Wait for threads to finish
    server_thread.join()
    client_thread.join()
    
if __name__ == "__main__":
    main()