Pcurve = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
Acurve = 0; Bcurve = 7
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
GPoint = (Gx, Gy)
#privKey = 0xA0DC65FFCA799873CBEA0AC274015B9526505DAAAED385155425F7337704883E
privKey=0x89

def modinv(a, n=Pcurve):

    lm,hm = 1,0
    low,high = a%n,n
    while low>1 :
        ratio=high/low
        nm, new = hm-lm*ratio, high-low*ratio
        lm, low, hm, high = nm, new, lm, low
    return lm % n

def ecadd(a,b):

    LamAdd = ((b[1]-a[1]) * modinv(b[0]-a[0], Pcurve)) % Pcurve
    x = (LamAdd*LamAdd-a[0]-b[0]) % Pcurve
    y = (LamAdd*(a[0]-x)-a[1]) % Pcurve
    return (x,y)

def ecdouble(a):

    lam =((3*a[0]*a[0]+Acurve)*modinv((2*a[1]), Pcurve)) % Pcurve
    x = (lam*lam-2*a[0]) % Pcurve
    y = (lam*(a[0]-x)-a[1]) % Pcurve
    return (x, y)

def eccmultiply(genpoint,scalarhex):

    if scalarhex == 0 or scalarhex >= N : raise Exception("invalid Scalar/private key")
    scalarbin = str(bin(scalarhex))[2:]
    Q = genpoint
    for i in range(1, len(scalarbin)):
        Q = ecdouble(Q);print("dub", Q[0])
        if scalarbin[i] == "1":
            Q = ecadd(Q, genpoint);print("add", Q[0])
    return Q

print ("*******public key generation*******")
PublicKey = eccmultiply(GPoint, privKey)
#print ("the private key:  "+privKey)
#print ("the uncompressed public key: "+PublicKey)
#print ("the official public key-compressed: "+"02"+str(hex(PublicKey[0])[2:-1]).zfill(64))
print(PublicKey)

