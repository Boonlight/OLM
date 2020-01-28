from selenium import webdriver
import csv
import datetime

now = datetime.datetime.now()

names = []
playerids = []
# Spielerliste einlesen
with open('C:/Users/User/Documents/Programmierung/Python/playerlist.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        names.append(row[0])
        playerids.append(row[1])

#for (x, y) in enumerate(zip(names, playerids)):
#  print(x, y)

# chromedriver PFad
pfad = "C:/Users/User/Documents/Programmierung/Python/chromedriver_win32/chromedriver.exe"
# Standard Player url without ID
url = 'https://www.onlineliga.de/#url=player/overview?playerId='

dateiname = now.strftime('%d.%m.%Y') + '.csv'
#neues CSV file für Kaderdownload
with open(dateiname, 'w', newline='') as f:
  fieldnames = ['NAME', 
                'ALTER', 
                'POSITION', 
                'FUSS', 
                'MARKTWERT', 
                'GEHALT',
                'Gesamt', 
                'Kondition', 
                'Schnelligkeit', 
                'Technik',
                'Schusstechnik', 
                'Schusskraft', 
                'Kopfball',
                'Zweikampf',
                'Taktik',
                'Athletik',
                'Talent',
                'Linie',
                'Libero',
                'Fuss',
                'Spieleröffnung',
                'Rauslaufen',
                'Strafraum']
  
  thewriter = csv.DictWriter(f, fieldnames=fieldnames)
  thewriter.writeheader()
# allgemeine Infos
#  0 ('NAME', 'Zoran Spahic')
#1 ('NATIONALITÄT', 'Bosnien-Herzegowina')
#2 ('AKTUELLES TEAM', '1. FC Lichtenhagen')
#3 ('ALTER', '25 Jahre')
#4 ('POSITION', 'Torwart')
#5 ('GEWICHT', '89 kg')
#6 ('GRÖSSE', '1,92 Meter')
#7 ('FUSS', 'Beide')
#8 ('MARKTWERT', '16.864 €')
#9 ('VERTRAGSLAUFZEIT', 'Ende Saison 2 (1 Saison, 32 Wochen)')
#10 ('JAHRESGEHALT', '3.047 €')
#11 ('IM VEREIN SEIT', 'Saison 1, Spieltag 1 (Woche 1)')
#12 ('KARTEN\n(AKTUELLE SAISON)', 'Keine Karten')
#
#    
    
# Feldspieler
# 0 Gesamt, 1 Leer, 2 Kondition, 3 Schnelligkeit, 4 Technik, 5 Schusstechnik
# 6 Schusskraft 7 Kopfball 8 Zweikampf 9 Taktik 10 Athletik 11 Talent

# Torwart
# 0 Gesamt 1 Leer 2 Linie 3 Libero 4 Fuss 5 Spieleröffnung 6 Rauslaufen
    # 7 Strafraum 8 Talent
#  first = 1  
# Schleife über alle Spieler-ID's
  
  for x in playerids:
    browser = webdriver.Chrome(pfad)
    player_url = url + x
    browser.get(player_url)

    elements = browser.find_elements_by_class_name("ol-player-table-row div:last-child")
    values = browser.find_elements_by_class_name("ol-value-bar-small-label-value")
    entwicklung = browser.find_element_by_class_name("ol-button-toggle.active")
    #bar = browser.find_elements_by_class_name("ol-value-bar-sub-progress-wrapper")
    # aktueller Spieler ist ein Torwart
    if ( elements[4].text == 'Torwart'):
        thewriter.writerow({'NAME'           : elements[0].text,
                            'ALTER'          : elements[3].text,
                            'POSITION'       : elements[4].text,
                            'FUSS'           : elements[7].text,
                            'MARKTWERT'      : elements[8].text,
                            'GEHALT'         : elements[10].text,
                            'Gesamt'         : values[0].text,
                            'Linie'          : values[2].text,
                            'Libero'         : values[3].text,
                            'Fuss'           : values[4].text,
                            'Spieleröffnung' : values[5].text,
                            'Rauslaufen'     : values[6].text,
                            'Strafraum'      : values[7].text,
                            'Talent'         : values[8].text})
    else:
       thewriter.writerow({ 'NAME'           : elements[0].text,
                            'ALTER'          : elements[3].text,
                            'POSITION'       : elements[4].text,
                            'FUSS'           : elements[7].text,
                            'MARKTWERT'      : elements[8].text,
                            'GEHALT'         : elements[10].text,
                            'Gesamt'         : values[0].text,
                            'Kondition'      : values[2].text,
                            'Schnelligkeit' : values[3].text,
                            'Technik'       : values[4].text,
                            'Schusstechnik' : values[5].text,
                            'Schusskraft'   : values[6].text,
                            'Kopfball'      : values[7].text,
                            'Zweikampf'     : values[8].text,
                            'Taktik'        : values[9].text,
                            'Athletik'      : values[10].text,
                            'Talent'        : values[11].text,}) 
    
    entwicklung.click()
#    for items in elements:
#      elementlist.append(items.text)
#    
#    for lable in lables:
#      lablelist.append(lable.text)
#
#    for value in values:
#      valuelist.append(value.text)
#    
#    for vlables in valuelables:
#      valuelablelist.append(vlables.text)  
#
#
#    for (x, y) in enumerate(zip(lablelist, elementlist)):
#      print(x, y)
#  
#    for (x, y) in enumerate(zip(valuelablelist, valuelist)):
#      print(x, y)
      
    browser.close()  
#browser.close()
#class QuotesSpider(scrapy.Spider):
#    name = 'quotes'
#    start_urls = [
#        'http://quotes.toscrape.com/tag/humor/',
#    ]
#
#    def parse(self, response):
#        for quote in response.css('div.quote'):
#            yield {
#                'text': quote.css('span.text::text').get(),
#                'author': quote.xpath('span/small/text()').get(),
#            }
#
#        next_page = response.css('li.next a::attr("href")').get()
#        if next_page is not None:
#            yield response.follow(next_page, self.parse)
