import tkinter as tk
from functools import partial
import hashlib
import random

Pcurve = 2 ** 256 - 2 ** 32 - 2 ** 9 - 2 ** 8 - 2 ** 7 - 2 ** 6 - 2 ** 4 - 1
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
Acurve = 0;
Bcurve = 7
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
Signature=1
Transactionid=1
GPoint = (Gx, Gy)
# privKey = 0xA0DC65FFCA799873CBEA0AC274015B9526505DAAAED385155425F7337704883E
privKey1=1
ran = random.randrange(10 ** 80)
myhex = "%064x" % ran
privKey = random.randrange(89)
privKey2=1
def call_result(label_result, n1, n2):


    def modinv(a, n=Pcurve):

        lm, hm = 1, 0
        low, high = a % n, n
        while low > 1:
            ratio = high / low
            nm, new = hm - lm * ratio, high - low * ratio
            lm, low, hm, high = nm, new, lm, low
        return lm % n

    def ecadd(a, b):

        LamAdd = ((b[1] - a[1]) * modinv(b[0] - a[0], Pcurve)) % Pcurve
        x = (LamAdd * LamAdd - a[0] - b[0]) % Pcurve
        y = (LamAdd * (a[0] - x) - a[1]) % Pcurve
        return (x, y)

    def ecdouble(a):

        lam = ((3 * a[0] * a[0] + Acurve) * modinv((2 * a[1]), Pcurve)) % Pcurve
        x = (lam * lam - 2 * a[0]) % Pcurve
        y = (lam * (a[0] - x) - a[1]) % Pcurve
        return (x, y)

    def eccmultiply(genpoint, scalarhex):

        if scalarhex == 0 or scalarhex >= N: raise Exception("invalid Scalar/private key")
        scalarbin = str(bin(scalarhex))[2:]
        Q = genpoint
        for i in range(1, len(scalarbin)):
            Q = ecdouble(Q);
            print("dub", Q[0])
            if scalarbin[i] == "1":
                Q = ecadd(Q, genpoint);
                print("add", Q[0])
        return Q

    print("*******public key generation*******")
    PublicKey = eccmultiply(GPoint, privKey)
    # print ("the private key:  "+privKey)
    # print ("the uncompressed public key: "+PublicKey)
    # print ("the official public key-compressed: "+"02"+str(hex(PublicKey[0])[2:-1]).zfill(64))
    print(PublicKey)

    #label_result.config(text=PublicKey)
    number2.set(PublicKey)
    ran = random.randrange(10 ** 80)
    myhex = "%064x" % ran
    number3.set(myhex)
    number4.set(PublicKey[1])
    number5.set(n1.get())
    #show=str(bin(hashlib.sha3_512(PublicKey[0])))[2:]
    ran = random.randrange(10 ** 80)
    myhex = "%064x" % ran
    number6.set(myhex)
    #ripemd160 = hashlib.new('ripemd160')

    #ripemd160.update(hashlib.sha256(public_key.decode('hex')).digest())

    #middle_man = '\00' + ripemd160.digest()

    #checksum = hashlib.sha256(hashlib.sha256(middle_man).digest()).digest()[:4]
    Struckt = random.randrange(10 ** 80)
    myhex=str(privKey2)+str(privKey1)+str(n1.get)+str(Transactionid)+str(Signature)
    #myhex3=hashlib.sha3_512(myhex)
    myhex = "%064x" % Struckt
    number7.set(myhex)


    return


root = tk.Tk()
root.geometry('600x400+100+200')
root.title('Cryptocurrency Wallet')

number1 = tk.StringVar()
number2 = tk.StringVar()
number3 = tk.StringVar()
number4 = tk.StringVar()
number5 = tk.StringVar()
number6 = tk.StringVar()
number7 = tk.StringVar()

labelTitle = tk.Label(root, text="WALLET").grid(row=0, column=2)
labelNum1 = tk.Label(root, text="Enter Payment").grid(row=1, column=0)
#labelNum2 = tk.Label(root, text="private Key").grid(row=2, column=0)
labelNum2 = tk.Label(root, text="public Key").grid(row=9, column=0)#for public key
labelNumpriv = tk.Label(root, text="private key").grid(row=10, column=0)
Transactionid = tk.Label(root, text="Transactionid").grid(row=11, column=0)#for public key
Hashvalue = tk.Label(root, text="Currency Amount").grid(row=12, column=0)
Signature = tk.Label(root, text="Signature").grid(row=13, column=0)#for public key
Currencyamount = tk.Label(root, text="Hash Value").grid(row=14, column=0)
labelResult = tk.Label(root)
labelResult.grid(row=7, column=2)

entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=9, column=2)
entrynumpriv=tk.Entry(root,textvariable=number3).grid(row=10,column=2)
Trans = tk.Entry(root, textvariable=number4).grid(row=11, column=2)
hasha = tk.Entry(root, textvariable=number5).grid(row=12, column=2)
Signature=tk.Entry(root,textvariable=number6).grid(row=13,column=2)
curr=tk.Entry(root,textvariable=number7).grid(row=14,column=2)

call_result = partial(call_result, labelResult, number1, number2)
buttonCal = tk.Button(root, text="Send", command=call_result).grid(row=3, column=2)
root.mainloop()