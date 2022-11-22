# BigProfiles

Ciao Valerio, queso è il codice che sono riuscito a produrre in questa settimana.
Le difficoltà che ho riscontrato ad essere sincero sono diverse, per questo alcune cose non sono riuscite a farle ma volevo
comunque presentare una risposta al test.

Di preciso le parti mancanti sono:
- Tempo di risposta random
- Il punto 3, quindi il GET che fa da retrivier

Per l'utilizzo dell'applicativo bisognerà cambiare dei settings all'interno del main.py
Nella parte relativa alla configurazione del database mongodb bisognerà inserire al posto di 

```
<username>
```

e 

```
<password>
```

i relativi dati e successivamente anche per la variabili 

```
<nome_database>
```

e 

```
<nome_collection>
```

nella seguente parte di codice:

```
client = pymongo.MongoClient(
    "mongodb+srv://<username>:<password>@cluster0.hqefbkn.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("<nome_database>")
collection = db.get_collection("<nome_collection>")
```

Per poter eseguire attraverso terminale basterà eseguire il comando

```
uvicorn main:app
```

che aprirà direttamente sul localhost.

