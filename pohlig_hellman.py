from Crypto.Util.number import inverse, long_to_bytes, getPrime
import random
from sympy.ntheory import discrete_log

def  baby_step_giant_step(a, b, p, g):# b^g = 1 mod p
    m = 1
    while m*m<g:
        m += 1
    ls = {}
    for i in range(0, m):
        ls[(a*pow(b, i, p))%p] = i 
    for i in range(0, m + 1):
        val = pow(b, i*m, p)
        try:
            x = i*m - ls[val]
            if x>=0:
                return x
        except KeyError:
            pass
    raise Exception

def caculate_part(a, b, p, G, g):#G : product of all g
    q, c = g
    A = a
    x = 0
    for i in range(c):
        p1 = pow(A, G // pow(q, i + 1), p) #p1 = a
        p2 = pow(b, G // q, p) #p2 = b
        cal = baby_step_giant_step(p1, p2, p, q)
        x = x + cal*pow(q, i)
        A = (A*pow(b, -cal*(q**i), p))%p
    return x

def crt_caculate(g):
    N = 1
    for x, y in g:
        N = N*y
    A = 0
    for x, y in g:
        A = A + x*(N // y)*pow(N // y, -1, y)
        A %= N
    return A

def pohlig_hellman(a, b, g, p, G):#G : product of all g
    crt = []
    for qi, ei in g:
        xi = caculate_part(a, b, p, G, (qi, ei))
        crt.append((xi, pow(qi, ei)))
        print("finished", qi, ei)
    return crt_caculate(crt)
# a = b^x(mod p)
#G : order of b
#g : list of factors



p = 13912479707615671771992568151874481903073684994506324867719769628549168284196058692755725914068362374530844491398962702845044765688436777526794986920095711658880021331684365369920211945613693096583037257643104489076407345489264104575942479302500575354302150523026969557478967141235277351781473564094541414443631276535699814821592831218562114114071475538300870839668854468754039085806543105621651381953288954430569302911155808361363237665087980832872160451244524545405755744458566804194374651416466895586084664060740285212509427511037469630155953059482773524842699757234170575247797635216192466068795070825766952960310479
G = p - 1
g = [(2 , 1) , (527327 , 1) , (528659 , 1) , (531457 , 1) , (539993 , 1) , (541129 , 1) , (546781 , 1) , (549121 , 1) , (553093 , 1) , (554849 , 1) , (574907 , 1) , (585199 , 1) , (589579 , 1) , (596083 , 1) , (600401 , 1) , (601943 , 1) , (612713 , 1) , (631931 , 1) , (634169 , 1) , (639433 , 1) , (641701 , 1) , (647189 , 1) , (657779 , 1) , (658127 , 1) , (669733 , 1) , (670577 , 1) , (679153 , 1) , (683201 , 1) , (687917 , 1) , (692821 , 1) , (693127 , 1) , (707501 , 1) , (708007 , 1) , (709649 , 1) , (709729 , 1) , (714061 , 1) , (716087 , 1) , (725507 , 1) , (734047 , 1) , (734627 , 1) , (735673 , 1) , (740021 , 1) , (749297 , 1) , (752083 , 1) , (752137 , 1) , (756887 , 1) , (760297 , 1) , (772073 , 1) , (779413 , 1) , (780601 , 1) , (789473 , 1) , (793927 , 1) , (805687 , 1) , (806941 , 1) , (808147 , 1) , (815333 , 1) , (820679 , 1) , (825007 , 1) , (829457 , 1) , (834593 , 1) , (837017 , 1) , (837257 , 1) , (841259 , 1) , (853319 , 1) , (855857 , 1) , (856693 , 1) , (857267 , 1) , (857513 , 1) , (857809 , 1) , (869579 , 1) , (872173 , 1) , (873617 , 1) , (876067 , 1) , (879391 , 1) , (888109 , 1) , (889037 , 1) , (897931 , 1) , (898519 , 1) , (907909 , 1) , (910771 , 1) , (911917 , 1) , (932441 , 1) , (941299 , 1) , (953969 , 1) , (958039 , 1) , (958141 , 1) , (959449 , 1) , (963031 , 1) , (972721 , 1) , (979717 , 1) , (995513 , 1) , (995737 , 1) , (1003753 , 1) , (1005409 , 1) , (1014743 , 1) , (1017031 , 1) , (1017209 , 1) , (1019399 , 1) , (1020259 , 1) , (1021621 , 1) , (1027739 , 1) , (1028329 , 1) , (1032881 , 1) , (1040563 , 1) , (1040747 , 1) , (1041091 , 1)]
b = 2
a = 0x1a11b2ec2d4684492877a0d4fd201eda21bbe35b950b6d268951bd264590bc8c584ec62c19c6f493da107aed7ad4edf05d0171ce188521a6a48a540f522540f6d413ab566274856ed813de64f8c4861c7efc46c4e33faaf5472da35453c806519fd31b1e8dbbf4e4b3c99f91cae2ccff9d4032c72f303eca5866394a174ee52cf4baf73bc8f2a95c4037be8fa2f54604f72b1f93b50cd35c226dd024faed0d7d9db81ef0bbe00748b682cc12598acf5a5620681acdecdd6a9f50877fba8e8e5d6fde14e1e2cec6c2dd57db82ca38c81479ca9301f564fd8edbe6339f8ca89fdcf813481913a55ade7ff6f8aadcfaf6b1aa8f12174da00a703d35b002633b060b5c
d = pohlig_hellman(a, b, g, p, G)
if pow(b,d,p) == a:
    print('correct')
print(d)