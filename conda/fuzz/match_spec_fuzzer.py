import atheris
import sys
from conda.exceptions import InvalidMatchSpec, InvalidVersionSpec, InvalidSpec

with atheris.instrument_imports():
    from conda.models import match_spec

def TestMatchSpec(data):
    try:
        match_spec.MatchSpec(str(data))
    except (InvalidMatchSpec, InvalidVersionSpec, InvalidSpec):
        pass

atheris.Setup(sys.argv, TestMatchSpec)
atheris.Fuzz()
