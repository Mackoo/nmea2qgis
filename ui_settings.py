# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_settings.ui'
#
# Created: Wed Nov 20 12:10:19 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(399, 283)
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
        self.epsgSpin.setProperty(_fromUtf8("value"), 2180)
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
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.matCheck = QtGui.QCheckBox(Dialog)
        self.matCheck.setObjectName(_fromUtf8("matCheck"))
        self.horizontalLayout_3.addWidget(self.matCheck)
        self.qwtCheck = QtGui.QCheckBox(Dialog)
        self.qwtCheck.setObjectName(_fromUtf8("qwtCheck"))
        self.horizontalLayout_3.addWidget(self.qwtCheck)
        self.noCheck = QtGui.QCheckBox(Dialog)
        self.noCheck.setObjectName(_fromUtf8("noCheck"))
        self.horizontalLayout_3.addWidget(self.noCheck)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Choose NMEA sentences to add to attribute table:", None, QtGui.QApplication.UnicodeUTF8))
        self.hdopCheck.setText(QtGui.QApplication.translate("Dialog", "hdop", None, QtGui.QApplication.UnicodeUTF8))
        self.svCheck.setText(QtGui.QApplication.translate("Dialog", "satelittes", None, QtGui.QApplication.UnicodeUTF8))
        self.utcCheck.setText(QtGui.QApplication.translate("Dialog", "utc", None, QtGui.QApplication.UnicodeUTF8))
        self.fixstatusCheck.setText(QtGui.QApplication.translate("Dialog", "fix status", None, QtGui.QApplication.UnicodeUTF8))
        self.datastatusCheck.setText(QtGui.QApplication.translate("Dialog", "datastatus", None, QtGui.QApplication.UnicodeUTF8))
        self.lonCheck.setText(QtGui.QApplication.translate("Dialog", "longitude", None, QtGui.QApplication.UnicodeUTF8))
        self.latCheck.setText(QtGui.QApplication.translate("Dialog", "latitude", None, QtGui.QApplication.UnicodeUTF8))
        self.mslCheck.setText(QtGui.QApplication.translate("Dialog", "mean sea level", None, QtGui.QApplication.UnicodeUTF8))
        self.geoidCheck.setText(QtGui.QApplication.translate("Dialog", "geoid", None, QtGui.QApplication.UnicodeUTF8))
        self.speedCheck.setText(QtGui.QApplication.translate("Dialog", "speed", None, QtGui.QApplication.UnicodeUTF8))
        self.saveCheck.setText(QtGui.QApplication.translate("Dialog", "Save on disk", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "EPSG code for lon/lat attributes", None, QtGui.QApplication.UnicodeUTF8))
        self.matCheck.setText(QtGui.QApplication.translate("Dialog", "use matplotlib", None, QtGui.QApplication.UnicodeUTF8))
        self.qwtCheck.setText(QtGui.QApplication.translate("Dialog", "use QWT", None, QtGui.QApplication.UnicodeUTF8))
        self.noCheck.setText(QtGui.QApplication.translate("Dialog", "no plot", None, QtGui.QApplication.UnicodeUTF8))

