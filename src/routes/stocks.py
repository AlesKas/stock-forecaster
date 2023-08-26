import os
import requests

from fastapi import APIRouter
from requests.auth import HTTPBasicAuth
from fastapi.responses import JSONResponse
from db_handler.influxHandler import InfluxHandler

router = APIRouter()
API_KEY = os.getenv('API_KEY')
API_BASE_URL = os.getenv('API_BASE_URL')

@router.get('/stock/{ticket}')
async def get_stock(ticket : str):
    return JSONResponse(
        status_code=200,
        content={"data" : "some data"}
    )

@router.post('/stock/{ticket}')
async def post_stock_ticket(ticket : str):
    url = API_BASE_URL + f'aggs/ticker/{ticket}/range/1/day/2023-01-09/2023-01-09?adjusted=true&sort=asc'
    pass

@router.post('/stock/')
async def post_stock():
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
    }

    url = API_BASE_URL + f'hi/history/AAPL/1d'
    print(url)
    r = requests.get(url, headers=headers)