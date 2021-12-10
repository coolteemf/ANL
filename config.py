import argparse
import json

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

def make_as_dotdict(obj):
    if type(obj) is dict:
        obj = dotdict(obj)
        for key in obj:
            if type(obj[key]) is dict:
                obj[key] = make_as_dotdict(obj[key])
    return obj

def parse():
    parser = argparse.ArgumentParser(description="config")
    parser.add_argument(
        "--config",
        type=str,
        default="configs/base.json",
        help="Configuration file to use"
    )
    cli_args = parser.parse_args()

    with open(cli_args.config) as fp:
        config = make_as_dotdict(json.loads(fp.read()))
    print(json.dumps(config, indent=4, sort_keys=True))
    return config

cfg = None
# if cfg is None:
#     try:
#         cfg = parse()
#     except:
#         print('** Assert in demo mode. **')

def parse_from_dict(d):
    global cfg
    cfg = make_as_dotdict(d)
