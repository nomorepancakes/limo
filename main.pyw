import PyQt4
import sys
import urllib2
import json

from  lite import Ui_MainWindow
from time import strftime, localtime

'''Web data'''
url = "https://api.kraken.com/0/public/Ticker"
data = "pair=xltczusd"
head = {'User-Agent': 'TickerCollectorBot'}

'''App data'''
app = PyQt4.QtGui.QApplication(sys.argv)
window = PyQt4.QtGui.QMainWindow()
timer = PyQt4.QtCore.QTimer()


class Controller_Main(PyQt4.QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self, templist, humlist):
		PyQt4.QtGui.QMainWindow.__init__(self)
		self.setupUi(self)
		self.refresh.clicked.connect(self.loop)


	def loopstarter(self):
		timer.timeout.connect(self.loop)
		timer.start(20000)


	def loop(self):
		req = urllib2.Request(url, data, head)
		result = urllib2.urlopen(req)
		beauty = json.loads(result.read())
		ltcusd = beauty["result"]["XLTCZUSD"]
		timenow = strftime("%H:%M:%S", localtime())
		ask = ltcusd["a"][0]
		bid = ltcusd["b"][0]

		askint = float(ask)
		bidint = float(bid)

		self.ask.setText(ask)
		self.bid.setText(bid)
		self.last.setText("Last Update: " + timenow)


ui = Controller_Main([], [])
ui.show()
PyQt4.QtCore.QTimer.singleShot(1000, ui.loop)
ui.loopstarter()
sys.exit(app.exec_())
