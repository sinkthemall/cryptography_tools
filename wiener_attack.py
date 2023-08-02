def cf_expansion(a,b):
    ls = []
    ls.append(a//b)
    a,b = b, a%b
    while(b!=0):
        ls.append(a // b)
        a , b = b, a%b
    return ls
import math
def cf_convergent(ls):
    n = []
    d = []
    for i in range(len(ls)):
        if (i == 0):
            n.append(ls[i])
            d.append(1)
        elif i == 1:
            n.append(ls[1]*ls[0] + 1)
            d.append(ls[1])
        else:
            n.append(n[i-1]*ls[i] + n[i-2])
            d.append(d[i-1]*ls[i] + d[i-2])
        yield n[i],d[i]

def solve(B,P):
    delta = B*B - 4*P
    if (delta<0):
        return 0,0
    rdel = math.isqrt(delta)
    return (B + rdel)//2, (B - rdel)//2

def find_d(n,e):
    for k,d in cf_convergent(cf_expansion(e,n)):
        if (k==0):
            continue
        phin = (e*d - 1)//k
        sum = n - phin + 1
        p, q = solve(sum, n)
        if (p*q==n):
            return d
    return 0

from Crypto.Util.number import long_to_bytes


n=  20730814227170035978651150623884113467538331364064187483844922915543368586281292758099778495492928622287063912938154562403564193508954661463984331992373565705874778794515848043194522715148247697317077843536935867831118970473687258003129536232635508875759320778737246294991836625989556126878715414854325861010168930046693321490383950756856275062743366177392961787099393260774462686316872849066513172992426455282401991962784621639336394969701176433226322521793535913848081544919180450319369134353108111744476102938201681536020411763003963118913899428856892281670591305762292489676542591268810772523288739892746986603947
e=1730242358296900068996718663153466313432077415930242828128741770469150991494902842314253939703650797756140830662720694593354528221055773356493344163840073363904032141322049886147439348709779018919584234346763671632615722761698136995113550484596339375276773323627600076356366024561773650829965098942289959384871256582924361015321036417147843348984658745217690489956401689984098636041621718559789522575875748325881202580463598115357000071506441156318590657066222960703226805887223723790964290589393729422073170749440322347564542635030839661110152810787612179637762984780409942946680625628299576067626355867728720874091
c = 17089642419716809928561105562907726606059137782926562737219648562239889440707259627027617778532174911169259323955372458720157910787593342386979225016536378446349096758157640977735040270654664158545944362543703558347005631353097935651281512899419003775791438503692399318131070741308274592520457860245363633007094625107831162905651251789181483146574134561283546576186677221836461827951051781207165308278641555216006944449170224403354520527059291631738647077743380621163736210918725954028605704980308772328755903008666899195409396301088787641915932201371748177886453007065944909260667047902066406456410674495714511580529
d = find_d(n,e)
if d!= 0:
    print(long_to_bytes(pow(c,d,n)))




