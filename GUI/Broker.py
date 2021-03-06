from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QDialog, QLineEdit, QFormLayout, QPushButton, QGroupBox

from GUI import SpinBox, HLayout, VLayout


class BrokerDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(BrokerDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle("MQTT Broker")

        self.settings = QSettings()

        gbHost = QGroupBox("Hostname and port")
        hfl = QFormLayout()
        self.hostname = QLineEdit()
        self.hostname.setText(self.settings.value("hostname", "localhost"))
        self.port = SpinBox(maximum=65535)
        self.port.setValue(self.settings.value("port", 1883, int))
        hfl.addRow("Hostname", self.hostname)
        hfl.addRow("Port", self.port)
        gbHost.setLayout(hfl)

        gbLogin = QGroupBox("Credentials [optional]")
        lfl = QFormLayout()
        self.username = QLineEdit()
        self.username.setText(self.settings.value("username", ""))
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.password.setText(self.settings.value("password", ""))
        lfl.addRow("Username", self.username)
        lfl.addRow("Password", self.password)
        gbLogin.setLayout(lfl)

        hlBtn = HLayout()
        btnSave = QPushButton("Save")
        btnCancel = QPushButton("Cancel")
        hlBtn.addWidgets([btnSave, btnCancel])

        vl = VLayout()
        vl.addWidgets([gbHost, gbLogin])
        vl.addLayout(hlBtn)

        self.setLayout(vl)

        btnSave.clicked.connect(self.accept)
        btnCancel.clicked.connect(self.reject)

    def accept(self):
        self.settings.setValue("hostname", self.hostname.text())
        self.settings.setValue("port", self.port.value())
        self.settings.setValue("username", self.username.text())
        self.settings.setValue("password", self.password.text())
        self.settings.sync()
        self.done(QDialog.Accepted)
