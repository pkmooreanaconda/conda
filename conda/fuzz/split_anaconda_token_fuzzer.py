import atheris
import sys

with atheris.instrument_imports():
    from conda.common import url
    

def TestSplitAnacondaToken(data):
    url.split_anaconda_token(str(data))

atheris.Setup(sys.argv, TestSplitAnacondaToken)
atheris.Fuzz()