import atheris
import sys
from conda.exceptions import InvalidMatchSpec, InvalidVersionSpec, InvalidSpec

with atheris.instrument_imports():
    from conda.models import match_spec


def TestParseSpecStr(data):
    try:
        match_spec._parse_spec_str(str(data))
    except (InvalidMatchSpec, InvalidVersionSpec, InvalidSpec):
        pass

atheris.Setup(sys.argv, TestParseSpecStr)
atheris.Fuzz()
