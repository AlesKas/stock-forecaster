import os

from influxdb_client import InfluxDBClient

class InfluxHandler():
    def __init__(self) -> None:
        self.client = InfluxDBClient(url=os.getenv('INFLUX_URL'), token=os.getenv('INFLUXDB_TOKEN'))

    def write(self, data) -> None:
        write_api = self.client.write_api()
        write_api.write(os.getenv('INFLUX_BUCKET'), os.getenv('INFLUX_ORG'), data)

    def read(self, query) -> list:
        query_api = self.client.query_api()
        query_result = query_api.query(query, org=os.getenv('INFLUX_ORG'))
        results = []
        for table in query_result:
            for record in table.records:
                results.append((record.get_value(), record.get_field()))
        return results