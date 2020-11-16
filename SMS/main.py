import datetime
import threading
import time
from threading import Thread
import asyncio
from PyQt5 import QtWidgets, QtCore
from gui import Ui_MainWindow
import sys
from smo import SMO, Channel, Request


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.start_simulation_btn.clicked.connect(self.start)

    def start(self):
        self.simulation(self.timer_func, int(self.ui.request_count.text()))

    def simulation(self, slot, count=1000, interval=117):
        counter = 0
        self.ui.progressBar.minimum = 0
        self.ui.progressBar.maximum = int(self.ui.request_count.text())
        smo = SMO(self.ui.progressBar, int(self.ui.request_count.text()), self.ui.outer_info)
        smo.add_channel(Channel('channel_1', self.ui.state_1, 0.6 / 4))
        smo.add_channel(Channel('channel_2', self.ui.state_2, 0.6 / 4))
        smo.add_channel(Channel('channel_3', self.ui.state_3, 0.6 / 4))
        smo.add_channel(Channel('channel_4', self.ui.state_4, 0.6 / 4))
        requests = [Request() for i in range(int(self.ui.request_count.text()))]

        def handler():
            nonlocal counter
            counter += 1
            slot(smo, requests.pop(), counter, count)
            if counter >= count:
                timer.stop()
                timer.deleteLater()

        timer = QtCore.QTimer()
        timer.timeout.connect(handler)
        timer.start(interval)

    def timer_func(self, smo, request, current_count, max_count):
        smo.execute_request(request)
        if (current_count == max_count):
            smo.return_remaining()
            denied = smo.get_dined_count()
            self.ui.outer_info.append('\n'*3)
            self.ui.outer_info.append(f'Обслужено заявок: {max_count - denied}')
            self.ui.outer_info.append(f'Откланено заявок: {denied}')
            self.ui.outer_info.append(f'Вероятность обслуживания заявки: {100 - denied/max_count*100}%')
            self.ui.progressBar.setValue(100)


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
