import os
import subprocess
from conda.exceptions import InvalidMatchSpec, CondaValueError
import sys

def main():
    harnesses = [('MatchSpec', ['python3', './conda/fuzz/match_spec_fuzzer.py', './conda/fuzz/match_spec_corpus', '-runs=100']),
                 ('_parse_spec_str', ['python3', './conda/fuzz/parse_spec_str_fuzzer.py', './conda/fuzz/match_spec_corpus', '-runs=100']),
    ]
    handles = {}
    while True:
        if len(harnesses) >= 8:
            time.sleep(5)
        else:
            with open(f"{i[0]}_out.log", 'w') as newout:
                with open(f"{i[0]}_err.log", 'w') as newerr:
                    p = subprocess.Popen(i[1], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                    print(f"queueing {p.pid}")
                    handles[p.pid] = p


    while len(handles) > 0:
        pid, status = os.wait()
        if pid in handles:
            del(handles[pid])
            print(f"Deleting handle {pid}")





if __name__ == "__main__":
    main()

         



