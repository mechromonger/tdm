from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QHBoxLayout, QGroupBox, QTableView, QSpinBox, QAction, QToolBar, QHeaderView

# from GUI.DeviceEdit import DeviceEditDialog
from Util import DevMdl, CnsMdl

columns = {
    DevMdl.LWT: ['LWT', False, QHeaderView.ResizeToContents],
    DevMdl.TOPIC: ['Topic', True, QHeaderView.ResizeToContents],
    DevMdl.FULL_TOPIC: ['Full topic', True, QHeaderView.ResizeToContents],
    DevMdl.FRIENDLY_NAME: ['Name', False, QHeaderView.Stretch],
    DevMdl.MODULE: ['Module', False, QHeaderView.Stretch],
    DevMdl.FIRMWARE: ['Firmware', False, QHeaderView.ResizeToContents],
    DevMdl.CORE: ['Core', True, QHeaderView.ResizeToContents],
    DevMdl.MAC: ['MAC', False, QHeaderView.ResizeToContents],
    DevMdl.IP: ['IP', False, QHeaderView.ResizeToContents],
    DevMdl.SSID: ['SSID', True, QHeaderView.ResizeToContents],
    DevMdl.BSSID: ['BSSID', True, QHeaderView.ResizeToContents],
    DevMdl.CHANNEL: ['Channel', True, QHeaderView.ResizeToContents],
    DevMdl.RSSI: ['RSSI', False, QHeaderView.ResizeToContents],
    DevMdl.UPTIME: ['Uptime', False, QHeaderView.ResizeToContents],
    DevMdl.RESTART_REASON: ['Restart reason', True, QHeaderView.ResizeToContents],
    DevMdl.POWER: ['Power', False, QHeaderView.ResizeToContents],
    DevMdl.LOADAVG: ['L. avg', False, QHeaderView.ResizeToContents],
    DevMdl.TELEPERIOD: ['TelePrd.', True, QHeaderView.ResizeToContents],
}

columns_console = {
    CnsMdl.TIMESTAMP: ['Timestamp', False, QHeaderView.ResizeToContents],
    CnsMdl.TOPIC: ['Topic', False, QHeaderView.ResizeToContents],
    CnsMdl.FRIENDLY_NAME: ['Friendly name', False, QHeaderView.ResizeToContents],
    CnsMdl.DESCRIPTION: ['Description', False, QHeaderView.Stretch],
    CnsMdl.PAYLOAD: ['Payload', True, 1],
    CnsMdl.KNOWN: ['Known', True, 1],
}


class VLayout(QVBoxLayout):
    def __init__(self, margin=3, spacing=3, label = '', *args, **kwargs):
        super(VLayout, self).__init__(*args, **kwargs)
        self.setContentsMargins(margin, margin, margin, margin)
        self.setSpacing(spacing)

        if label:
            self.addWidget(QLabel(label))

    def addWidgets(self, widgets):
        for w in widgets:
            self.addWidget(w)


class HLayout(QHBoxLayout):
    def __init__(self, margin=3, spacing=3, label='', *args, **kwargs):
        super(HLayout, self).__init__(*args, **kwargs)
        self.setContentsMargins(margin, margin, margin, margin)
        self.setSpacing(spacing)

        if label:
            self.addWidget(QLabel(label))

    def addWidgets(self, widgets):
        for w in widgets:
            self.addWidget(w)


class GroupBoxV(QGroupBox):
    def __init__(self, title, *args, **kwargs):
        super(GroupBoxV, self).__init__(*args, **kwargs)

        self.setTitle(title)
        self.setLayout(VLayout())


class GroupBoxH(QGroupBox):
    def __init__(self, title, *args, **kwargs):
        super(GroupBoxH, self).__init__(*args, **kwargs)
        self.setTitle(title)

        self.setLayout(HLayout())


class TableView(QTableView):
    def __init__(self, *args, **kwargs):
        super(TableView, self).__init__(*args, **kwargs)
        self.setAlternatingRowColors(True)

        self.horizontalHeader().setHighlightSections(False)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalHeader().setVisible(False)
        self.verticalHeader().setHighlightSections(False)
        # self.verticalHeader().setDefaultSectionSize(24)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.setSelectionBehavior(QTableView.SelectRows)
        self.setSelectionMode(QTableView.SingleSelection)

        self.setEditTriggers(self.NoEditTriggers)

    def setColumnTitles(self, titles):
        for col, title in enumerate(titles):
            self.model().setHeaderData(col, Qt.Horizontal, title)

    def setColumnsHidden(self, columns):
        for col in columns:
            self.setColumnHidden(col, True)

    def setupColumns(self, columns, hidden=None):
        for col, opts in columns.items():
            if not hidden:
                self.setColumnHidden(col, opts[1])

            if type(opts[2]) == int:
                self.setColumnWidth(col, opts[2])

            else:
                self.horizontalHeader().setSectionResizeMode(col, opts[2])

        if hidden:
            for col in hidden:
                self.setColumnHidden(int(col), True)


class SpinBox(QSpinBox):
    def __init__(self, *args, **kwargs):
        super(SpinBox, self).__init__(*args, **kwargs)
        self.setButtonSymbols(self.NoButtons)
        self.setMinimum(kwargs.get('minimum', 1))
        self.setMaximum(kwargs.get('maximum', 65535))
        self.setAlignment(Qt.AlignCenter)
        self.setMaximumWidth(45)


class CheckableAction(QAction):
    def __init__(self, *args, **kwargs):
        super(CheckableAction, self).__init__(*args, **kwargs)
        self.setCheckable(True)


class Toolbar(QToolBar):
    def __init__(self, orientation = Qt.Horizontal, iconsize=32, label_position=Qt.ToolButtonTextUnderIcon, *args, **kwargs):
        super(QToolBar, self).__init__(*args, **kwargs)
        self.setMovable(False)
        self.setIconSize(QSize(iconsize,iconsize))
        self.setOrientation(orientation)
        self.setToolButtonStyle(label_position)


