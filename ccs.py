#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import getopt
import os

sqlite_file = 'ccs.db'
directory = '/opt/ccsheet/'

class Color():
    def black(self, text, endLine):
        if endLine:
            print chr(27) + "[0;30m" + text + chr(27) + "[0m" 
        else:
            print chr(27) + "[0;30m" + text + chr(27) + "[0m", 
    def red(self, text, endLine):
        if endLine:
            print chr(27) + "[0;31m" + text + chr(27) + "[0m"
        else:
            print chr(27) + "[0;31m" + text + chr(27) + "[0m", 
    def green(self, text, endLine):
        if endLine:
            print chr(27) + "[0;32m" + text + chr(27) + "[0m"
        else:
            print chr(27) + "[0;32m" + text + chr(27) + "[0m", 
    def yellow(self, text, endLine):
        if endLine:
            print chr(27) + "[0;33m" + text + chr(27) + "[0m"
        else:
            print chr(27) + "[0;33m" + text + chr(27) + "[0m", 
    def blue(self, text, endLine):
        if endLine:
            print chr(27) + "[0;34m" + text + chr(27) + "[0m"
        else:
            print chr(27) + "[0;34m" + text + chr(27) + "[0m", 
    def purple(self, text, endLine):
        if endLine:
            print chr(27) + "[0;35m" + text + chr(27) + "[0m"
        else:
            print chr(27) + "[0;35m" + text + chr(27) + "[0m", 
    def aqua(self, text, endLine):
        if endLine:
            print chr(27) + "[0;36m" + text + chr(27) + "[0m"
        else:
            print chr(27) + "[0;36m" + text + chr(27) + "[0m", 
    def gray(self, text, endLine):
        if endLine:
            print chr(27) + "[1;30m" + text + chr(27) + "[0m"
        else:
            print chr(27) + "[1;30m" + text + chr(27) + "[0m", 
    def white(self, text, endLine):
        if endLine:
            print chr(27) + "[1;37m" + text + chr(27) + "[0m"
        else:
            print chr(27) + "[1;37m" + text + chr(27) + "[0m", 
    def light_gray(self, text, endLine):
        if endLine:
            print chr(27) + "[0;37m" + text + chr(27) + "[0m"
        else:
            print chr(27) + "[0;37m" + text + chr(27) + "[0m", 
    def light_red(self, text, endLine):
        if endLine:
            print chr(27) + "[1;31m" + text + chr(27) + "[0m"
        else:
            print chr(27) + "[1;31m" + text + chr(27) + "[0m", 
    def light_green(self, text, endLine):
        if endLine:
            print chr(27) + "[1;32m" + text + chr(27) + "[0m"
        else:
            print chr(27) + "[1;32m" + text + chr(27) + "[0m", 
    def light_yellow(self, text, endLine):
        if endLine:
            print chr(27) + "[1;33m" + text + chr(27) + "[0m"
        else:
            print chr(27) + "[1;33m" + text + chr(27) + "[0m", 
    def light_blue(self, text, endLine):
        if endLine:
            print chr(27) + "[1;34m" + text + chr(27) + "[0m"
        else:
            print chr(27) + "[1;34m" + text + chr(27) + "[0m", 
    def light_purple(self, text, endLine):
        if endLine:
            print chr(27) + "[1;35m" + text + chr(27) + "[0m"
        else:
            print chr(27) + "[1;35m" + text + chr(27) + "[0m", 
    def light_aqua(self, text, endLine):
        if endLine:
            print chr(27) + "[1;36m" + text + chr(27) + "[0m"
        else:
            print chr(27) + "[1;36m" + text + chr(27) + "[0m", 

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def connect():
    con = lite.connect(sqlite_file)
    cur = con.cursor()
    return con, cur

def get_categories(cur):
    cur.execute("SELECT id_category,name FROM category ORDER BY LOWER(name)")
    return cur.fetchall()
