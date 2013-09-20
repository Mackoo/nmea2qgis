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
        QObject.connect(self.dlg2.ui.sqlCheck,SIGNAL("clicked()"), self.whereSet)

        QObject.connect(self.dlg2.ui.sentCombo,SIGNAL("currentIndexChanged(int)"), self.ggaOnly)
        QObject.connect(self.dlg2.ui.mat1Combo,SIGNAL("currentIndexChanged(int)"), self.chmat1)
        QObject.connect(self.dlg2.ui.mat2Combo,SIGNAL("currentIndexChanged(int)"), self.chmat2)



    def initGui(self):
        #QMessageBox.information(self.iface.mainWindow(), "Info", "gui")
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/nmea_main/icon.png"),
            u"nmea2qgis", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&nmea2qgis", self.action)
        self.fd = QFileDialog()
        self.fd1 = QFileDialog()
        settings=QSettings()
        dir=settings.value('/nmea2qgis/dir', QVariant('C:\Users')).toString()
        #self.fd.setDirectory("C:\Users\Maciek\Documents\GIG\magisterka\STD Oszczak\praca_mag")
        self.fd.setDirectory(dir)

    def unload(self):
        self.iface.removePluginMenu(u"&nmea2qgis", self.action)
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
        #try:
        nmeafile=open(self.dlg.ui.lineEdit.text())
        for line in nmeafile:
                 nmeacur.insertText(line)
        self.dlg2.ui.nmeaBrowser.setDocument(nmeadoc)
        self.lines = unicode(self.dlg2.ui.nmeaBrowser.toPlainText()).split('\n')

        self.nmeaDict()

        self.plotmat(self.dlg2.ui.mat1Combo.currentText(),self.dlg2.ui.mat2Combo.currentText())
        self.whereSet()
        self.dlg2.show()
        #except:
            #QMessageBox.information(self.iface.mainWindow(), "Info", "Cannot open nmea file")


    def addLayer(self):
        self.nmeaDict()
        self.addSave()


    def nmeaDict(self):
        nmeafile=open(self.dlg.ui.lineEdit.text())
        try:
