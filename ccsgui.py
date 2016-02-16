#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path
import sqlite3 as lite
from PyQt4 import QtCore, QtGui

sqlite_file = 'ccs.db'

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

class Ui_Form(QtGui.QMainWindow, QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.con = None

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(820, 460)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(820, 460))
        Form.setMaximumSize(QtCore.QSize(820, 460))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 26, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 33, 33))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 93, 93))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 93, 93))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 93, 93))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("ccs.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStatusTip(_fromUtf8(""))
        Form.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(Form)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 140, 801, 261))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.verticalLayoutWidget_2)
        self.tabWidget.setEnabled(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.tabWidget.setPalette(palette)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.txtEditRaw = QtGui.QTextEdit(self.tab1)
        self.txtEditRaw.setGeometry(QtCore.QRect(0, 0, 778, 208))
        self.txtEditRaw.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.txtEditRaw.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.txtEditRaw.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.txtEditRaw.setTabStopWidth(80)
        self.txtEditRaw.setObjectName(_fromUtf8("txtEditRaw"))
        self.tabWidget.addTab(self.tab1, _fromUtf8(""))
        self.tab2 = QtGui.QWidget()
        self.tab2.setObjectName(_fromUtf8("tab2"))
        self.txtEditDone = QtGui.QTextEdit(self.tab2)
        self.txtEditDone.setGeometry(QtCore.QRect(0, 0, 778, 208))
        self.txtEditDone.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.txtEditDone.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.txtEditDone.setObjectName(_fromUtf8("txtEditDone"))
        self.tabWidget.addTab(self.tab2, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 561, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label.setPalette(palette)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.btnNewCategory = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnNewCategory.setObjectName(_fromUtf8("btnNewCategory"))
        self.horizontalLayout.addWidget(self.btnNewCategory)
        self.btnDeleteCategory = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnDeleteCategory.setObjectName(_fromUtf8("btnDeleteCategory"))
        self.horizontalLayout.addWidget(self.btnDeleteCategory)
        self.cbCategory = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.cbCategory.setObjectName(_fromUtf8("cbCategory"))
        self.horizontalLayout.addWidget(self.cbCategory)
        self.horizontalLayout.setStretch(3, 8)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 50, 561, 41))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.btnNewCommand = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.btnNewCommand.setObjectName(_fromUtf8("btnNewCommand"))
        self.horizontalLayout_3.addWidget(self.btnNewCommand)
        self.btnDeleteCommand = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.btnDeleteCommand.setObjectName(_fromUtf8("btnDeleteCommand"))
        self.horizontalLayout_3.addWidget(self.btnDeleteCommand)
        self.cbCommand = QtGui.QComboBox(self.horizontalLayoutWidget_2)
        self.cbCommand.setObjectName(_fromUtf8("cbCommand"))
        self.horizontalLayout_3.addWidget(self.cbCommand)
        self.horizontalLayout_3.setStretch(3, 8)
        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 90, 561, 41))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_5.addWidget(self.label_3)
        self.btnNewSection = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        self.btnNewSection.setObjectName(_fromUtf8("btnNewSection"))
        self.horizontalLayout_5.addWidget(self.btnNewSection)
        self.btnDeleteSection = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        self.btnDeleteSection.setObjectName(_fromUtf8("btnDeleteSection"))
        self.horizontalLayout_5.addWidget(self.btnDeleteSection)
        self.cbSection = QtGui.QComboBox(self.horizontalLayoutWidget_4)
        self.cbSection.setObjectName(_fromUtf8("cbSection"))
        self.horizontalLayout_5.addWidget(self.cbSection)
        self.horizontalLayout_5.setStretch(3, 8)
        self.btnSave = QtGui.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(723, 410, 81, 29))
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        Form.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 818, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        Form.setMenuBar(self.menubar)
        self.actionOpenFile = QtGui.QAction(Form)
        self.actionOpenFile.setObjectName(_fromUtf8("actionOpenFile"))
        self.actionInfo = QtGui.QAction(Form)
        self.actionInfo.setObjectName(_fromUtf8("actionInfo"))
        self.actionQuit = QtGui.QAction(Form)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionOpenFile)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionInfo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.txtTitle = QtGui.QTextEdit(self.centralwidget)
        self.txtTitle.setGeometry(QtCore.QRect(80, 410, 300, 29))

        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setText("Titulo")
        self.label_5.setGeometry(QtCore.QRect(20, 410, 100, 29))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Command Cheatsheet GUI", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("Form", "Raw", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("Form", "Done", None))
        self.label.setText(_translate("Form", "Category:", None))
        self.label_2.setText(_translate("Form", "Command:", None))
        self.label_3.setText(_translate("Form", "Section:", None))
        self.btnNewCategory.setText(_translate("Form", "New", None))
        self.btnDeleteCategory.setText(_translate("Form", "Delete", None))
        self.btnNewCommand.setText(_translate("Form", "New", None))
        self.btnDeleteCommand.setText(_translate("Form", "Delete", None))
        self.btnNewSection.setText(_translate("Form", "New", None))
        self.btnDeleteSection.setText(_translate("Form", "Delete", None))
        self.btnSave.setText(_translate("Form", "Save", None))
        self.menuFile.setTitle(_translate("Form", "File", None))
        self.menuHelp.setTitle(_translate("Form", "Help", None))
        self.actionOpenFile.setText(_translate("Form", "Open Sqlite file", None))
        self.actionInfo.setText(_translate("Form", "Info", None))
        self.actionQuit.setText(_translate("Form", "Quit", None))

        self.btnNewCategory.clicked.connect(self.addCategory)
        self.btnDeleteCategory.clicked.connect(self.delCategory)
        self.btnNewCommand.clicked.connect(self.addCommand)
        self.btnDeleteCommand.clicked.connect(self.delCommand)
        self.btnNewSection.clicked.connect(self.addSection)
        self.btnDeleteSection.clicked.connect(self.delSection)
        self.btnSave.clicked.connect(self.saveBd)

        self.cbCategory.activated[str].connect(self.onCbCategory_change)
        self.cbCommand.activated[str].connect(self.onCbCommand_change)
        self.cbSection.activated[str].connect(self.onCbSection_change)
        
        self.actionInfo.triggered.connect(self.showInfo)
        self.actionOpenFile.triggered.connect(self.openFile)
        self.actionQuit.triggered.connect(self.exitApp)
  
    def onCbCategory_change(self):
        value = self.cbCategory.currentText()
        select = str("SELECT id_category FROM category WHERE name=\"" + value + "\"")
        self.cbCommand.clear()
        self.cbSection.clear()
        self.txtEditRaw.clear()
        self.txtEditDone.clear()
        self.txtTitle.clear()
        self.getCategories(select)
    
    def onCbCommand_change(self):
        valueCategory = self.cbCategory.currentText()
        select = "SELECT id_category FROM category WHERE name=\"" + str(valueCategory) + "\""
        self.cur.execute(select)
        idCat = self.cur.fetchone()
        valueCmd = self.cbCommand.currentText()
        select = str("SELECT id_command FROM command WHERE name=\"" + valueCmd + "\"" + " AND id_category=" + str(idCat[0]))
        self.cbSection.clear()
        self.txtEditRaw.clear()
        self.txtEditDone.clear()
        self.txtTitle.clear()
        self.getCommands(select)
        
    def onCbSection_change(self):
        valueCmd = self.cbCommand.currentText()
        select = "SELECT id_command FROM command WHERE name=\"" + str(valueCmd) + "\""
        self.cur.execute(select)
        idCmd = self.cur.fetchone()
        valueSect = self.cbSection.currentText()
        select = str("SELECT id_section FROM Section WHERE name=\"" + valueSect + "\"" + " AND id_command=" + str(idCmd[0]))
        self.txtEditRaw.clear()
        self.txtEditDone.clear()
        self.txtTitle.clear()
        self.getSections(select)

    def openFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, "Open File")
        self.openBd(filename)

    def getCategories(self, select):
        self.cur.execute(select)
        rows = self.cur.fetchall()
        if len(rows) > 0:
            if self.cbCategory.count() == 0:
                for r in rows:
                    self.cbCategory.addItem(r[1])
            select = "SELECT * FROM Command WHERE id_category=" + str(rows[0][0])
            self.getCommands(select)

    def getCommands(self, select):
        self.cur.execute(select)
        rows = self.cur.fetchall()
        if len(rows) > 0:
            if self.cbCommand.count() == 0:
                for r in rows:
                    self.cbCommand.addItem(r[2])
            select = "SELECT * FROM Section WHERE id_command=" + str(rows[0][0])
            self.getSections(select)

    def getSections(self, select):
        self.cur.execute(select)
        rows = self.cur.fetchall()
        if len(rows) > 0:
            if self.cbSection.count() == 0:
                for r in rows:
                    self.cbSection.addItem(r[2])
            select = "SELECT * FROM Data WHERE id_section=" + str(rows[0][0])
            self.getData(select)

    def getData(self, select):
        self.cur.execute(select)
        rows = self.cur.fetchall()
        if len(rows) > 0:
            self.txtTitle.setText(rows[0][2])
            self.txtEditRaw.append(rows[0][3])

    def insertDataInCombo(self, comboBox, index_row):
        rows = self.cur.fetchall()
        for r in rows:
            comboBox.addItem(r[index_row])
        return len(rows)

    def openBd(self, filename):
        self.con = lite.connect(str(filename))
        self.cur = self.con.cursor()
        self.cur.execute("PRAGMA foreign_keys = ON")
        self.getAllDataFromBD()

    def getAllDataFromBD(self):
        self.cbCategory.clear()
        self.cbCommand.clear()
        self.cbSection.clear()
        self.txtEditRaw.clear()
        self.txtEditDone.clear()
        self.txtTitle.clear()
        self.getCategories("SELECT * FROM Category")

    def exitApp(self):
        sys.exit()

    def showInfo(self):
        QtGui.QMessageBox.information(self, "Information", "Author: Hector Riesco\nEmail: hectorriesco@hotmail.com", QtGui.QMessageBox.Ok)

    def addCategory(self):
        text, ok = QtGui.QInputDialog.getText(self, 'New Category', 'Enter the name of Category:')
        if ok:
            self.cur.execute("SELECT name FROM category")
            rows = self.cur.fetchall()
            enc = False
            for r in rows:
                if str(text).lower() == r[0].lower():
                    enc = True 
                    break
            if enc:
                QtGui.QMessageBox.information(self, "Information", "This name is in database, try other name.", QtGui.QMessageBox.Ok)
                self.addCategory()
            else:
                if str(text).isalnum():
                    self.cur.execute("INSERT INTO category(name) VALUES(?)", (str(text),))
                    self.con.commit()
                    self.getAllDataFromBD()
                    index = self.cbCategory.count() - 1
                    self.cbCategory.setCurrentIndex(index)
                    self.onCbCategory_change()
                else:
                    QtGui.QMessageBox.information(self, "Information", "The name can only contains letters and numbers.", QtGui.QMessageBox.Ok)
                    self.addCategory()


    def delCategory(self):
        if self.cbCategory.count() > 0:
            reply = QtGui.QMessageBox.question(self, 'Delete Category', 'Are you sure?:', QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
            if reply == QtGui.QMessageBox.Ok:
                value = self.cbCategory.currentText()
                select = str("SELECT id_category FROM category WHERE name=\"" + value + "\"")
                self.cur.execute(select)
                id_cat = self.cur.fetchone()
                self.cur.execute("SELECT id_command FROM command WHERE id_category=?", id_cat)
                id_cmd = self.cur.fetchall() 
                for i in id_cmd:
                    self.cur.execute("SELECT id_section FROM Section WHERE id_command=?", i)
                    id_sect = self.cur.fetchall()
                    for j in id_sect:
                        self.cur.execute("DELETE FROM data WHERE id_section=?", (str(j[0]),))
                    self.cur.execute("DELETE FROM section WHERE id_command=?", (str(i[0]),))
                self.cur.execute("DELETE FROM command WHERE id_category=?", (str(id_cat[0]),))
                self.cur.execute("DELETE FROM category WHERE id_category=?", (str(id_cat[0]),))
                self.con.commit()

                self.getAllDataFromBD()
                self.cbCategory.setCurrentIndex(0)
                self.onCbCategory_change()
        else:
            QtGui.QMessageBox.information(self, "Information", "There is no category to remove.", QtGui.QMessageBox.Ok)

    def addCommand(self):
        if self.cbCategory.count() > 0:
            text, ok = QtGui.QInputDialog.getText(self, 'New Command', 'Enter the name of Command:')
            if ok:
                value = self.cbCategory.currentText()
                select = str("SELECT id_category FROM category WHERE name=\"" + value + "\"")
                self.cur.execute(select)
                id_cat = self.cur.fetchone()
                self.cur.execute("SELECT name FROM command WHERE id_category=?", (str(id_cat[0]),))
                rows = self.cur.fetchall()
                enc = False
                for r in rows:
                    if str(text).lower() == r[0].lower():
                        enc = True 
                        break
                if enc:
                    QtGui.QMessageBox.information(self, "Information", "This name is in database, try other name.", QtGui.QMessageBox.Ok)
                    self.addCommand()
                else:
                    if str(text).isalnum():
                        data = [str(id_cat[0]), str(text)]
                        self.cur.execute("INSERT INTO command(id_category, name) VALUES(?,?)", data)
                        self.con.commit()
                        self.cbCommand.addItem(text)
                        index = self.cbCommand.count() - 1
                        self.cbCommand.setCurrentIndex(index)
                        self.onCbCommand_change()
                    else:
                        QtGui.QMessageBox.information(self, "Information", "The name can only contains letters and numbers.", QtGui.QMessageBox.Ok)
                        self.addCommand()
        else:
            QtGui.QMessageBox.information(self, "Information", "There is no category to add a command.", QtGui.QMessageBox.Ok)
        

    def delCommand(self):
        if self.cbCommand.count() > 0:
            reply = QtGui.QMessageBox.question(self, 'Delete Command', 'Are you sure?:', QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
            if reply == QtGui.QMessageBox.Ok:
                value = self.cbCommand.currentText()
                select = str("SELECT id_command FROM command WHERE name=\"" + value + "\"")
                self.cur.execute(select)
                id_cmd = self.cur.fetchone() 
                self.cur.execute("SELECT id_section FROM Section WHERE id_command=?", (str(id_cmd[0]),))
                id_sect = self.cur.fetchall()
                for j in id_sect:
                    self.cur.execute("DELETE FROM data WHERE id_section=?", (str(j[0]),))
                self.cur.execute("DELETE FROM section WHERE id_command=?", (str(id_cmd[0]),))
                self.cur.execute("DELETE FROM command WHERE id_command=?", (str(id_cmd[0]),))
                self.con.commit()

                self.getAllDataFromBD()
                self.cbCommand.setCurrentIndex(0)
                self.onCbCategory_change()
        else:
            QtGui.QMessageBox.information(self, "Information", "There is no command to delete.", QtGui.QMessageBox.Ok)

    def addSection(self):
        if self.cbCommand.count() > 0 and self.cbCategory.count() > 0:
            text, ok = QtGui.QInputDialog.getText(self, 'New Section', 'Enter the name of section:')
            if ok:
                valueCategory = self.cbCategory.currentText()
                select = "SELECT id_category FROM category WHERE name=\"" + str(valueCategory) + "\""
                self.cur.execute(select)
                idCat = self.cur.fetchone()
                valueCmd = self.cbCommand.currentText()
                select = str("SELECT id_command FROM command WHERE name=\"" + valueCmd + "\"" + " AND id_category=" + str(idCat[0]))
                self.cur.execute(select)
                id_cmd = self.cur.fetchone()
                self.cur.execute("SELECT name FROM section WHERE id_command=?", (str(id_cmd[0]),))
                rows = self.cur.fetchall()
                enc = False
                text = unicode(text)
                for r in rows:
                    if str(text).lower() == r[0].lower():
                        enc = True 
                        break
                if enc:
                    QtGui.QMessageBox.information(self, "Information", "This name is in database, try other name.", QtGui.QMessageBox.Ok)
                    self.addSection()
                else:
                    if str(text).isalnum():
                        data = [str(id_cmd[0]), str(text)]
                        self.cur.execute("INSERT INTO section(id_command, name) VALUES(?,?)", data)
                        self.con.commit()
                        self.cbSection.addItem(text)
                        index = self.cbSection.count() - 1
                        self.cbSection.setCurrentIndex(index)
                        self.onCbSection_change()
                    else:
                        QtGui.QMessageBox.information(self, "Information", "The name can only contains letters and numbers.", QtGui.QMessageBox.Ok)
                        self.addSection()
        else:
            QtGui.QMessageBox.information(self, "Information", "There is no command to add a section.", QtGui.QMessageBox.Ok)


    def delSection(self):
        if self.cbSection.count() > 0:
            reply = QtGui.QMessageBox.question(self, 'Delete section', 'Are you sure?:', QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
            if reply == QtGui.QMessageBox.Ok:
                value = self.cbSection.currentText()
                select = str("SELECT id_section FROM section WHERE name=\"" + value + "\"")
                self.cur.execute(select)
                id_sect = self.cur.fetchone() 
                self.cur.execute("DELETE FROM data WHERE id_section=?", (str(id_sect[0]),))
                self.cur.execute("DELETE FROM section WHERE id_section=?", (str(id_sect[0]),))
                self.con.commit()

                self.getAllDataFromBD()
                self.cbSection.setCurrentIndex(0)
                self.onCbCategory_change()
        else:
            QtGui.QMessageBox.information(self, "Information", "There is no section to delete.", QtGui.QMessageBox.Ok)
        


    def saveBd(self):
        value = self.cbSection.currentText()
        select = str("SELECT id_section FROM section WHERE name=\"" + value + "\"")
        self.cur.execute(select)
        id_sect = self.cur.fetchone()
        value = self.cbCommand.currentText()
        self.cur.execute("SELECT COUNT(*) FROM data WHERE id_section=?", (str(id_sect[0]),))
        items = self.cur.fetchone()
        title = self.txtTitle.toPlainText()
        text = self.txtEditRaw.toPlainText()
        title = unicode(title)
        text = unicode(text)
        if int(items[0]) > 0:
            self.cur.execute("UPDATE data SET title=?, text=? WHERE id_section=?", (title, text, id_sect[0]))
        else:
            self.cur.execute("INSERT INTO data(id_section, title, text) VALUES(?,?,?)", (id_sect[0], title, text))
        QtGui.QMessageBox.information(self, "Information", "Data were up to date.", QtGui.QMessageBox.Ok)
        self.con.commit()


    def __del__(self):
        if self.con != None:
            self.con.close()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Ui_Form()
    if os.path.exists(sqlite_file):
        window.openBd(sqlite_file)
    window.show()
    sys.exit(app.exec_())
