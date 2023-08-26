import os
import requests

from fastapi import APIRouter
from utils.date import date, daterange
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
        'Accept': 'application/json',
        'Authorization' : f"Bearer {API_KEY}"
    }

    start_date = date(2022, 1, 3)
    end_date = date(2021, 2, 1)
    # for single_date in daterange(start_date, end_date):
    #     print(single_date.strftime("%Y-%m-%d"))
    url = API_BASE_URL + f'aggs/grouped/locale/us/market/stocks/{start_date.strftime("%Y-%m-%d")}'
    print(url)
    r = requests.get(url, headers=headers)
    print(r.status_code)
    print(r.content)
    print(r.json())
