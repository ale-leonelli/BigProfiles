import pymongo
from datetime import datetime, date
import time
import fastapi
from fastapi import Security, Depends, Request
from fastapi.security import APIKeyHeader
from random import randint

# Mi connetto al database
client = pymongo.MongoClient(
    "mongodb+srv://<username>:<password>@cluster0.hqefbkn.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("<nome_database>")
collection = db.get_collection("<nome_collection>")

# Security check con key
API_KEY = "BigProfiles-API"
API_KEY_NAME = "X-API-KEY"

api_key_header_auth = APIKeyHeader(name=API_KEY_NAME, auto_error=True)


async def get_api_key(api_key_header: str = Security(api_key_header_auth)):
    if api_key_header != API_KEY:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )



app = fastapi.FastAPI()


@app.get("/{date_from}-{date_to}")
async def retrieve(date_from: datetime, date_to: datetime, api_key: str = Depends(get_api_key)):
    # TODO Get method attraverso data in formato ISO
    # TODO Formattare i dati in base all'orario
    # TODO Unire le key, n di errori, tot_response_time
    # TODO Creare il log
    pass


@app.post("/{key}/{payload}")
async def ingestion(key: int, payload: str, api_key: str = Depends(get_api_key)):
    # Creo una variabile randomica per decidere se mi darà risposta 200 o 500 il server
    random_numb = randint(0, 9)
    # Controllo che la key ed il payload siano esatti
    if 1 <= key <= 6 and 10 <= len(payload) <= 255:
        # Caso in cui dà error 500
        if random_numb == 9:
            status_code = 500
            data = {
                "key": key,
                "creation_time": datetime.now().isoformat(),
                "payload": payload,
                "response_time": "-",
                "status_code": status_code,
            }

            # Colleziono comunque i dati nel database
            collection.insert_one(data)

            raise fastapi.HTTPException(status_code=fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            # Caso in cui il server da risposta 200 Ok
            status_code = 200
            data = {
                "key": key,
                "creation_time": datetime.now().isoformat(),
                "payload": payload,
                "response_time": "-",
                "status_code": status_code,
            }

            # Inserisco i dati nel database
            collection.insert_one(data)

            return {
                "key": key,
                "creation_time": datetime.now().isoformat(),
                "payload": payload,
                "response_time": "-",
                "status_code": status_code,
            }
    else:
        raise fastapi.HTTPException(status_code=fastapi.status.HTTP_400_BAD_REQUEST)