##            self.connectionObject=db.connect('C:\Users\Maciek\Documents\GIG\magisterka\STD Oszczak\praca_mag\dbnmea.sqlite')
            self.connectionObject=db.connect(':memory:')
            #QMessageBox.critical(self.iface.mainWindow(), 'info', 'connected to database')
        except:
            QMessageBox.critical(self.iface.mainWindow(), 'info', 'cannot connect to database')

        cur=self.connectionObject.cursor()
        qu="CREATE TABLE nmeaGGA(utcgga datetime primary key, latgga real,longga real, fixstatus integer, numsv integer, hdop real, msl real, geoid real, speed real, datastatus text)"
        cur.execute(qu)
        qu="CREATE TABLE nmeaRMC(utcrmc datetime primary key, latrmc real,lonrmc real,fixstatus integer, numsv integer, hdop real, msl real, geoid real, speed real, datastatus text)"
        cur.execute(qu)
        qu="CREATE TABLE nmeaGLL(utcgll datetime primary key, latgll real,longll real, fixstatus integer, numsv integer, hdop real, msl real, geoid real, speed real, datastatus text)"
        cur.execute(qu)

        qu="CREATE VIEW nmea23 as  select case when t1.utcgga is null then "
        qu+="(select case when t2.utcrmc is null then t3.utcgll else t2.utcrmc end)    else t1.utcgga     end as utc   ,case when t1.latgga is null"
        qu+=" then (select case when t2.latrmc is null then t3.latgll else t2.latrmc end)     else t1.latgga     end as lat ,case when t1.longga is null     then (select case when t2.lonrmc is null then t3.longll else t2.lonrmc end)    else t1.longga     end as lon   , t1.numsv as numsv ,"
        qu+=" t1.fixstatus as fix  , t1.hdop as hdop , t1.msl as msl , t1.geoid as geoid ,t2.speed  as speed , case when t2.datastatus is null then t3.datastatus else t2.datastatus end as datastatus from nmeaGGA t1 left outer join nmeaRMC t2 on t1.utcgga=t2.utcrmc left outer join nmeaGLL t3 on t3.utcgll=t1.utcgga  union all  select case when t2.utcrmc is null then t3.utcgll    else t2.utcrmc    end as utc   ,case when t2.latrmc is null"
        qu+=" then  t3.latgll else t2.latrmc end as lat ,case when t2.lonrmc is null     then  t3.longll else t2.lonrmc end    as lon   , t2.numsv as numsv , t2.fixstatus as fix  , t2.hdop as hdop , t2.msl as msl , t2.geoid as geoid ,t2.speed  as speed , case when t2.datastatus is null then t3.datastatus else t2.datastatus end as datastatus from nmeaRMC  t2 left outer join nmeaGGA t1 on t1.utcgga=t2.utcrmc left outer join nmeaGLL t3 on t3.utcgll=t1.utcgga where t1.utcgga is null  union all  select case when t2.utcrmc is null then t3.utcgll    else t2.utcrmc    end as utc   ,case when t2.latrmc is null     then  t3.latgll else t2.latrmc end as lat ,case when t2.lonrmc is null     then  t3.longll else t2.lonrmc end    as lon   , t2.numsv as numsv , t2.fixstatus as fix  , t2.hdop as hdop ,"
        qu+=" t2.msl as msl , t2.geoid as geoid ,t2.speed  as speed , case when t2.datastatus is null then t3.datastatus else t2.datastatus end as datastatus from nmeaGLL  t3 left outer join nmeaGGA t1 on t1.utcgga=t3.utcgll left outer join nmearmc t2 on t3.utcgll=t2.utcrmc where t1.utcgga is null and t2.utcrmc is null"
        #QMessageBox.information(self.iface.mainWindow(), "Info", qu)
        cur.execute(qu)
        self.connectionObject.commit()




        nmeafile.seek(0)
        from funkcje_parse import funkcje
        funkcje=funkcje()
        for line in nmeafile:
            if line[3:6]=='GGA' or line[3:6]=='RMC'or line[3:6]=='GLL':
                try:
                    parser={'GGA':funkcje.par_gga,'RMC':funkcje.par_rmc,'GLL':funkcje.par_gll}[line[3:6]]
                    query=parser(line)
                    #QMessageBox.information(self.iface.mainWindow(), 'info', query)
                    cursor=self.connectionObject.cursor()
                    cursor.execute(query)
                except:
                    #QMessageBox.critical(self.iface.mainWindow(), 'error', line)
                    continue

        self.connectionObject.commit()

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
        if self.dlg3.ui.latCheck.isChecked():
               pr.addAttributes( [ QgsField("latitude", QVariant.Double)] )
               fields[a]=QgsField("latitude", QVariant.Double)
               qu+=',lat'
               a+=1
        if self.dlg3.ui.lonCheck.isChecked():
               pr.addAttributes( [ QgsField("longitude", QVariant.Double)] )
               fields[a]=QgsField("longitude", QVariant.Double)
               qu+=',lon'
               a+=1
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
               qu+=',numsv'
               a+=1
        if self.dlg3.ui.hdopCheck.isChecked():
               pr.addAttributes( [ QgsField("hdop", QVariant.Double)] )
##               att.append(self.hdop)
               fields[a]=QgsField("hdop", QVariant.Double)
               qu+=',hdop'
               a+=1
        if self.dlg3.ui.mslCheck.isChecked():
               pr.addAttributes( [ QgsField("msl", QVariant.Double)] )
               qu+=',msl'
##               att.append(self.msl)
               fields[a]=QgsField("msl", QVariant.Double)
               a+=1
        if self.dlg3.ui.geoidCheck.isChecked():
               pr.addAttributes( [ QgsField("geoid", QVariant.Double)] )
