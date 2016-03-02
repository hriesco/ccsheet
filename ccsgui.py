# -*- coding: utf-8 -*-

import sys
import os.path
import sqlite3 as lite
from PyQt4 import QtCore, QtGui

sqlite_file = 'ccs.db'
isOpenBd = False

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
        self.dicCat = {}
        self.dicCmd = {}
        self.dicSec = {}
        self.dicTit = {}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(782, 544)
        MainWindow.setMaximumSize(QtCore.QSize(782, 544))
        MainWindow.setMinimumSize(QtCore.QSize(782, 544))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("ccs.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 761, 501))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridButtons = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridButtons.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.gridButtons.setContentsMargins(-1, -1, 0, -1)
        self.gridButtons.setHorizontalSpacing(6)
        self.gridButtons.setVerticalSpacing(2)
        self.gridButtons.setObjectName(_fromUtf8("gridButtons"))
        self.btnDeleteCommand = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnDeleteCommand.setObjectName(_fromUtf8("btnDeleteCommand"))
        self.gridButtons.addWidget(self.btnDeleteCommand, 1, 3, 1, 1)
        self.btnSaveBd = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnSaveBd.setObjectName(_fromUtf8("btnSaveBd"))
        self.gridButtons.addWidget(self.btnSaveBd, 7, 4, 1, 1)
        self.txtEditRaw = QtGui.QTextEdit(self.gridLayoutWidget)
        self.txtEditRaw.setObjectName(_fromUtf8("txtEditRaw"))
        self.gridButtons.addWidget(self.txtEditRaw, 4, 1, 3, 4)
        self.lblCategory = QtGui.QLabel(self.gridLayoutWidget)
        self.lblCategory.setObjectName(_fromUtf8("lblCategory"))
        self.gridButtons.addWidget(self.lblCategory, 0, 1, 1, 1)
        self.btnNewCategory = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnNewCategory.setObjectName(_fromUtf8("btnNewCategory"))
        self.gridButtons.addWidget(self.btnNewCategory, 0, 2, 1, 1)
        self.cbCategory = QtGui.QComboBox(self.gridLayoutWidget)
        self.cbCategory.setObjectName(_fromUtf8("cbCategory"))
        self.gridButtons.addWidget(self.cbCategory, 0, 4, 1, 1)
        self.lblSection = QtGui.QLabel(self.gridLayoutWidget)
        self.lblSection.setObjectName(_fromUtf8("lblSection"))
        self.gridButtons.addWidget(self.lblSection, 2, 1, 1, 1)
        self.btnDeleteCategory = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnDeleteCategory.setObjectName(_fromUtf8("btnDeleteCategory"))
        self.gridButtons.addWidget(self.btnDeleteCategory, 0, 3, 1, 1)
        self.lblCommand = QtGui.QLabel(self.gridLayoutWidget)
        self.lblCommand.setObjectName(_fromUtf8("lblCommand"))
        self.gridButtons.addWidget(self.lblCommand, 1, 1, 1, 1)
        self.btnNewCommand = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnNewCommand.setObjectName(_fromUtf8("btnNewCommand"))
        self.gridButtons.addWidget(self.btnNewCommand, 1, 2, 1, 1)
        self.cbTitle = QtGui.QComboBox(self.gridLayoutWidget)
        self.cbTitle.setObjectName(_fromUtf8("cbTitle"))
        self.gridButtons.addWidget(self.cbTitle, 3, 4, 1, 1)
        self.cbCommand = QtGui.QComboBox(self.gridLayoutWidget)
        self.cbCommand.setObjectName(_fromUtf8("cbCommand"))
        self.gridButtons.addWidget(self.cbCommand, 1, 4, 1, 1)
        self.btnNewSection = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnNewSection.setObjectName(_fromUtf8("btnNewSection"))
        self.gridButtons.addWidget(self.btnNewSection, 2, 2, 1, 1)
        self.btnDeleteSection = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnDeleteSection.setObjectName(_fromUtf8("btnDeleteSection"))
        self.gridButtons.addWidget(self.btnDeleteSection, 2, 3, 1, 1)
        self.lblTitle = QtGui.QLabel(self.gridLayoutWidget)
        self.lblTitle.setObjectName(_fromUtf8("lblTitle"))
        self.gridButtons.addWidget(self.lblTitle, 3, 1, 1, 1)
        self.btnNewTitle = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnNewTitle.setObjectName(_fromUtf8("btnNewTitle"))
        self.gridButtons.addWidget(self.btnNewTitle, 3, 2, 1, 1)
        self.cbSection = QtGui.QComboBox(self.gridLayoutWidget)
        self.cbSection.setObjectName(_fromUtf8("cbSection"))
        self.gridButtons.addWidget(self.cbSection, 2, 4, 1, 1)
        self.btnDeleteTitle = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnDeleteTitle.setObjectName(_fromUtf8("btnDeleteTitle"))
        self.gridButtons.addWidget(self.btnDeleteTitle, 3, 3, 1, 1)
        self.gridButtons.setColumnStretch(4, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.actionOpenFile = QtGui.QAction(MainWindow)
        self.actionOpenFile.setObjectName(_fromUtf8("actionOpenFile"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionInfo = QtGui.QAction(MainWindow)
        self.actionInfo.setObjectName(_fromUtf8("actionInfo"))
        self.menuFile.addAction(self.actionOpenFile)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionInfo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Command CheatSheet v2.0", None))
        self.btnDeleteCommand.setText(_translate("MainWindow", "Delete", None))
        self.btnSaveBd.setText(_translate("MainWindow", "Save text into Database", None))
        self.lblCategory.setText(_translate("MainWindow", "Category", None))
        self.btnNewCategory.setText(_translate("MainWindow", "New", None))
        self.lblSection.setText(_translate("MainWindow", "Section", None))
        self.btnDeleteCategory.setText(_translate("MainWindow", "Delete", None))
        self.lblCommand.setText(_translate("MainWindow", "Command", None))
        self.btnNewCommand.setText(_translate("MainWindow", "New", None))
        self.btnNewSection.setText(_translate("MainWindow", "New", None))
        self.btnDeleteSection.setText(_translate("MainWindow", "Delete", None))
        self.lblTitle.setText(_translate("MainWindow", "Title", None))
        self.btnNewTitle.setText(_translate("MainWindow", "New", None))
        self.btnDeleteTitle.setText(_translate("MainWindow", "Delete", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionOpenFile.setText(_translate("MainWindow", "Open sqlite file", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionInfo.setText(_translate("MainWindow", "Info", None))

        self.btnNewCategory.clicked.connect(self.addCategory)
        self.btnDeleteCategory.clicked.connect(self.delCategory)
        self.btnNewCommand.clicked.connect(self.addCommand)
        self.btnDeleteCommand.clicked.connect(self.delCommand)
        self.btnNewSection.clicked.connect(self.addSection)
        self.btnDeleteSection.clicked.connect(self.delSection)
        self.btnNewTitle.clicked.connect(self.addTitle)
        self.btnDeleteTitle.clicked.connect(self.delTitle)
        self.btnSaveBd.clicked.connect(self.saveBd)

        self.cbCategory.activated[str].connect(self.onCbCategory_change)
        self.cbCommand.activated[str].connect(self.onCbCommand_change)
        self.cbSection.activated[str].connect(self.onCbSection_change)
        self.cbTitle.activated[str].connect(self.onCbTitle_change)
        
        self.actionInfo.triggered.connect(self.showInfo)
        self.actionOpenFile.triggered.connect(self.openFile)
        self.actionQuit.triggered.connect(self.exitApp)

    def openBd(self, filename):
        openBd = True
        self.con = lite.connect(str(filename))
        self.cur = self.con.cursor()
        self.cur.execute("PRAGMA foreign_keys = ON")
        self.getCategories()

    def exitApp(self):
        sys.exit()

    def showInfo(self):
        QtGui.QMessageBox.information(self, "Information", "Author: Hector Riesco\nEmail: hectorriesco@hotmail.com", QtGui.QMessageBox.Ok)

    def openFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, "Open File")
        self.openBd(filename)

    def onCbCategory_change(self):
        self.getCommands()
    
    def onCbCommand_change(self):
        self.getSections()
        
    def onCbSection_change(self):
        self.getTitles()

    def onCbTitle_change(self):
        self.getData()

    def getCategories(self):
        self.cur.execute("SELECT id_category,name FROM category ORDER BY LOWER(name)")
        rows = self.cur.fetchall()
        if len(rows) > 0:
            self.cbCategory.clear()
            self.dicCat.clear()
            for id_cat, name in rows:
                self.dicCat[str(name)] = id_cat
                self.cbCategory.addItem(str(name))
            self.getCommands()
        else:
            self.cbCategory.clear()
            self.cbCommand.clear()
            self.cbSection.clear()
            self.cbTitle.clear()
            self.txtEditRaw.clear()
            self.dicCat.clear()
            self.dicCmd.clear()
            self.dicSec.clear()
            self.dicTit.clear()

    def getCommands(self):
        if self.cbCategory.count() > 0:
            value = str(self.cbCategory.currentText())
            select = "SELECT id_command,name FROM command WHERE id_category=" + str(self.dicCat[value])  + " ORDER BY LOWER(name)"
            self.cur.execute(select)
            rows = self.cur.fetchall()
            if len(rows) > 0:
                self.cbCommand.clear()
                self.dicCmd.clear()
                for id_cmd, name in rows:
                    self.dicCmd[str(name)] = id_cmd
                    self.cbCommand.addItem(str(name))
                self.getSections()
            else:
                self.cbCommand.clear()
                self.cbSection.clear()
                self.cbTitle.clear()
                self.txtEditRaw.clear()
                self.dicCmd.clear()
                self.dicSec.clear()
                self.dicTit.clear()

    def getSections(self):
        if self.cbCommand.count() > 0:
            value = str(self.cbCommand.currentText())
            select = "SELECT id_section,name FROM section WHERE id_command=" + str(self.dicCmd[value]) + " ORDER BY LOWER(name)"
            self.cur.execute(select)
            rows = self.cur.fetchall()
            if len(rows) > 0:
                self.cbSection.clear()
                self.dicSec.clear()
                for id_sect, name in rows:
                    self.dicSec[str(name)] = id_sect
                    self.cbSection.addItem(str(name))
                self.getTitles()
            else:
                self.cbSection.clear()
                self.cbTitle.clear()
                self.txtEditRaw.clear()
                self.dicSec.clear()
                self.dicTit.clear()

    def getTitles(self):
        if self.cbSection.count() > 0:
            value = str(self.cbSection.currentText())
            select = "SELECT id_data,title,text FROM data WHERE id_section=" + str(self.dicSec[value]) + " ORDER BY LOWER(title)"
            self.cur.execute(select)
            rows = self.cur.fetchall()
            if len(rows) > 0:
                self.cbTitle.clear()
                self.txtEditRaw.clear()
                self.txtEditRaw.append(rows[0][2])
                self.dicTit.clear()
                for id_data, title, text in rows:
                    self.dicTit[str(title)] = id_data
                    self.cbTitle.addItem(str(title))
            else:
                self.cbTitle.clear()
                self.txtEditRaw.clear()
                self.dicTit.clear()

    def getData(self):
        if self.cbTitle.count() > 0:
            nameTitle = str(self.cbTitle.currentText())
            id_data = str(self.dicTit[nameTitle])
            self.cur.execute("SELECT text FROM data WHERE id_data=?", (id_data,))
            row = self.cur.fetchone()
            self.txtEditRaw.clear()
            self.txtEditRaw.setText(row[0])
            
    def addCategory(self):
        if isOpenBd:
            text, ok = QtGui.QInputDialog.getText(self, 'New Category', 'Enter the name of Category:')
            if ok:
                if str(text).isalnum():
                    if str(text) in self.dicCat: 
                        QtGui.QMessageBox.information(self, "Information", "This name is in database, try other name.", QtGui.QMessageBox.Ok)
                        self.addCategory()
                    else:
                        self.cur.execute("INSERT INTO category(name) VALUES(?)", (str(text),))
                        self.con.commit()
                        self.getCategories()
                else:
                    QtGui.QMessageBox.information(self, "Information", "The name can only contains letters and numbers.", QtGui.QMessageBox.Ok)
                    self.addCategory()
        else:
            QtGui.QMessageBox.information(self, "Information", "Not connected to database.", QtGui.QMessageBox.Ok)

    def delCategory(self):
        if self.cbCategory.count() > 0:
            reply = QtGui.QMessageBox.question(self, 'Delete Category', 'Are you sure?:', QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
            if reply == QtGui.QMessageBox.Ok:
                nameCat = str(self.cbCategory.currentText())
                id_cat = str(self.dicCat[nameCat])
                self.cur.execute("SELECT id_command FROM command WHERE id_category=?", (str(self.dicCat[nameCat]),))
                id_cmd = self.cur.fetchall() 
                if len(id_cmd) > 0:
                    for i in id_cmd:
                        self.cur.execute("SELECT id_section FROM Section WHERE id_command=?", i)
                        id_sect = self.cur.fetchall()
                        for j in id_sect:
                            self.cur.execute("DELETE FROM data WHERE id_section=?", (str(j[0]),))
                        self.cur.execute("DELETE FROM section WHERE id_command=?", (str(i[0]),))
                    self.cur.execute("DELETE FROM command WHERE id_category=?", (str(id_cat),))
                self.cur.execute("DELETE FROM category WHERE id_category=?", (str(id_cat),))
                self.con.commit()
                self.getCategories()
        else:
            QtGui.QMessageBox.information(self, "Information", "There is no category to remove.", QtGui.QMessageBox.Ok)

    def addCommand(self):
        if isOpenBd:
            if self.cbCategory.count() > 0:
                text, ok = QtGui.QInputDialog.getText(self, 'New Command', 'Enter the name of Command:')
                if ok:
                    if str(text).isalnum():
                        if str(text) in self.dicCmd: 
                            QtGui.QMessageBox.information(self, "Information", "This name is in database, try other name.", QtGui.QMessageBox.Ok)
                            self.addCommand()
                        else:
                            nameCat = str(self.cbCategory.currentText())
                            id_cat = str(self.dicCat[nameCat])
                            data = [id_cat, str(text)]
                            self.cur.execute("INSERT INTO command(id_category, name) VALUES(?,?)", data)
                            self.con.commit()
                            self.getCommands()
                    else:
                        QtGui.QMessageBox.information(self, "Information", "The name can only contains letters and numbers.", QtGui.QMessageBox.Ok)
                        self.addCommand()
            else:
                QtGui.QMessageBox.information(self, "Information", "Need a category to introduce command", QtGui.QMessageBox.Ok)
        else:
            QtGui.QMessageBox.information(self, "Information", "Not connected to database.", QtGui.QMessageBox.Ok)

    def delCommand(self):
        if self.cbCommand.count() > 0:
            reply = QtGui.QMessageBox.question(self, 'Delete Command', 'Are you sure?:', QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
            if reply == QtGui.QMessageBox.Ok:
                nameCmd = str(self.cbCommand.currentText())
                id_cmd = str(self.dicCmd[nameCmd])
                self.cur.execute("SELECT id_section FROM Section WHERE id_command=?", (id_cmd,))
                id_sect = self.cur.fetchall()
                if len(id_sect) > 0:
                    for j in id_sect:
                        self.cur.execute("DELETE FROM data WHERE id_section=?", (str(j[0]),))
                    self.cur.execute("DELETE FROM section WHERE id_command=?", (str(id_cmd[0]),))
                self.cur.execute("DELETE FROM command WHERE id_command=?", (str(id_cmd[0]),))
                self.con.commit()
                self.getCategories()
        else:
            QtGui.QMessageBox.information(self, "Information", "There is no command to delete.", QtGui.QMessageBox.Ok)

    def addSection(self):
        if isOpenBd:
            if self.cbCommand.count() > 0 and self.cbCategory.count() > 0:
                text, ok = QtGui.QInputDialog.getText(self, 'New Section', 'Enter the name of section:')
                if ok:
                    if str(text).isalnum():
                        if str(text) in self.dicSec: 
                            QtGui.QMessageBox.information(self, "Information", "This name is in database, try other name.", QtGui.QMessageBox.Ok)
                            self.addSection()
                        else:
                            nameCmd = str(self.cbCommand.currentText())
                            id_cmd = str(self.dicCmd[nameCmd])
                            data = [id_cmd, str(text)]
                            self.cur.execute("INSERT INTO section(id_command, name) VALUES(?,?)", data)
                            self.con.commit()
                            self.getSections()
                    else:
                        QtGui.QMessageBox.information(self, "Information", "The name can only contains letters and numbers.", QtGui.QMessageBox.Ok)
                        self.addSection()
            else:
                QtGui.QMessageBox.information(self, "Information", "Need a command to introduce section", QtGui.QMessageBox.Ok)
        else:
            QtGui.QMessageBox.information(self, "Information", "Not connected to database.", QtGui.QMessageBox.Ok)

    def delSection(self):
        if self.cbSection.count() > 0:
            reply = QtGui.QMessageBox.question(self, 'Delete section', 'Are you sure?:', QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
            if reply == QtGui.QMessageBox.Ok:
                nameSect = str(self.cbSection.currentText())
                id_sect = str(self.dicSec[nameSect])
                self.cur.execute("DELETE FROM data WHERE id_section=?", (id_sect,))
                self.cur.execute("DELETE FROM section WHERE id_section=?", (id_sect,))
                self.con.commit()
                self.getCategories()
        else:
            QtGui.QMessageBox.information(self, "Information", "There is no command to delete.", QtGui.QMessageBox.Ok)
   
    def addTitle(self):
        if isOpenBd:
            if self.cbCommand.count() > 0 and self.cbCategory.count() > 0 and self.cbSection.count() > 0:
                text, ok = QtGui.QInputDialog.getText(self, 'New Title', 'Enter the name of title:')
                if ok:
                    if all(x.isalnum() or x.isspace() for x in str(text)):
                        if str(text) in self.dicTit: 
                            QtGui.QMessageBox.information(self, "Information", "This name is in database, try other name.", QtGui.QMessageBox.Ok)
                            self.addTitle()
                        else:
                            nameSect = str(self.cbSection.currentText())
                            id_sect = str(self.dicSec[nameSect])
                            data = [id_sect, str(text), ""]
                            self.cur.execute("INSERT INTO data(id_section, title, text) VALUES(?,?,?)", data)
                            self.con.commit()
                            self.getTitles()
                    else:
                        QtGui.QMessageBox.information(self, "Information", "The name can only contains letters and numbers.", QtGui.QMessageBox.Ok)
                        self.addTitle()
            else:
                QtGui.QMessageBox.information(self, "Information", "Need a section to introduce title", QtGui.QMessageBox.Ok)
        else:
            QtGui.QMessageBox.information(self, "Information", "Not connected to database.", QtGui.QMessageBox.Ok)

    def delTitle(self):
        if self.cbTitle.count() > 0:
            reply = QtGui.QMessageBox.question(self, 'Delete title', 'Are you sure?:', QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
            if reply == QtGui.QMessageBox.Ok:
                nameTitle = str(self.cbTitle.currentText())
                id_data = str(self.dicTit[nameTitle])
                self.cur.execute("DELETE FROM data WHERE id_data=?", (id_data,))
                self.con.commit()
                self.getCategories()
        else:
            QtGui.QMessageBox.information(self, "Information", "There is no command to delete.", QtGui.QMessageBox.Ok)


    def saveBd(self):
        if isOpenBd:
            if self.cbTitle.count() > 0:
                nameTitle = str(self.cbTitle.currentText())
                id_data = str(self.dicTit[nameTitle])
                text = self.txtEditRaw.toPlainText()
                text = unicode(text)
                if not text:
                    QtGui.QMessageBox.information(self, "Information", "Text is empty", QtGui.QMessageBox.Ok)
                else:
                    self.cur.execute("UPDATE data SET text=? WHERE id_data=?", (text, id_data))
                    QtGui.QMessageBox.information(self, "Information", "Data were up to date.", QtGui.QMessageBox.Ok)
                    self.con.commit()
            else:
                QtGui.QMessageBox.information(self, "Information", "Need a tile to save text", QtGui.QMessageBox.Ok)
        else:
            QtGui.QMessageBox.information(self, "Information", "Not connected to database.", QtGui.QMessageBox.Ok)


    def __del__(self):
        if self.con != None:
            self.con.close()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Ui_Form()
    if os.path.exists(sqlite_file):
        window.openBd(sqlite_file)
        isOpenBd = True
    window.show()
    sys.exit(app.exec_())
