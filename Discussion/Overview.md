# Descrizione del progetto

Il progetto **learn** ha lo scopo di gestire una modalità di apprendimento
non lineare in cui lo studente può decidere un percorso di apprendimento
autonomo avendo comunque modo di accedere solo alle unità didattiche ammesse
in base a quelle che ha già superato.


Le tabelle principali identificate sono

- student
- unit
- unit_tree
- requirement
- history
- unit_comment

## Tabella student

Chiave primaria **id** e gli altri campi saranno oggetto di separata discussione

Campi:

- id
- name
- surname
- nickname
- country
- city
- user_id
- i rimanenti saranno oggetto di separata discussione

## Tabella unit

Chiave primaria **id** e gli altri campi saranno oggetto di separata discussione

Campi:

- id
- description
- i rimanenti saranno oggetto di separata discussione

## Tabella unit_tree

Chiave primaria **id** tabella gerarchica

Campi:

- id
- description
- i rimanenti saranno oggetto di separata discussione


Chiave primaria **id** e gli altri campi saranno oggetto di separata discussione

Campi:

- unit_id
- description
- i rimanenti saranno oggetto di separata discussione

## Tabella requirement 

La tabella serve a conoscere le unità che lo studente deve aver svolto per poter accedere.

Chiave primaria : **id** 

Campi:

- unit_id
- required_unit_id

## Tabella history

La tabella serve a conoscere le unità che lo studente ha svolto.

Chiave primaria **id** 
e gli altri campi saranno oggetto di separata discussione

Campi:

- student_id
- unit_id


## Tabella unit_comment

Tabella per permettere agli studenti di commentare le unità e gestire discussioni sul
contenuto

Chiave primaria **id** 
e gli altri campi saranno oggetto di separata discussione

Campi:

- unit_id
- student_id
- comment
- thread
