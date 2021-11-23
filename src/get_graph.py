import yaml

def main(conf):
    with open('graph.yaml') as f:
        d=yaml.safe_load(f.read())
    return d
