import os
import asyncio
from urllib.parse import urlencode

import pandas as pd
import aiohttp

class Fred:
    base_url = "https://api.stlouisfed.org/fred"

    def __init__(self, session: aiohttp.ClientSession):
        self.session = session
        self.api_key = os.getenv("FRED_API_KEY")

        if not self.api_key:
            raise ValueError("API key not found.")

    async def __fetch_data(self, endpoint: str, params: dict) -> dict:
        url = f"{self.base_url}/{endpoint}?{urlencode(params)}"

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

    async def __get_series(self, series_id: str) -> pd.DataFrame:
        metadata = await self.__get_series_metadata(series_id)
        series = await self.__get_series_observations(series_id)

        title = metadata["seriess"][0]["title"]
        frequency = metadata["seriess"][0]["frequency"]
        units = metadata["seriess"][0]["units"]

        df = pd.DataFrame(series["observations"])

        df.attrs["title"] = title
        df.attrs["frequency"] = frequency
        df.attrs["units"] = units.lower()

        df.drop(columns=["realtime_start", "realtime_end"], inplace=True)

        return df

    async def get_gdp(self):
        series = await self.__get_series("GDP")

        return series

    async def get_cpi(self):
        series = await self.__get_series("CPIA")

        return series

    async def get_unemployment_rate(self):
        series = await self.__get_series("UNRATE")

        return series

    async def get_interest_rate(self):
        series = await self.__get_series("FEDFUNDS")

        return series

    async def get_trade_balance(self):
        series = await self.__get_series("NETEXP")

        return series

    async def get_employment(self):
        series = await self.__get_series("PAYEMS")

        return series

    async def get_pce(self):
        series = await self.__get_series("PCE")

        return series

    async def get_house_price_index(self):
        series = await self.__get_series("SPCS10R")
        
        return series

    async def get_wages(self):
        series = await self.__get_series("CES3000000001")

        return series

async def main():
    pd.set_option('display.float_format', '{:.10f}'.format)

    async with aiohttp.ClientSession() as session:
        fred = Fred(session)
        df = await fred.get_gdp()
        print(df)

if __name__ == '__main__':
    asyncio.run(main())
