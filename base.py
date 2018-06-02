class ArticleSet:

    def __repr__(self):
        return '{0} {1}' .format(self.__name__, len(self.articles))

    def __getitem__(self, index):
        return self.articles[index]

    def __len__(self):
        return len(self.articles)

    def to_json(self, fp):
        dd = [a.dict for a in self.articles]
        with open(fp, 'w', encoding='utf-8') as f:
            json.dump(dd, fp)


class Article:

    def __repr__(self):
        return '{0} {1}' .format(self.__name__, self.title)
