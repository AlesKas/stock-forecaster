import os

from fastapi import FastAPI

from .routes.idk1 import router as router1
from .routes.idk2 import router as router2

from influxdb_client import InfluxDBClient

client = InfluxDBClient(url='http://db:8086/', token=os.getenv('INFLUXDB_TOKEN'))
write_api = client.write_api()
write_api.write("bucket", "org", ["h2o_feet,location=coyote_creek water_level=1"])

app = FastAPI()
app.include_router(router1)
app.include_router(router2)
