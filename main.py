########################################################################################################################
##
## BY: AFONIN VLADIMIR ALEKSEEVICH
##
## PROJECT: GYROTRON CAVITY GUI
##
## V: 0.6.0
##
########################################################################################################################

from Gyrotron_Cavity_GUI import *

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
