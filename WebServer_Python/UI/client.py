# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from resources import Icons

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(767, 401)
        Form.setWindowOpacity(1.0)
        Form.setStyleSheet("#Frame{\n"
"    font: 12pt \"Comic Sans MS\";\n"
"    background-color:rgb(214, 214, 214);\n"
"    border-radius:10px;\n"
"}\n"
"QTableWidget{\n"
"    border-radius:5px;\n"
"    border-style:none;\n"
"    border:2px solid;\n"
"    font: 14pt \"幼圆\";\n"
"    color:rgb(168,139,99)\n"
"}\n"
"QTableWidget:focus{\n"
"    border-color:#FF5511;\n"
"}\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Frame = QtWidgets.QFrame(Form)
        self.Frame.setMinimumSize(QtCore.QSize(534, 350))
        self.Frame.setStyleSheet("")
        self.Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame.setObjectName("Frame")
        self.gridLayout = QtWidgets.QGridLayout(self.Frame)
        self.gridLayout.setObjectName("gridLayout")
        self.infoTable = QtWidgets.QTableWidget(self.Frame)
        self.infoTable.setMinimumSize(QtCore.QSize(0, 0))
        self.infoTable.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.infoTable.setStyleSheet("font: 12pt \"Comic Sans MS\";\n"
"\n"
"\n"
"\n"
"")
        self.infoTable.setObjectName("infoTable")
        self.infoTable.setColumnCount(2)
        self.infoTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.infoTable, 1, 0, 1, 1)
        self.top_left_Label = QtWidgets.QLabel(self.Frame)
        self.top_left_Label.setMinimumSize(QtCore.QSize(0, 20))
        self.top_left_Label.setStyleSheet("font: 12pt \"Comic Sans MS\";")
        self.top_left_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.top_left_Label.setObjectName("top_left_Label")
        self.gridLayout.addWidget(self.top_left_Label, 0, 0, 1, 1)
        self.top_right_Label = QtWidgets.QLabel(self.Frame)
        self.top_right_Label.setMinimumSize(QtCore.QSize(0, 20))
        self.top_right_Label.setStyleSheet("font: 12pt \"Comic Sans MS\";")
        self.top_right_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.top_right_Label.setObjectName("top_right_Label")
        self.gridLayout.addWidget(self.top_right_Label, 0, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.Frame)
        self.groupBox.setMinimumSize(QtCore.QSize(250, 120))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setStyleSheet("QComboBox{\n"
"    border:2px solid;\n"
"    border-radius:5px;\n"
"    border-style:none;\n"
"}\n"
"QGroupBox{\n"
"    font: 11pt \"Comic Sans MS\";\n"
"}\n"
"QPushButton{\n"
"    font: 11pt \"Comic Sans MS\";\n"
"    border-radius:25px;\n"
"    border-width:3px;\n"
"    border-style:outset;\n"
"    border-color: rgb(255, 255, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,  \n"
"                                 stop: 0 #ffff00, stop: 0.5 #ffff7f,  \n"
"                                 stop: 1.0 #ffffff);  \n"
"}\n"
"QPushButton:pressed{\n"
"        \n"
"    background-color: rgb(202, 202, 0);\n"
"}\n"
"\n"
"QTextEdit{\n"
"    border-radius:10px;\n"
"    border-style:none;\n"
"    border:2px solid;\n"
"    font: 14pt \"幼圆\";\n"
"    color:rgb(168,139,99)\n"
"}\n"
"QTextEdit:focus{\n"
"    border-color:#FF5511;\n"
"}\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mid_Label = QtWidgets.QLabel(self.groupBox)
        self.mid_Label.setMinimumSize(QtCore.QSize(0, 25))
        self.mid_Label.setStyleSheet("font: 11pt \"Comic Sans MS\";")
        self.mid_Label.setObjectName("mid_Label")
        self.gridLayout_2.addWidget(self.mid_Label, 2, 0, 1, 1)
        self.closeBtn = QtWidgets.QPushButton(self.groupBox)
        self.closeBtn.setMinimumSize(QtCore.QSize(104, 50))
        self.closeBtn.setObjectName("closeBtn")
        self.gridLayout_2.addWidget(self.closeBtn, 4, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 4, 1, 1, 1)
        self.clearBtn = QtWidgets.QPushButton(self.groupBox)
        self.clearBtn.setMinimumSize(QtCore.QSize(104, 50))
        self.clearBtn.setMaximumSize(QtCore.QSize(70, 16777215))
        self.clearBtn.setStyleSheet("")
        self.clearBtn.setObjectName("clearBtn")
        self.gridLayout_2.addWidget(self.clearBtn, 4, 2, 1, 1)
        self.payloadInput = QtWidgets.QTextEdit(self.groupBox)
        self.payloadInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.payloadInput.setObjectName("payloadInput")
        self.gridLayout_2.addWidget(self.payloadInput, 0, 0, 1, 5)
        self.sendBtn = QtWidgets.QPushButton(self.groupBox)
        self.sendBtn.setMinimumSize(QtCore.QSize(0, 50))
        self.sendBtn.setStyleSheet("font: 11pt \"Comic Sans MS\";")
        self.sendBtn.setObjectName("sendBtn")
        self.gridLayout_2.addWidget(self.sendBtn, 4, 0, 1, 1)
        self.serverChoice = QtWidgets.QComboBox(self.groupBox)
        self.serverChoice.setMinimumSize(QtCore.QSize(0, 25))
        self.serverChoice.setStyleSheet("font: 11pt \"Comic Sans MS\";")
        self.serverChoice.setObjectName("serverChoice")
        self.serverChoice.addItem("")
        self.serverChoice.addItem("")
        self.gridLayout_2.addWidget(self.serverChoice, 2, 2, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 4, 3, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.addBtn = QtWidgets.QPushButton(self.Frame)
        self.addBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.addBtn.setStyleSheet("QPushButton{\n"
"    font: 11pt \"Comic Sans MS\";\n"
"    border-radius:15px;\n"
"    border-width:3px;\n"
"    border-style:outset;\n"
"    border-color: rgb(255, 255, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,  \n"
"                                 stop: 0 #ffff00, stop: 0.5 #ffff7f,  \n"
"                                 stop: 1.0 #ffffff);  \n"
"}\n"
"QPushButton:pressed{\n"
"        \n"
"    background-color: rgb(202, 202, 0);\n"
"}\n"
"")
        self.addBtn.setObjectName("addBtn")
        self.verticalLayout_2.addWidget(self.addBtn)
        spacerItem3 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)
        self.subBtn = QtWidgets.QPushButton(self.Frame)
        self.subBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.subBtn.setStyleSheet("QPushButton{\n"
"    font: 11pt \"Comic Sans MS\";\n"
"    border-radius:15px;\n"
"    border-width:3px;\n"
"    border-style:outset;\n"
"    border-color: rgb(255, 255, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,  \n"
"                                 stop: 0 #ffff00, stop: 0.5 #ffff7f,  \n"
"                                 stop: 1.0 #ffffff);  \n"
"}\n"
"QPushButton:pressed{\n"
"        \n"
"    background-color: rgb(202, 202, 0);\n"
"}\n"
"")
        self.subBtn.setObjectName("subBtn")
        self.verticalLayout_2.addWidget(self.subBtn)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.Frame)

        self.retranslateUi(Form)
        self.addBtn.clicked.connect(Form.addRow)
        self.subBtn.clicked.connect(Form.delRow)
        self.closeBtn.clicked.connect(Form.closeWin)
        self.clearBtn.clicked.connect(Form.clearAll)
        self.sendBtn.clicked.connect(Form.sendResquest)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.infoTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Status"))
        item = self.infoTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "E-mail"))
        self.top_left_Label.setText(_translate("Form", "Set Target Person(s)"))
        self.top_right_Label.setText(_translate("Form", "Set Specific content"))
        self.groupBox.setTitle(_translate("Form", "GroupBox"))
        self.mid_Label.setText(_translate("Form", "Choose Service"))
        self.closeBtn.setText(_translate("Form", "Exit"))
        self.clearBtn.setText(_translate("Form", "Clear All"))
        self.sendBtn.setText(_translate("Form", "Send"))
        self.serverChoice.setItemText(0, _translate("Form", "Soap"))
        self.serverChoice.setItemText(1, _translate("Form", "Rest"))
        self.addBtn.setText(_translate("Form", "+"))
        self.subBtn.setText(_translate("Form", "-"))