##               att.append(self.geoid)
               fields[a]=QgsField("geoid", QVariant.Double)
               qu+=',geoid'
               a+=1
        if self.dlg3.ui.speedCheck.isChecked():
               pr.addAttributes( [ QgsField("speed", QVariant.Double)] )
##               att.append(self.speed)
               fields[a]=QgsField("speed", QVariant.Double)
               qu+=',speed'
               a+=1
        if self.dlg3.ui.fixstatusCheck.isChecked():
               pr.addAttributes( [ QgsField("fixstatus", QVariant.Double)] )
##               att.append(self.fixstatus)
               fields[a]=QgsField("fixstatus", QVariant.Double)
               qu+=',fix'
               a+=1
        if self.dlg3.ui.datastatusCheck.isChecked():
               pr.addAttributes( [ QgsField("datastatus", QVariant.Double)] )
##               att.append(self.datastatus)
               fields[a]=QgsField("datastatus", QVariant.Double)
               qu+=',datastatus'
               a+=1

        cur=self.connectionObject.cursor()
        qu=qu+""" FROM nmea23 """
        qu=qu+str(self.dlg2.ui.sqlText.toPlainText())
        QMessageBox.information(self.iface.mainWindow(),"info",qu)

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


    def whereSet(self):
        uii=self.dlg2.ui
        if uii.sqlCheck.isChecked():
            uii.utcCheck.setEnabled(True)
            uii.numsvCheck1.setEnabled(True)
            uii.hdopCheck1.setEnabled(True)
            uii.mslCheck1.setEnabled(True)
            uii.geoidCheck1.setEnabled(True)
            uii.speedCheck1.setEnabled(True)
            uii.datastatusCheck1.setEnabled(True)
            uii.fixstatusCheck1.setEnabled(True)

            uii.numsvCheck2.setEnabled(True)
            uii.hdopCheck2.setEnabled(True)
            uii.mslCheck2.setEnabled(True)
            uii.geoidCheck2.setEnabled(True)
            uii.speedCheck2.setEnabled(True)

            QObject.connect(uii.utcCheck,SIGNAL("stateChanged(int)"), self.utcCheck)
            QObject.connect(uii.numsvCheck1,SIGNAL("stateChanged(int)"), self.numsvCheck1)
            QObject.connect(uii.hdopCheck1,SIGNAL("stateChanged(int)"), self.hdopCheck1)
            QObject.connect(uii.mslCheck1,SIGNAL("stateChanged(int)"), self.mslCheck1)
            QObject.connect(uii.geoidCheck1,SIGNAL("stateChanged(int)"), self.geoidCheck1)
            QObject.connect(uii.speedCheck1,SIGNAL("stateChanged(int)"), self.speedCheck1)
            QObject.connect(uii.datastatusCheck1,SIGNAL("stateChanged(int)"), self.datastatusCheck1)
            QObject.connect(uii.fixstatusCheck1,SIGNAL("stateChanged(int)"), self.fixstatusCheck1)

            QObject.connect(uii.numsvCheck2,SIGNAL("stateChanged(int)"), self.numsvCheck2)
            QObject.connect(uii.hdopCheck2,SIGNAL("stateChanged(int)"), self.hdopCheck2)
            QObject.connect(uii.mslCheck2,SIGNAL("stateChanged(int)"), self.mslCheck2)
            QObject.connect(uii.geoidCheck2,SIGNAL("stateChanged(int)"), self.geoidCheck2)
            QObject.connect(uii.speedCheck2,SIGNAL("stateChanged(int)"), self.speedCheck2)


        else:
            uii.utcCheck.setEnabled(False)
            uii.numsvCheck1.setEnabled(False)
            uii.hdopCheck1.setEnabled(False)
            uii.mslCheck1.setEnabled(False)
            uii.geoidCheck1.setEnabled(False)
            uii.speedCheck1.setEnabled(False)
            uii.datastatusCheck1.setEnabled(False)
            uii.fixstatusCheck1.setEnabled(False)

            uii.numsvCheck2.setEnabled(False)
            uii.hdopCheck2.setEnabled(False)
            uii.mslCheck2.setEnabled(False)
            uii.geoidCheck2.setEnabled(False)
            uii.speedCheck2.setEnabled(False)

            uii.utcCheck.setChecked(False)
            uii.numsvCheck1.setChecked(False)
            uii.hdopCheck1.setChecked(False)
            uii.mslCheck1.setChecked(False)
            uii.geoidCheck1.setChecked(False)
            uii.speedCheck1.setChecked(False)
            uii.datastatusCheck1.setChecked(False)
            uii.fixstatusCheck1.setChecked(False)

            uii.numsvCheck2.setChecked(False)
            uii.hdopCheck2.setChecked(False)
            uii.mslCheck2.setChecked(False)
            uii.geoidCheck2.setChecked(False)
            uii.speedCheck2.setChecked(False)

    def utcCheck(self):
        uii=self.dlg2.ui
        if uii.utcCheck.isChecked():
            uii.spinBox_10.setEnabled(True)
            uii.spinBox_11.setEnabled(True)
            uii.spinBox_12.setEnabled(True)
            uii.spinBox_13.setEnabled(True)
            uii.spinBox_14.setEnabled(True)
            uii.spinBox_15.setEnabled(True)
        else:
            uii.spinBox_10.setEnabled(False)
            uii.spinBox_11.setEnabled(False)
            uii.spinBox_12.setEnabled(False)
            uii.spinBox_13.setEnabled(False)
            uii.spinBox_14.setEnabled(False)
            uii.spinBox_15.setEnabled(False)


    def numsvCheck1(self):
        uii=self.dlg2.ui
        if uii.numsvCheck1.isChecked():
            uii.numsvCheck2.setChecked(False)
            uii.spinBox_16.setEnabled(True)
        else:
            uii.spinBox_16.setEnabled(False)

    def hdopCheck1(self):
        uii=self.dlg2.ui
        if uii.hdopCheck1.isChecked():
            uii.hdopCheck2.setChecked(False)
            uii.doubleSpinBox.setEnabled(True)
        else:
            uii.doubleSpinBox.setEnabled(False)

    def mslCheck1(self):
        uii=self.dlg2.ui
        if uii.mslCheck1.isChecked():
            uii.mslCheck2.setChecked(False)
            uii.doubleSpinBox_4.setEnabled(True)
        else:
            uii.doubleSpinBox_4.setEnabled(False)

    def geoidCheck1(self):
        uii=self.dlg2.ui
        if uii.geoidCheck1.isChecked():
            uii.geoidCheck2.setChecked(False)
            uii.doubleSpinBox_7.setEnabled(True)
        else:
            uii.doubleSpinBox_7.setEnabled(False)

    def speedCheck1(self):
        uii=self.dlg2.ui
        if uii.speedCheck1.isChecked():
            uii.speedCheck2.setChecked(False)
            uii.doubleSpinBox_10.setEnabled(True)
        else:
            uii.doubleSpinBox_10.setEnabled(False)

    def datastatusCheck1(self):
        uii=self.dlg2.ui
        if uii.datastatusCheck1.isChecked():
            uii.spinBox_19.setEnabled(True)

        else:
            uii.spinBox_19.setEnabled(False)

    def fixstatusCheck1(self):
        uii=self.dlg2.ui
        if uii.fixstatusCheck1.isChecked():
            uii.spinBox_20.setEnabled(True)

        else:
            uii.spinBox_20.setEnabled(False)

    def numsvCheck2(self):
        uii=self.dlg2.ui
        if uii.numsvCheck2.isChecked():
            uii.numsvCheck1.setChecked(False)
            uii.spinBox_17.setEnabled(True)
            uii.spinBox_18.setEnabled(True)
        else:

            uii.spinBox_17.setEnabled(False)
            uii.spinBox_18.setEnabled(False)

    def hdopCheck2(self):
        uii=self.dlg2.ui
        if uii.hdopCheck2.isChecked():
            uii.hdopCheck1.setChecked(False)
            uii.doubleSpinBox_2.setEnabled(True)
            uii.doubleSpinBox_3.setEnabled(True)
        else:

            uii.doubleSpinBox_2.setEnabled(False)
            uii.doubleSpinBox_3.setEnabled(False)

    def mslCheck2(self):
        uii=self.dlg2.ui
        if uii.mslCheck2.isChecked():
            uii.mslCheck1.setChecked(False)
            uii.doubleSpinBox_5.setEnabled(True)
            uii.doubleSpinBox_6.setEnabled(True)
        else:

            uii.doubleSpinBox_5.setEnabled(False)
            uii.doubleSpinBox_6.setEnabled(False)

    def geoidCheck2(self):
        uii=self.dlg2.ui
        if uii.geoidCheck2.isChecked():
            uii.geoidCheck1.setChecked(False)
            uii.doubleSpinBox_8.setEnabled(True)
            uii.doubleSpinBox_9.setEnabled(True)
        else:

            uii.doubleSpinBox_8.setEnabled(False)
            uii.doubleSpinBox_9.setEnabled(False)

    def speedCheck2(self):
        uii=self.dlg2.ui
        if uii.speedCheck2.isChecked():
            uii.speedCheck1.setChecked(False)
            uii.doubleSpinBox_11.setEnabled(True)
            uii.doubleSpinBox_12.setEnabled(True)
        else:

            uii.doubleSpinBox_11.setEnabled(False)
            uii.doubleSpinBox_12.setEnabled(False)


    def plotmat(self,data,data2):
        cur=self.connectionObject.cursor()
        qu1="""select utc,"""+data+""","""+data2+""" from nmea23"""
        #QMessageBox.information(self.iface.mainWindow(), 'inff', qu1)
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

    def chmat1(self):
        cur=self.connectionObject.cursor()
        qu="""select utc,"""+self.dlg2.ui.mat1Combo.currentText()+""" from nmea23"""
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
        qu="""select utc,"""+self.dlg2.ui.mat2Combo.currentText()+""" from nmea23"""
        cur.execute(str(qu))
        fetched=cur.fetchall()
        dates=[datetime.datetime.strptime(f[0],'%H:%M:%S') for f in fetched]
        yy=[f[1] for f in fetched]
