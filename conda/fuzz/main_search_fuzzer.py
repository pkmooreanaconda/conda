import atheris
import sys

with atheris.instrument_imports():
    from conda.cli import main_search
    

def TestMatchSpec(data):
    arg_obj = type('', (), {})()
    arg_obj.match_spec = data
    arg_obj.envs = None
    arg_obj.info = None
    main_search.execute(arg_obj, None)

atheris.Setup(sys.argv, TestMatchSpec)
atheris.Fuzz()
