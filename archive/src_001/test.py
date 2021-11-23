import pandas as pd
import os
import conf

def get_data():
    # Get data
    add=pd.read_csv(os.path.join(conf.data, 'address.csv'))
    tok=pd.read_csv(os.path.join(conf.data, 'token.csv'))
    root=pd.read_csv(os.path.join(conf.data, 'root.csv'))
    sema=pd.read_csv(os.path.join(conf.data, 'semantics.csv'))

    # Join
    on='token_id'
    df=pd.merge(add, tok, left_on=on, right_on=on)
    df=pd.merge(df, root, left_on=on, right_on=on)
    df=pd.merge(df, sema, left_on=on, right_on=on)

    sort=['address', 'source_node', 'target_node']
    df=df.sort_values(by=sort).fillna('-')

    return df

def get_ayah(quran, ayah_address):

    ayah=quran[quran.address.str.startswith(ayah_address)]

    ayah_str=ayah_address+' '
    ayah_str2='        '

    sema_rows=0
    for address in ayah.address:
        word=ayah[ayah.address==address]
        if word.shape[0] > sema_rows: sema_rows=word.shape[0]

    buf=4
    token_spc=ayah.source_node.str.len().append(ayah.target_node.str.len()).max()+buf

    if token_spc<5: token_spc=5
    for address in ayah.address.unique():
        token=ayah[ayah.address==address].token.tolist()[0]+' '
        pad=' '*(token_spc-len(token))
        ayah_str+=token+pad

        word_address=address[-3:]
        pad2=' '*(token_spc-len(word_address))
        ayah_str2+=word_address+pad2

    txt=ayah_str.rstrip()+'\n'+ayah_str2.rstrip()

    """
    for i in range(sema_rows):
        txt+='\n        '
        for address in ayah.address.unique():
            word=ayah[ayah.address==address]
            try:
                if word.sema_level.tolist()[i]==1:
                    x=word.source_node.tolist()[i]
                    pad=' '*(token_spc-len(x))
                    txt+=x+pad
            except IndexError:
                txt+=' '*token_spc
                continue
            try:
                if word.sema_level.tolist()[i]==2:
                    x=word.source_node.tolist()[i]
                    x=' '+x
                    pad=' '*(token_spc-len(x))
                    txt+=x+pad
            except IndexError:
                txt+=' '*token_spc
                continue
            try:
                if word.sema_level.tolist()[i]==3:
                    x=word.source_node.tolist()[i]
                    x='  '+x
                    pad=' '*(token_spc-len(x))
                    txt+=x+pad
            except IndexError:
                txt+=' '*token_spc
                continue
        txt+='\n        '
        for address in ayah.address.unique():
            word=ayah[ayah.address==address]
            try:
                if word.sema_level.tolist()[i]==1:
                    x=word.target_node.tolist()[i]
                    x=' '+x
                    pad=' '*(token_spc-len(x))
                    txt+=x+pad
                elif word.sema_level.tolist()[i]==2:
                    x=word.target_node.tolist()[i]
                    x='  '+x
                    pad=' '*(token_spc-len(x))
                    txt+=x+pad
                elif word.sema_level.tolist()[i]==3:
                    x=word.target_node.tolist()[i]
                    x='   '+x
                    pad=' '*(token_spc-len(x))
                    txt+=x+pad
            except IndexError:
                continue
    """
    print(txt)

    return ayah

    
    """
    if ayah!=address[:-4]:
        ayah=address[:-4]
        mushaf+='\n'+address[:-4]+' '
    x=df[df.address==address]
    mushaf+=x.token.unique().tolist()[0]+' '
    """

def test():
    quran=get_data()
    print(get_ayah(quran, '001.001'))

if __name__=='__main__':
    test()
