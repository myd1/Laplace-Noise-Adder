import sys
from PyQt4 import QtCore, QtGui,uic
from backend import *

class MyWindow(QtGui.QMainWindow):

	nodes = []
	edges = []
	graph = nx.Graph()

	def __init__(self):
		super(MyWindow, self).__init__()
		uic.loadUi('gui.ui', self)
		self.actionAdd_Node.triggered.connect(self.nodeOpener)
		self.actionAdd_Edge.triggered.connect(self.edgeOpener)
		self.actionExit.triggered.connect(self.goOut)
		self.actionRemove_Network.triggered.connect(self.clearFiles)
		self.actionExport.triggered.connect(self.exportGraph)
		self.applyButton.clicked.connect(self.applyButtonClicked)
		self.eValueSlider.valueChanged.connect(self.displayChange)
		self.eValueHolder.setText(str(self.eValueSlider.value()/100.0))
		self.show()

	def applyButtonClicked(self):
		if isEmpty(self.graph):
			print("The Graph is Empty.")
		else:
			epsilon = float(self.eValueHolder.text())
			anonimizeDegreeSequence = anonimizer(self.graph,epsilon)
			drawHistogram(anonimizeDegreeSequence,"modifiedHistogram","images/")
			self.modifiedHistogramHolder.setPixmap(QtGui.QPixmap('images/modifiedHistogram.png'))

	def displayChange(self,val):
		self.eValueHolder.setText(str(val/100.0))

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
		data = []
		try :
			data = nx.degree_histogram(graph)
		except ValueError :
			data = [0]
		drawHistogram(data,"originalHistogram","images/")
		self.originalHistogramHolder.setPixmap(QtGui.QPixmap('images/originalHistogram.png'))
		statstring, globalSensitivity, averageDegree = getstats(graph)
		self.statsHolder.setPlainText(statstring.format(averageDegree))
		return graph

	def clearFiles(self):
		self.nodes = []
		self.edges = []
		self.graph = clearNetwork(self.graph)
		statstring, globalSensitivity, averageDegree = getstats(self.graph)
		self.statsHolder.setPlainText(statstring.format(averageDegree))
		drawHistogram([0],"modifiedHistogram","images/")
		self.modifiedHistogramHolder.setPixmap(QtGui.QPixmap('images/modifiedHistogram.png'))
		self.graph = self.plotNetwork()

	def goOut(self):
		sys.exit()

	def exportGraph(self):
		dlg = QtGui.QFileDialog()
		dlg.setFileMode(QtGui.QFileDialog.DirectoryOnly)
		dlg.exec_()
		folderName = dlg.selectedFiles()
		if isEmpty(self.graph):
			print("The Graph is Empty.")
		else:
			epsilon = float(self.eValueHolder.text())
			anonimizeDegreeSequence = anonimizer(self.graph,epsilon)
			drawHistogram(anonimizeDegreeSequence,"modifiedHistogram",folderName[0]+"/")
			self.modifiedHistogramHolder.setPixmap(QtGui.QPixmap('images/modifiedHistogram.png'))


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = MyWindow()
	sys.exit(app.exec_())