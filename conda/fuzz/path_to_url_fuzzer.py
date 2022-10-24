import atheris
import sys

with atheris.instrument_imports():
    from conda.common import url

def TestPathToUrl(data):
    url.path_to_url(str(data))
atheris.Setup(sys.argv, TestPathToUrl)
atheris.Fuzz()