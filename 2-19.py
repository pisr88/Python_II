import requests
from bs4 import BeautifulSoup
import os

urls = ['https://stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters', 'https://www.kursyonline24.eu/', 'https://www.mobilo24.eu/spis/']
i = 1

for url in urls:
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        web = soup.prettify()
        path = os.path.abspath(os.path.dirname(__file__))
        file = path + "\\" + str(i) +'.txt'
        with open(file,'x', encoding="utf-8") as f:
            f.write(web)
        i+=1
    except:
        print('Proces zakończony niepowowdzeniem')
        break
else:
    print("Proces zakończony")       
    
    
    
