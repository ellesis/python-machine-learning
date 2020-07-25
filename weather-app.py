# -*- coding: utf-8 -*-

"""
weather underground
https://www.wunderground.com/weather/us/ca/palo-alto/94303

"""
import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport','cond, temp, scale, loc')

def print_the_header():
    print('---------------------------------------')
    print('             Weather App')
    print('---------------------------------------')
    print()

def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather/us/ca/palo-alto/{}'.format(zipcode)
    # url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    # print(url)
    response = requests.get(url)
    # print(response.text[:250])
    return response.text

def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html,'html.parser')
    # print(soup)
    # div.city-header h1 span
    loc = soup.find('div', {"class": "city-header"}).find('h1').find('span').text
    # $('div.city-conditions div.condition-icon p').innerText
    condition = soup.find(class_='city-conditions').find(class_='condition-icon').find('p').get_text()
    # $('#inner-content span.wu-value').innerText
    temp = soup.find(id='inner-content').find(class_='wu-value').get_text()
    # $('#inner-content span.wu-label span.ng-star-inserted').innerText
    scale = soup.find(id='inner-content').find(class_='wu-label').find(class_='ng-star-inserted').get_text()

    loc = find_city_and_state_from_location(loc)

    loc = cleanup_text(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)
    # print(condition, temp, '\xb0', scale, loc)
    # return condition, temp, '\xb0'+scale, loc
    report = WeatherReport(cond=condition, temp=temp, scale='\xb0' + scale, loc=loc)
    return report

def cleanup_text(text: str):
    if text:
        text = text.strip()
    return text

def find_city_and_state_from_location(text: str):
    return text.replace('Weather Conditions', '')
    
def main():
    print_the_header()

    zipCode = input('What zipcode do you want the weather for(94303)?')
    html = get_html_from_web(zipCode)
    report = get_weather_from_html(html)
    print(report)
    #condition, temp, '\xb0'+scale, loc
    print('The temp in {} is {} {} and {}'.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond
    ))

if __name__ == "__main__":
    main()