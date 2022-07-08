from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import re

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()
url_1 = 'https://comidasperuanas.net/platos-tipicos-de-la-costa-peruana/'
ourUrl_1 = opener.open(url_1)
soup_1 = BeautifulSoup(ourUrl_1,'html.parser')

comida = soup_1.find_all('h3', class_= 'uagb-post__title')
comida_costa = list()

for i in comida:
    comida_costa.append(i.text.replace("\n",""))

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://comidasperuanas.net/platos-tipicos-de-la-costa-peruana/")

link_comidas = driver.find_elements_by_xpath('.//a[contains(@href, "comidasperuanas")]')
link_comida_aux_1 = list()

for j in link_comidas:
    link_comida_aux_1.append(j.get_attribute('href'))

link_comida_aux_2 = list()

for elemento in link_comida_aux_1:
    if elemento not in link_comida_aux_2:
        link_comida_aux_2.append(elemento)

link_comida = link_comida_aux_2[11:59]

url_2 = link_comida[0]
page = urllib.request.urlopen(url_2)
soup_2 = BeautifulSoup(page, 'lxml')
content = soup_2.find_all('span')
print(content)

#ingredientes = list()
#lista_ingredientes = list()
#pasos_preparacion = list()
#lista_preparacion = list()
#df = pd.DataFrame({'Platillo':comida_costa}, index = list(range(1,49)))
#print(df)