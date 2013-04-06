#! /usr/bin/python
#Written By Tom Paulus, @tompaulus, www.tompaulus.com


class NewsAPI:
    def __init__(self):
        return

    def get(self,count,key):
        """
        Get the homepage form HackerNews
        :return: JSON object
        """
        url = 'http://api.usatoday.com/open/articles/topnews/news?count='+str(count)+'&days=0&page=0&encoding=json&api_key='+key
        d = requests.get(url)
        JSON = d.json()
        return JSON
