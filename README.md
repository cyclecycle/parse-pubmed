# parse-pmc

## Getting started

Clone into your project folder:

```
git clone https://github.com/cyclecycle/parse-pmc
```

## Example usage

Get a PubMed Central XML document, for example using Biopython:

```python

from Bio import Entrez, Medline
Entrez.email = 'your.email@domain.com'

ids = [5878862, 5870202, 5861634]

handle = Entrez.efetch(db='pmc', id=ids, rettype='full', retmode='xml')
xml = handle.read()  # PMC article set

```

Parse it:

```python
from parse_pmc import PMCArticleSet

articles = PMCArticleSet(xml).articles  # List of PMCArticle objects

for article in articles:
  print(article.title)
  # print(article.body)  # Full text
  # print(article.ids)
  # print(article.keywords)
```

## Development

Contributions and feature requests welcome.
