# python3

import heapq

class JobQueue:
    def assign_jobs(self):
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
          next_worker = 0
          for j in range(self.num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
              next_worker = j
          self.assigned_workers[i] = next_worker
          self.start_times[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]

    class Worker(object):
      def __init__(self, id):
        self.id = id
        self.next_free_time = 0

      def __lt__(self, other):
        if self.next_free_time == other.next_free_time:
          return self.id < other.id
        return self.next_free_time < other.next_free_time

      def __gt__(self, other):
        if self.next_free_time == other.next_free_time:
          return self.id > other.id
        return self.next_free_time > other.next_free_time


    def assign_jobs_fast(self):
      self.assigned_workers = [self.Worker(i) for i in range(self.num_workers)]
      self.results = []

      heapq.heapify(self.assigned_workers)

      for job in self.jobs:
        free_thread = heapq.heappop(self.assigned_workers)

        self.results.append((free_thread.id, free_thread.next_free_time))

        free_thread.next_free_time += job
        heapq.heappush(self.assigned_workers, free_thread)


    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i, j in self.results:
          print(i, j)

    def solve(self):
        self.read_data()
        self.assign_jobs_fast()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

