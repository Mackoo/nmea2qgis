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

class nmea_main:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/nmea2qgis"
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
        #QMessageBox.information(self.iface.mainWindow(), 'info', dir)
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
        self.nmeadoc=QTextDocument()
        self.nmeacur=QTextCursor(self.nmeadoc)
        #try:
        self.nmeafile=open(self.dlg.ui.lineEdit.text())
        start=time.time()
        self.nmeaDict(self.nmeafile,1)
        self.dlg2.ui.nmeaBrowser.setDocument(self.nmeadoc)
        self.plotmat()
        end=time.time()
        #QMessageBox.information(self.iface.mainWindow(),"info",str(end-start))
        self.dlg2.show()

        #except:
            #QMessageBox.information(self.iface.mainWindow(), "Info", "Cannot open nmea file")


    def addLayer(self):
        #try:
            nmeafile=open(self.dlg.ui.lineEdit.text())
            self.nmeaDict(nmeafile,0)
            self.addSave()
        #except:
            #QMessageBox.information(self.iface.mainWindow(), "Info", "Cannot open nmea file")

    def nmeaDict(self,nmeafile,insert):
        start=time.time()
        self.nmeadict={}
        nmeafile.seek(0)

        self.dlg.close()
        for line in nmeafile:
             if insert==1:
                 self.nmeacur.insertText(line)
             linee=line.split(',')
             if line[3:6]=='GGA' or line[3:6]=='RMC':
                 self.nmeadict[linee[1]]=['',0,0,0,0,0,0,0,0,0,0,0,0]
             if line[3:6]=='GLL':
                 self.nmeadict[linee[5]]=['',0,0,0,0,0,0,0,0,0,0,0,0]
        nmeafile.seek(0)
        for line in nmeafile:
            if line.startswith('$'):
                try:
                    parser={'GGA':self.par_gga,'RMC':self.par_rmc,'GLL':self.par_gll}[line[3:6]]
                    #QMessageBox.information(self.iface.mainWindow(), 'info', line[3:6])
                    parser(line)
                except:
                    #QMessageBox.critical(self.iface.mainWindow(), 'info', line)
                    continue

        end=time.time()
        #QMessageBox.information(self.iface.mainWindow(),'info',str(end-start))
        nmeafile.close()

        self.dates=[]
        self.utc=[]
        self.lat=[]
        self.lon=[]
        self.numSV=[]
        self.hdop=[]
        self.vdop=[]
        self.pdop=[]
        self.msl=[]
        self.geoid=[]
        self.speed=[]
        self.fixstatus=[]
        self.datastatus=[]

        for keyy in self.nmeadict.keys():
            self.utc.append(self.nmeadict[keyy][0])
            self.dates.append(datetime.datetime.strptime(self.nmeadict[keyy][0],'%H:%M:%S'))
            self.numSV.append(float(self.nmeadict[keyy][3]))
            try:    self.hdop.append(float(self.nmeadict[keyy][4]))
            except:  self.hdop.append(0)

            self.lon.append(self.nmeadict[keyy][2])
            self.lat.append(self.nmeadict[keyy][1])
            self.vdop.append(float(self.nmeadict[keyy][5]))
            self.pdop.append(float(self.nmeadict[keyy][6]))
            try:    self.msl.append(float(self.nmeadict[keyy][7]))
            except: self.msl.append(0)
            try:    self.geoid.append(float(self.nmeadict[keyy][8]))
            except: self.geoid.append(0)
            self.speed.append(float(self.nmeadict[keyy][9]))
            self.fixstatus.append(int(self.nmeadict[keyy][11]))
            datastatus=0
            if self.nmeadict[keyy][12]=='A':    datastatus=1
            self.datastatus.append(datastatus)




    def addSave(self):
        fields = {}
        self.epsg4326= QgsCoordinateReferenceSystem()
        self.epsg4326.createFromString("epsg:4326")
        nmealayer = QgsVectorLayer("Point?crs=epsg:4326", "nmealeayer", "memory")
        nmealayer.startEditing()

        pr = nmealayer.dataProvider()
        att=[]
        a=0
        if self.dlg3.ui.latCheck.isChecked():
               pr.addAttributes( [ QgsField("latitude", QVariant.Double)] )
               att.append(self.lat)
               fields[a]=QgsField("latitude", QVariant.Double)
               a+=1
        if self.dlg3.ui.lonCheck.isChecked():
               pr.addAttributes( [ QgsField("longitude", QVariant.Double)] )
               att.append(self.lon)
               fields[a]=QgsField("longitude", QVariant.Double)
               a+=1
        if self.dlg3.ui.utcCheck.isChecked():
               pr.addAttributes( [ QgsField("utc", QVariant.String)] )
               att.append(self.utc)
               fields[a]=QgsField("utc", QVariant.String)
               a+=1
        if self.dlg3.ui.svCheck.isChecked():
               pr.addAttributes( [ QgsField("numSV", QVariant.Double)] )
               att.append(self.numSV)
               fields[a]=QgsField("numSV", QVariant.Double)
               a+=1
        if self.dlg3.ui.hdopCheck.isChecked():
               pr.addAttributes( [ QgsField("hdop", QVariant.Double)] )
               att.append(self.hdop)
               fields[a]=QgsField("hdop", QVariant.Double)
               a+=1
        if self.dlg3.ui.vdopCheck.isChecked():
               pr.addAttributes( [ QgsField("vdop", QVariant.Double)] )
               att.append(self.vdop)
               fields[a]=QgsField("vdop", QVariant.Double)
               a+=1
        if self.dlg3.ui.pdopCheck.isChecked():
               pr.addAttributes( [ QgsField("pdop", QVariant.Double)] )
               att.append(self.pdop)
               fields[a]=QgsField("pdop", QVariant.Double)
               a+=1
        if self.dlg3.ui.mslCheck.isChecked():
               pr.addAttributes( [ QgsField("msl", QVariant.Double)] )
               att.append(self.msl)
               fields[a]=QgsField("msl", QVariant.Double)
               a+=1
        if self.dlg3.ui.geoidCheck.isChecked():
               pr.addAttributes( [ QgsField("geoid", QVariant.Double)] )
               att.append(self.geoid)
               fields[a]=QgsField("geoid", QVariant.Double)
               a+=1
        if self.dlg3.ui.speedCheck.isChecked():
               pr.addAttributes( [ QgsField("speed", QVariant.Double)] )
               att.append(self.speed)
               fields[a]=QgsField("speed", QVariant.Double)
               a+=1
        if self.dlg3.ui.fixstatusCheck.isChecked():
               pr.addAttributes( [ QgsField("fixstatus", QVariant.Double)] )
               att.append(self.fixstatus)
               fields[a]=QgsField("fixstatus", QVariant.Double)
               a+=1
        if self.dlg3.ui.datastatusCheck.isChecked():
               pr.addAttributes( [ QgsField("datastatus", QVariant.Double)] )
               att.append(self.datastatus)
               fields[a]=QgsField("datastatus", QVariant.Double)
               a+=1



        fett=[]
        for a,lat in enumerate(self.lat):
            fet = QgsFeature()
            fet.setGeometry(QgsGeometry.fromPoint(QgsPoint(self.lon[a],lat)))
            b=0
            for aa in att:
                fet.addAttribute(b,QVariant(aa[a]))
                b+=1
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
        self.dlg2.ui.matplot1.canvas.ax1.clear()
        self.dlg2.ui.matplot1.canvas.ax2.clear()
        self.dlg2.ui.nmeaBrowser.clear()
        self.dlg2.close()




    def plotmat(self):
        self.oy1={'hdop':self.hdop,'numSV':self.numSV,'vdop':self.vdop,'pdop':self.pdop,'msl':self.msl,'geoid':self.geoid,'speed':self.speed,'fixstatus':self.fixstatus}[str(self.dlg2.ui.mat1Combo.currentText())]
        self.oy2={'hdop':self.hdop,'numSV':self.numSV,'vdop':self.vdop,'pdop':self.pdop,'msl':self.msl,'geoid':self.geoid,'speed':self.speed,'datastatus':self.datastatus}[str(self.dlg2.ui.mat2Combo.currentText())]
        self.dlg2.ui.matplot1.canvas.ax1.cla()
        self.dlg2.ui.matplot1.canvas.ax2.cla()
        self.dlg2.ui.matplot1.canvas.ax1.vlines(self.dates,0,self.oy1,lw=5,rasterized=True)
        #self.dlg2.ui.matplot1.canvas.ax1.bar(self.dates,self.oy1)
        self.dlg2.ui.matplot1.canvas.ax1.xaxis_date()
        self.dlg2.ui.matplot1.canvas.ax2.vlines(self.dates,0,self.oy2,lw=5,rasterized=True)
        #self.dlg2.ui.matplot1.canvas.ax2.bar(self.dates,self.oy1)
        self.dlg2.ui.matplot1.canvas.ax2.xaxis_date()
        self.dlg2.ui.matplot1.canvas.fig.autofmt_xdate()
        self.dlg2.ui.matplot1.canvas.draw()



    def chmat1(self):

        self.oy1={'hdop':self.hdop,'numSV':self.numSV,'vdop':self.vdop,'pdop':self.pdop,'msl':self.msl,'geoid':self.geoid,'speed':self.speed,'fixstatus':self.fixstatus}[str(self.dlg2.ui.mat1Combo.currentText())]
        self.dlg2.ui.matplot1.canvas.ax1.cla()
        self.dlg2.ui.matplot1.canvas.ax1.vlines(self.dates,0,self.oy1,lw=5,rasterized=True)
        self.dlg2.ui.matplot1.canvas.ax1.xaxis_date()
        self.dlg2.ui.matplot1.canvas.ax1.grid(True)
        self.dlg2.ui.matplot1.canvas.fig.autofmt_xdate()
        self.dlg2.ui.matplot1.canvas.draw()

    def chmat2(self):
        self.oy2={'hdop':self.hdop,'numSV':self.numSV,'vdop':self.vdop,'pdop':self.pdop,'msl':self.msl,'geoid':self.geoid,'speed':self.speed,'datastatus':self.datastatus}[str(self.dlg2.ui.mat2Combo.currentText())]
        self.dlg2.ui.matplot1.canvas.ax2.cla()
        self.dlg2.ui.matplot1.canvas.ax2.vlines(self.dates,0,self.oy2,lw=5,rasterized=True)
        self.dlg2.ui.matplot1.canvas.ax2.xaxis_date()
        self.dlg2.ui.matplot1.canvas.ax2.grid(True)
        self.dlg2.ui.matplot1.canvas.fig.autofmt_xdate()
        self.dlg2.ui.matplot1.canvas.draw()


    def par_gga(self,line):
        data=[]
        data=line.split(',')
        key=data[1]
        utc=data[1][:2]+':'+data[1][2:4]+':'+data[1][4:6]
        latt=float(data[2][:2])+float(data[2][2:])/60
        ind=string.find(data[4],".")
        lonn=float(data[4][:(ind-2)])+float(data[4][(ind-2):])/60
        numsv=data[7]
        hdop=data[8]
        msl=data[9]
        geoid=data[11]
        fixstatus=data[6]
        self.nmeadict[key][0]=utc
        self.nmeadict[key][1]=latt
        self.nmeadict[key][2]=lonn
        self.nmeadict[key][3]=numsv
        self.nmeadict[key][4]=hdop
        self.nmeadict[key][7]=msl
        self.nmeadict[key][8]=geoid
        self.nmeadict[key][11]=fixstatus

    def par_rmc(self,line):
        data=[]
        data=line.split(',')
        key=data[1]
        utc=data[1][:2]+':'+data[1][2:4]+':'+data[1][4:6]
        latt=float(data[3][:2])+float(data[3][2:])/60
        ind=string.find(data[5],".")
        lonn=float(data[5][:(ind-2)])+float(data[5][(ind-2):])/60
        speed=data[7]
        datastatus=data[2]
        self.nmeadict[key][0]=utc
        self.nmeadict[key][1]=latt
        self.nmeadict[key][2]=lonn
        self.nmeadict[key][9]=speed
        self.nmeadict[key][12]=datastatus

    def par_gll(self,line):
        data=[]
        data=line.split(',')
        key=data[5]
        utc=data[5][:2]+':'+data[5][2:4]+':'+data[5][4:6]
        latt=float(data[1][:2])+float(data[1][2:])/60
        ind=string.find(data[3],".")
        lonn=float(data[3][:(ind-2)])+float(data[3][(ind-2):])/60
        datastatus=data[6]
        self.nmeadict[key][0]=utc
        self.nmeadict[key][1]=latt
        self.nmeadict[key][2]=lonn
        self.nmeadict[key][12]=datastatus



    def ggaOnly(self):
        lines = unicode(self.dlg2.ui.nmeaBrowser.toPlainText()).split('\n')
        nmeadocc=QTextDocument()
        nmeacurr=QTextCursor(nmeadocc)
        self.dlg2.ui.nmeaBrowser.clear()


        for linee in lines:
            #QMessageBox.information( self.iface.mainWindow(),"Info", linee )
            if linee.startswith('$GPGGA'):
                nmeacurr.insertText(linee)

        self.dlg2.ui.nmeaBrowser.setDocument(nmeadocc)
