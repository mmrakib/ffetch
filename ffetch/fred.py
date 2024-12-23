import os
import re
import asyncio
from urllib.parse import urlencode
from pprint import pprint

import pandas as pd
import aiohttp

class Fred:
    base_url = "https://api.stlouisfed.org/fred"

    def __init__(self, session: aiohttp.ClientSession):
        self.session = session
        self.api_key = os.getenv("FRED_API_KEY")

        if not self.api_key:
            raise ValueError("Could not find API key.")
        
    async def __fetch_data(self, endpoint: str, params: dict) -> dict:
        url = f"{self.base_url}/{endpoint}?{urlencode(params)}"

        print(f"Fetching from: {url}")

        async with self.session.get(url) as response:
            data = await response.json()

        return data
    
    async def __get_series_metadata(self, series_id: str) -> dict:
        endpoint = "series"
        params = {
            "series_id": series_id,
            "api_key": self.api_key,
            "file_type": "json"
        }

        data = await self.__fetch_data(endpoint, params)

        return data
    
    async def __get_series_observations(self, series_id: str) -> dict:
        endpoint = "series/observations"
        params = {
            "series_id": series_id,
            "api_key": self.api_key,
            "file_type": "json"
        }

        data = await self.__fetch_data(endpoint, params)

        return data
    
    def __convert_to_df(self, data: dict) -> pd.DataFrame:
        pass

async def main():
    async with aiohttp.ClientSession() as session:
        pass

if __name__ == '__main__':
    asyncio.run(main())
