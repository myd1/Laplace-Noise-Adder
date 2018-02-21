# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from backend import *
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

class Ui_MainWindow(object):

    nodes = []
    edges = [] 
    graph = nx.Graph()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(840, 659)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.eValueSlider = QtGui.QSlider(self.centralwidget)
        self.eValueSlider.setGeometry(QtCore.QRect(20, 50, 160, 29))
        self.eValueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.eValueSlider.setObjectName(_fromUtf8("eValueSlider"))
        self.titleText = QtGui.QLineEdit(self.centralwidget)
        self.titleText.setEnabled(False)
        self.titleText.setGeometry(QtCore.QRect(20, 20, 161, 30))
        self.titleText.setObjectName(_fromUtf8("titleText"))
        self.eValueHolder = QtGui.QLineEdit(self.centralwidget)
        self.eValueHolder.setGeometry(QtCore.QRect(20, 90, 31, 30))
        self.eValueHolder.setObjectName(_fromUtf8("eValueHolder"))
        self.applyButton = QtGui.QPushButton(self.centralwidget)
        self.applyButton.setGeometry(QtCore.QRect(80, 90, 90, 30))
        self.applyButton.setObjectName(_fromUtf8("applyButton"))
        self.statsHolder = QtGui.QPlainTextEdit(self.centralwidget)
        self.statsHolder.setGeometry(QtCore.QRect(210, 20, 241, 211))
        self.statsHolder.setObjectName(_fromUtf8("statsHolder"))
        self.originalHistogramHolder = QtGui.QLabel(self.centralwidget)
        self.originalHistogramHolder.setGeometry(QtCore.QRect(20, 280, 360, 270))
        self.originalHistogramHolder.setText(_fromUtf8(""))
        self.originalHistogramHolder.setObjectName(_fromUtf8("originalHistogramHolder"))
        self.modifiedHistogramHolder = QtGui.QLabel(self.centralwidget)
        self.modifiedHistogramHolder.setGeometry(QtCore.QRect(410, 280, 360, 270))
        self.modifiedHistogramHolder.setText(_fromUtf8(""))
        self.modifiedHistogramHolder.setObjectName(_fromUtf8("modifiedHistogramHolder"))
        self.socialNetworkHolder = QtGui.QLabel(self.centralwidget)
        self.socialNetworkHolder.setGeometry(QtCore.QRect(480, 20, 320, 240))
        self.socialNetworkHolder.setText(_fromUtf8(""))
        self.socialNetworkHolder.setObjectName(_fromUtf8("socialNetworkHolder"))
        self.textHolder1 = QtGui.QLineEdit(self.centralwidget)
        self.textHolder1.setEnabled(False)
        self.textHolder1.setGeometry(QtCore.QRect(90, 570, 161, 30))
        self.textHolder1.setObjectName(_fromUtf8("textHolder1"))
        self.textHolder2 = QtGui.QLineEdit(self.centralwidget)
        self.textHolder2.setEnabled(False)
        self.textHolder2.setGeometry(QtCore.QRect(570, 570, 161, 30))
        self.textHolder2.setObjectName(_fromUtf8("textHolder2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 840, 28))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_Node = QtGui.QAction(MainWindow)
        self.actionAdd_Node.setObjectName(_fromUtf8("actionAdd_Node"))
        self.actionAdd_Edge = QtGui.QAction(MainWindow)
        self.actionAdd_Edge.setObjectName(_fromUtf8("actionAdd_Edge"))
        self.actionExport = QtGui.QAction(MainWindow)
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionRemove_Network = QtGui.QAction(MainWindow)
        self.actionRemove_Network.setObjectName(_fromUtf8("actionRemove_Network"))
        self.menuFile.addAction(self.actionAdd_Node)
        self.menuFile.addAction(self.actionAdd_Edge)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionRemove_Network)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        # custom code starts from here
        self.actionAdd_Node.triggered.connect(self.nodeOpener)
        self.actionAdd_Edge.triggered.connect(self.edgeOpener)
        self.actionExit.triggered.connect(self.goOut)
        self.actionRemove_Network.triggered.connect(self.clearFiles)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def nodeOpener(self):
        nodeFile = self.fileOpener()
        self.nodes = nodeReader(nodeFile,self.nodes)
        self.graph = self.plotNetwork()

    def edgeOpener(self):
        edgeFile = self.fileOpener()
        self.edges = edgeReader(edgeFile,self.edges)
        self.graph = self.plotNetwork()

    def fileOpener(self):
        dlg = QtGui.QFileDialog()
        dlg.setFileMode(QtGui.QFileDialog.AnyFile)
        dlg.setFilter("Text files (*.txt)")
        dlg.exec_()
        fileNames = dlg.selectedFiles()
        return (fileNames[0])

    def plotNetwork(self):
        graph = generateNetwork(self.nodes,self.edges,self.graph)
        self.socialNetworkHolder.setPixmap(QtGui.QPixmap('images/network.png'))
        drawHistogram(nx.degree_histogram(graph),"originalHistogram")
        self.originalHistogramHolder.setPixmap(QtGui.QPixmap('images/originalHistogram.png'))
        statstring = getstats(graph)
        self.statsHolder.setPlainText(statstring)
        return graph

    def clearFiles(self):
        self.nodes = []
        self.edges = []
        self.graph = clearNetwork(self.graph)
        self.graph = self.plotNetwork()

    def goOut(self):
        sys.exit()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.titleText.setText(_translate("MainWindow", "Ɛ - slider", None))
        self.applyButton.setText(_translate("MainWindow", "Apply", None))
        self.textHolder1.setText(_translate("MainWindow", "Original Histogram", None))
        self.textHolder2.setText(_translate("MainWindow", "Modified Histogram", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.actionAdd_Node.setText(_translate("MainWindow", "Add Node", None))
        self.actionAdd_Edge.setText(_translate("MainWindow", "Add Edge", None))
        self.actionExport.setText(_translate("MainWindow", "Export", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionRemove_Network.setText(_translate("MainWindow", "Remove Network", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

