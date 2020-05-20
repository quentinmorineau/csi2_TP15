from PySide2.QtWidgets import *
from PySide2.QtGui import *
app = QApplication([])

class LabeledTextField(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QHBoxLayout()
        self.label = QLabel("text")
        self.text = QTextEdit()
        self.text.setMaximumHeight(30)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.text)
        self.setLayout(self.layout)

class ConfigurationDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.layout = QVBoxLayout()
        self.adress = LabeledTextField()
        self.user = LabeledTextField()
        self.password = LabeledTextField()
        self.layout.addWidget(self.adress)
        self.layout.addWidget(self.user)
        self.layout.addWidget(self.password)
        self.setLayout(self.layout)

a = ConfigurationDialog()
a.show()
app.exec_()
