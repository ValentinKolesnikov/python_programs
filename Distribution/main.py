from PyQt5 import QtWidgets
from gui import Ui_MainWindow
import sys
import Logic as distr


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.run_even.clicked.connect(self.form_even_sequence)
        self.ui.save_to_file.clicked.connect(self.save_to_file)
        self.ui.even_list.setReadOnly(True)

    def form_even_sequence(self):
        self.ui.even_list.clear()
        a = float(self.ui.a_even.text())
        b = float(self.ui.b_even.text())
        accuracy = float(self.ui.accurancy_even.text())
        number_count = int(self.ui.number_count_even.text())

        even = distr.Even(a, b, accuracy, number_count)
        if even.distribute():
            self.ui.even_list.setText('\n'.join(map(to_str, even.sequence)))
            self.ui.m_pract.setText(str(even.get_exp_value()))
            self.ui.m_theor.setText(str(even.exp_value_theor))
            self.ui.m_theor.setText(str(even.exp_value_theor))
            self.ui.dispertion.setText(str(even.dispersion))

        else:
            self.ui.even_list.setText(even.error_message)

    def save_to_file(self):
        file = open('output.txt', 'w')
        file.write(self.ui.even_list.toPlainText())
        file.close()

def to_str(i):
    return str(i).replace('.', ',')

app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
