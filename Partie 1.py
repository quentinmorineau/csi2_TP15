from PySide2.QtWidgets import *
from PySide2.QtGui import *
app = QApplication([])

class SQLClientWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("SQL Client")
        self.setMinimumSize(600,400)
        self.layout = QVBoxLayout()
        self.buttonsPanel = ButtonsPanel()
        self.notificationPanel = QTextEdit()
        self.resultable = QTableWidget(5,3)
        self.resultable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.buttonsPanel)
        self.layout.addWidget(self.notificationPanel)
        self.layout.addWidget(self.resultable)
        self.setLayout(self.layout)

class ButtonsPanel(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QHBoxLayout()
        self.button1 = QPushButton("Configure")
        self.button2 = QPushButton("Connect")
        self.button3 = QPushButton("Disconnect")
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.setLayout(self.layout)

class LabeledTextField(QWidget):
    def __init__(self,text):
        QWidget.__init__(self,text)
        self.layout = QHBoxLayout()
        self.label = QLabel(text)
        self.text = QTextEdit()
        self.text.setMaximumHeight(30)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.text)
        self.setLayout(self.layout)

class ConfigurationDialog(QDialog):
    def __init__(self,text):
        QDialog.__init__(self)
        self.layout = QVBoxLayout()
        ipadress = LabeledTextField("IP adress")
        user = LabeledTextField("user")
        password = LabeledTextField("password")
        self.layout.addWidget(ipadress)
        self.layout.addWidget(user)
        self.layout.addWidget(password)
        self.setLayout(self.layout)

a = SQLClientWindow()
b = ConfigurationDialog()
a.show()
b.show()
app.exec_()
