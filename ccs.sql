PRAGMA foreign_keys = ON;
BEGIN TRANSACTION;

CREATE TABLE category (
	id_category INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL UNIQUE 
);
CREATE TABLE command (
	id_command INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	id_category INTEGER NOT NULL,
	name TEXT NOT NULL,
	FOREIGN KEY(id_category) REFERENCES category(id_category) 
);
CREATE TABLE section (
	id_section INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	id_command INTEGER NOT NULL,
	name TEXT NOT NULL,
	FOREIGN KEY(id_command) REFERENCES command(id_command) 
);
CREATE TABLE data (
	id_data INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	id_section INTEGER NOT NULL,
	title TEXT NOT NULL,
	text TEXT NOT NULL,
	FOREIGN KEY(id_section) REFERENCES section(id_section)
);


INSERT INTO category(name) VALUES('Programacion');
INSERT INTO category(name) VALUES('Seguridad');
INSERT INTO command(id_category, name) VALUES(1, 'Python');
INSERT INTO command(id_category, name) VALUES(1, 'Bash');
INSERT INTO section(id_command, name) VALUES(1, 'Ficheros');
INSERT INTO section(id_command, name) VALUES(1, 'SQLite');
INSERT INTO data(id_section, title, text) VALUES(1, "Abrir Fichero", "f = open(filename, mode)");
INSERT INTO data(id_section, title, text) VALUES(1, "Leer de Fichero", "print f.readline()");


COMMIT;
