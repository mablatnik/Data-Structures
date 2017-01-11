# python3

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    @property
    def is_full(self):
        if len(self.finish_time) == self.size:
            return True
        return False

    @property
    def is_empty(self):
        if not len(self.finish_time):
            return True
        return False

    @property
    def last_element(self):
        return self.finish_time[-1]

    def clear_processed(self, request):
        while self.finish_time:
            if self.finish_time[0] <= request.arrival_time:
                self.finish_time.pop(0)
            else:
                break

    def process(self, request):
        self.clear_processed(request)

        if self.is_full:
            return Response(True, -1)

        if self.is_empty:
            self.finish_time = [request.arrival_time + request.process_time]
            return Response(False, request.arrival_time)

        response  = Response(False, self.last_element)
        self.finish_time.append(self.last_element + request.process_time)
        return response


class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)
