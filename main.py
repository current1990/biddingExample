from __future__ import print_function

import logging

import grpc

import third.biddingAPI.generated.python.apis.get_url_pb2 as req_pb
import third.biddingAPI.generated.python.service.service_pb2_grpc as service_pb2_grpc

def run():
    print("Will try to ping world ...")
    with grpc.insecure_channel("localhost:9876") as channel:
        stub = service_pb2_grpc.BiddingStub(channel)
        response = stub.Ping(req_pb.PingReq(ping="ping"))
    print("Ping client received: " + response.pong)


if __name__ == "__main__":
    logging.basicConfig()
    run()