# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_nmea.ui'
#
# Created: Fri Sep 20 12:46:07 2013
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

class Ui_nmea(object):
    def setupUi(self, nmea):
        nmea.setObjectName(_fromUtf8("nmea"))
        nmea.resize(777, 686)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(nmea.sizePolicy().hasHeightForWidth())
        nmea.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(nmea)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.addBut = QtGui.QPushButton(nmea)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addBut.sizePolicy().hasHeightForWidth())
        self.addBut.setSizePolicy(sizePolicy)
        self.addBut.setIconSize(QtCore.QSize(40, 16))
        self.addBut.setObjectName(_fromUtf8("addBut"))
        self.verticalLayout.addWidget(self.addBut)
        self.tabWidget = QtGui.QTabWidget(nmea)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.nmeaBrowser = QtGui.QTextBrowser(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nmeaBrowser.sizePolicy().hasHeightForWidth())
        self.nmeaBrowser.setSizePolicy(sizePolicy)
        self.nmeaBrowser.setMinimumSize(QtCore.QSize(650, 0))
        self.nmeaBrowser.setObjectName(_fromUtf8("nmeaBrowser"))
        self.horizontalLayout.addWidget(self.nmeaBrowser)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        spacerItem = QtGui.QSpacerItem(30, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.sentCombo = QtGui.QComboBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sentCombo.sizePolicy().hasHeightForWidth())
        self.sentCombo.setSizePolicy(sizePolicy)
        self.sentCombo.setObjectName(_fromUtf8("sentCombo"))
        self.sentCombo.addItem(_fromUtf8(""))
        self.sentCombo.addItem(_fromUtf8(""))
        self.sentCombo.addItem(_fromUtf8(""))
        self.sentCombo.addItem(_fromUtf8(""))
        self.verticalLayout_3.addWidget(self.sentCombo)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.matplot1 = mplc(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matplot1.sizePolicy().hasHeightForWidth())
        self.matplot1.setSizePolicy(sizePolicy)
        self.matplot1.setObjectName(_fromUtf8("matplot1"))
        self.horizontalLayout_3.addWidget(self.matplot1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.mat1Combo = QtGui.QComboBox(self.tab_2)
        self.mat1Combo.setObjectName(_fromUtf8("mat1Combo"))
        self.mat1Combo.addItem(_fromUtf8(""))
        self.mat1Combo.addItem(_fromUtf8(""))
        self.mat1Combo.addItem(_fromUtf8(""))
        self.mat1Combo.addItem(_fromUtf8(""))
        self.mat1Combo.addItem(_fromUtf8(""))
        self.mat1Combo.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.mat1Combo)
        self.mat2Combo = QtGui.QComboBox(self.tab_2)
        self.mat2Combo.setObjectName(_fromUtf8("mat2Combo"))
        self.mat2Combo.addItem(_fromUtf8(""))
        self.mat2Combo.addItem(_fromUtf8(""))
        self.mat2Combo.addItem(_fromUtf8(""))
        self.mat2Combo.addItem(_fromUtf8(""))
        self.mat2Combo.addItem(_fromUtf8(""))
        self.mat2Combo.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.mat2Combo)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.widget = QtGui.QWidget(self.tab_3)
        self.widget.setGeometry(QtCore.QRect(10, 40, 731, 401))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.sqlCheck = QtGui.QCheckBox(self.widget)
        self.sqlCheck.setEnabled(True)
        self.sqlCheck.setObjectName(_fromUtf8("sqlCheck"))
        self.verticalLayout_6.addWidget(self.sqlCheck)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.utcCheck = QtGui.QCheckBox(self.widget)
        self.utcCheck.setEnabled(False)
        self.utcCheck.setObjectName(_fromUtf8("utcCheck"))
        self.horizontalLayout_9.addWidget(self.utcCheck)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.label_12 = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_9.addWidget(self.label_12)
        self.spinBox_10 = QtGui.QSpinBox(self.widget)
        self.spinBox_10.setEnabled(False)
        self.spinBox_10.setObjectName(_fromUtf8("spinBox_10"))
        self.horizontalLayout_9.addWidget(self.spinBox_10)
        self.label_13 = QtGui.QLabel(self.widget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_9.addWidget(self.label_13)
        self.spinBox_11 = QtGui.QSpinBox(self.widget)
        self.spinBox_11.setEnabled(False)
        self.spinBox_11.setMaximum(59)
        self.spinBox_11.setObjectName(_fromUtf8("spinBox_11"))
        self.horizontalLayout_9.addWidget(self.spinBox_11)
        self.label_14 = QtGui.QLabel(self.widget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_9.addWidget(self.label_14)
        self.spinBox_12 = QtGui.QSpinBox(self.widget)
        self.spinBox_12.setEnabled(False)
        self.spinBox_12.setMaximum(59)
        self.spinBox_12.setObjectName(_fromUtf8("spinBox_12"))
        self.horizontalLayout_9.addWidget(self.spinBox_12)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.label_15 = QtGui.QLabel(self.widget)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_9.addWidget(self.label_15)
        self.spinBox_13 = QtGui.QSpinBox(self.widget)
        self.spinBox_13.setEnabled(False)
        self.spinBox_13.setObjectName(_fromUtf8("spinBox_13"))
        self.horizontalLayout_9.addWidget(self.spinBox_13)
        self.label_16 = QtGui.QLabel(self.widget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_9.addWidget(self.label_16)
        self.spinBox_14 = QtGui.QSpinBox(self.widget)
        self.spinBox_14.setEnabled(False)
        self.spinBox_14.setMaximum(59)
        self.spinBox_14.setObjectName(_fromUtf8("spinBox_14"))
        self.horizontalLayout_9.addWidget(self.spinBox_14)
        self.label_17 = QtGui.QLabel(self.widget)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_9.addWidget(self.label_17)
        self.spinBox_15 = QtGui.QSpinBox(self.widget)
        self.spinBox_15.setEnabled(False)
        self.spinBox_15.setMaximum(59)
        self.spinBox_15.setObjectName(_fromUtf8("spinBox_15"))
        self.horizontalLayout_9.addWidget(self.spinBox_15)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.numsvCheck1 = QtGui.QCheckBox(self.widget)
        self.numsvCheck1.setEnabled(False)
        self.numsvCheck1.setObjectName(_fromUtf8("numsvCheck1"))
        self.horizontalLayout_10.addWidget(self.numsvCheck1)
        self.spinBox_16 = QtGui.QSpinBox(self.widget)
        self.spinBox_16.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_16.sizePolicy().hasHeightForWidth())
        self.spinBox_16.setSizePolicy(sizePolicy)
        self.spinBox_16.setObjectName(_fromUtf8("spinBox_16"))
        self.horizontalLayout_10.addWidget(self.spinBox_16)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.numsvCheck2 = QtGui.QCheckBox(self.widget)
        self.numsvCheck2.setEnabled(False)
        self.numsvCheck2.setObjectName(_fromUtf8("numsvCheck2"))
        self.horizontalLayout_10.addWidget(self.numsvCheck2)
        self.spinBox_17 = QtGui.QSpinBox(self.widget)
        self.spinBox_17.setEnabled(False)
        self.spinBox_17.setObjectName(_fromUtf8("spinBox_17"))
        self.horizontalLayout_10.addWidget(self.spinBox_17)
        self.label_18 = QtGui.QLabel(self.widget)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_10.addWidget(self.label_18)
        self.spinBox_18 = QtGui.QSpinBox(self.widget)
        self.spinBox_18.setEnabled(False)
        self.spinBox_18.setObjectName(_fromUtf8("spinBox_18"))
        self.horizontalLayout_10.addWidget(self.spinBox_18)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.hdopCheck1 = QtGui.QCheckBox(self.widget)
        self.hdopCheck1.setEnabled(False)
        self.hdopCheck1.setObjectName(_fromUtf8("hdopCheck1"))
        self.horizontalLayout_11.addWidget(self.hdopCheck1)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.widget)
        self.doubleSpinBox.setEnabled(False)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.horizontalLayout_11.addWidget(self.doubleSpinBox)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem5)
        self.hdopCheck2 = QtGui.QCheckBox(self.widget)
        self.hdopCheck2.setEnabled(False)
        self.hdopCheck2.setObjectName(_fromUtf8("hdopCheck2"))
        self.horizontalLayout_11.addWidget(self.hdopCheck2)
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_2.setEnabled(False)
        self.doubleSpinBox_2.setSingleStep(0.01)
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.horizontalLayout_11.addWidget(self.doubleSpinBox_2)
        self.label_19 = QtGui.QLabel(self.widget)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_11.addWidget(self.label_19)
        self.doubleSpinBox_3 = QtGui.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_3.setEnabled(False)
        self.doubleSpinBox_3.setSingleStep(0.01)
        self.doubleSpinBox_3.setObjectName(_fromUtf8("doubleSpinBox_3"))
        self.horizontalLayout_11.addWidget(self.doubleSpinBox_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.mslCheck1 = QtGui.QCheckBox(self.widget)
        self.mslCheck1.setEnabled(False)
        self.mslCheck1.setObjectName(_fromUtf8("mslCheck1"))
        self.horizontalLayout_12.addWidget(self.mslCheck1)
        self.doubleSpinBox_4 = QtGui.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_4.setEnabled(False)
        self.doubleSpinBox_4.setDecimals(1)
        self.doubleSpinBox_4.setObjectName(_fromUtf8("doubleSpinBox_4"))
        self.horizontalLayout_12.addWidget(self.doubleSpinBox_4)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem6)
        self.mslCheck2 = QtGui.QCheckBox(self.widget)
        self.mslCheck2.setEnabled(False)
        self.mslCheck2.setObjectName(_fromUtf8("mslCheck2"))
        self.horizontalLayout_12.addWidget(self.mslCheck2)
        self.doubleSpinBox_5 = QtGui.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_5.setEnabled(False)
        self.doubleSpinBox_5.setDecimals(1)
        self.doubleSpinBox_5.setObjectName(_fromUtf8("doubleSpinBox_5"))
        self.horizontalLayout_12.addWidget(self.doubleSpinBox_5)
        self.label_20 = QtGui.QLabel(self.widget)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_12.addWidget(self.label_20)
        self.doubleSpinBox_6 = QtGui.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_6.setEnabled(False)
        self.doubleSpinBox_6.setDecimals(1)
        self.doubleSpinBox_6.setObjectName(_fromUtf8("doubleSpinBox_6"))
        self.horizontalLayout_12.addWidget(self.doubleSpinBox_6)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.geoidCheck1 = QtGui.QCheckBox(self.widget)
        self.geoidCheck1.setEnabled(False)
        self.geoidCheck1.setObjectName(_fromUtf8("geoidCheck1"))
        self.horizontalLayout_13.addWidget(self.geoidCheck1)
        self.doubleSpinBox_7 = QtGui.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_7.setEnabled(False)
        self.doubleSpinBox_7.setDecimals(1)
        self.doubleSpinBox_7.setObjectName(_fromUtf8("doubleSpinBox_7"))
        self.horizontalLayout_13.addWidget(self.doubleSpinBox_7)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem7)
        self.geoidCheck2 = QtGui.QCheckBox(self.widget)
        self.geoidCheck2.setEnabled(False)
        self.geoidCheck2.setObjectName(_fromUtf8("geoidCheck2"))
        self.horizontalLayout_13.addWidget(self.geoidCheck2)
        self.doubleSpinBox_8 = QtGui.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_8.setEnabled(False)
        self.doubleSpinBox_8.setDecimals(1)
        self.doubleSpinBox_8.setObjectName(_fromUtf8("doubleSpinBox_8"))
        self.horizontalLayout_13.addWidget(self.doubleSpinBox_8)
        self.label_21 = QtGui.QLabel(self.widget)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_13.addWidget(self.label_21)
        self.doubleSpinBox_9 = QtGui.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_9.setEnabled(False)
        self.doubleSpinBox_9.setDecimals(1)
        self.doubleSpinBox_9.setObjectName(_fromUtf8("doubleSpinBox_9"))
        self.horizontalLayout_13.addWidget(self.doubleSpinBox_9)
        self.verticalLayout_6.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.speedCheck1 = QtGui.QCheckBox(self.widget)
        self.speedCheck1.setEnabled(False)
        self.speedCheck1.setObjectName(_fromUtf8("speedCheck1"))
        self.horizontalLayout_14.addWidget(self.speedCheck1)
        self.doubleSpinBox_10 = QtGui.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_10.setEnabled(False)
        self.doubleSpinBox_10.setObjectName(_fromUtf8("doubleSpinBox_10"))
        self.horizontalLayout_14.addWidget(self.doubleSpinBox_10)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem8)
        self.speedCheck2 = QtGui.QCheckBox(self.widget)
        self.speedCheck2.setEnabled(False)
        self.speedCheck2.setObjectName(_fromUtf8("speedCheck2"))
        self.horizontalLayout_14.addWidget(self.speedCheck2)
        self.doubleSpinBox_11 = QtGui.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_11.setEnabled(False)
        self.doubleSpinBox_11.setObjectName(_fromUtf8("doubleSpinBox_11"))
        self.horizontalLayout_14.addWidget(self.doubleSpinBox_11)
        self.label_22 = QtGui.QLabel(self.widget)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_14.addWidget(self.label_22)
        self.doubleSpinBox_12 = QtGui.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_12.setEnabled(False)
        self.doubleSpinBox_12.setObjectName(_fromUtf8("doubleSpinBox_12"))
        self.horizontalLayout_14.addWidget(self.doubleSpinBox_12)
        self.verticalLayout_6.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.datastatusCheck1 = QtGui.QCheckBox(self.widget)
        self.datastatusCheck1.setEnabled(False)
        self.datastatusCheck1.setObjectName(_fromUtf8("datastatusCheck1"))
        self.horizontalLayout_15.addWidget(self.datastatusCheck1)
        self.spinBox_19 = QtGui.QSpinBox(self.widget)
        self.spinBox_19.setEnabled(False)
        self.spinBox_19.setMaximum(1)
        self.spinBox_19.setObjectName(_fromUtf8("spinBox_19"))
        self.horizontalLayout_15.addWidget(self.spinBox_19)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem9)
        self.fixstatusCheck1 = QtGui.QCheckBox(self.widget)
        self.fixstatusCheck1.setEnabled(False)
        self.fixstatusCheck1.setObjectName(_fromUtf8("fixstatusCheck1"))
        self.horizontalLayout_15.addWidget(self.fixstatusCheck1)
        self.spinBox_20 = QtGui.QSpinBox(self.widget)
        self.spinBox_20.setEnabled(False)
        self.spinBox_20.setMaximum(1)
        self.spinBox_20.setObjectName(_fromUtf8("spinBox_20"))
        self.horizontalLayout_15.addWidget(self.spinBox_20)
        self.verticalLayout_6.addLayout(self.horizontalLayout_15)
        self.resetBut = QtGui.QPushButton(self.tab_3)
        self.resetBut.setGeometry(QtCore.QRect(20, 460, 75, 23))
        self.resetBut.setObjectName(_fromUtf8("resetBut"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(nmea)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(nmea)

    def retranslateUi(self, nmea):
        nmea.setWindowTitle(_translate("nmea", "nmea_main", None))
        self.addBut.setText(_translate("nmea", "add layer", None))
        self.label_2.setText(_translate("nmea", "Sentences:", None))
        self.sentCombo.setItemText(0, _translate("nmea", "ALL", None))
        self.sentCombo.setItemText(1, _translate("nmea", "GGA", None))
        self.sentCombo.setItemText(2, _translate("nmea", "RMC", None))
        self.sentCombo.setItemText(3, _translate("nmea", "GLL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("nmea", "NMEA", None))
        self.mat1Combo.setItemText(0, _translate("nmea", "numSV", None))
        self.mat1Combo.setItemText(1, _translate("nmea", "hdop", None))
        self.mat1Combo.setItemText(2, _translate("nmea", "msl", None))
        self.mat1Combo.setItemText(3, _translate("nmea", "geoid", None))
        self.mat1Combo.setItemText(4, _translate("nmea", "speed", None))
        self.mat1Combo.setItemText(5, _translate("nmea", "fix", None))
        self.mat2Combo.setItemText(0, _translate("nmea", "hdop", None))
        self.mat2Combo.setItemText(1, _translate("nmea", "numSV", None))
        self.mat2Combo.setItemText(2, _translate("nmea", "msl", None))
        self.mat2Combo.setItemText(3, _translate("nmea", "geoid", None))
        self.mat2Combo.setItemText(4, _translate("nmea", "speed", None))
        self.mat2Combo.setItemText(5, _translate("nmea", "datastatus", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("nmea", "GRAPH", None))
        self.sqlCheck.setText(_translate("nmea", "Use SQL WHERE clause:", None))
        self.utcCheck.setText(_translate("nmea", "utc is between:", None))
        self.label_12.setText(_translate("nmea", "h", None))
        self.label_13.setText(_translate("nmea", "m", None))
        self.label_14.setText(_translate("nmea", "s", None))
        self.label_15.setText(_translate("nmea", "h", None))
        self.label_16.setText(_translate("nmea", "m", None))
        self.label_17.setText(_translate("nmea", "s", None))
        self.numsvCheck1.setText(_translate("nmea", "numsv equals:", None))
        self.numsvCheck2.setText(_translate("nmea", "is between:", None))
        self.label_18.setText(_translate("nmea", "and", None))
        self.hdopCheck1.setText(_translate("nmea", "hdop equals:", None))
        self.hdopCheck2.setText(_translate("nmea", "is between:", None))
        self.label_19.setText(_translate("nmea", "and", None))
        self.mslCheck1.setText(_translate("nmea", "msl equals:", None))
        self.mslCheck2.setText(_translate("nmea", "is between:", None))
        self.label_20.setText(_translate("nmea", "and", None))
        self.geoidCheck1.setText(_translate("nmea", "geoid equals:", None))
        self.geoidCheck2.setText(_translate("nmea", "is between:", None))
        self.label_21.setText(_translate("nmea", "and", None))
        self.speedCheck1.setText(_translate("nmea", "speed equals:", None))
        self.speedCheck2.setText(_translate("nmea", "is between:", None))
        self.label_22.setText(_translate("nmea", "and", None))
        self.datastatusCheck1.setText(_translate("nmea", "datastatus equals:", None))
        self.fixstatusCheck1.setText(_translate("nmea", "fixstatus equals:", None))
        self.resetBut.setText(_translate("nmea", "RESET", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("nmea", "SQL", None))

from graphs import mplc
