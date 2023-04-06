import requests
from bs4 import BeautifulSoup
import time

# zalando
urls =["https://www.zalando.nl/dames/?q=jassen&p=","https://www.zalando.nl/heren/?q=jassen&p="]
i = 0
for url in urls:
    for i2 in range(20):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(urls[0]+str(i2), headers=headers)
        content = BeautifulSoup(response.content,'html.parser')
        imgs = content.find_all('img', {'class': ['KVKCn3','jDGwVr','OSvTKp', '_7ZONEy','mu8J0f']})
        for img in imgs:
            i = i +1
            try:
                img_link = img["src"].split('?imwidth=300')[0] + "?imwidth=500"
                if img_link.startswith("http"):
                    response = requests.get(img_link)
                    # Schrijf de inhoud van de response weg naar een lokale bestand
                    bestandsnaam =  f'imgs/zb{str(i)}.jpg'   
                    with open(bestandsnaam, 'wb') as f:
                     f.write(response.content)
                    print(f'Afbeelding opgeslagen als {bestandsnaam} {img_link}.')
                    time.sleep(1)
            except:
                    print(f'link:{i} werkte niet')
print("Done")