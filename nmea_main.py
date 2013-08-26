# -*- coding: utf-8 -*-
"""
/***************************************************************************
 nmea_main
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from nmea_dialog import nmea_Dialog,nmea_mainDialog,nmea_settDialog
import datetime, time,os,string,numpy
##from pyspatialite import dbapi2 as db #Load PySpatiaLite
import sqlite3 as db



class nmea_main:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/nmea2dbqgis"
        # initialize locale
        localePath = ""
        locale = QSettings().value("locale/userLocale").toString()[0:2]
        if QFileInfo(self.plugin_dir).exists():
            localePath = self.plugin_dir + "/i18n/nmea_main_" + locale + ".qm"

        if QFileInfo(localePath).exists():
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = nmea_mainDialog()
        self.dlg2=nmea_Dialog()
        self.dlg3=nmea_settDialog()

        QObject.connect(self.dlg.ui.pushButton,SIGNAL("clicked()"), self.dialog)
        QObject.connect(self.dlg.ui.ButOpenNmea,SIGNAL("clicked()"), self.openNmea)
        QObject.connect(self.dlg.ui.ButExit,SIGNAL("clicked()"), self.exit)
        QObject.connect(self.dlg.ui.addBut,SIGNAL("clicked()"), self.addLayer)
        QObject.connect(self.dlg.ui.settBut,SIGNAL("clicked()"), self.sett)
        QObject.connect(self.dlg2.ui.addBut,SIGNAL("clicked()"), self.addSave)

        QObject.connect(self.dlg2.ui.mat1Combo,SIGNAL("currentIndexChanged(int)"), self.chmat1)
        QObject.connect(self.dlg2.ui.mat2Combo,SIGNAL("currentIndexChanged(int)"), self.chmat2)



    def initGui(self):
        #QMessageBox.information(self.iface.mainWindow(), "Info", "gui")
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/nmea_main/icon.png"),
            u"nmea2dbqgis", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&nmea2qgis", self.action)
        self.fd = QFileDialog()
        self.fd1 = QFileDialog()
        settings=QSettings()
        dir=settings.value('/nmea2dbqgis/dir', QVariant('C:\Users')).toString()
        #self.fd.setDirectory("C:\Users\Maciek\Documents\GIG\magisterka\STD Oszczak\praca_mag")


        self.fd.setDirectory(dir)
    def unload(self):
        self.iface.removePluginMenu(u"&dbnmea2qgis", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        # show the dialog
        self.dlg.show()
        result=self.dlg.exec_()

    def dialog(self):
        self.filename = self.fd.getOpenFileName()
        from os.path import isfile
        if isfile(self.filename):
            self.dlg.ui.lineEdit.setText(self.filename)
            settings=QSettings()
            settings.setValue('/nmea2qgis/dir',QVariant(self.filename))
            self.fd.setDirectory(os.path.dirname(str(self.filename)))


    def exit(self):
        self.dlg.close()
        self.dlg.ui.lineEdit.setText("")

    def changeCombo(self):
        if self.dlg2.ui.saveCheck.isChecked():
            self.dlg2.ui.formatCombo.setEnabled(True)
        else:
            self.dlg2.ui.formatCombo.setEnabled(False)

    def sett(self):
        self.dlg3.show()





    def openNmea(self):
        nmeadoc=QTextDocument()
        nmeacur=QTextCursor(nmeadoc)
        start=time.time()

        #try:
        nmeafile=open(self.dlg.ui.lineEdit.text())
        try:
##            self.connectionObject=db.connect('C:\Users\Maciek\Documents\GIG\magisterka\STD Oszczak\praca_mag\dbnmea.sqlite')
            self.connectionObject=db.connect(':memory:')
            #QMessageBox.critical(self.iface.mainWindow(), 'info', 'connected to database')
        except:
            QMessageBox.critical(self.iface.mainWindow(), 'info', 'cannot connect to database')

        cur=self.connectionObject.cursor()
        qu="CREATE TABLE nmea2GGA(utc datetime primary key, lat real,lon real, fixstatus integer, numsv integer, hdop real, msl real, geoid real,speed real, datastatus text)"
        cur.execute(qu)
        self.connectionObject.commit()

        for line in nmeafile:
                 nmeacur.insertText(line)
        self.dlg2.ui.nmeaBrowser.setDocument(nmeadoc)

        self.nmeaDict(nmeafile,self.connectionObject)

        self.plotmat(self.dlg2.ui.mat1Combo.currentText(),self.dlg2.ui.mat2Combo.currentText())

        end=time.time()
        QMessageBox.information(self.iface.mainWindow(),"info",str(end-start))
        self.dlg2.show()
        #except:
            #QMessageBox.information(self.iface.mainWindow(), "Info", "Cannot open nmea file")


    def addLayer(self):
        #try:
        nmeafile=open(self.dlg.ui.lineEdit.text())
        try:
##            self.connectionObject=db.connect('C:\Users\Maciek\Documents\GIG\magisterka\STD Oszczak\praca_mag\dbnmea.sqlite')
            self.connectionObject=db.connect(':memory:')
            #QMessageBox.critical(self.iface.mainWindow(), 'info', 'connected to database')
        except:
            QMessageBox.critical(self.iface.mainWindow(), 'info', 'cannot connect to database')
        cur=self.connectionObject.cursor()
        qu="CREATE TABLE nmea2GGA(utc datetime primary key, lat real,lon real, fixstatus integer, numsv integer, hdop real, msl real, geoid real,speed real, datastatus text)"
        cur.execute(qu)
        self.connectionObject.commit()
        self.nmeaDict(nmeafile,self.connectionObject)
        self.addSave()
        #except:
            #QMessageBox.information(self.iface.mainWindow(), "Info", "Cannot open nmea file")

    def nmeaDict(self,nmeafile,connectionObject):
        nmeafile.seek(0)
        for line in nmeafile:
             linee=line.split(',')
             if line[3:6]=='GGA' or line[3:6]=='RMC':
                 cur=connectionObject.cursor()
                 key=linee[1][:2]+':'+linee[1][2:4]+':'+linee[1][4:6]
                 qu="""insert or ignore into nmea2GGA(utc) values('"""+key+"""')"""
                 #QMessageBox.information(self.iface.mainWindow(), 'inff', qu)
                 cur.execute(qu)

             if line[3:6]=='GLL':
                 cur=connectionObject.cursor()
                 key=linee[5][:2]+':'+linee[5][2:4]+':'+linee[5][4:6]
                 qu="""insert or ignore into nmea2GGA(utc) values('"""+key+"""')"""
                 #QMessageBox.information(self.iface.mainWindow(), 'inff2', qu)
                 cur.execute(qu)
        connectionObject.commit()

        nmeafile.seek(0)
        from funkcje_parse import funkcje
        funkcje=funkcje()
        for line in nmeafile:
            if line.startswith('$'):
                try:
                    parser={'GGA':funkcje.par_gga,'RMC':funkcje.par_rmc,'GLL':funkcje.par_gll}[line[3:6]]
                    query=parser(line)
##                    QMessageBox.information(self.iface.mainWindow(), 'info', query)
                    cursor=connectionObject.cursor()
                    cursor.execute(query)
                except:
                    #QMessageBox.critical(self.iface.mainWindow(), 'info', line)
                    continue
        connectionObject.commit()

        nmeafile.close()
        self.dlg.close()

    def addSave(self):
        fields = {}
        self.epsg4326= QgsCoordinateReferenceSystem()
        self.epsg4326.createFromString("epsg:4326")
        nmealayer = QgsVectorLayer("Point?crs=epsg:4326", "nmealeayer", "memory")
        nmealayer.startEditing()
        qu="""SELECT lat,lon"""
        pr = nmealayer.dataProvider()
        att=[]
        a=0
##        if self.dlg3.ui.latCheck.isChecked():
##               pr.addAttributes( [ QgsField("latitude", QVariant.Double)] )
##               att.append(self.lat)
##               fields[a]=QgsField("latitude", QVariant.Double)
##               a+=1
##        if self.dlg3.ui.lonCheck.isChecked():
##               pr.addAttributes( [ QgsField("longitude", QVariant.Double)] )
##               att.append(self.lon)
##               fields[a]=QgsField("longitude", QVariant.Double)
##               a+=1
        if self.dlg3.ui.utcCheck.isChecked():
               pr.addAttributes( [ QgsField("utc", QVariant.String)] )
##               att.append(self.utc)
               fields[a]=QgsField("utc", QVariant.String)
               qu+=',utc'
               a+=1
        if self.dlg3.ui.svCheck.isChecked():
               pr.addAttributes( [ QgsField("numSV", QVariant.Double)] )
##               att.append(self.numSV)
               fields[a]=QgsField("numSV", QVariant.Double)
               qu+=',numSV'
               a+=1
        if self.dlg3.ui.hdopCheck.isChecked():
               pr.addAttributes( [ QgsField("hdop", QVariant.Double)] )
##               att.append(self.hdop)
               fields[a]=QgsField("hdop", QVariant.Double)
               a+=1
        if self.dlg3.ui.vdopCheck.isChecked():
               pr.addAttributes( [ QgsField("vdop", QVariant.Double)] )
##               att.append(self.vdop)
               fields[a]=QgsField("vdop", QVariant.Double)
               a+=1
        if self.dlg3.ui.pdopCheck.isChecked():
               pr.addAttributes( [ QgsField("pdop", QVariant.Double)] )
##               att.append(self.pdop)
               fields[a]=QgsField("pdop", QVariant.Double)
               a+=1
        if self.dlg3.ui.mslCheck.isChecked():
               pr.addAttributes( [ QgsField("msl", QVariant.Double)] )
##               att.append(self.msl)
               fields[a]=QgsField("msl", QVariant.Double)
               a+=1
        if self.dlg3.ui.geoidCheck.isChecked():
               pr.addAttributes( [ QgsField("geoid", QVariant.Double)] )
##               att.append(self.geoid)
               fields[a]=QgsField("geoid", QVariant.Double)
               a+=1
        if self.dlg3.ui.speedCheck.isChecked():
               pr.addAttributes( [ QgsField("speed", QVariant.Double)] )
##               att.append(self.speed)
               fields[a]=QgsField("speed", QVariant.Double)
               a+=1
        if self.dlg3.ui.fixstatusCheck.isChecked():
               pr.addAttributes( [ QgsField("fixstatus", QVariant.Double)] )
##               att.append(self.fixstatus)
               fields[a]=QgsField("fixstatus", QVariant.Double)
               a+=1
        if self.dlg3.ui.datastatusCheck.isChecked():
               pr.addAttributes( [ QgsField("datastatus", QVariant.Double)] )
##               att.append(self.datastatus)
               fields[a]=QgsField("datastatus", QVariant.Double)
               a+=1

        cur=self.connectionObject.cursor()
        qu=qu+""" FROM nmea2GGA"""
        cur.execute(qu)
        fetched=cur.fetchall()

        fett=[]
        for f in fetched:
            fet = QgsFeature()
            fet.setGeometry(QgsGeometry.fromPoint(QgsPoint(f[1],f[0])))
            for i in range(a):
                fet.addAttribute(i,QVariant(f[i+2]))
            fett.append(fet)

        if self.dlg3.ui.saveCheck.isChecked():
            self.filename = self.fd.getSaveFileName()
            writer = QgsVectorFileWriter(self.filename, "CP1250", fields, QGis.WKBPoint, self.epsg4326, "ESRI Shapefile")
            for fet in fett:
                writer.addFeature(fet)
            del writer

        pr.addFeatures(fett)
        nmealayer.commitChanges()
        nmealayer.updateExtents()
        QgsMapLayerRegistry.instance().addMapLayer(nmealayer)

        self.iface.mapCanvas().zoomToFullExtent()
##        self.dlg2.ui.matplot1.canvas.ax1.clear()
##        self.dlg2.ui.matplot1.canvas.ax2.clear()
##        self.dlg2.ui.nmeaBrowser.clear()
        self.dlg2.close()




    def plotmat(self,data,data2):
        cur=self.connectionObject.cursor()
        qu1="""select utc,"""+data+""","""+data2+""" from nmea2GGA"""
        QMessageBox.information(self.iface.mainWindow(), 'inff', qu1)
        cur.execute(str(qu1))
        fetched=cur.fetchall()
        dates=[datetime.datetime.strptime(f[0],'%H:%M:%S') for f in fetched]
        yyy1=[f[1] for f in fetched]
        yyy2=[f[2] for f in fetched]

        self.dlg2.ui.matplot1.canvas.ax1.cla()
        self.dlg2.ui.matplot1.canvas.ax2.cla()
        self.dlg2.ui.matplot1.canvas.ax1.vlines(dates,0,yyy1,lw=5,rasterized=True)
        #self.dlg2.ui.matplot1.canvas.ax1.bar(self.dates,self.oy1)
        self.dlg2.ui.matplot1.canvas.ax1.xaxis_date()
        self.dlg2.ui.matplot1.canvas.ax2.vlines(dates,0,yyy2,lw=5,rasterized=True)
        #self.dlg2.ui.matplot1.canvas.ax2.bar(self.dates,self.oy1)
        self.dlg2.ui.matplot1.canvas.ax2.xaxis_date()
        self.dlg2.ui.matplot1.canvas.fig.autofmt_xdate()
        self.dlg2.ui.matplot1.canvas.draw()

    def chmat1(self,connectionObject):
        cur=self.connectionObject.cursor()
        qu="""select utc,"""+self.dlg2.ui.mat1Combo.currentText()+""" from nmea2GGA"""
##        QMessageBox.information(self.iface.mainWindow(), 'inff', qu)
        cur.execute(str(qu))
        fetched=cur.fetchall()
        dates=[datetime.datetime.strptime(f[0],'%H:%M:%S') for f in fetched]
        yy=[f[1] for f in fetched]

        self.dlg2.ui.matplot1.canvas.ax1.cla()
        self.dlg2.ui.matplot1.canvas.ax1.vlines(dates,0,yy,lw=5,rasterized=True)
        #self.dlg2.ui.matplot1.canvas.ax1.xaxis_date()
        self.dlg2.ui.matplot1.canvas.ax1.grid(True)
        self.dlg2.ui.matplot1.canvas.fig.autofmt_xdate()
        self.dlg2.ui.matplot1.canvas.draw()

    def chmat2(self):
        cur=self.connectionObject.cursor()
        qu="""select utc,"""+self.dlg2.ui.mat2Combo.currentText()+""" from nmea2GGA"""
        cur.execute(str(qu))
        fetched=cur.fetchall()
        dates=[datetime.datetime.strptime(f[0],'%H:%M:%S') for f in fetched]
        yy=[f[1] for f in fetched]
        if self.dlg2.ui.mat2Combo.currentText()=="datastatus":
            QMessageBox.information(self.iface.mainWindow(), 'info', "datastatus")
            zz=[]
            for stauts in yy:
                if stauts=="A": zz.append(1)
                else:   zz.append(0)
            yy=zz
        self.dlg2.ui.matplot1.canvas.ax2.cla()
        self.dlg2.ui.matplot1.canvas.ax2.vlines(dates,0,yy,lw=5,rasterized=True)
        #self.dlg2.ui.matplot1.canvas.ax2.xaxis_date()
        self.dlg2.ui.matplot1.canvas.ax2.grid(True)
        self.dlg2.ui.matplot1.canvas.fig.autofmt_xdate()
        self.dlg2.ui.matplot1.canvas.draw()





##    def ggaOnly(self):
##        lines = unicode(self.dlg2.ui.nmeaBrowser.toPlainText()).split('\n')
##        nmeadocc=QTextDocument()
##        nmeacurr=QTextCursor(nmeadocc)
##        self.dlg2.ui.nmeaBrowser.clear()
##
##        #formm=QTextCharFormat()
##        #brus=QBrush()
##        #brus.setColor(Qt.red)
##        #formm.setBackground(brus)
##        #formm.setForeground(brus)
##        #formm.setFontItalic(True)
##        for linee in lines:
##            #QMessageBox.information( self.iface.mainWindow(),"Info", linee )
##            if linee.startswith('$GPGGA'):
##                nmeacurr.insertText(linee)
##
##        self.dlg2.ui.nmeaBrowser.setDocument(nmeadocc)
