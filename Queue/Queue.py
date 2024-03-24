import queue
import threading
from package.patient import Patient

class PatientOperationQueue:
    def __init__(self):
        self.queue = queue.Queue()
        self.results = {}

    def enqueue(self, patient_id, operation_type):
        self.queue.put((patient_id, operation_type))

    def worker(self):
        while True:
            try:
                patient_id, operation_type = self.queue.get(timeout=1)
                patient = Patient()
                if operation_type == 'get':
                    result = patient.get(patient_id)
                elif operation_type == 'delete':
                    result = patient.delete(patient_id)
                elif operation_type == 'put':
                    result = patient.put(patient_id)
                else:
                    result = 'Invalid operation type'

                self.results[(patient_id, operation_type)] = result
                self.queue.task_done()
            except queue.Empty:
                break

    def process_queue(self):
        num_threads = min(10, self.queue.qsize())
        threads = []
        for _ in range(num_threads):
            thread = threading.Thread(target=self.worker)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    def get_result(self, patient_id, operation_type):
        return self.results.get((patient_id, operation_type))

# Usage example
# queue = PatientOperationQueue()
# queue.enqueue(1, "get")
# queue.enqueue(2, "delete")
# queue.process_queue()
# print(queue.get_result(1, "get"))
# print(queue.get_result(2, "delete"))