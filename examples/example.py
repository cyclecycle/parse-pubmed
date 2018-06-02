''' Get PubMed Central full text XML with Biopython '''

from Bio import Entrez, Medline
Entrez.email = 'your.email@domain.com'

handle = Entrez.efetch(db='pmc', id=2747014, rettype='full', retmode='xml')
xml = handle.read()

''' Parse with parse-pmc '''

from parse_pmc import ParsePMC

article = ParsePMC(xml)

print(article.title)
print(article.text)
print(article.ids)