def get_names_category(cur, nameCat, myFilter):
    if not myFilter:
        cur.execute("SELECT id_category,name FROM category WHERE LOWER(name)=? ORDER BY LOWER(name)", (nameCat,))
    else:
        value = nameCat[:-1] + '%'
        cur.execute("SELECT id_category,name FROM category WHERE name LIKE ? ORDER BY LOWER(name)", (value,))
    return cur.fetchall()
def get_commands_by_idCat(cur, idCat):
    cur.execute("SELECT id_command,name FROM command WHERE id_category=? ORDER BY LOWER(name)", (idCat,))
    return cur.fetchall()
def get_sections_by_idCmd(cur, idCmd):
    cur.execute("SELECT id_section,name FROM section WHERE id_command=? ORDER BY LOWER(name)", (idCmd,))
    return cur.fetchall()
def get_title_by_idSect(cur, idSect):
    cur.execute("SELECT id_data,title FROM data WHERE id_section=? ORDER BY LOWER(title)", (idSect,))
    return cur.fetchall()
def get_data_by_idData(cur, idSect, idData):
    cur.execute("SELECT text FROM data WHERE id_data=? and id_section=?", (idData, idSect))
    return cur.fetchall()

def get_nameCat_byIdCat(cur, idCat):
    cur.execute("SELECT name FROM category WHERE id_category=?", (idCat,))
    return str(cur.fetchone()[0])
def get_nameCmd_byIdCmd(cur, idCmd):
    cur.execute("SELECT name FROM command WHERE id_command=?", (idCmd,))
    return str(cur.fetchone()[0])
def get_nameSect_byIdSect(cur, idSec):
    cur.execute("SELECT name FROM section WHERE id_section=?", (idSec,))
    return str(cur.fetchone()[0])
def get_nameTitle_byIdData(cur, idData):
    cur.execute("SELECT title FROM data WHERE id_data=?", (idData,))
    return str(cur.fetchone()[0])

def func_print_header_data(cur, idCat, idCmd, idSect):
    cls()
    col = Color()
    col.light_blue("---------------------------------------------------------",True)
    col.light_green(" "+ get_nameCat_byIdCat(cur, idCat), False)
    col.light_blue(">> " + get_nameCmd_byIdCmd(cur, idCmd), False)
    col.light_purple(">> " + get_nameSect_byIdSect(cur, idSect), True)

def func_printData(cur, idCat, idCmd, idSect, idData):
    rows = get_data_by_idData(cur, idSect, idData)   
    if len(rows) > 0:
        col = Color()
        col.light_blue("---------------------------------------------------------",True)
        col.light_red(" " + get_nameTitle_byIdData(cur, idData), True)
        col.light_blue("---------------------------------------------------------",True)
        print rows[0][0]
        print
    else:
        print "No text in this section"

def func_listData(cur, idCat, idCmd, idSect):
    col = Color()
    dic = {}
    rows = get_title_by_idSect(cur, idSect)   
    if len(rows) > 0:
        col.light_aqua("--- DATA --------------------------", True)
        col.light_blue("0)", False)
        col.light_red("EXIT", True)
        col.light_blue("a)", False)
        col.light_red("ALL", True)
        for i, idData, in enumerate(rows):
            dic[i+1] = str(idData[0])
            if i == len(rows) - 1:
                col.light_blue(str(i+1) + ")", False)
                print "%s\t\t" % rows[i][1]
            else:
                col.light_blue(str(i+1) + ")", False)
                print "%s\t\t" % rows[i][1],

        data = raw_input("ID > ")
        if (data == "a"):
            func_print_header_data(cur, idCat, idCmd, idSect)
            for i in dic:
                func_printData(cur, idCat, idCmd, idSect, dic[i])
        else:
            indice = int(data)
            if indice > len(dic) or indice == 0:
                sys.exit(2)
            idData = dic.get(indice)
            func_print_header_data(cur, idCat, idCmd, idSect)
            func_printData(cur, idCat, idCmd, idSect, idData)
    else:
        print "No data in section"