##        if self.dlg2.ui.mat2Combo.currentText()=="datastatus":
##            QMessageBox.information(self.iface.mainWindow(), 'info', "datastatus")
##            zz=[]
##            for stauts in yy:
##                if stauts=="A": zz.append(1)
##                else:   zz.append(0)
##            yy=zz
        self.dlg2.ui.matplot1.canvas.ax2.cla()
        self.dlg2.ui.matplot1.canvas.ax2.vlines(dates,0,yy,lw=5,rasterized=True)
        #self.dlg2.ui.matplot1.canvas.ax2.xaxis_date()
        self.dlg2.ui.matplot1.canvas.ax2.grid(True)
        self.dlg2.ui.matplot1.canvas.fig.autofmt_xdate()
        self.dlg2.ui.matplot1.canvas.draw()





    def ggaOnly(self,ind):

        nmeadocc=QTextDocument()
        nmeacurr=QTextCursor(nmeadocc)
        self.dlg2.ui.nmeaBrowser.clear()
        if self.dlg2.ui.sentCombo.currentText()=="ALL":
            for linee in self.lines:
                nmeacurr.insertText(linee+'\n')
        else:

            for linee in self.lines:
                if linee[3:6]==self.dlg2.ui.sentCombo.currentText():
                    nmeacurr.insertText(linee+'\n')

        self.dlg2.ui.nmeaBrowser.setDocument(nmeadocc)
