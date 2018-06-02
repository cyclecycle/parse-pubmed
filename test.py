"""Requires pip install biopython"""

from Bio import Entrez, Medline
from pubmed import PubMedArticleSet, PubMedArticle
from pmc import PMCArticleSet, PMCArticle


Entrez.email = 'your.email@domain.com'

query = 'amyloid cascade'

# Pubmed abstracts

# with Entrez.esearch(db='pubmed', term=query, retmax=2) as handle:
#     record = Entrez.read(handle)
#     pmids = record['IdList']
    
# print(len(pmids))

# handle = Entrez.efetch(db='pubmed', id=pmids, rettype='full', retmode='xml')
# xml = handle.read()

# with open('data/amyloid_cascade_pmc.xml', 'w', encoding='utf-8') as f:
#     f.write(xml)

with open('data/amyloid_cascade_pmc.xml', encoding='utf-8') as f:
    xml = f.read()

article_set = PubMedArticleSet(xml)
# print(article_set[0].title)
# print(article_set[0].abstract)
# print(article_set[0].date)
# print(article_set[0].keywords)

for article in article_set:
    print(article.ids)

# handle = Entrez.efetch(db='pmc', id=5861634, rettype='full', retmode='xml')
# xml = handle.read()

# with open('pmc_xml_example.xml', 'w') as f:
#     f.write(xml)

# with open('pmc_xml_example.xml') as f:
#     xml = f.read()

# article = PMCArticle(xml)
# print(article.body)

# # print(article.title)
# # print(article.sections)
# # print(article.id)
# # print(article.authors)
# # print(article.citations)