def func_listSections(cur, idCat, idCmd):
    rows = get_sections_by_idCmd(cur, idCmd)   
    if len(rows) > 0:
        col = Color()
        dic = {}
        col.light_aqua("---- SECTIONS ----------------------", True)
        col.light_blue("0)", False)
        col.light_red("EXIT", True)
        for i, idSect, in enumerate(rows):
            dic[i+1] = str(idSect[0])
            if i == len(rows) - 1:
                col.light_blue(str(i+1) + ")", False)
                print "%s\t\t" % rows[i][1]
            else:
                col.light_blue(str(i+1) + ")", False)
                print "%s\t\t" % rows[i][1],

        indice = int(raw_input("ID > "))
        if indice > len(dic) or indice == 0:
            sys.exit(2)
        idSect = dic.get(indice)
        func_listData(cur, idCat, idCmd, idSect)
    else:
        print "No section in command"

def func_listCommands(cur, idCat):
    rows = get_commands_by_idCat(cur, idCat)   
    if len(rows) > 0:
        col = Color()
        dic = {}
        col.light_aqua("---- COMMANDS ---------------------", True)
        col.light_blue("0)", False)
        col.light_red("EXIT", True)
        for i, idCmd, in enumerate(rows):
            dic[i+1] = str(idCmd[0])
            if i == len(rows) - 1:
                col.light_blue(str(i+1) + ")", False)
                print "%s\t\t" % rows[i][1]
            else:
                col.light_blue(str(i+1) + ")", False)
                print "%s\t\t" % rows[i][1],

        indice = int(raw_input("ID > "))
        if indice > len(dic) or indice == 0:
            sys.exit(2)
        idCmd = dic.get(indice)
        func_listSections(cur, idCat, idCmd)
    else:
        print "No command in category"

def func_listCategories(cur, rows = None):
    if rows == None:
        rows = get_categories(cur)
    if len(rows) > 0:
        cls()
        col = Color()
        dic = {}
        col.light_aqua("--- CATEGORIES --------------------", True)
        col.light_blue("0)", False)
        col.light_red("EXIT", True)
        for i, idCat in enumerate(rows):
            dic[i+1] = str(idCat[0])
            if i == len(rows) - 1:
                col.light_blue(str(i+1) + ")", False)
                print "%s\t\t" % rows[i][1]
            else:
                col.light_blue(str(i+1) + ")", False)
                print "%s\t\t" % rows[i][1],
        
        indice = int(raw_input("ID > "))
        if indice > len(dic) or indice == 0:
            sys.exit(2)
        idCat = dic.get(indice)
        func_listCommands(cur, idCat)
    else:
        print "No categories in database"

def func_category(cur, arg):
    myFilter = False
    if arg[-1] == '*':
        myFilter = True

    rows = get_names_category(cur, arg, myFilter)
    if rows:
        func_listCategories(cur, rows)
    else:
        print "This category not exist in database."

def main(cur):
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'lc:h', ['category=', 
                                                            'help',])
    
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    if len(opts) == 0:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit(2)
        elif opt in ('-l'):
            func_listCategories(cur)
        elif opt in ('-c', '--category'):
            func_category(cur, str(arg).lower())
        else:
            usage()
            sys.exit(2)

def usage():
    print "\n usage: " + sys.argv[0] + " <parameter>"
    print """
    -h --help                  Print this
    -l                         List all categories in database
    -c --category <name[*]>    List category with name
    """
    print "Examples:"
    print "\t" + sys.argv[0] + " -c Programacion"
    print "\t" + sys.argv[0] + " -c Program*"
    print ""

if __name__ == "__main__":
    location = "./" + sqlite_file
    location2 = directory + sqlite_file

    if os.path.exists(location):
        con, cur = connect()
        main(cur)
    elif os.path.exists(location2):
        con, cur = connect()
        main(cur)
    else:
        print sqlite_file + " not exist"
