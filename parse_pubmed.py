from pprint import pprint
import xml.etree.ElementTree as et
import datetime
import re
import json
import util
from base import ArticleSet, Article


class PubMedArticleSet(ArticleSet):

    def __init__(self, xml):

        self.xml = xml
        self.root = et.fromstring(xml)

        self.articles = []

        for el in self.root.iter('PubmedArticle'):
            xml = et.tostring(el)
            article = PubMedArticle(xml)
            self.articles.append(article)


class PubMedArticle(Article):

    def __init__(self, xml):

        self.xml = xml
        self.root = et.fromstring(xml)

        self.dict = {
            'ids': self.ids(),
            'title': self.title(),
            'abstract': self.abstract(),
            'date': self.date(),
            'keywords': self.keywords(),
        }

        for key, val in self.dict.items():
            self.__setattr__(key, val)

    def ids(self):
        ids = {}
        for child in self.root.iter('ArticleId'):
            _type = child.attrib['IdType']
            ids[_type] = child.text
        return ids

    def title(self):
        title = list(self.root.iter('ArticleTitle'))[0]
        return util.all_element_content(title, join=True)

    def abstract(self):
        try:
            abstract = list(self.root.iter('AbstractText'))[0]
        except:
            return ''
        return util.all_element_content(abstract, join=True)

    def date(self):
        date_tag = list(self.root.iter('PubDate'))[0]
        date = {}
        for el in date_tag:
            date[el.tag] = el.text
        string = '{day} {month} {year}' .format(
            day=date['Day'],
            month=date['Month'],
            year=date['Year']
        )
        d = datetime.datetime.strptime(string, '%d %B %Y')
        return d

    def keywords(self):
        keywords = []
        for el in self.root.iter('Keyword'):
            keywords.append(el.text)
        return keywords
