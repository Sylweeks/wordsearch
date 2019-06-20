
import string
import random
import numpy
kropka=('.')

cfg = [line.rstrip('\n') for line in open("config.txt")]
n=cfg[0]
n=int(n)
KOL=cfg[1]
WIER=cfg[2]
KOL=int(KOL)
WIER=int(WIER)
print("liczba slow, kolumn, wierszy",n,KOL,WIER)
powt = []
litery = list(string.ascii_lowercase)

f = open("slowa.txt", 'r' )
i=0
listaslow = []
liczby = []
while i < n:  #tworzenie losowych liczb
    a = (random.randint(0, 199))
    if a not in liczby:
        liczby.append(a)
        i=i+1
    else: continue

#print(liczby)

listaslow = [line.rstrip('\n') for line in open("slowa.txt")]   #zapis pliku do tablicy
#print(listaslow)

wylosowane=[]    #tworzenie tablicy z wylosowanymi slowami
i = 0
while i < n:
    tmp = liczby[i]
    tmp2 = listaslow[tmp]
    wylosowane.append(tmp2)
    i = i + 1

print(wylosowane)
dlug=0
#sprawdzanie czy dlugosc slowa nie przerasta tablicy
while dlug<=n-1:
    slo=wylosowane[dlug]
    dlu=len(slo)
    if dlug<n/2:
        if dlu>=KOL:
            del wylosowane[dlug]
            n-=1
        else: dlug+=1

    else:
        if dlu>=WIER:
           del wylosowane[dlug]
           n-=1
        else: dlug+=1


print("\nNowa lista slow\n",wylosowane)
#------------------------------------
gierka=numpy.chararray((WIER, KOL), unicode=True)
gierka[:] = '.'
print(gierka)
i = 0

while i < n:
    if i<n/2:
        sl = wylosowane[i]  #tworzenie chara
        print(sl)
        m = len(sl)  #dlugosc slowa
        print(m)
        polozenie=random.randint(1,2)

       # polozenie=random.randint(0, 2) #pion czy poziom
        if polozenie==1:

            for p in range(10):
                kol = random.randint(0, (KOL - m-1))  # losowanie pozycji pierwszej liczby
                wiersz = random.randint(0, WIER-1)

                if wiersz not in powt:
                    powt.append(wiersz)
                    break
                else: continue


            print(wiersz,kol)
            end=kol+m-1
            j=0
            while j<=(m-1):
                while kol<=end:
                    gierka[wiersz][kol] = sl[j]
                    j+=1
                    kol+=1

        elif polozenie==2:
            for p in range(10):
                kol = random.randint(0+m, KOL-1)  # losowanie pozycji pierwszej liczby
                wiersz = random.randint(0, WIER-1)

                if wiersz not in powt:
                    powt.append(wiersz)
                    break
                else: continue
            print(wiersz, kol)
            end = kol - m + 1
            j = 0
            while j <= (m - 1):
                while kol >= end:
                    gierka[wiersz][kol] = sl[j]
                    j += 1
                    kol -= 1
        print(gierka)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    else:
        sl = wylosowane[i]  # tworzenie chara
        print(sl)
        m = len(sl)  # dlugosc slowa
        print(m)
        polozenie = random.randint(1, 2)
        print(polozenie," polozenie")
        # polozenie=random.randint(0, 2) #pion czy poziom
        if polozenie == 1:

            for p in range(20):
                wiersz = random.randint(0, WIER-m-1)  # losowanie pozycji pierwszej liczby
                kol = random.randint(0, KOL-1)
                indeks = 0
                wolne = 0
                wpisane=False
                while indeks <= m:
                    if gierka[wiersz + indeks, kol] == '.':
                        wolne += 1
                        indeks+=1
                        if wolne == m:
                            print(wiersz, kol)
                            end = wiersz + m - 1
                            j = 0
                            while j <= (m - 1):
                                while wiersz <= end:
                                    gierka[wiersz][kol] = sl[j]
                                    j += 1
                                    wiersz += 1
                            print(gierka)
                            wpisane=True
                            break

                    else:
                        break
                if wpisane==True:
                    break
                else:
                    continue
            # losuje miejsce>sprawdzam od 0 do n czy sa w tym miejscu kropki> jezeli tak to wpisuje> nie to jeszcze raz losuje miejsce


        elif polozenie == 2:
            for p in range(20):
                wiersz = random.randint(0+m, WIER-1)  # losowanie pozycji pierwszej liczby
                kol = random.randint(0, KOL-1)
                indeks = 0
                wolne = 0
                wpisane=False
                while indeks <= m:
                    if gierka[wiersz - indeks, kol] == '.':
                        wolne += 1
                        indeks += 1
                        if wolne == m:
                            print(wiersz, kol)
                            end = wiersz - m + 1
                            j = 0
                            while j <= (m - 1):
                                while wiersz >= end:
                                    gierka[wiersz][kol] = sl[j]
                                    j += 1
                                    wiersz -= 1
                            print(gierka)
                            wpisane=True
                            break

                    else:
                        break
                if wpisane==True:
                    break

    i=i+1
