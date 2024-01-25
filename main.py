# Imports
import requests
from bs4 import BeautifulSoup
import pandas as pd
from itertools import zip_longest
from bot import FormFiller

# Links
form_link = 'https://forms.gle/cNmFCVLLtETEnoMo7'
zillow_link = 'https://appbrewery.github.io/Zillow-Clone/'

# TODO: Scrape the page and make the soup
response = requests.get(zillow_link)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

# TODO: Get links, prices, addresses of all property listings
# Links
links = soup.find_all(class_='property-card-link')
links = [link.get('href') for link in list(links)]
# print(links)

# Prices
prices = soup.find_all(class_='PropertyCardWrapper__StyledPriceLine')
prices = [price.text.replace('$', '').replace(',', '').replace('+', '').replace('/mo', '').replace('1bd', '').replace('1 bd', '').replace(' ', '') for price in list(prices)]
# print(prices)

# Addresses
addresses = soup.find_all('address', {'data-test': 'property-card-addr'})
addresses = [address.text.replace('\n', '').strip() for address in list(addresses)]
# print(addresses)

# TODO: Compile all the scraped data into a single dataframe
zipped_data = zip_longest(links, prices, addresses, fillvalue=None)
df = pd.DataFrame(zipped_data, columns=['Link', 'Price', 'Address'], index=None)
# print(df)

# TODO: Fill in the Google Form for each entry in the data frame
bot = FormFiller()
bot.open_form(form_link)

for idx, row in df.iterrows():
    bot.enter_form(link=row.Link, price=row.Price, address=row.Address)
    bot.open_new_form()

print('Done')