#define curve, modify this to your solution

p = 0xfffffffffffffffffffffffffffffffeffffffffffffffff
a = 0xfffffffffffffffffffffffffffffffefffffffffffffffc
b = 0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1
Fp = GF(p)

from random import randint 

def generate_smooth_order_curve():
    #not completely smooth, only a part of it,as gening a completely smooth gonna take lots of time

    while True:
        B = randint(1, p - 1)
        EC = EllipticCurve(Fp, [a, B])
        N = EC.order()
        ok = prime_factors(N)
        pt = EC.gen(0)
        for i in ok:
            if i > 2 ^ 25:
                pt = pt * i 
        if pt.order() >= 2 ^ 32: #you can change the smoothness to any number
            print(ok)
            print(prime_factors(pt.order()))
            return (EC, pt) 
        
ec = EllipticCurve(GF(p), [a, b])
temp = []

times = 10 # modify this to suit your solution

for i in range(times):
    temp.append(generate_smooth_order_curve())
print("gen curve complete")


G = ec.gen(0) # the generator point
privatekey = randint(1, p-1)
pubkey = G * privatekey


# Task: finding private key


def queries(pt):
    '''
    query point to the server and get the correspond_pubkey = pt * privatekey
    '''
    return x,y 

mod = []
res = []


for i in range(times):
    curve, pt = temp[i] 
    x,y = pt.xy()

    correspond_pubkey = curve(queries(pt))
    _k = pt.discrete_log(correspond_pubkey)
    mod.append(pt.order())
    res.append(_k)


secretkey = crt(res, mod)

basepoint = pubkey * int(pow(secretkey, -1, ec.order()))

assert(basepoint == G)

