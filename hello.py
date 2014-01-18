import sys
from PySide import QtGui, QtCore
from wordplay.onvertercay import OnverterCay

class ExampleWindow (QtGui.QMainWindow):
    
    def __init__(self):
        super(ExampleWindow, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        self.statusBar().showMessage('Ready for ducks')
        self.ex = Example(self)
        self.setCentralWidget(self.ex)
        self.setWindowTitle('Pig Latinizer')    
        self.show()

class Example (QtGui.QWidget):

    def __init__(self, parent):
        super(Example, self).__init__(parent)
        self.mOnverterCay = OnverterCay()
        self.initUI()
        
    def initUI(self):
        
        self.xtTay = QtGui.QLineEdit()
        okButton = QtGui.QPushButton("Onvertcay")
        self.lbl = QtGui.QLabel('test')
        
        okButton.clicked.connect(self.onvertcayText)

        vbox = QtGui.QVBoxLayout()
        
        vbox.addWidget(self.xtTay)
        vbox.addWidget(self.lbl)
        vbox.addWidget(okButton)
        
        self.setLayout(vbox)    
        
        #self.setGeometry(10, 10, 300, 150)
        #self.setWindowTitle('Pig Latinizer')    
        #self.show()
        
    def onvertcayText(self):
        onvertedcayResult = self.mOnverterCay.onvertCay(self.xtTay.text())
        self.lbl.setText(onvertedcayResult)
        
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = ExampleWindow()
    sys.exit(app.exec_())