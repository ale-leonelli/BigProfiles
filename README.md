# BigProfiles

Ciao Valerio, queso è il codice che sono riuscito a produrre in questa settimana.
Le difficoltà che ho riscontrato ad essere sincero sono diverse, per questo alcune cose non sono riuscite a farle ma volevo
comunque presentare una risposta al test.

Di preciso le parti mancanti sono:
- Tempo di risposta random
- Il punto 3, quindi il GET che fa da retrivier

Per l'utilizzo dell'applicativo bisognerà cambiare dei settings all'interno del main.py
Nella parte relativa alla configurazione del database mongodb bisognerà inserire al posto di **username** e **Password** i relativi dati per la variabile **db**
e **collection**

Per poter eseguire attraverso terminale basterà eseguire il comando

uvicorn main:app che aprirà direttamente sul localhost.
