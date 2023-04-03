import sys
import os
op = os.environ.get("OPERATOR",'+')
a= os.environ.get("ADDENDO1",1)
b= os.environ.get("ADDENDO2",1)
if op==str('+'):
    risultato = int(a) + int(b)
elif op==str('-'):
    risultato = int(a) - int(b)
elif op==str('x'):
    risultato = int(a) * int(b)
elif op==str('/'):
    risultato= float(a)/float(b)
else:
    risultato='niente di sensato'
print("Hai chiesto "+str(a)+str(op)+str(b))
print ("risultato: "+ str(risultato))