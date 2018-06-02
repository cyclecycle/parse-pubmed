import json


class ArticleSet:

    def __repr__(self):
        return '{0} {1}' .format(self.__class__, len(self.articles))

    def __getitem__(self, index):
        return self.articles[index]

    def __len__(self):
        return len(self.articles)

    def as_dicts(self):
        return [a.dict for a in self.articles]

    def to_json(self, fp):
        dd = self.as_dicts()
        with open(fp, 'w') as f:
            json.dump(dd, f, ensure_ascii=False, indent=2)


class Article:

    def __repr__(self):
        return '{0} {1}' .format(self.__class__, self.title)
