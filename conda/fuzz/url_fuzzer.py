import atheris
import sys

with atheris.instrument_imports():
    from conda.common import url
    

def TestSplitAnacondaToken(data):
    url.split_anaconda_token(str(data))

def TestPathToUrl(data):
    url.path_to_url(str(data))
atheris.Setup([sys.argv[0], 'conda/fuzz/url_corpus', '-runs=1000000'], TestSplitAnacondaToken)
atheris.Fuzz()
atheris.Setup([sys.argv[0], 'conda/fuzz/path_corpus', '-runs=1000000'], TestPathToUrl)
atheris.Fuzz()