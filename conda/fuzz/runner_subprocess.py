import os
import subprocess
import multiprocessing
from conda.exceptions import InvalidMatchSpec, CondaValueError
import uuid
import sys
import datetime

RUNS = "-runs=10000"

def run_subproc(harness):
    start_time = datetime.datetime.now()
    base_dir = os.getcwd()
    execution_id = uuid.uuid4()
    output_path = f"./conda/fuzz/output/{harness[0]}/{execution_id}"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    os.chdir(output_path)
    with open(f"{harness[0]}_out.log", 'wb') as newout:
        p = subprocess.Popen(harness[1] + [RUNS], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print(f"queueing {harness[0]} {p.pid} {output_path}")
        p.wait()
        newout.write(p.stdout.read())
    os.chdir(base_dir)
    end_time = datetime.datetime.now()
    print(f"dequeueing {harness[0]} {p.pid} {output_path} after {(end_time - start_time).seconds} seconds")


def main():      # MatchSpec related harnesses
    harnesses = [('MatchSpec', ['python3', '../../../match_spec_fuzzer.py', '../../../match_spec_corpus']),
                 ('MatchSpec', ['python3', '../../../match_spec_fuzzer.py', '../../../match_spec_corpus']),
                 ('MatchSpec', ['python3', '../../../match_spec_fuzzer.py', '../../../match_spec_corpus']),
                 ('_parse_spec_str', ['python3', '../../../parse_spec_str_fuzzer.py', '../../../match_spec_corpus']),
                 ('_parse_version_plus_build', ['python3', '../../../parse_version_plus_build_fuzzer.py', '../../../match_spec_corpus']),
                 # URL related harnesses
                 ('path_to_url', ['python3', '../../../path_to_url_fuzzer.py', '../../../url_corpus']),
                 ('split_anaconda_token', ['python3', '../../../split_anaconda_token_fuzzer.py', '../../../url_corpus']),
    ]

    with multiprocessing.Pool() as pool:
            pool.map(run_subproc, harnesses)
            pool.close()
            pool.join()




if __name__ == "__main__":
    main()

         



