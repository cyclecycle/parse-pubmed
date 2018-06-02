''' Get PubMed Central full text XML with Biopython '''

from Bio import Entrez, Medline
Entrez.email = 'your.email@domain.com'

handle = Entrez.efetch(db='pmc', id=2747014, rettype='full', retmode='xml')
xml = handle.read()

''' Parse with parse-pmc '''
#TODO