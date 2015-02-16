from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from NewBrowser_ui import Ui_MainWindow
import qdarkstyle

class Operation(QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self,parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.calldata)
	
	def calldata(self):
		qrstr = self.ui.lineEdit.text()
		self.ui.webView.setUrl(QtCore.QUrl('http://en.wikipedia.org/w/index.php?search='+qrstr+''))
		
if __name__=='__main__':
	
	import sys
	app = QApplication(sys.argv)
	window = Operation()
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
	window.show()
	sys.exit(app.exec_())
