from idlelib.outwin import OutputWindow

import Output as op
import sys


class Fox:

    def __init__(self, x):
        self.x = x

    def did(self, y):
        t = y


data = Fox(11)
print(data.x)

if __name__ == "__main__":
    app = op.QtWidgets.QApplication(sys.argv)
    OutputWindow = op.QtWidgets.QMainWindow()
    ui = op.Ui_OutputWindow(OutputWindow)
    ui.__init__(OutputWindow)
    OutputWindow.show()
    sys.exit(app.exec_())
