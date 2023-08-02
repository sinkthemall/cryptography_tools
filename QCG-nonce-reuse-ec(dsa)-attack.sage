#this is the list of signature
p = 12345 #this is the finite field you are currently working on, setup this the same prime as yours

Fp = GF(p); 
P.<x> = PolynomialRing(Fp)
# x is the secret key in this case

R = []
S = []
H = []


def kij(i, j):
    h_i, h_j = Fp(H[i]), Fp(H[j])
    inv_s_i, inv_s_j = Fp(pow(S[i], -1, p)), Fp(pow(S[j], -1, p))
    r_i, r_j = Fp(R[i]), Fp(R[j])
    return x * (r_i * inv_s_i - r_j * inv_s_j) + h_i * inv_s_i - h_j * inv_s_j

def dpoly(n, i, j):
    if i == 0:
        return (kij(j + 1, j + 2) * kij(j + 1, j + 2)) - (kij(j + 2, j + 3) * kij(j, j + 1)) 
    else:
        left = dpoly(n, i - 1, j)
        for m in range(1, i + 2):
            left = left * kij(j + m, j + i + 2)
        right = dpoly(n, i - 1, j + 1)
        for m in range(1, i + 2):
            right = right * kij(j, j + m)
        return left - right

N = len(H)
# N is the number of nonce that were generated, N - 3 should be the degree of polynomial, and N - 2 is number of coefficients

f = dpoly(N - 4, N - 4, 0) # this was from documents, you can read about it here: https://eprint.iacr.org/2023/305.pdf

for i in f.roots():
    print("found possible secret key")
    print(i)


