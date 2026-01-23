import math

def sjekk_tom(inp):
    try:
        return float(inp)
    except ValueError:
        print('Input er tom eller ugyldig')
        return None


a = sjekk_tom(input('Skriv inn A: '))
b = sjekk_tom(input('Skriv inn B: '))
c = sjekk_tom(input('Skriv inn C: '))

    

def ABC_kalk(a,b,c):
    if a is None or b is None or c is None:
        print('Kan ikke regne med ugyldige verdier')
        return None
    if a == 0:
        print('A kan ikke være 0')
        return None
    
    diskriminant = b**2-4*a*c
    if diskriminant<0:
        print('Diskriminant er mindre enn 0, dermed ingen løsninger')
        return None
    rot = math.sqrt(b**2-4*a*c)
    x1 = (-b+rot)/(2*a)
    x2 = (-b-rot)/(2*a)
    if x1==x2:
        print('A :',a,'B :',b,'C :',c,'\n\nSvar:',x1)
        return x1
    else:
        print('A :',a,'B :',b,'C :',c,'\n\nsvar x1:',x1,'\nsvar x2',x2)
        return x1,x2

ABC_kalk(a,b,c)