#!/usr/bin/env python
# coding: utf8
from bs4 import BeautifulSoup
import re


class Parser:
    def get(self, response, page):

        channel = {
            'page': page,
            'page_patten': None,
            'movies': []
        }

        soup = BeautifulSoup(response, "html.parser")
        # get total page
        last_page = soup.select_one('div.wp-pagenavi > a.last')
        print("*********************** Get pages ")
        if last_page is not None:
            page = re.search('/(\d+)/$', last_page.get('href')).group(1)
            channel['page'] = int(page)
            print(page)

        for movie in soup.select('ul.list-film > li > div.inner'):
            title = movie.select_one('div.name > a').find(text=True, recursive=False).strip()
            type = ""
            realtitle = ""

            if movie.select_one('div.status') is not None:
                type = movie.select_one('div.status').text.strip()
            if movie.select_one('div.name2') is not None:
                realtitle = movie.select_one('div.name2').text.strip()
            if realtitle is not None:
                label = "[%s] %s - %s" % (type, title, realtitle)
            else:
                label = "[%s] %s" % (type, title)

            thumb = movie.select_one('a img.lazy').get('data-original')

            channel['movies'].append({
                'id': movie.select_one('div.name > a').get('href'),
                'label': label.encode("utf-8"),
                'title': title.encode("utf-8"),
                'realtitle': realtitle.encode("utf-8"),
                'thumb': thumb,
                'type': type.encode("utf-8"),
            })

        return channel