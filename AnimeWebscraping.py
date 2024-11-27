import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
print('-------------------------------------------')
print("Select your Genre from below:")
genre_list = ['action','adventure','cars','comedy','dementia','demons','drama','echhi','fantasy','game'
              'harem','historical','horror','isekai','josei','kids','magic','martial arts','mecha','military',
              'music','mistery','parody','police','psychological','romance','samurai','school','sci-fi','seinen','shoujo'
              'shoujo ai','shounen','shounen ai','slice of life','space','sports','super power','supernatural','thriller'
              'vampire']
print(genre_list)
genre = input("Enter the genre: ").lower()

# Define the headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# URL of the Anime website
url = 'https://hianime.to/genre/'+genre
# Sending the GET request with headers
r = requests.get(url, headers=headers)

# Check the status code to see if the request was successful (status code 200)
if input in genre_list:

    if r.status_code == 200:
        print(f"Successfully accessed the page: {url}")

        # Get the HTML content of the page
        html_content = r.text

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content,'html.parser')
        #getting data of all the common parent class 
        Animes = soup.find_all('div',class_='flw-item')
        #getting the animes and its current dubbed and subbed episodes
        Titles = []
        Subbed = []
        Dubbed = []
        for details in Animes:
            title = details.find('a',class_='dynamic-name')
            subbed = details.find('div',class_='tick-sub')
            dubbed = details.find('div',class_ = 'tick-dub')
            Titles.append(title.get_text(strip=True) if title else "No Title")
            Subbed.append(subbed.get_text(strip=True) if subbed else "0")
            Dubbed.append(dubbed.get_text(strip=True) if dubbed else "0")
        #importing the data into a data frame
        df =pd.DataFrame({
            'Title':Titles,
            'Subbed':Subbed,
            'Dubbed': Dubbed
        })
        print(df.to_string(index=False))
        df.to_csv("Animes.csv",index = False)
    else:
        print('Cant fetch the request')
else:
    print("Invalid Genre!!")



