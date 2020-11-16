import time
import math
import random


class SMO:
    def __init__(self, progress_bar, max_value, output):
        self.channels = []
        self.finished_requests = []
        self.progress_bar = progress_bar
        self.max_value = max_value
        self.output = output

    def return_remaining(self):
        for i in self.channels:
            if i.current_request:
                self.finished_requests.append(i.current_request)
                i.label.setText('Free')
                i.label.setStyleSheet('color: lime;')
                self.output.append(f'{i.name} - is free')

    def find_free_channel(self):
        for channel in self.channels:
            if channel.is_free():
                if channel.current_request:
                    self.finished_requests.append(channel.return_request())
                    channel.label.setText('Free')
                    channel.label.setStyleSheet('color: lime;')
                    self.output.append(f'{channel.name} - is free')

    def get_dined_count(self):
        return len([i for i in self.finished_requests if i.is_denied])

    def add_channel(self, channel):
        self.channels.append(channel)

    def execute_request(self, request):
        dine_count = 0
        self.find_free_channel()
        self.output.append(f'New request is gone')
        for channel in self.channels:
            if channel.is_free():
                if channel.current_request:
                    self.finished_requests.append(channel.return_request())
                    channel.start_processing(request, self.output)
                    self.output.append(f'{channel.name} is busy')
                    break
                else:
                    channel.start_processing(request, self.output)
                    self.output.append(f'{channel.name} is busy')
                    break
            else:
                dine_count += 1
        if dine_count == len(self.channels):
            request.is_denied = True
            self.finished_requests.append(request)
        self.progress_bar.setValue(int(len(self.finished_requests)/self.max_value*100))


class Channel:
    def __init__(self, name, label, processing_intensity):
        self.name = name
        self.label = label
        self.time_of_receipt = 0
        self.time_of_processing = 0
        self.current_request = None
        self.processing_intensity = processing_intensity

    def start_processing(self, request, output):
        self.time_of_receipt = time.time()
        self.current_request = request
        self.time_of_processing = self.generate_processing_time()
        self.label.setText('Busy')
        self.label.setStyleSheet('color: red;')
        output.append(f'{self.name} - is free')

    def generate_processing_time(self):
        return -(1 / self.processing_intensity) * math.log10(random.random())

    def is_free(self):
        return ((time.time() - self.time_of_receipt)*10 > self.time_of_processing) or self.current_request == None

    def return_request(self):
        request = self.current_request
        self.current_request = None
        return request


class Request:
    def __init__(self):
        self.is_denied = False
