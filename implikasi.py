def implikasi(p, q): 
    return not p or q 
 
def konvers(p, q): 
    return implikasi(q, p) 
 
def invers(p, q): 
    return implikasi(not p, not q) 
 
def kontraposisi(p, q): 
    return implikasi(not q, not p) 
 
def tabel_kebenaran(): 
    print("tabel kebenaran proposisi bersyarat") 
    print("--------------------------------------") 
    print("P\t|Q\t|P -> Q\t|Q->P\t~P->~Q\t~Q->~P ") 
    print("--------------------------------------") 
    for p in [True, False]: 
        for q in [True, False]: 
            print(f"{p}\t|{q}\t|{implikasi(p, q)}\t|{konvers(p, q)}\t|{invers(p, q)}\t|{kontraposisi(p, q)}") 
 
tabel_kebenaran() 
