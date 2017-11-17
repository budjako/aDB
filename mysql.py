# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Tue Oct 10 00:40:57 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

# libraries
import csv
import re
import os
import time
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QFileDialog


sys.path.insert(0, "..")

if sys.version_info[0] >= 3:
    raw_input = input

import mysqllex
import mysqlparse
import btrees

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

# main window
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        def __init__(self, parent=None):
            super(MainWindow, self).__init__(parent)

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(732, 570)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.centralwidget.setLayout(QtGui.QGridLayout())

        # labels
        self.label = QtGui.QLabel()
        self.label.setGeometry(QtCore.QRect(50, 10, 121, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel()
        self.label_2.setGeometry(QtCore.QRect(420, 10, 121, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        # tables table widget
        self.tablesTW = QtGui.QTableWidget()
        self.tablesTW.setEnabled(True)
        self.tablesTW.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers) # disable editing of cell contents
        self.tablesTW.setGeometry(QtCore.QRect(10, 30, 211, 251))
        self.tablesTW.setStyleSheet(_fromUtf8(""))
        self.tablesTW.setAutoScroll(False)
        self.tablesTW.setAlternatingRowColors(True)
        self.tablesTW.setTextElideMode(QtCore.Qt.ElideNone)
        self.tablesTW.setShowGrid(True)
        self.tablesTW.setGridStyle(QtCore.Qt.SolidLine)
        self.tablesTW.setWordWrap(False)
        self.tablesTW.setCornerButtonEnabled(False)
        self.tablesTW.setObjectName(_fromUtf8("tablesTW"))
        self.tablesTW.setColumnCount(1)
        self.tablesTW.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tablesTW.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablesTW.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablesTW.setItem(0, 0, item)
        self.tablesTW.horizontalHeader().setVisible(True)
        self.tablesTW.horizontalHeader().setCascadingSectionResizes(False)
        self.tablesTW.horizontalHeader().setHighlightSections(False)
        self.tablesTW.horizontalHeader().setStretchLastSection(True)
        self.tablesTW.verticalHeader().setVisible(False)
        self.tablesTW.verticalHeader().setSortIndicatorShown(False)
        self.tablesTW.verticalHeader().setStretchLastSection(False)

        self.tablesTW.cellClicked.connect(self.tableClick)

        # column - data type table widget
        self.coldatatypeTW = QtGui.QTableWidget()
        self.coldatatypeTW.setEnabled(True)
        self.coldatatypeTW.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers) # disable editing of cell contents
        self.coldatatypeTW.setGeometry(QtCore.QRect(10, 290, 211, 231))
        self.coldatatypeTW.setStyleSheet(_fromUtf8(""))
        self.coldatatypeTW.setAutoScroll(False)
        self.coldatatypeTW.setAlternatingRowColors(True)
        self.coldatatypeTW.setTextElideMode(QtCore.Qt.ElideNone)
        self.coldatatypeTW.setShowGrid(True)
        self.coldatatypeTW.setGridStyle(QtCore.Qt.SolidLine)
        self.coldatatypeTW.setWordWrap(False)
        self.coldatatypeTW.setCornerButtonEnabled(False)
        self.coldatatypeTW.setObjectName(_fromUtf8("coldatatypeTW"))
        self.coldatatypeTW.setColumnCount(2)
        self.coldatatypeTW.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.coldatatypeTW.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.coldatatypeTW.setHorizontalHeaderItem(1, item)
        self.coldatatypeTW.horizontalHeader().setVisible(True)
        self.coldatatypeTW.horizontalHeader().setCascadingSectionResizes(False)
        self.coldatatypeTW.horizontalHeader().setHighlightSections(False)
        self.coldatatypeTW.horizontalHeader().setStretchLastSection(True)
        self.coldatatypeTW.verticalHeader().setVisible(False)
        self.coldatatypeTW.verticalHeader().setSortIndicatorShown(False)
        self.coldatatypeTW.verticalHeader().setStretchLastSection(False)

        # query result table widget
        self.queryResultTW = QtGui.QTableWidget()
        self.queryResultTW.setEnabled(True)
        self.queryResultTW.setGeometry(QtCore.QRect(230, 320, 491, 201))
        self.queryResultTW.setStyleSheet(_fromUtf8(""))
        self.queryResultTW.setAutoScroll(False)
        self.queryResultTW.setAlternatingRowColors(True)
        self.queryResultTW.setTextElideMode(QtCore.Qt.ElideNone)
        self.queryResultTW.setShowGrid(True)
        self.queryResultTW.setGridStyle(QtCore.Qt.SolidLine)
        self.queryResultTW.setWordWrap(False)
        self.queryResultTW.setCornerButtonEnabled(False)
        self.queryResultTW.setObjectName(_fromUtf8("queryResultTW"))
        self.queryResultTW.setColumnCount(0)
        self.queryResultTW.setRowCount(0)
        self.queryResultTW.horizontalHeader().setVisible(True)
        self.queryResultTW.horizontalHeader().setCascadingSectionResizes(False)
        self.queryResultTW.horizontalHeader().setHighlightSections(False)
        self.queryResultTW.horizontalHeader().setStretchLastSection(False)
        self.queryResultTW.verticalHeader().setVisible(False)
        self.queryResultTW.verticalHeader().setSortIndicatorShown(False)
        self.queryResultTW.verticalHeader().setStretchLastSection(False)


        # execute one line push button
        self.lineBtn = QtGui.QPushButton()
        self.lineBtn.setGeometry(QtCore.QRect(300, 285, 211, 27))
        self.lineBtn.setObjectName(_fromUtf8("lineBtn"))
        self.lineBtn.setStatusTip("Execute line under cursor")
        self.lineBtn.clicked.connect(self.lineExec)     # save a line in text edit content

        # execute all push button
        self.allBtn = QtGui.QPushButton()
        self.allBtn.setGeometry(QtCore.QRect(520, 285, 98, 27))
        self.allBtn.setObjectName(_fromUtf8("allBtn"))
        self.allBtn.setStatusTip("Execute all")
        self.allBtn.clicked.connect(self.allExec)       # save all text edit contents

        # text edit
        self.textEdit = QtGui.QTextEdit()
        self.textEdit.setGeometry(QtCore.QRect(230, 30, 491, 251))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        # menubar
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 732, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        # menubar files
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)

        # status bar
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        # actions
        # import action
        self.actionImport = QtGui.QAction(MainWindow)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))
        self.actionImport.setShortcut("Ctrl+I")
        self.actionImport.setStatusTip("Import database file")
        self.actionImport.triggered.connect(self.importDB)
        # exit action
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit.setShortcut("Ctrl+X")
        self.actionExit.setStatusTip("Close the application")
        self.actionExit.triggered.connect(self.exitApp)

        # add actions to respective menu file
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        # positioning of widgets in the QGridLayout
        self.centralwidget.layout().addWidget(self.label, 0, 0, QtCore.Qt.AlignCenter)
        self.centralwidget.layout().addWidget(self.label_2, 0, 1, 1, 2, QtCore.Qt.AlignCenter)
        self.centralwidget.layout().addWidget(self.tablesTW, 1, 0)
        self.centralwidget.layout().addWidget(self.textEdit, 1, 1, 1, 2)
        self.centralwidget.layout().addWidget(self.coldatatypeTW, 2, 0, 2, 1)
        self.centralwidget.layout().addWidget(self.lineBtn, 2, 1)
        self.centralwidget.layout().addWidget(self.allBtn, 2, 2)
        self.centralwidget.layout().addWidget(self.queryResultTW, 3, 1, 1, 2)

        # set focus to textedit widget upon opening the window
        self.textEdit.setFocus(True)

        # make only the columns on the right stretchable
        self.centralwidget.layout().setColumnStretch(0, 0)
        self.centralwidget.layout().setColumnStretch(1, 1)
        self.centralwidget.layout().setColumnStretch(2, 1)

        self.centralwidget.layout().setSpacing(10)

        self.populateTables()

        self.retranslateUi(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        item = self.tablesTW.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Tables", None))
        self.label.setText(_translate("MainWindow", "Database Schema", None))
        item = self.coldatatypeTW.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Column", None))
        item = self.coldatatypeTW.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Datatype", None))
        self.lineBtn.setText(_translate("MainWindow", "Execute Line Under Cursor", None))
        self.allBtn.setText(_translate("MainWindow", "Execute All", None))
        self.label_2.setText(_translate("MainWindow", "Command Editor", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionImport.setText(_translate("MainWindow", "Import", None))

    # exit function
    def exitApp(self, event):
        quit_msg = "Are you sure you want to exit the program?"
        reply = QtGui.QMessageBox.question(self.centralwidget, 'Message',
                         quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            sys.exit()
            return
        else:
            return

    # import db function (edit this)
    def importDB(self):
        print("Edit importDB function")

        dlg = QtGui.QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        filenames = list()

        if dlg.exec_():
         filenames = dlg.selectedFiles()
         f = open(filenames[0], 'rU')
         # with f:
         #    data = f.read()
         #    print(data)
        a =0
        nameOfFile = os.path.basename(f.name[:-4])
        append = open(nameOfFile + ".dat", 'a')
        tableColumns = []
        tableStringEx = "("
        print(f.name[:])
        if f.name[-4:] == ('.csv'):

            # Show QInputDialog with dropdown list to choose which table to import into
            self.dropdown, ok = QtGui.QInputDialog.getItem(self.centralwidget, "Select table name", "", list(tables.keys()), 0, False )

            if ok and self.dropdown:
                print(self.dropdown)

                reader = csv.reader(f)
                for row in reader:
                    if a == 0:                                          #To get first line
                        for column in row:
                            tableColumns.append(column)
                            tableStringEx = tableStringEx + column + ","
                        tableStringEx=tableStringEx[:-1] + ")"
                        a+=1
                    else:
                        dataString = ""
                        for data in row:
                            if data.isdigit() or data == "NULL":
                                dataString += data + ","
                            else:
                                dataString += "'" + data + "',"
                        dataString = dataString[:-1]
                        insertString2 = "INSERT INTO " + self.dropdown + " VALUES(" + dataString + ");"                      #Without column names
                        # print(insertString2)
                        # append.write(dataString+";\n")

                        # insertString2 = insertString2.lower()
                        prog = mysqlparse.parse(insertString2)

                        if mysqlparse.operation.lower() == 'insert':
                            #returned_rows = trees[mysqlparse.table_selected].insert
                            errorcheck = trees[mysqlparse.table_selected].insert(mysqlparse.value_list_bool, mysqlparse.column_name_bool, mysqlparse.value_list, mysqlparse.col_name, mysqlparse.assignment_list)
                            if not errorcheck:
                                print("Insert successful")
                            else:
                                print("Error seen")
        elif f.name[-4:] == ('.sql'):
            multiLineCommentFlag = False
            commentRegex = r'/\*|.*\*/|//'
            for line in iter(f):
                if re.match(commentRegex, line) and not multiLineCommentFlag:
                    multiLineCommentFlag = True
                    # print "Start"
                elif re.match(commentRegex, line) and multiLineCommentFlag:
                    multiLineCommentFlag = False
                    # print "End"
                elif not multiLineCommentFlag and not re.match(commentRegex, line):
                    # print(line[line.find("VALUES (")+1:line.find(");")])                      #Will then be sent to finished parser
                    line = line.lower()
                    prog = mysqlparse.parse(line)

                    if mysqlparse.operation == 'insert':
                        #returned_rows = trees[mysqlparse.table_selected].insert
                        errorcheck = trees[mysqlparse.table_selected].insert(mysqlparse.value_list_bool, mysqlparse.column_name_bool, mysqlparse.value_list, mysqlparse.col_name, mysqlparse.assignment_list)
                        if not errorcheck:
                            print("Insert successful")
                        else:
                            print("Error seen")
                    # print(line)
                    # # print(tables[nameOfFile])
                    # if(line[line.find(nameOfFile)+len(nameOfFile):line.find("VALUES")].strip() == ""):
                    #     # append.write(line[line.find("VALUES (")+6:line.find(");")+2])
                    #     print(line[line.find("VALUES (")+6:line.find(");")+2])
                    # else:
                    #     print("with column names")
        else:
            self.showErrorDialog("Only csv and sql files are accepted!", "File type error")

        f.close()
        append.close()

    def populateTables(self):
        i=0
        # print(tables)
        # print("keys")
        # print(keys)
        for i in range(0,len(keys)):                        # for each table specified in the metadata
            pos = self.tablesTW.rowCount()                       # create a corresponding row
            self.tablesTW.insertRow(pos)
            self.tablesTW.setItem(i,0, QtGui.QTableWidgetItem(keys[i]))

    # show query result
    def showQueryResult(self, results):
        print('showQueryResult')
        print(results)
        self.queryResultTW.clear()
        self.queryResultTW.clearContents()
        self.queryResultTW.setColumnCount(0)
        self.queryResultTW.setRowCount(0)

        # create table size
        if results:
            col = (len(results[0]))
            self.queryResultTW.setColumnCount(col)

            # add column names to table
            self.queryResultTW.setHorizontalHeaderLabels(results[0])

            print(len(results))
            if(len(results) == 0):
                return
            if(len(results) == 1):
                pos = self.queryResultTW.rowCount()                       # create a corresponding row
                self.queryResultTW.insertRow(pos)
                for j in range(0, len(results[0])):
                    self.queryResultTW.setItem(pos,j, QtGui.QTableWidgetItem("NULL"))
            for i in range(1, len(results)):
                pos = self.queryResultTW.rowCount()                       # create a corresponding row
                self.queryResultTW.insertRow(pos)
                for j in range(0, len(results[i])):
                    self.queryResultTW.setItem(pos,j, QtGui.QTableWidgetItem(str(results[i][j])))

            # adjust size of table according to contents
            self.queryResultTW.resizeColumnsToContents()
            self.queryResultTW.resizeRowsToContents()


    @pyqtSlot()
    def addColumnNamesAndDataTypes():
        for column in tables['table']:                        # for each table specified in the metadata
            print(column)

    def clearGlobals(self):
        mysqlparse.operation = None
        mysqlparse.columns = []
        mysqlparse.table_selected = None
        mysqlparse.withcondition = False
        mysqlparse.value_list = None
        mysqlparse.assignment_list = None
        mysqlparse.value_list_bool = False
        mysqlparse.column_name_bool = False
        mysqlparse.col_name = None
        mysqlparse.comp_operator = None
        mysqlparse.cond_exp = None
        mysqlparse.error1 = None

    # execute one line in text edit
    def lineExec(self):
        # text edit cursor
        cursor = self.textEdit.textCursor()
        # curPos = cursor.blockNumber() + 1                   # position of the cursor in text edit
        cursor.select(QtGui.QTextCursor.LineUnderCursor)

        selText = cursor.selectedText()            # save content of line under cursor in text edit
        # print("selText")
        # selText = "insert into student values ('2013-12345', 'Juan Dela Cruz', '1994-01-01', 'BS Computer Science', 'Security', 144);"
        # selText = "insert into student values ('2013-12345', 'Juan Dela Cruz', '1994-01-01', 'BS Computer Science', 'Security', 144);"
        print(selText)

        prog = mysqlparse.parse(selText)
        print('operation: ', mysqlparse.operation)
        print('columns: ', mysqlparse.columns)           #
        print('table_selected: ', mysqlparse.table_selected)
        print('withcondition: ', mysqlparse.withcondition)     #
        print('condition: ', mysqlparse.condition)     #
        print('value_list: ', mysqlparse.value_list)
        print('assignment_list: ', mysqlparse.assignment_list)
        print('value_list_bool: ', mysqlparse.value_list_bool)       #
        print('column_name_bool: ', mysqlparse.column_name_bool)
        print('col_name: ', mysqlparse.col_name)
        print('comp_operator: ', mysqlparse.comp_operator)
        print('cond_exp: ', mysqlparse.cond_exp)

        # print('\ntrees: ', trees)
        mysqlparse.table_selected = mysqlparse.table_selected.lower()
        if mysqlparse.operation.lower() == 'select':
            returned_rows = trees[mysqlparse.table_selected].select(mysqlparse.columns, mysqlparse.withcondition, mysqlparse.condition, mysqlparse.col_name, mysqlparse.comp_operator, mysqlparse.cond_exp)
            self.showQueryResult(returned_rows)

        if mysqlparse.operation.lower() == 'delete':
            returned_rows = trees[mysqlparse.table_selected].delete(mysqlparse.columns, mysqlparse.withcondition, mysqlparse.col_name, mysqlparse.comp_operator, mysqlparse.cond_exp)
            self.showQueryResult(returned_rows)

        if mysqlparse.operation.lower() == 'insert':
            #returned_rows = trees[mysqlparse.table_selected].insert
            errorcheck = trees[mysqlparse.table_selected].insert(mysqlparse.value_list_bool, mysqlparse.column_name_bool, mysqlparse.value_list, mysqlparse.col_name, mysqlparse.assignment_list)
            if errorcheck is None:
                print("Insert successful")
            else:
                print("Error seen")
                self.showErrorDialog(errorcheck,"Error at Insert")


        self.clearGlobals()
    # execute all lines in text edit
    def allExec(self):
        # count lines in text edit
        self.textEdit.moveCursor(QtGui.QTextCursor.End)
        self.textEdit.setFocus(True)
        cursor = self.textEdit.textCursor()
        curEnd = cursor.blockNumber() + 1

        # print(curEnd)

        # start at the beginning of text edit
        self.textEdit.moveCursor(QtGui.QTextCursor.Start)

        for i in range(0, curEnd):
            # save line in text edit
            cursor = self.textEdit.textCursor()
            cursor.select(QtGui.QTextCursor.LineUnderCursor)
            selText = cursor.selectedText().lower()

            selText = cursor.selectedText().lower()            # save content of line under cursor in text edit
            # print("selText")
            print(selText)

            selText = selText.lower()
            prog = mysqlparse.parse(selText)
            print(mysqlparse.operation)

            # move to next line
            curPos = cursor.blockNumber() + 1
            self.textEdit.moveCursor(QtGui.QTextCursor.Down)


    # no query prompt method
    def noQuery(self):
        self.noQueryMsgBox = QtGui.QMessageBox()
        self.noQueryMsgBox.setWindowTitle('My Database (Error)')
        self.noQueryMsgBox.setWindowIcon(QtGui.QIcon('dblogo.png'))
        self.noQueryMsgBox.setIcon(QtGui.QMessageBox.Warning)
        self.noQueryMsgBox.setText('Syntax Error')
        self.noQueryMsgBox.addButton(QtGui.QMessageBox.Ok)
        self.noQueryMsgBox.show()


    @pyqtSlot()
    def tableClick(self, row, column):
        self.coldatatypeTW.clearContents()
        self.coldatatypeTW.setRowCount(len(tables[keys[row]]))

        columns = list(tables[keys[row]].keys())

        for i in range(0, len(columns)):                                                  # insert rows in the table
            self.coldatatypeTW.setItem(i,0, QtGui.QTableWidgetItem(columns[i]))           # column
            self.coldatatypeTW.setItem(i,1, QtGui.QTableWidgetItem(tables[keys[row]][columns[i]]))         # datatype

    def showErrorDialog(self, errormessage, errortitle):
        self.fileNameError = QtGui.QMessageBox()
        self.fileNameError.setIcon(QtGui.QMessageBox.Warning)
        self.fileNameError.setText(errormessage)
        self.fileNameError.setWindowTitle(errortitle)
        self.fileNameError.addButton(QtGui.QMessageBox.Ok)
        self.fileNameError.show()


trees = {}
tables = {}
keys = []
textIn = ''

if __name__ == "__main__":
    tables = mysqllex.tables
    keys = list(tables.keys())


    # for i in range(0, 1):
        # trees['course'] = btrees.TableBTree('course', tables['course'])
        # trees['course'].saveToFile()
        # trees['courseoffering'] = btrees.TableBTree('courseoffering', tables['courseoffering'])
        # trees['student'] = btrees.TableBTree('student', tables['student'])
        # trees['studenthistory'] = btrees.TableBTree('studenthistory', tables['studenthistory'])
        # trees['studcourse'] = btrees.TableBTree('studcourse', tables['studcourse'])

    print("trees")
    for i in range(0, len(keys)):
        trees[keys[i]] = btrees.TableBTree(keys[i], tables[keys[i]])
        # trees[keys[i]].saveToFile()
    print(list(trees['student'].data))

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle('My Database')
    MainWindow.setWindowIcon(QtGui.QIcon('dblogo.png'))
    MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
    MainWindow.show()
    sys.exit(app.exec_())
