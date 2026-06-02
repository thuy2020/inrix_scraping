import pandas as pd
import requests
import os
from dotenv import load_dotenv

#downloading ACS data from Census, year 2024, metro area, table S0802 Means of transportation

load_dotenv()
API_KEY = os.getenv("CENSUS_API_KEY")


url = "https://api.census.gov/data/2024/acs/acs1/subject"
params = {
    "get": "group(S0802)",
    "ucgid": "pseudo(0100000US$31000M1)",
    "key": API_KEY
}
#"key": "6da96730998a0a1fbdd8ac727b1de5626c5eb1a7"

r = requests.get(url, params=params)

print(r.status_code)
print(r.url)

data = r.json()

df = pd.DataFrame(data[1:], columns=data[0])

print(df.shape)
print(df.head())

df.to_csv(
    "output/acs_2024_s0802_metros.csv",
    index=False
)