#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import getopt
import os

sqlite_file = 'ccs.db'

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def connect():
    con = lite.connect(sqlite_file)
    cur = con.cursor()
    return con, cur

def get_categories(cur):
    cur.execute("SELECT name FROM category")
    return cur.fetchall()
def get_id_category(cur, nameCat, filter):
    if not filter:
        cur.execute("SELECT id_category FROM category WHERE name =?", (nameCat,))
    else:
        value = nameCat[:-1] + '%'
        cur.execute("SELECT id_category FROM category WHERE name LIKE ?", (value,))
    return cur.fetchall()

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

def func_listCategories(cur):
    dic = {}
    rows = get_categories(cur)
    if len(rows) > 0:
        print "--- CATEGORIES --------------------"
        print "0 -> EXIT"
        for i, r in enumerate(rows):
            dic[i+1] = str(r[0])
            if i == len(rows) - 1:
                print "%s) %s\t\t" % (str(i + 1),  r[0])
            else:
                print "%s) %s\t\t" % (str(i + 1),  r[0]),
        
        indice = int(raw_input("ID > "))
        if indice > len(dic) or indice == 0:
            sys.exit(2)
        name_cat = dic.get(indice)

        rows = get_commands_by_nameCat(cur, name_cat)   
        if len(rows) > 0:
            dic.clear()
            print "--- COMMANDS ----------------------"
            print "0 -> EXIT"
            for i, r, in enumerate(rows):
                dic[i+1] = str(r[0])
                if i == len(rows) - 1:
                    print "%s) %s\t\t" % (str(i + 1),  r[0])
                else:
                    print "%s) %s\t\t" % (str(i + 1),  r[0]),

            indice = int(raw_input("ID > "))
            if indice > len(dic) or indice == 0:
                sys.exit(2)
            name_cmd = dic.get(indice)

            rows = get_sections_by_nameCmd(cur, name_cmd)   
            if len(rows) > 0:
                dic.clear()
                print "--- SECTIONS ----------------------"
                print "0 -> EXIT"
                for i, r, in enumerate(rows):
                    dic[i+1] = str(r[0])
                    if i == len(rows) - 1:
                        print "%s) %s\t\t" % (str(i + 1),  r[0])
                    else:
                        print "%s) %s\t\t" % (str(i + 1),  r[0]),

                indice = int(raw_input("ID > "))
                if indice > len(dic) or indice == 0:
                    sys.exit(2)
                name_sect = dic.get(indice)

                rows = get_title_by_nameSect(cur, name_sect)   
                if len(rows) > 0:
                    dic.clear()
                    print "--- DATA --------------------------"
                    print "0 -> EXIT"
                    for i, r, in enumerate(rows):
                        dic[i+1] = str(r[0])
                        if i == len(rows) - 1:
                            print "%s) %s\t\t" % (str(i + 1),  r[0])
                        else:
                            print "%s) %s\t\t" % (str(i + 1),  r[0]),

                    indice = int(raw_input("ID > "))
                    if indice > len(dic) or indice == 0:
                        sys.exit(2)
                    name_title = dic.get(indice)

                    rows = get_data_by_title(cur, name_sect, name_title)   
                    if len(rows) > 0:
                        cls()
                        print "---------------------------------------------------------"
                        print " " + name_cat + " >> " + name_cmd + " >> " + name_sect   
                        print "---------------------------------------------------------"
                        print " " + name_title
                        print "---------------------------------------------------------"
                        print rows[0][0]
                    else:
                        print "No text in this section"
                else:
                    print "No data in section"
            else:
                print "No section in command"
        else:
            print "No command in category"
    else:
        print "No categories in database"

def func_category(cur, arg):
    filter = False
    if arg[-1] == '*':
        filter = True

    id_cat = get_id_category(cur, arg, filter)
    if id_cat:
        for r in id_cat:
            print r[0]
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

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit(2)
        elif opt in ('-l'):
            func_listCategories(cur)
        elif opt in ('-C', '--category'):
            func_category(cur, arg)
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

