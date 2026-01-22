import math

a = float(input("Skriv inn A: "))
b = float(input("Skriv inn B: "))
c = float(input("Skriv inn C: "))

def ABC_kalk(a,b,c):
    diskriminant = b**2-4*a*c
    error_code = ""
    if diskriminant<0:
        error_code = "Diskriminant er mindre enn 0, dermed ingen løsninger"
        print(error_code)
        return None
    rot = math.sqrt(b**2-4*a*c)
    x1 = (-b+rot)/(2*a)
    x2 = (-b-rot)/(2*a)
    print(x1,x2)
    return x1,x2

ABC_kalk(a,b,c)