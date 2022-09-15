import atheris
import sys

with atheris.instrument_imports():
    from conda.models import match_spec

def TestMatchSpec(data):
    match_spec.MatchSpec(name='test')

atheris.Setup(sys.argv, TestMatchSpec)
atheris.Fuzz()
