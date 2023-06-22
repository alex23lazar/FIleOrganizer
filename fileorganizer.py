print("Hello World!")
print("Salut!")
print(2)

a = 45.82
nume = "Codex"
f = 45.82
com = 3.14j
adevarat = True

print (a)
print (nume)
print (f)
print (com)
print(adevarat)

print (type(a))
print (type(nume))
print (type(f))
print (type(com))
print (type(adevarat))

suma = a / f

print(suma)

if a > f:
    print ("#1 Variabila a este mai mare decat f")
elif a < f:
    print ("#2 a < f")
    sumb = a - f
    print("Valoarea lui sumb este:", sumb)
elif a == f:
    print ("#3 Cele 2 variabile sunt egale")
else:
    print("Nu este adevarat")
    
b = 102
c = -86

#Comparare
if b > c:
    print ("#1 Variabila b este mai mare decat c")
elif b < c:
    print ("#2 b < c")
    sumd = b - c
    print("Valoarea lui sumb este:", sumd)
elif b == c:
    print ("#3 Cele 2 variabile sunt egale")
else:
    print("Nu este adevarat")
   
#Functia noastra  
def comparare(nrA, nrB):
    print ("####RULEZ FUNCTIA####")
    if nrA > nrB:
        print ("#1 Variabila b este mai mare decat c")
    elif nrA < nrB:
        print ("#2 nrA < nrB")
        sumd = nrA + nrB
        print("Valoarea lui sumb este:", sumd)
    elif nrA == nrB:
        print ("#3 Cele 2 variabile sunt egale")
    else:
        print("Nu este adevarat")
        
comparare(20,21)
comparare(10, 10)
comparare(41.51, -32.12)

def inmultire(nrA, nrB):
    rez = nrA * nrB
    return rez
var = inmultire(53, 21)

print(var)

def impartire():
    rez = 25 / 41
    return rez

imp = impartire()

print(imp)

sumfor = 0


for x in range(1, 101):
    sumfor = sumfor + x
    
print("Suma numerelor este:", sumfor)

rezFor = 0

for i in range (1, 50):
    rezFor = inmultire(i, i + 1) 
    print(rezFor)
   
nrVocale = 0 
textAnaliza = "Masina are mai multe roti"

for cuv in textAnaliza:
    if cuv == "a":
        print("Am gasit vocala", cuv)
        nrVocale += 1
    elif cuv == "i":
        print("Am gasit vocala", cuv)
        nrVocale += 1
    elif cuv == "o":
        print("Am gasit vocala", cuv)
        nrVocale += 1
    elif cuv == "u":
        print("Am gasit vocala", cuv)
        nrVocale += 1
    else:
        print("Litera nu este o vocala", cuv)
        
print ("Numarul total de vocale", nrVocale)
    