print(gierka)


#====================================================================
ww=0            #wypelnianie losowymi literami
while ww<KOL:
    cc=0
    while cc<WIER:
        if gierka[cc,ww]=='.':
            losowalitera = (random.randint(0, 25))
            los=litery[losowalitera]
            gierka[cc,ww]=los
        cc+=1
    ww+=1
print("\n\n\n",gierka)
#dodanie tego samego co jest w wierszach tylko ze w kolumnach
#i dodac pętle while z boolem true ktory sie zmienia i sprawdza czy w danej przestrzeni  sa jakies litery

#-------------------------------wyszukiwanie slow-------------------
for slowko in range(len(listaslow)):
    b = listaslow[slowko]
    pattern = b
    rec=0
    for record in gierka: # to do tylu bierz, kolumna:jak bedzie liczone od tylu to ok, jak od zera to len text-rec
        text = ''.join(record)
        M = len(pattern)
        N = len(text)
        counter = 0
        #musze zebrac slowo z pliku, przejc po wszystkich wierszach
        #czyli for w nim każe slowo, w nim for inkrementujacy linie z tabliocy
        for i in range(N - M + 1):
            j = 0
            podobne=0

            for j in range(0, M):
                if (text[i + j] != pattern[j]):
                    break
                else: podobne+=1
            if (podobne == M):
                print (pattern)
                print("kolumna", i,"wiersz ", rec)


        rec+=1

#sprawdzenie odwrotnej
print ("\nodwrotne\n")
for slowko in range(len(listaslow)):
    b = listaslow[slowko]
    pattern = b
    rec=0
    for record in gierka: # to do tylu bierz, kolumna:jak bedzie liczone od tylu to ok, jak od zera to len text-rec
        text = ''.join(record)
        text=text[::-1]
        M = len(pattern)
        N = len(text)
        counter = 0
        #musze zebrac slowo z pliku, przejc po wszystkich wierszach
        #czyli for w nim każe slowo, w nim for inkrementujacy linie z tabliocy
        for i in range(N - M + 1):
            j = 0
            podobne=0
            # For current index i, check
            # for pattern match */
            for j in range(0, M):
                if text[i + j] != pattern[j]:
                    break
                else:
                    podobne += 1
            if (podobne == M):
                print (pattern)
                print("kolumna", N-i-1 ,"wiersz ", rec)
        rec+=1
#szukanie w pionie++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
trans=numpy.transpose(gierka)

print("\nw pionie\n")
for slowko in range(len(listaslow)):
    b = listaslow[slowko]
    pattern = b
    rec=0

    for record in trans: # to do tylu bierz, kolumna:jak bedzie liczone od tylu to ok, jak od zera to len text-rec
        text = ''.join(record)
        M = len(pattern)
        N = len(text)
        counter = 0
        #musze zebrac slowo z pliku, przejc po wszystkich wierszach
        #czyli for w nim każe slowo, w nim for inkrementujacy linie z tabliocy
        for i in range(N - M + 1):
            j = 0
            podobne=0
            #kot
            #asdfghjkotplow
            for j in range(0, M):
                if (text[i + j] != pattern[j]):
                    break
                else: podobne+=1
            if (podobne == M):
                print (pattern)
                print("kolumna", rec,"wiersz ", i)
        rec+=1

#w pionie na odwrot++++++++++++++++++++++++++++++++++++++++++++++++++++++
print("\nw pionie na odwrot\n")
for slowko in range(len(listaslow)):
    b = listaslow[slowko]
    pattern = b
    rec=0
    for record in trans: # to do tylu bierz, kolumna:jak bedzie liczone od tylu to ok, jak od zera to len text-rec
        text = ''.join(record)
        text=text[::-1]
        M = len(pattern)
        N = len(text)
        counter = 0
        #musze zebrac slowo z pliku, przejc po wszystkich wierszach
        #czyli for w nim każe slowo, w nim for inkrementujacy linie z tabliocy
        for i in range(N - M + 1):
            j = 0
            podobne=0
            # For current index i, check
            # for pattern match */
            for j in range(0, M):
                if text[i + j] != pattern[j]:
                    break
                else:
                    podobne += 1
            if (podobne == M):
                print (pattern)
                print("kolumna", rec ,"wiersz ", N-i-1)
        rec+=1


