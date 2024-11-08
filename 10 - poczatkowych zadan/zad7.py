def wb(a):
    if a>=0:
        return a
    return -a
def sort_szyb(liczby):
    dl = len(liczby)
    if dl<2:
        return liczby
    pi=dl-1
    p=[]
    l=[]
    for i in range(dl-1):
        if liczby[i]>liczby[pi]:
            p.append(liczby[i])
        else:
            l.append(liczby[i])
    return sort_szyb(l)+[liczby[pi]]+sort_szyb(p)
def czy_jest(element,zbior):
    for i in range(len(zbior)):
        if element==zbior[i]:
            return 1
    return 0
def sort_bab(liczby,dlugosc,sr):
    tab=[]
    ile=0
    for i in range(dlugosc):
        w=wb(sr-liczby[i])
        if w>0:
            ile+=1
            tab.append([liczby[i],wb(sr-liczby[i])])
    print(tab)
    for i in range(ile):
        for j in range(1,ile):
            if tab[j][1]<tab[j-1][1]:
                t1=tab[j][1]
                tab[j][1]=tab[j-1][1]
                tab[j-1][1]=t1
                t1=tab[j][0]
                tab[j][0]=tab[j-1][0]
                tab[j-1][0]=t1
    print(tab)
    liczby=[]
    for i in range(6):
        liczby.append(tab[i][0])
    return liczby
def tab_z_liczbami(a,b):
    tab=[]
    for i in range(a,b+1):
        tab.append(i)
    return tab
a,b=map(int,input().split())
sr=(a+b)/2
print('sr',sr)
tab=tab_z_liczbami(a,b)
print("test1",wb(a-b))
if wb(a-b)>20:
    print("test2 - 1")
    tab = sort_bab(tab,wb(a-b)+1,sr)
    print(tab)
    i=0
    ile=0
    while ile<6:
        if tab[i]!=sr:
          print(tab[i])
          ile+=1
        i+=1
else:
    print("test2 - 2")
    for i in range(wb(a-b)+1):
        print(tab[i])
        
