from threading import Thread

from clock import Clock
from observable import Subscriber
from logger import Logger


class CPU:
    def __init__(self, core_num: int) -> None:
          # number of cores
        self.cores = [None for _ in range(core_num)]
        self.logger = Logger()

    def is_available(self) -> bool:
        return None in self.cores

    def is_empty(self) -> bool:
        for core in self.cores:
            if core is not None:
                return False
        return True

    def start_process(self, process) -> None:
        for i in range(len(self.cores)):
            if self.cores[i] is None:
                self.cores[i] = process
                return
            # run thread when thread.start() is called
    def run(self, current_time: int) -> None:
        for core_id, process in enumerate(self.cores):
            if process is not None:
                process.execute(current_time)
                if process.is_done():
                    self.logger.log_process_finish(current_time + 100, process)
                    self._release(core_id)

    def _release(self, core_id: int) -> None:
        self.cores[core_id] = None


class Scheduler(Subscriber, Thread):
    def __init__(
        self, clock: Clock, name: str, core_num: int, all_processes=[]
    ) -> None:
      # create process threads
        Thread.__init__(self)
        Subscriber.__init__(self, name)
        clock.register(self)
        self._clock = clock
        self.logger = Logger()

        self.cpu = CPU(core_num)
        self.all_processes = all_processes
        self.processes_queue = []
            
    def update(self, message):
        if not self.all_processes and not self.processes_queue and self.cpu.is_empty():
            self._clock.stop()

        self.update_processes_queue(message)

        if self.processes_queue and self.cpu.is_available():
            process = self.processes_queue.pop(0)
            self.logger.log_process_start(message, process)
            self.cpu.start_process(process)

        self.cpu.run(message)

    def update_processes_queue(self, time: int) -> None:
        ready_processes = [p for p in self.all_processes if p.arrive_time == time]
        self.processes_queue += ready_processes
        for process in ready_processes:
            self.all_processes.remove(process)