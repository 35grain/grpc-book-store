# To start managing a book store
Make sure to generate the required client and server classes from the .proto file:

`python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. books.proto`

Then simply run `python3 bookstore.py`