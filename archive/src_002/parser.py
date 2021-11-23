import json

def load_data(x):
    """
    x: context, graph
    """
    with open(f'{x}.json') as f:
        d=json.loads(f.read())
    return d

def get_graph_table(graph): # Then extend with context
    table=str()
    columns=['source','edge','target','references']
    for c in columns:
        table+=f'{c},'
    table=table[:-1]+'\n'

    for s in graph:
        source=s['name']
        for e in s['edges']:
            edge=e['name']
            for t in e['targets']:
                target=t['name']
                refs=str()
                refs_list=t['ref']
                refs_list.sort()
                for r in refs_list:
                    refs+=f'{r}-'
                refs=refs[:-1]
                line=f'{source},{edge},{target},{refs}'
                table+=line+'\n'

    fp='table_graph.csv'
    with open(fp, 'w') as f:
        f.write(table)
    print(f'Wrote {fp}')
    print(table[:1000])


if __name__=='__main__':
    #context=load_data('context')
    graph=load_data('graph')
    get_graph_table(graph)

