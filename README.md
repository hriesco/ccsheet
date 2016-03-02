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
* Fifth file install.sh is the script that install the application to O.S.    
* Sixth file uninstall.sh is the script that uninstall the application to O.S.    

## Install

* To install in Linux you need the following packages:

  ```
    sudo apt-get install libsqlite3-dev sqlite3
    sudo apt-get install python-qt4
  ```
* To generate the database with the sql script (if you want, you can use my own ccs.db and you can discard this step):

  ```
    sqlite3 ccs.db < ccs.sql
  ```
* Install the program from the install.sh script :

  ```
    sudo chmod +x install.sh
    sudo ./install.sh
  ```


## Uninstall

* Uninstall the application to the OS:

  ```
    sudo chmod +x uninstall.sh
    sudo ./uninstall.sh
  ```


## Usage

* **ccs**    -> Calls application command cheatsheet help
* **ccsl**   -> List all categories in command cheatsheet
* **ccsgui** -> Open the application interface to write new cheatsheets
 

## Suggestions

* I accept any suggestion to make any changes to the application
* Write me at the following email: hectorriesco@hotmail.com
