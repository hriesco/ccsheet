#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import getopt
import os

sqlite_file = 'ccs.db'

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
    cur.execute("SELECT name FROM category")
    return cur.fetchall()
def get_names_category(cur, nameCat, myFilter):
    if not myFilter:
        cur.execute("SELECT name FROM category WHERE LOWER(name)=?", (nameCat,))
    else:
        value = nameCat[:-1] + '%'
        cur.execute("SELECT name FROM category WHERE name LIKE ?", (value,))
    return cur.fetchall()
def get_nameCategory_by_idCat(cur, idCat):
    cur.execute("SELECT name FROM category WHERE id_category=?", (idCat,))
    return cur.fetchone()
def get_commands_by_nameCat(cur, name):
    cur.execute("SELECT id_category FROM category WHERE name=?", (name,))
    indice = cur.fetchone()
    cur.execute("SELECT name FROM command WHERE id_category=?", indice)
    return cur.fetchall()
def get_sections_by_nameCmd(cur, name):
    cur.execute("SELECT id_command FROM command WHERE name=?", (name,))
    indice = cur.fetchone()
    cur.execute("SELECT name FROM section WHERE id_command=?", indice)
    return cur.fetchall()
def get_title_by_nameSect(cur, name):
    cur.execute("SELECT id_section FROM section WHERE name=?", (name,))
    indice = cur.fetchone()
    cur.execute("SELECT title FROM data WHERE id_section=?", indice)
    return cur.fetchall()
def get_data_by_title(cur, name_sect, name_title):
    cur.execute("SELECT id_section FROM section WHERE name=?", (name_sect,))
    indice = cur.fetchone()
    cur.execute("SELECT text FROM data WHERE title=? and id_section=?", (name_title, indice[0]))
    return cur.fetchall()

def func_printData(cur, name_cat, name_cmd, name_sect, name_title):
    col = Color()
    rows = get_data_by_title(cur, name_sect, name_title)   
    if len(rows) > 0:
        cls()
        col.light_blue("---------------------------------------------------------",True)
        col.light_green(" "+ name_cat, False)
        col.light_blue(">> " + name_cmd, False)
        col.light_purple(">> " + name_sect, True)
        col.light_blue("---------------------------------------------------------",True)
        col.light_red(" " + name_title, True)
        col.light_blue("---------------------------------------------------------",True)
        print rows[0][0]
    else:
        print "No text in this section"

def func_listData(cur, name_cat, name_cmd, name_sect):
    col = Color()
    dic = {}
    rows = get_title_by_nameSect(cur, name_sect)   
    if len(rows) > 0:
        col.light_aqua("--- DATA --------------------------", True)
        col.light_blue("0)", False)
        col.light_red("EXIT", True)
        for i, r, in enumerate(rows):
            dic[i+1] = str(r[0])
            if i == len(rows) - 1:
                col.light_blue(str(i+1) + ")", False)
                print "%s\t\t" % r[0]
            else:
                col.light_blue(str(i+1) + ")", False)
                print "%s\t\t" % r[0],

        indice = int(raw_input("ID > "))
        if indice > len(dic) or indice == 0:
            sys.exit(2)
        name_title = dic.get(indice)
        func_printData(cur, name_cat, name_cmd, name_sect, name_title)
    else:
        print "No data in section"

def func_listSections(cur, name_cat, name_cmd):
    col = Color()
    dic = {}
    rows = get_sections_by_nameCmd(cur, name_cmd)   
    if len(rows) > 0:
        col.light_aqua("---- SECTIONS ----------------------", True)
        col.light_blue("0)", False)
        col.light_red("EXIT", True)
        for i, r, in enumerate(rows):
            dic[i+1] = str(r[0])
            if i == len(rows) - 1:
                col.light_blue(str(i+1) + ")", False)
                print "%s\t\t" % r[0]
            else:
                col.light_blue(str(i+1) + ")", False)
                print "%s\t\t" % r[0],

        indice = int(raw_input("ID > "))
        if indice > len(dic) or indice == 0:
            sys.exit(2)
        name_sect = dic.get(indice)
        func_listData(cur, name_cat, name_cmd, name_sect)
    else:
        print "No section in command"

def func_listCommands(cur, name_cat):
    col = Color()
    dic = {}
    rows = get_commands_by_nameCat(cur, name_cat)   
    if len(rows) > 0:
        col.light_aqua("---- COMMANDS ---------------------", True)
        col.light_blue("0)", False)
        col.light_red("EXIT", True)
        for i, r, in enumerate(rows):
            dic[i+1] = str(r[0])
            if i == len(rows) - 1:
                col.light_blue(str(i+1) + ")", False)
                print "%s\t\t" % r[0]
            else:
                col.light_blue(str(i+1) + ")", False)
                print "%s\t\t" % r[0],

        indice = int(raw_input("ID > "))
        if indice > len(dic) or indice == 0:
            sys.exit(2)
        name_cmd = dic.get(indice)
        func_listSections(cur, name_cat, name_cmd)
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
        for i, r in enumerate(rows):
            dic[i+1] = str(r[0])
            if i == len(rows) - 1:
                col.light_blue(str(i+1) + ")", False)
                print "%s\t\t" % r[0]
            else:
                col.light_blue(str(i+1) + ")", False)
                print "%s\t\t" % r[0],
        
        indice = int(raw_input("ID > "))
        if indice > len(dic) or indice == 0:
            sys.exit(2)
        name_cat = dic.get(indice)
        func_listCommands(cur, name_cat)
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
        opts, args = getopt.getopt(sys.argv[1:], 'lC:c:s:t:h', ['category=', 
                                                            'command=', 
                                                            'section=', 
                                                            'title=', 
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
        elif opt in ('-C', '--category'):
            func_category(cur, str(arg).lower())
        elif opt in ('-c', '--command'):
            print "Command" + arg
        elif opt in ('-s', '--section'):
            print "Section"
        elif opt in ('-t', '--title'):
            print "Title"
        else:
            usage()
            sys.exit(2)

def usage():
    print "\n usage: " + sys.argv[0] + " <parameter>"
    print """
    -h --help                  Print this
    -l                         List all categories in database
    -C --category <name[*]>    List category with name
    -c --command  <name[*]>    List command with name
    -s --section  <name[*]>    List section with name
    -t --title                 List title with name
    """
    print "Examples:"
    print "\t" + sys.argv[0] + " -C Programacion"
    print "\t" + sys.argv[0] + " -C Program*"
    print ""

if __name__ == "__main__":
    location = "./" + sqlite_file
    if os.path.exists(location):
        con, cur = connect()
        main(cur)
    else:
        print sqlite_file + " not exist"

