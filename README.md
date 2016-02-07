## Command Cheatsheet

* Command cheatsheet is a program for personal use that I've created to have organized my cheatsheets of topics such as programming, pentest, notes, hotkeys, etc... to consult them quickly from the console.
* This application I've done in python and I used sqlite3 database.
* I have only tested on Linux so I don't know the operation on other operating systems.

## Files

* The application consists of two programs a database file in sqlite and the script that creates de database
* First program is **ccs.py** : 
    - This application query all the information in the database
    - ![Alt text](images/help.png?raw=true "Help")
* Second program is **ccsgui.py** :
    - This application use it to graphically enter the data into the database
    - ![Alt text](images/gui.png?raw=true "Gui")
* Third file is the sqlite database **ccs.db**
    - This contains the database with all registers
* Fourth file is the script that generates database **ccs.sql**
    

## Installation

* To install in Linux you need the following packages:

  ```
    sudo apt-get install libsqlite3-dev sqlite3
    sudo apt-get install python-qt4
  ```
* To generate the database with the sql script:

  ```
    sqlite3 ccs.db < ccs.sql
  ```
* Copy the files to a folder where you can access anywhere:

  ```
    sudo cp ccs.db ccs.py ccsgui.py /usr/local/bin/
  ```
  
## Suggestions

* I accept any suggestion to make any changes to the application
* Write me at the following email: hectorriesco@hotmail.com
