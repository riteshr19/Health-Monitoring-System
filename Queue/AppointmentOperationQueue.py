from package.doctor import Doctor
from package.appointment import Appointment

class DoctorOperationQueue:
    def __init__(self):
        self.queue = queue.Queue()
        self.results = {}

    def enqueue(self, doctor_id, operation_type):
        self.queue.put((doctor_id, operation_type))

    def worker(self):
        while True:
            try:
                doctor_id, operation_type = self.queue.get(timeout=1)
                doctor = Doctor()
                if operation_type == 'get':
                    result = doctor.get(doctor_id)
                elif operation_type == 'delete':
                    result = doctor.delete(doctor_id)
                elif operation_type == 'put':
                    result = doctor.put(doctor_id)
                else:
                    result = 'Invalid operation type'

                self.results[(doctor_id, operation_type)] = result
                self.queue.task_done()
            except queue.Empty:
                break

class AppointmentOperationQueue:
    def __init__(self):
        self.queue = queue.Queue()
        self.results = {}

    def enqueue(self, appointment_id, operation_type):
        self.queue.put((appointment_id, operation_type))

    def worker(self):
        while True:
            try:
                appointment_id, operation_type = self.queue.get(timeout=1)
                appointment = Appointment()
                if operation_type == 'get':
                    result = appointment.get(appointment_id)
                elif operation_type == 'delete':
                    result = appointment.delete(appointment_id)
                elif operation_type == 'put':
                    result = appointment.put(appointment_id)
                else:
                    result = 'Invalid operation type'

                self.results[(appointment_id, operation_type)] = result
                self.queue.task_done()
            except queue.Empty:
                break