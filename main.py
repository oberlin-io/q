import os
from src import conf
from src import get_graph
from src import parser

def main():
    graph=get_graph.main(conf)

    u=input('''
    c: graph to csv
    ''')

    if u=='c':
        parser.to_csv(conf, graph)

    import pandas as pd

    df=pd.read_csv(conf.graph_csv_fp)

    #sort=['source', 'edge', 'target', 'ref']
    sort=['ref', 'source', 'edge', 'target',]
    df.sort_values(by=sort, inplace=True)

    print(df.to_string(index=False))

    return df

if __name__=='__main__':
    main()
