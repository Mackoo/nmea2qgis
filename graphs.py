from PyQt4 import QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure
from math import pi

class MplCanvas(FigureCanvas):
 
    def __init__(self):
        self.fig = Figure()
        self.ax1 = self.fig.add_subplot(211, axis_bgcolor='w')
        self.ax2 = self.fig.add_subplot(212, sharex=self.ax1, axis_bgcolor='w')
        self.ax1.set_title('num of SV')
        self.ax2.set_title('Dop')
        
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
 
 
class mplc(QtGui.QWidget):
 
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.canvas = MplCanvas()
        self.mpl_toolbar = NavigationToolbar(self.canvas,parent)
        
        self.vbl = QtGui.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.vbl.addWidget(self.mpl_toolbar)
        self.setLayout(self.vbl)