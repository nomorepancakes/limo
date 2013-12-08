# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lite.ui'
#
# Created: Sun Dec 08 16:35:18 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(190, 145)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(190, 145))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/root/lite.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.askl = QtGui.QLabel(self.centralwidget)
        self.askl.setGeometry(QtCore.QRect(10, 20, 46, 21))
        self.askl.setObjectName(_fromUtf8("askl"))
        self.bidl = QtGui.QLabel(self.centralwidget)
        self.bidl.setGeometry(QtCore.QRect(10, 60, 46, 21))
        self.bidl.setObjectName(_fromUtf8("bidl"))
        self.ask = QtGui.QLabel(self.centralwidget)
        self.ask.setGeometry(QtCore.QRect(50, 12, 191, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans Semibold"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ask.setFont(font)
        self.ask.setObjectName(_fromUtf8("ask"))
        self.bid = QtGui.QLabel(self.centralwidget)
        self.bid.setGeometry(QtCore.QRect(50, 50, 191, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans Semibold"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bid.setFont(font)
        self.bid.setText(_fromUtf8(""))
        self.bid.setObjectName(_fromUtf8("bid"))
        self.low = QtGui.QLineEdit(self.centralwidget)
        self.low.setGeometry(QtCore.QRect(20, 100, 41, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans"))
        font.setPointSize(10)
        self.low.setFont(font)
        self.low.setInputMask(_fromUtf8(""))
        self.low.setMaxLength(2)
        self.low.setObjectName(_fromUtf8("low"))
        self.high = QtGui.QLineEdit(self.centralwidget)
        self.high.setGeometry(QtCore.QRect(130, 100, 41, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans"))
        font.setPointSize(10)
        self.high.setFont(font)
        self.high.setMaxLength(3)
        self.high.setFrame(True)
        self.high.setObjectName(_fromUtf8("high"))
        self.alertl = QtGui.QLabel(self.centralwidget)
        self.alertl.setGeometry(QtCore.QRect(70, 101, 46, 20))
        self.alertl.setAlignment(QtCore.Qt.AlignCenter)
        self.alertl.setObjectName(_fromUtf8("alertl"))
        self.last = QtGui.QLabel(self.centralwidget)
        self.last.setGeometry(QtCore.QRect(30, 120, 151, 20))
        self.last.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.last.setObjectName(_fromUtf8("last"))
        self.refresh = QtGui.QPushButton(self.centralwidget)
        self.refresh.setGeometry(QtCore.QRect(0, 120, 31, 23))
        self.refresh.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/root/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh.setIcon(icon1)
        self.refresh.setIconSize(QtCore.QSize(35, 35))
        self.refresh.setFlat(True)
        self.refresh.setObjectName(_fromUtf8("refresh"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.refresh, self.high)
        MainWindow.setTabOrder(self.high, self.low)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "LiteCoin", None))
        self.askl.setText(_translate("MainWindow", "Ask:", None))
        self.bidl.setText(_translate("MainWindow", "Bid:", None))
        self.ask.setText(_translate("MainWindow", "Loading...", None))
        self.low.setText(_translate("MainWindow", "15", None))
        self.high.setText(_translate("MainWindow", "30", None))
        self.alertl.setText(_translate("MainWindow", "Alert", None))
        self.last.setText(_translate("MainWindow", "Last Update: ", None))

import hello_rc
