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
from ui_nmea import Ui_nmea
# create the dialog for zoom to point


class nmea_Dialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_nmea()
        self.ui.setupUi(self)
