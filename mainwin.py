# Form implementation generated from reading ui file 'mainwin.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(354, 401)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 351, 351))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(parent=self.tab)
        self.lcdNumber_3.setGeometry(QtCore.QRect(80, 160, 211, 51))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(parent=self.tab)
        self.lcdNumber_2.setGeometry(QtCore.QRect(80, 80, 211, 51))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label = QtWidgets.QLabel(parent=self.tab)
        self.label.setGeometry(QtCore.QRect(10, 30, 54, 17))
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(parent=self.tab)
        self.lcdNumber.setGeometry(QtCore.QRect(80, 10, 211, 51))
        self.lcdNumber.setMouseTracking(False)
        self.lcdNumber.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.lcdNumber.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_2 = QtWidgets.QLabel(parent=self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 54, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 54, 16))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(parent=self.tab_2)
        self.lcdNumber_4.setGeometry(QtCore.QRect(0, 0, 341, 101))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.pushButton = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 120, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 120, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 354, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyQt-clock"))
        self.label.setText(_translate("MainWindow", "当前时间"))
        self.label_2.setText(_translate("MainWindow", "当前日期"))
        self.label_3.setText(_translate("MainWindow", "星期"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "时钟"))
        self.pushButton.setText(_translate("MainWindow", "启动秒表"))
        self.pushButton_2.setText(_translate("MainWindow", "清零"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "秒表"))
