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

        try:
            async with self.session.get(url) as response:
                if response.status != 200:
                    raise ValueError(f"Error fetching data: {response.status}")
                
                data = await response.json()
                if "error_code" in data:
                    raise ValueError(f"API error: {data['error_message']}")

                return data
        except Exception as e:
            print(f"Request failed: {e}")
            return {}

    async def __get_series_metadata(self, series_id: str) -> dict:
        endpoint = "series"
        params = {
            "series_id": series_id, 
            "api_key": self.api_key, 
            "file_type": "json"
        }

        return await self.__fetch_data(endpoint, params)

    async def __get_series_observations(self, series_id: str) -> dict:
        endpoint = "series/observations"
        params = {
            "series_id": series_id,
            "api_key": self.api_key,
            "file_type": "json"
        }

        return await self.__fetch_data(endpoint, params)

    async def __get_series(self, series_id: str) -> pd.DataFrame:
        metadata = await self.__get_series_metadata(series_id)
        series = await self.__get_series_observations(series_id)

        if not metadata or not series:
            return pd.DataFrame()

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
        return await self.__get_series("GDP")

    async def get_cpi(self):
        return await self.__get_series("CPIA")

    async def get_unemployment_rate(self):
        return await self.__get_series("UNRATE")

    async def get_interest_rate(self):
        return await self.__get_series("FEDFUNDS")

    async def get_trade_balance(self):
        return await self.__get_series("NETEXP")

    async def get_employment(self):
        return await self.__get_series("PAYEMS")

    async def get_pce(self):
        return await self.__get_series("PCE")

    async def get_house_price_index(self):
        return await self.__get_series("SPCS10R")
        
    async def get_wages(self):
        return await self.__get_series("CES3000000001")

async def main():
    pd.set_option('display.float_format', '{:.10f}'.format)

    async with aiohttp.ClientSession() as session:
        fred = Fred(session)
        
        gdp_df = await fred.get_gdp()
        if not gdp_df.empty:
            print("GDP Data:\n", gdp_df.head())
        
        cpi_df = await fred.get_cpi()
        if not cpi_df.empty:
            print("CPI Data:\n", cpi_df.head())

if __name__ == '__main__':
    asyncio.run(main())
