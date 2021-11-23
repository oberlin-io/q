import yaml

def to_csv(conf, graph):
    c='source,edge,target,ref,tag\n'
    for s in graph:
        for e in s['edges']:
            for t in e['targets']:
                if 'tag' in t.keys():
                    tag=t['tag']
                else:
                    tag=str()
                for r in t['refs']:
                    c+=f"{s['@id']},{e['@id']},{t['@id']},{r},{tag}\n"
    with open(conf.graph_csv_fp, 'w') as f:
        f.write(c)
