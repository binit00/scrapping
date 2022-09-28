from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import json
import copy

driver = webdriver.Chrome(".\chromedriver.exe")

ab = True

json_data = {
    'score': ""
}

match_code = "cplt20_2022_e"

while ab:
    driver.get('https://www.cricketlineguru.com/match-detail/'+ match_code +'/commentary')
    content = driver.page_source
    soup = BeautifulSoup(content)

    card = soup.find_all(attrs={'id': 'mat-tab-content-0-0'})[0]

    score_tag = card.findAll(attrs={'class':'score', '': ''})

    new_json = copy.deepcopy(json_data)
    
    if( score_tag ):
        score_tag = score_tag[1]
        new_json['score'] = score_tag.text
        if( new_json != json_data):
            file = open('data.json', 'w')
            json.dump(new_json, file, indent=4)
            file.close()
            json_data = copy.deepcopy(new_json)
