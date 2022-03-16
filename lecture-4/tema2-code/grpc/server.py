import Service_pb2
import Service_pb2_grpc
import grpc
from concurrent import futures

class CalculatorServer(Service_pb2_grpc.CalculatorServicer):
    def isEven(self, request, context):
        if request.value % 2 == 0:
            return Service_pb2.Reply(value=True)
        else:
            return Service_pb2.Reply(value=False)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
Service_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServer(), server)
server.add_insecure_port('[::]:50051')
server.start()
server.wait_for_termination()

