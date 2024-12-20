`ffetch` is a tool for fetching/parsing financial, economic and geographical data from various sources. It provides a unified interface for fetching from disparate datasets and parses raw data into accessible dataframe objects. It also provides functionality for data transformation and cleaning.

The following is a list of all data sources supported or where support is in development. Where an API key is required, it must be set as an environment variable of the specified name.

| Name | URL | Cost | API Key Required? | Environment Variable |
| --- | --- | --- | --- | --- |
| World Bank Open Data | [databank.worldbank.org](https://databank.worldbank.org) | Free. | Yes. | WORLD_BANK_API_KEY |
| International Monetary Fund (IMF) | [imf.org](https://imf.org) | Free. | Yes. | IMF_API_KEY |
| OECD | [oecd.org](https://oecd.org) | Free. | Yes. | OECD_API_KEY |
| United Nations Statistics Division (UNSD) | [unstats.un.org](https://unstats.un.org) | Free. | No. | |
| Federal Reserve Economic Data (FRED) | [fred.stlouisfed.org](https://fred.stlouisfed.org) | Free. | Yes. | FRED_API_KEY |
| SEC EDGAR | [sec.gov](https://sec.gov) | Free. | No. | |
| U.S. Treasury | [fiscaldata.treasury.gov](https://fiscaldata.treasury.gov) | Free. | No. | |
| U.S. Census Bureau | [data.census.gov](https://data.census.gov) | Free. | Yes. | CB_API_KEY |
| U.S. Bureau of Economic Analysis (BEA) | [bea.gov](https://bea.gov) | Free. | Yes. | BEA_API_KEY |
| Reserve Bank of Australia (RBA) | [rba.gov.au](https://rba.gov.au) | Free. | No. | |
| Australian Bureau of Statistics (ABS) | [abs.gov.au](https://abs.gov.au) | Free. | No. | |
| Australian Prudential Regulation Authority (APRA) | [apra.gov.au](https://apra.gov.au) | Free. | No. | |
| Australian Securities and Investment Commission (ASIC) | [asic.gov.au](https://asic.gov.au) | Free. | No. | |
| European Central Bank (ECB) | [data.ecb.europa.eu](https://data.ecb.europa.eu) | Free. | Yes. | ECB_API_KEY |
| Eurostat | [ec.europa.eu](https://ec.europa.eu) | Free. | Yes. | EUROSTAT_API_KEY |
