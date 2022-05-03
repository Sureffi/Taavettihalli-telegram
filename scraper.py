from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self):
        html_text = requests.get('https://www.luumaki.fi/varauskalenteri/taavettihallin-kuntosali').text
        self.soup = BeautifulSoup(html_text, 'lxml')
    
    def scrape(self):
        result = ''
        for x in range(7):
            reservations = ''
            container = self.soup.find('div', class_='dayColumn day'+str(x))
            day = container.find('div', class_='dayname_date').text
            #reservation_hours = container.find_all('div', class_='srHours confirmed')
            reservation_hours = container.find_all('div', class_='srHours confirmed', recursive=True)
            for item in reservation_hours:
                item = item.text.replace('\n', '')
                #print comment
                #print time only
                reservations += '-' + item[48:].strip() + ':\n    ' + item[12:25] + '\n'
            result += day + '\n' + reservations + '\n'
        return result
