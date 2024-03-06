from bs4 import BeautifulSoup
from html_doc import html_doc
import pandas as pd
import os

soup = BeautifulSoup(html_doc, 'lxml')
containers = soup.find_all('div', role='row')

data = []
for container in containers:
    # Attempt to find the urban_area and 2022_delay within each container
    urban_area_div = container.find('div', {'col-id': 'urban_area'})
    delay_div = container.find('div', {'col-id': '2022_delay'})


    # Check if both urban_area_div and delay_div are found before attempting to extract text
    if urban_area_div and delay_div:
        urban_area_text = urban_area_div.find('span').get_text(strip=True)
        country = urban_area_div.find('img')['src']
        # Split the string by '/' and get the last part
        country = country.split('/')[-1]

        # Split the filename by '.' and get the first part
        country = country.split('.')[0]

        delay_text = delay_div.get_text(strip=True)
        # Append the extracted data as a dictionary to the data list
        data.append({'urban_area': urban_area_text,
                     'country': country,
                     'delay_2022': delay_text})

# Create a DataFrame from the accumulated data
df = pd.DataFrame(data)
df = df[df['country'] == 'unitedstates']
df = df.drop('country', axis=1)

print(df)

output = os.path.join(os.getcwd(), 'output')
os.makedirs(output)

df.to_csv('output/delay_hour_2022_US_urban_area.csv')