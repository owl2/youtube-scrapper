import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json
import requests


def get_view_count(url):
    """
    :param url: URL of the video
    :return: Video views count
    """
    req = Request(url)
    content = urlopen(req).read().decode('utf8')

    soup = BeautifulSoup(content, 'lxml')

    tag = soup.find_all('script', text=re.compile("viewCount"))
    infos = tag[0].get_text().replace(' ', '').split('=', 1)[1].replace(';', '')

    json_object = json.loads(infos)
    view_count = json_object['videoDetails']['viewCount']

    return view_count


def get_video_id(url):
    """
    :param url: URL of the video
    :return: Id of the video
    """
    req = Request(url)
    content = urlopen(req).read().decode('utf8')

    soup = BeautifulSoup(content, 'lxml')

    tag = soup.find_all('script', text=re.compile("viewCount"))
    infos = tag[0].get_text().replace(' ', '').split('=', 1)[1].replace(';', '')

    json_object = json.loads(infos)
    video_id = json_object['videoDetails']['videoId']

    return video_id


def get_like_count(url):
    """
    :param url: URL of the video
    :return: Video likes count
    """
    # proxies = {'http': '20.105.253.176'}
    req = Request(url)
    content = urlopen(req).read().decode('utf8')
    # content = requests.get(url, proxies=proxies).text

    soup = BeautifulSoup(content, 'lxml')

    tag = soup.find_all('script', text=re.compile("J'aime"))
    infos = tag[0].get_text().replace(' ', '').split('=', 1)[1].replace(';', '').replace(u"\u2022", "*")

    json_object = json.loads(infos)

    like_infos = json_object['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]\
        ['videoPrimaryInfoRenderer']['videoActions']['menuRenderer']['topLevelButtons'][0]['toggleButtonRenderer']\
        ['defaultText']['accessibility']['accessibilityData']['label']

    extract = like_infos.encode("ascii", "ignore")
    like_count = extract.decode().split('clic')[0]
    return like_count


def get_http_proxy():
    url = 'https://sslproxies.org/'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'lxml')
    for tr in soup.find_all('tr', class_=False):
        current = []
        for td in tr.find_all('td'):
            current.append(td.get_text())
        print(current)
