import atheris
import sys

with atheris.instrument_imports():
    from conda.models import match_spec


def TestParseSpecStr(data):
    match_spec._parse_spec_str(data)

atheris.Setup(sys.argv, TestParseSpecStr)
atheris.Fuzz()
