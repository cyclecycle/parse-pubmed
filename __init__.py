import os
import sys
cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(cwd)
from pmc import PMCArticleSet, PMCArticle
from pubmed import PubMedArticleSet, PubMedArticle