"""
print("\n\nkarp rabin")

res=False
for slowko in range(len(listaslow)):
    koll = 0
    for record in gierka:
        koll +=1
        text=record
        pattern = listaslow[slowko]
        n = len(text)
        d = 30
        q = 97
        m = len(pattern)
        h = pow(d, m - 1) % q
        p = 0
        t = 0
        i
        result = 0
        for i in range(m):  # preprocessing
            p = (d * p + ord(pattern[i])) % q
            t = (d * t + ord(text[i])) % q
        for s in range(n - m + 1):  # note the +1
            if p == t:  # check character by character
                match = True
                for i in range(m):
                    if pattern[i] != text[s + i]:
                        match = False
                        break
                if match:
                    result = result + s
                    res=True
            if s < n - m:
                t = (t - h * ord(text[s])) % q  # remove letter s
                t = (t * d + ord(text[s + m])) % q  # add letter s+m
                t = (t + q) % q  # make sure that t >= 0
        if res==True:
            koll -= 1
            print(pattern, "  kolumna: ",result," wiersz: ", koll)
            res = False

print("\npoziom odwrotnie")
res=False
for slowko in range(len(listaslow)):
    koll = 0
    for record in gierka:
        koll +=1
        text=record
        pattern = listaslow[slowko]
        text = text[::-1]
        n = len(text)
        d = 30
        q = 97
        m = len(pattern)
        h = pow(d, m - 1) % q
        p = 0
        t = 0
        result =0
        for i in range(m):  # preprocessing
            p = (d * p + ord(pattern[i])) % q
            t = (d * t + ord(text[i])) % q
        for s in range(n - m + 1):  # note the +1
            if p == t:  # check character by character
                match = True
                for i in range(m):
                    if pattern[i] != text[s + i]:
                        match = False
                        break
                if match:
                    result = result + s
                    res=True
            if s < n - m:
                t = (t - h * ord(text[s])) % q  # remove letter s
                t = (t * d + ord(text[s + m])) % q  # add letter s+m
                t = (t + q) % q  # make sure that t >= 0
        if res==True:
            koll-=1
            result=n-result-1
            print(pattern, "  kolumna: ",result," wiersz: ", koll)

            res=False

print("\npion\n")

res=False
for slowko in range(len(listaslow)):
    koll = 0
    for record in trans:
        koll +=1
        text=record
        pattern = listaslow[slowko]
        n = len(text)
        d = 30
        q = 97
        m = len(pattern)
        h = pow(d, m - 1) % q
        p = 0
        t = 0
        result = 0
        for i in range(m):  # preprocessing
            p = (d * p + ord(pattern[i])) % q
            t = (d * t + ord(text[i])) % q
        for s in range(n - m + 1):  # note the +1
            if p == t:  # check character by character
                match = True
                for i in range(m):
                    if pattern[i] != text[s + i]:
                        match = False
                        break
                if match:
                    result = result + s
                    res=True
            if s < n - m:
                t = (t - h * ord(text[s])) % q  # remove letter s
                t = (t * d + ord(text[s + m])) % q  # add letter s+m
                t = (t + q) % q  # make sure that t >= 0
        if res==True:
            koll -= 1
            print(pattern, "  kolumna: ",koll," wiersz: ", result)
            res = False

print("\nod dolu do gory\n")

res=False
for slowko in range(len(listaslow)):
    koll = 0
    for record in trans:
        koll +=1
        text=record
        pattern = listaslow[slowko]
        text = text[::-1]
        n = len(text)
        d = 30
        q = 97
        m = len(pattern)
        h = pow(d, m - 1) % q
        p = 0
        t = 0
        result =0
        for i in range(m):  # preprocessing
            p = (d * p + ord(pattern[i])) % q
            t = (d * t + ord(text[i])) % q
        for s in range(n - m + 1):  # note the +1
            if p == t:  # check character by character
                match = True
                for i in range(m):
                    if pattern[i] != text[s + i]:
                        match = False
                        break
                if match:
                    result = result + s
                    res=True
            if s < n - m:
                t = (t - h * ord(text[s])) % q  # remove letter s
                t = (t * d + ord(text[s + m])) % q  # add letter s+m
                t = (t + q) % q  # make sure that t >= 0
        if res==True:
            koll-=1
            result=n-result-1
            print(pattern, "  kolumna: ",koll," wiersz: ", result)

            res=False
            """





