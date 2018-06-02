import os
import sys
cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(cwd)
from parse_pmc import PMCArticleSet, PMCArticle
from parse_pubmed import PubMedArticleSet, PubMedArticle
