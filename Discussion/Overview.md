# Descrizione del progetto

Il progetto **learn** ha lo scopo di gestire una modalità di apprendimento
non lineare in cui lo studente può decidere un percorso di apprendimento
autonomo avendo comunque modo di accedere solo alle unità didattiche ammesse
in base a quelle che ha già superato.


Le tabelle principali identificate sono

- student
- teaching_unit
- requirement
- learn_history

## Tabella student

Chiave primaria **student_id** e gli altri campi saranno oggetto di separata discussione

Campi:

- student_id
- cognome
- nome
- nicknema
- citta
- i rimanenti saranno oggetto di separata discussione

## Tabella teaching_unit

Chiave primaria **teaching_unit_id** e gli altri campi saranno oggetto di separata discussione

Campi:

- teaching_unit_id
- description
- i rimanenti saranno oggetto di separata discussione

## Tabella requirement 

La tabella serve a conoscere le unità che lo studente deve aver svolto per poter accedere.

Chiave primaria : **requirement_id** 

Campi:

- teaching_unit_id
- required_teaching_unit_id

## Tabella learn_history

La tabella serve a conoscere le unità che lo studente ha svolto.

Chiave primaria **learn_history_id** 
e gli altri campi saranno oggetto di separata discussione

Campi:

- student_id
- teaching_unit_id
