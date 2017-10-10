# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Tue Oct 10 00:40:57 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSlot

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
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(732, 549)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 211, 251))
        self.tableWidget.setStyleSheet(_fromUtf8(""))
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 121, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(230, 30, 491, 251))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.tableWidget_2 = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget_2.setEnabled(True)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 290, 211, 231))
        self.tableWidget_2.setStyleSheet(_fromUtf8(""))
        self.tableWidget_2.setAutoScroll(False)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setTextElideMode(QtCore.Qt.ElideNone)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_2.setWordWrap(False)
        self.tableWidget_2.setCornerButtonEnabled(False)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setHighlightSections(False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 285, 211, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 285, 98, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 10, 121, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tableWidget_3 = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget_3.setEnabled(True)
        self.tableWidget_3.setGeometry(QtCore.QRect(230, 320, 491, 201))
        self.tableWidget_3.setStyleSheet(_fromUtf8(""))
        self.tableWidget_3.setAutoScroll(False)
        self.tableWidget_3.setAlternatingRowColors(True)
        self.tableWidget_3.setTextElideMode(QtCore.Qt.ElideNone)
        self.tableWidget_3.setShowGrid(True)
        self.tableWidget_3.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_3.setWordWrap(False)
        self.tableWidget_3.setCornerButtonEnabled(False)
        self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.tableWidget_3.horizontalHeader().setVisible(True)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.horizontalHeader().setHighlightSections(False)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_3.verticalHeader().setStretchLastSection(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 732, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionImport = QtGui.QAction(MainWindow)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.populateTables()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Tables", None))
        self.label.setText(_translate("MainWindow", "Database Schema", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Column", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Datatype", None))
        self.pushButton.setText(_translate("MainWindow", "Execute Line Under Cursor", None))
        self.pushButton_2.setText(_translate("MainWindow", "Execute All", None))
        self.label_2.setText(_translate("MainWindow", "Command Editor", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionImport.setText(_translate("MainWindow", "Import", None))

    def populateTables(self):
        i=0
        for table in tables:                        # for each table specified in the metadata
            pos = self.tableWidget.rowCount()       # create a corresponding row
            self.tableWidget.insertRow(pos)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(pos, item)

            item = QtGui.QTableWidgetItem()
            item.setText(table)
            self.tableWidget.setItem(i,0,item)
            i=i+1


                    # pos = self.tableWidget.rowCount()       # create a corresponding row
                    # self.tableWidget.insertRow(pos)
                    # item = QtGui.QTableWidgetItem()
                    # self.tableWidget.setVerticalHeaderItem(pos, item)
                    #
                    # item = QtGui.QTableWidgetItem()
                    # item.setText(table)
                    # self.tableWidget.setItem(i,0,item)
                    # i=i+1

            # item.itemClicked.connect(self.addColumnNamesAndDataTypes)
            # @pyqtSlot()
            # item.tableSelect():
            #     print("a table entry was selected")
            #     item.itemClicked.connect(tableSelect)
    @pyqtSlot()
    def addColumnNamesAndDataTypes():
        for column in tables['table']:                        # for each table specified in the metadata
            print(column)
tables = {}

def readMetadata():
    metadata = open("metadata.txt", "r")

    for line in metadata:
        nonewline = line.rstrip('\n')
        print(nonewline);
        tokens = nonewline.split(" ")
        tokens.reverse()
        tablename = tokens.pop()
        tokens.reverse()
        for i in range(0,len(tokens)):
            tokens[i] = tokens[i]
            # tokens[i] = str.lower(tokens[i])
        tables[str.lower(tablename)] = tokens
    # print(tables)

if __name__ == "__main__":
    readMetadata()
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
