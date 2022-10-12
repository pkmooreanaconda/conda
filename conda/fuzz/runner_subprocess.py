import os
import subprocess
import multiprocessing
from conda.exceptions import InvalidMatchSpec, CondaValueError
import uuid
import sys

def run_subproc(harness):
    base_dir = os.getcwd()
    execution_id = uuid.uuid4()
    output_path = f"./conda/fuzz/output/{harness[0]}/{execution_id}"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    os.chdir(output_path)
    with open(f"{harness[0]}_out.log", 'wb') as newout:
        p = subprocess.Popen(harness[1], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print(f"queueing {p.pid} {output_path}")
        p.wait()
        newout.write(p.stdout.read())
    os.chdir(base_dir)
    print(f"dequeueing {p.pid} {output_path}")


def main():
    harnesses = [('MatchSpec', ['python3', '../../../match_spec_fuzzer.py', '../../../match_spec_corpus', '-runs=100']),
                 ('MatchSpec', ['python3', '../../../match_spec_fuzzer.py', '../../../match_spec_corpus', '-runs=100']),
                 ('_parse_spec_str', ['python3', '../../../parse_spec_str_fuzzer.py', '../../../match_spec_corpus', '-runs=100']),
                 ('_parse_spec_str', ['python3', '../../../parse_spec_str_fuzzer.py', '../../../match_spec_corpus', '-runs=100']),
                 ('_parse_spec_str', ['python3', '../../../parse_spec_str_fuzzer.py', '../../../match_spec_corpus', '-runs=100']),
                 ('_parse_spec_str', ['python3', '../../../parse_spec_str_fuzzer.py', '../../../match_spec_corpus', '-runs=100']),
                 ('_parse_spec_str', ['python3', '../../../parse_spec_str_fuzzer.py', '../../../match_spec_corpus', '-runs=100']),
                 ('_parse_spec_str', ['python3', '../../../parse_spec_str_fuzzer.py', '../../../match_spec_corpus', '-runs=100']),
                 ('_parse_spec_str', ['python3', '../../../parse_spec_str_fuzzer.py', '../../../match_spec_corpus', '-runs=100']),
                 ('_parse_spec_str', ['python3', '../../../parse_spec_str_fuzzer.py', '../../../match_spec_corpus', '-runs=100']),
                 ('_parse_spec_str', ['python3', '../../../parse_spec_str_fuzzer.py', '../../../match_spec_corpus', '-runs=100']),
                 ('_parse_spec_str', ['python3', '../../../parse_spec_str_fuzzer.py', '../../../match_spec_corpus', '-runs=100']),
                 ('_parse_spec_str', ['python3', '../../../parse_spec_str_fuzzer.py', '../../../match_spec_corpus', '-runs=100']),
                 ('_parse_spec_str', ['python3', '../../../parse_spec_str_fuzzer.py', '../../../match_spec_corpus', '-runs=100']),
                 ('_parse_spec_str', ['python3', '../../../parse_spec_str_fuzzer.py', '../../../match_spec_corpus', '-runs=100']),
    ]
    with multiprocessing.Pool() as pool:
            pool.map(run_subproc, harnesses)
            pool.close()
            pool.join()




if __name__ == "__main__":
    main()

         



