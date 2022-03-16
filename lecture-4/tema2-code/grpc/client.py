import grpc
import Service_pb2_grpc
import Service_pb2

channel = grpc.insecure_channel('localhost:50051')
stub = Service_pb2_grpc.CalculatorStub(channel)
response = stub.isEven(Service_pb2.Question(value=5))
print("isEvent(5) :" + str(response.value))
response = stub.isEven(Service_pb2.Question(value=10))
print("isEvent(10) :" + str(response.value))
