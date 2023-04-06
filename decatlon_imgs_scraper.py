import requests
from bs4 import BeautifulSoup
import json
import csv
import time
import re
to = "200"
# decathlon de, fr, en nl imgs scraper
urls =[
     "https://www.decathlon.nl/search?Ntt=jas&facets=genderLabels:HEREN_&from=0&size="+to,
    "https://www.decathlon.de/browse/c0-damen/c1-sportbekleidung/c3-jacken/_/N-5jidwr?from=0&size="+to,
    "https://www.decathlon.de/browse/c0-herren/c1-sportbekleidung/c3-jacken/_/N-jvebss?from=0&size="+to,
    "https://www.decathlon.fr/search?Ntt=manteau&from=0&size="+to,
    "https://www.decathlon.nl/search?Ntt=jas%20vrouwen&facets=genderLabels:DAMES_&from=0&size="+to
    ]
i = 0
for url in urls:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(urls[0], headers=headers)
    content = BeautifulSoup(response.content,'html.parser')
    imgs = content.find_all('img', {'class': ['svelte-11itto', 'svelte-1aq4t4d', 'svelte-1bclr8g']})
    for img in imgs:
        i = i +1
        try:
            img_link = img["src"].split('&f=')[0] + "?f=600x0"
            if img_link.startswith("http"):
                response = requests.get(img_link)
                # Schrijf de inhoud van de response weg naar een lokale bestand
                bestandsnaam =  f'imgs/d{str(i)}.jpg'   
                with open(bestandsnaam, 'wb') as f:
                    f.write(response.content)
                print(f'Afbeelding opgeslagen als {bestandsnaam} {img_link}.')
                time.sleep(1)
        except:
                print(f'link:{i} werkte niet')
print("Done")