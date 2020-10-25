# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 's:\write_tutorial\code\pyqt5-basic-tutorial\1-2\one.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(529, 326)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/1-2/Icon/call_merge-24px.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.name_lab = QtWidgets.QLineEdit(self.centralwidget)
        self.name_lab.setObjectName("name_lab")
        self.horizontalLayout.addWidget(self.name_lab)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.sex_lab = QtWidgets.QLineEdit(self.centralwidget)
        self.sex_lab.setObjectName("sex_lab")
        self.horizontalLayout_2.addWidget(self.sex_lab)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.close_btn = QtWidgets.QPushButton(self.centralwidget)
        self.close_btn.setObjectName("close_btn")
        self.verticalLayout.addWidget(self.close_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 529, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.menuFile.addAction(self.actionNew)
        self.menubar.addAction(self.menuFile.menuAction())
        self.label.setBuddy(self.name_lab)
        self.label_2.setBuddy(self.sex_lab)

        self.retranslateUi(MainWindow)
        self.close_btn.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.close_btn, self.name_lab)
        MainWindow.setTabOrder(self.name_lab, self.sex_lab)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hellow"))
        self.label.setText(_translate("MainWindow", "姓名：(&T)"))
        self.label_2.setText(_translate("MainWindow", "性别：(&U)"))
        self.close_btn.setText(_translate("MainWindow", "PushButton"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
import new_rc
