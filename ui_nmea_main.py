# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_nmea_main.ui'
#
# Created: Thu May 30 15:02:33 2013
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_nmea_main(object):
    def setupUi(self, nmea_main):
        nmea_main.setObjectName(_fromUtf8("nmea_main"))
        nmea_main.setEnabled(True)
        nmea_main.resize(495, 76)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(nmea_main.sizePolicy().hasHeightForWidth())
        nmea_main.setSizePolicy(sizePolicy)
        nmea_main.setMaximumSize(QtCore.QSize(600, 150))
        nmea_main.setMouseTracking(False)
        nmea_main.setAutoFillBackground(False)
        self.verticalLayout = QtGui.QVBoxLayout(nmea_main)
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ButOpenNmea = QtGui.QPushButton(nmea_main)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButOpenNmea.sizePolicy().hasHeightForWidth())
        self.ButOpenNmea.setSizePolicy(sizePolicy)
        self.ButOpenNmea.setObjectName(_fromUtf8("ButOpenNmea"))
        self.gridLayout.addWidget(self.ButOpenNmea, 1, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(nmea_main)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 3, 1, 1)
        self.settBut = QtGui.QPushButton(nmea_main)
        self.settBut.setObjectName(_fromUtf8("settBut"))
        self.gridLayout.addWidget(self.settBut, 1, 2, 1, 1)
        self.lineEdit = QtGui.QLineEdit(nmea_main)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 3)
        self.addBut = QtGui.QPushButton(nmea_main)
        self.addBut.setObjectName(_fromUtf8("addBut"))
        self.gridLayout.addWidget(self.addBut, 1, 1, 1, 1)
        self.ButExit = QtGui.QPushButton(nmea_main)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButExit.sizePolicy().hasHeightForWidth())
        self.ButExit.setSizePolicy(sizePolicy)
        self.ButExit.setObjectName(_fromUtf8("ButExit"))
        self.gridLayout.addWidget(self.ButExit, 1, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(nmea_main)
        QtCore.QMetaObject.connectSlotsByName(nmea_main)

    def retranslateUi(self, nmea_main):
        nmea_main.setWindowTitle(_translate("nmea_main", "nmea_main", None))
        self.ButOpenNmea.setText(_translate("nmea_main", "open NMEA", None))
        self.pushButton.setText(_translate("nmea_main", "search", None))
        self.settBut.setText(_translate("nmea_main", "Settings", None))
        self.addBut.setText(_translate("nmea_main", "addLayer", None))
        self.ButExit.setText(_translate("nmea_main", "cancel", None))

