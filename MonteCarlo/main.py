import math
import numpy
from PyQt5 import QtWidgets
from gui import Ui_MainWindow
from plot import Ui_Plot
import sys
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from Logic import MonteCarlo


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.plot_btn.clicked.connect(self.open_plot)
        self.ui.square_btn.clicked.connect(self.show_square)
        self.dialog = 0

    def open_plot(self):
        self.dialog = PlotWindow(-2, 8.3, original_func, int(self.ui.num_count.text()) or 100)
        self.dialog.show()

    def show_square(self):
        mont = MonteCarlo(-2, 8.3, original_func, int(self.ui.num_count.text()) or 100)
        monts = [MonteCarlo(-2, 8.3, original_func, int(self.ui.num_count.text()) or 100) for i in
                 range(int(self.ui.iterations_count.text()))]
        values = []
        for i in monts:
            i.generate_points()
            values.append(i.square())
        square = sum(values) / len(values)
        self.ui.square.setText(f'Sрасч = {square}')
        self.ui.error.setText(str(round(abs((square-38.7925786761)/38.7925786761)*100, 3)) + '%')


class PlotWindow(QtWidgets.QMainWindow):
    def __init__(self, a, b, func, num_count):
        super(PlotWindow, self).__init__()
        self.ui = Ui_Plot()
        self.ui.setupUi(self)
        mont = MonteCarlo(a, b, func, num_count)
        mont.generate_points()

        out_x = []
        out_y = []
        in_x = []
        in_y = []
        for x, y in mont.in_zone:
            in_x.append(x)
            in_y.append(y)
        for x, y in mont.out_zone:
            out_x.append(x)
            out_y.append(y)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        self.graphWidget.showGrid(x=True, y=True)

        self.graphWidget.plot(out_x, out_y,
                              pen=None,
                              name="BEP",
                              symbol='o',
                              symbolPen=pg.mkPen(color=(255, 0, 0), width=0),
                              symbolBrush=pg.mkBrush(255, 0, 0),
                              symbolSize=7)
        self.graphWidget.plot(in_x, in_y,
                              pen=None,
                              name="BEP",
                              symbol='o',
                              symbolPen=pg.mkPen(color=(0, 255, 0), width=0),
                              symbolBrush=pg.mkBrush(0, 255, 0),
                              symbolSize=7)

        x = numpy.arange(-5, 10, 0.1)
        y = [original_func(i) for i in x]
        s = mont.square()
        a = 0
        self.graphWidget.plot(x, y)


def original_func(x):
    return 2.5 + 7.2 * math.sin(x)


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
