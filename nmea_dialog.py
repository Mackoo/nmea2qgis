# -*- coding: utf-8 -*-
"""
/***************************************************************************
 nmea_mainDialog
                                 A QGIS plugin
 load nmea file to qgis
                             -------------------
        begin                : 2013-05-11
        copyright            : (C) 2013 by Maciej Olszewski
        email                : mackoo@opoczta.pl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_nmea_main import Ui_nmea_main
from ui_nmea import Ui_nmea
from ui_settings import Ui_Dialog
import PyQt4.Qwt5 as Qwt
# create the dialog for zoom to point


class nmea_Dialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_nmea()
        self.ui.setupUi(self)



        self.plot1 = Qwt.QwtPlot()
        self.plot2 = Qwt.QwtPlot()
        self.plot1.plotLayout().setCanvasMargin(0)
        self.plot1.plotLayout().setAlignCanvasToScales(True)
        self.plot2.plotLayout().setCanvasMargin(0)
        self.plot2.plotLayout().setAlignCanvasToScales(True)
        self.ui.verticalLayout_4.addWidget(self.plot1)
        self.ui.verticalLayout_4.addWidget(self.plot2)


##
##
##        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
####        sizePolicy.setHorizontalStretch(0)
####        sizePolicy.setVerticalStretch(0)
####        sizePolicy.setHeightForWidth(self.plot.sizePolicy().hasHeightForWidth())
##        self.plot.setSizePolicy(sizePolicy)
##        self.plot.setMinimumSize(QtCore.QSize(0,0))
##        self.plot.setAutoFillBackground(False)
##        #Decoration
##
##        self.plot.plotLayout().setAlignCanvasToScales(True)
##        zoomer = Qwt.QwtPlotZoomer(Qwt.QwtPlot.xBottom, Qwt.QwtPlot.yLeft, Qwt.QwtPicker.DragSelection, Qwt.QwtPicker.AlwaysOff, self.plot.canvas())
##        zoomer.setRubberBandPen(QtGui.QPen(QtCore.Qt.blue))




##        self.plot.setCanvasBackground(QtCore.Qt.white)

class nmea_mainDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_nmea_main()
        self.ui.setupUi(self)

class nmea_settDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        #QtCore.QObject.connect(self.ui.utcCheck, SIGNAL('stateChanged(int)'),nmea_Dialog.ui.utcCheck.setCheckState(True))

        self.ui.setupUi(self)