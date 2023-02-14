import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime

current_time = datetime.now()
# url lists:
weather_url = "https://weather.com/weather/today/l/de8c78996a73470bbe53d7ea51b93a733ee74f0744de3cf7660665e506a33862"
world_news_url = "https://www.nbcnews.com/world"
politics_news_url = "https://www.nbcnews.com/politics"
us_news_url = "https://www.nbcnews.com/us-news"

# weather soup
res_weather = requests.get(weather_url)
res_weather.raise_for_status()
weather_soup = BeautifulSoup(res_weather.text, "lxml")

# world news soup
res_world_news = requests.get(world_news_url)
res_world_news.raise_for_status()
world_news_soup = BeautifulSoup(res_world_news.text, "lxml")

# politics news soup
res_politics_news = requests.get(politics_news_url)
res_politics_news.raise_for_status()
politics_news_soup = BeautifulSoup(res_politics_news.text, "lxml")

# us news soup
res_us_news = requests.get(us_news_url)
res_us_news.raise_for_status()
us_news_soup = BeautifulSoup(res_us_news.text, "lxml")


def scrape_weather():

    print("Today's Weather: ")
    location = weather_soup.find("h1", attrs={"class": "CurrentConditions--location--1YWj_"}).get_text()
    weather = weather_soup.find("div", attrs={"class": "CurrentConditions--phraseValue--mZC_p"}).get_text()
    curr_temp = weather_soup.find("span", attrs={"class": "CurrentConditions--tempValue--MHmYY"}).get_text()
    high_low = weather_soup.find("div", attrs={"class": "CurrentConditions--tempHiLoValue--3T1DG"}).get_text()

    print(location + " " + current_time.strftime("%Y-%m-%d %H:%M"))
    print(weather)
    print("Current Temp: " + curr_temp)
    print(high_low)


def scrape_world_news():

    print("\nNBC Top World News: ")
    world_top = world_news_soup.find_all("div", attrs={"class": re.compile("^tease-card__info")})
    print(world_top[0].span.get_text())
    print(world_top[0].a["href"])
    print(world_top[1].span.get_text())
    print(world_top[1].a["href"])


def scrape_politics_news():

    print("\nNBC Top Politics News: ")
    politics_top = politics_news_soup.find_all("div", attrs={"class": re.compile("^tease-card__info")})
    print(politics_top[0].span.get_text())
    print(politics_top[0].a["href"])
    print(politics_top[1].span.get_text())
    print(politics_top[1].a["href"])


def scrape_us_news():

    print("\nNBC Top US News: ")
    us_top = us_news_soup.find_all("div", attrs={"class": re.compile("^tease-card__info")})
    print(us_top[0].span.get_text())
    print(us_top[0].a["href"])
    print(us_top[1].span.get_text())
    print(us_top[1].a["href"])


if __name__ == "__main__":
    scrape_weather()
    scrape_world_news()
    scrape_politics_news()
    scrape_us_news()
