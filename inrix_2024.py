import pandas as pd
import requests

url = "https://inrix.com/wp-content/themes/inrix/assets/data/Scorecard_Delays-2025.json?v=1.1.0.1764106094"

data = requests.get(url).json()

# Check top-level structure
print(data.keys())

# If the main data is inside one key:
key = list(data.keys())[0]
df = pd.DataFrame(data[key])

print(df.shape)
print("\nColumns:")

for col in df.columns:

    print(col)

df.to_csv(
    "inrix_city_ranking_list_2025_full_table.csv",
    index=False
)

delay_df = df[[
    "country",
    "urban_area",
    "2024_delay"
]
]

# Filter to United States only
us_df = delay_df[
    delay_df["country"] == "United States"
].copy()

# Split urban_area into city name and state abbreviation
# Examples:
# "Los Angeles CA" -> city="Los Angeles", state="CA"
# "New York City NY" -> city="New York City", state="NY"
us_df["state_abbr"] = us_df["urban_area"].str.extract(r'\s([A-Z]{2})$')
us_df["city"] = us_df["urban_area"].str.replace(r'\s[A-Z]{2}$', '', regex=True)

# Reorder columns
us_df = us_df[[
    "state_abbr",
    "city",
    "urban_area",
    "2024_delay"
]]

# Save United States cities
us_df.to_csv(
    "inrix_delay_hour_2024_us.csv",
    index=False
)

print(us_df.head())
print(us_df.shape)

