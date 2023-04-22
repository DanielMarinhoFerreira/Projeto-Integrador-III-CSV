from controller.get_cs import LiquiApi

from bs4 import BeautifulSoup
#from pandas import DataFrame
'''
soup:BeautifulSoup = api.get_cs_page('Portal:Players/Europe','LOGRESTAPI',True)
soup.append('Americas')
print(soup)
'''
api = LiquiApi()
player = api.get_cs_player('LOGRESTAPI',True)

print(player)

