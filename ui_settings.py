# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_settings.ui'
#
# Created: Sun Sep 29 22:13:22 2013
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(393, 256)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.hdopCheck = QtGui.QCheckBox(Dialog)
        self.hdopCheck.setObjectName(_fromUtf8("hdopCheck"))
        self.gridLayout_2.addWidget(self.hdopCheck, 2, 0, 1, 1)
        self.svCheck = QtGui.QCheckBox(Dialog)
        self.svCheck.setChecked(True)
        self.svCheck.setObjectName(_fromUtf8("svCheck"))
        self.gridLayout_2.addWidget(self.svCheck, 1, 0, 1, 1)
        self.utcCheck = QtGui.QCheckBox(Dialog)
        self.utcCheck.setChecked(True)
        self.utcCheck.setTristate(False)
        self.utcCheck.setObjectName(_fromUtf8("utcCheck"))
        self.gridLayout_2.addWidget(self.utcCheck, 0, 0, 1, 1)
        self.fixstatusCheck = QtGui.QCheckBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fixstatusCheck.sizePolicy().hasHeightForWidth())
        self.fixstatusCheck.setSizePolicy(sizePolicy)
        self.fixstatusCheck.setObjectName(_fromUtf8("fixstatusCheck"))
        self.gridLayout_2.addWidget(self.fixstatusCheck, 0, 2, 1, 1)
        self.datastatusCheck = QtGui.QCheckBox(Dialog)
        self.datastatusCheck.setObjectName(_fromUtf8("datastatusCheck"))
        self.gridLayout_2.addWidget(self.datastatusCheck, 1, 2, 1, 1)
        self.lonCheck = QtGui.QCheckBox(Dialog)
        self.lonCheck.setObjectName(_fromUtf8("lonCheck"))
        self.gridLayout_2.addWidget(self.lonCheck, 2, 2, 1, 1)
        self.latCheck = QtGui.QCheckBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.latCheck.sizePolicy().hasHeightForWidth())
        self.latCheck.setSizePolicy(sizePolicy)
        self.latCheck.setObjectName(_fromUtf8("latCheck"))
        self.gridLayout_2.addWidget(self.latCheck, 3, 2, 1, 1)
        self.mslCheck = QtGui.QCheckBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mslCheck.sizePolicy().hasHeightForWidth())
        self.mslCheck.setSizePolicy(sizePolicy)
        self.mslCheck.setObjectName(_fromUtf8("mslCheck"))
        self.gridLayout_2.addWidget(self.mslCheck, 0, 1, 1, 1)
        self.geoidCheck = QtGui.QCheckBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.geoidCheck.sizePolicy().hasHeightForWidth())
        self.geoidCheck.setSizePolicy(sizePolicy)
        self.geoidCheck.setObjectName(_fromUtf8("geoidCheck"))
        self.gridLayout_2.addWidget(self.geoidCheck, 1, 1, 1, 1)
        self.speedCheck = QtGui.QCheckBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speedCheck.sizePolicy().hasHeightForWidth())
        self.speedCheck.setSizePolicy(sizePolicy)
        self.speedCheck.setObjectName(_fromUtf8("speedCheck"))
        self.gridLayout_2.addWidget(self.speedCheck, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.saveCheck = QtGui.QCheckBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveCheck.sizePolicy().hasHeightForWidth())
        self.saveCheck.setSizePolicy(sizePolicy)
        self.saveCheck.setObjectName(_fromUtf8("saveCheck"))
        self.horizontalLayout_2.addWidget(self.saveCheck)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.epsgSpin = QtGui.QSpinBox(Dialog)
        self.epsgSpin.setMaximum(9999)
        self.epsgSpin.setProperty("value", 2180)
        self.epsgSpin.setObjectName(_fromUtf8("epsgSpin"))
        self.horizontalLayout_2.addWidget(self.epsgSpin)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Choose NMEA sentences to add to attribute table:", None))
        self.hdopCheck.setText(_translate("Dialog", "hdop", None))
        self.svCheck.setText(_translate("Dialog", "satelittes", None))
        self.utcCheck.setText(_translate("Dialog", "utc", None))
        self.fixstatusCheck.setText(_translate("Dialog", "fix status", None))
        self.datastatusCheck.setText(_translate("Dialog", "datastatus", None))
        self.lonCheck.setText(_translate("Dialog", "longitude", None))
        self.latCheck.setText(_translate("Dialog", "latitude", None))
        self.mslCheck.setText(_translate("Dialog", "mean sea level", None))
        self.geoidCheck.setText(_translate("Dialog", "geoid", None))
        self.speedCheck.setText(_translate("Dialog", "speed", None))
        self.saveCheck.setText(_translate("Dialog", "Save on disk", None))
        self.label_2.setText(_translate("Dialog", "EPSG code for lon/lat attributes", None))

