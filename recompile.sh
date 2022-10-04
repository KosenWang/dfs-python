rm -rf __pycache__
rm dfs_pb2_grpc.py
rm dfs_pb2.py
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./dfs.proto
