from pprint import pprint
import xml.etree.ElementTree as et
import re
import util
from base import ArticleSet, Article


class PMCArticleSet(ArticleSet):

    def __init__(self, xml):

        self.xml = xml
        self.root = et.fromstring(xml)

        self.articles = []

        for el in self.root.iter('article'):
            xml = et.tostring(el)
            article = PMCArticle(xml)
            self.articles.append(article)


class PMCArticle(Article):

    def __init__(self, xml):

        self.xml = xml
        self.root = et.fromstring(xml)

        self.dict = {
            'ids': self.ids(),
            'title': self.title(),
            'abstract': self.abstract(),
            # 'date': self.date(),
            'keywords': self.keywords(),
            'body': self.body(),
            'sections': self.sections()
        }

        for key, val in self.dict.items():
            self.__setattr__(key, val)

        text = []
        for s in [self.title, self.abstract, self.body]:
            if s:
                if s[-1] != '.':
                    s += '.'
                text.append(s)
        self.text = '\n'.join(text)

    def ids(self):
        ids = {}
        for child in self.root.iter('article-id'):
            _type = child.attrib['pub-id-type']
            ids[_type] = child.text
        return ids

    def title(self):
        title = list(self.root.iter('article-title'))[0]
        return util.all_element_content(title, join=True)

    def abstract(self):
        try:
            abstract = list(self.root.iter('abstract'))[0]
        except:
            return ''
        return util.all_element_content(abstract, join=True)

    def body(self):
        try:
            body = list(self.root.iter('body'))[0]
        except IndexError as e:
            return ''
        content = util.all_element_content(body, join=True)
        return content

    def keywords(self):
        keywords = []
        for el in self.root.iter('kwd'):
            keywords.append(el.text)

    def sections(self):
        sections = {}

        try:
            body = list(self.root.iter('body'))[0]
        except IndexError as e:
            return {}

        for section in body.findall('sec'):
            title = section[0].text
            section.remove(section[0])
            content = util.all_element_content(section, join=True)
            sections[title] = content

        return sections
