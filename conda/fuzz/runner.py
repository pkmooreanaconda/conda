import os
import multiprocessing
import pathlib
import atheris
from conda.exceptions import InvalidMatchSpec, CondaValueError
import sys

with atheris.instrument_imports():
    from conda.models import match_spec

def TestMatchSpec(data):
    try:
        match_spec.MatchSpec(name='test')
    except InvalidMatchSpec:
        pass

def TestParseSpecStr(data):
    try:
        match_spec._parse_spec_str(str(data))
    except InvalidMatchSpec:
        pass

def run_fuzz_matchspec(ignore):
    with open(f'{ignore}_match_spec_out.log', 'w') as sys.stdout:
        with open(f'{ignore}_match_spec_err.log', 'w') as sys.stderr:
            atheris.Setup(['./conda/fuzz/match_spec_fuzzer.py', './conda/fuzz/match_spec_corpus', '-runs=100'], TestMatchSpec)
            atheris.Fuzz()

def run_fuzz_parse_spec_str(ignore):
    with open(f'{ignore}_parse_spec_str_out.log', 'w') as sys.stdout:
        with open(f'{ignore}_parse_spec_str_err.log', 'w') as sys.stderr:
            atheris.Setup(['./conda/fuzz/match_spec_fuzzer.py', './conda/fuzz/match_spec_corups', '-runs=100'], TestParseSpecStr)
            atheris.Fuzz()

def main():
    multiprocessing.set_start_method("spawn")
    for i in [run_fuzz_matchspec, run_fuzz_parse_spec_str]:
        with multiprocessing.get_context("spawn").Pool(processes=8) as p:
            p.map(i, range(os.cpu_count()))



if __name__ == "__main__":
    main()

         



