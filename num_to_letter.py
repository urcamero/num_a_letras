""" My Docstring """

# COLLECTIONS

numeros = {'1':'UN','2':'DOS','3':'TRES','4':'CUATRO','5':'CINCO','6':'SEIS','7':'SIETE','8':'OCHO','9':'NUEVE','10':'DIEZ', '11':'ONCE','12':'DOCE','13':'TRECE','14':'CATORCE','15':'QUINCE','16':'DIECISEIS','17':'DIECISIETE','18':'DIECIOCHO','19':'DIECINUEVE','20':'VEINTE','E21':'VEINTI','30':'TREINTA','40':'CUARENTA','50':'CINCUENTA','60':'SESENTA','70':'SETENTA','80':'OCHENTA','90':'NOVENTA','100':'CIENTO', '200':'DOSCIENTOS','300':'TRESCIENTOS','400':'CUATROCIENTOS','500':'QUINIENTOS','600':'SEISCIENTOS','700':'SETECIENTOS', '800':'OCHOCIENTOS','900':'NOVECIENTOS','E100':'CIEN'}

# V A R I A B L E S
n = ""

# L O G I C A L    F U N C T I O N S

def unidad(n):

    if n == "0":
        return 'CERO'
    else:
        return numeros[n]

def decenas(n):

    if n[0] == "1":
        return numeros[n[0:2]]
    elif n[0] == "2" and n[1] != "0":
        return numeros['E21']+numeros[n[-1]]
    else:
        if n[1] == "0":
            return numeros[n[0]+'0']
        else:
            return numeros[n[0]+'0'] + " Y " + numeros[n[-1]]

def cientos(n):

    if n == "000":
        return ""
    elif n[0:2] == "00":
        return numeros[n[-1]]
    elif n[0] == "0":
        if n[1] == "1":
            return numeros[n[1:]]
        elif n[1] == "2" and n[2] != "0":
            return numeros['E21'] + numeros[n[-1]]
        elif n[1] != "1" and n[1] != "2" and n[-1] == "0":
            return numeros[n[1]+'0']
        else:
            return numeros[n[1]+'0'] + " Y " + numeros[n[-1]]
    elif n[1:3] == "00":
        if n[0] == "1":
            return numeros['E100']
        else:
            return numeros[n]
    elif n[1] == "0" and n[2] != "0":
        return numeros[n[0]+'00'] + " " + numeros[n[2]]
    elif n[1] != "0" and n[2] == "0":
        return numeros[n[0]+'00'] + " " + numeros[n[1]+'0']
    else:
        if n[1] == "1":
            return numeros[n[0]+'00'] + " " + numeros[n[1:]]
        elif n[1] == "2":
            return numeros[n[0]+'00'] + " " + numeros['E21'] + numeros[n[-1]]
        else:
            return numeros[n[0]+'00'] + " " + numeros[n[1]+'0'] + " Y " + numeros[n[-1]]

# C O R E   F U N C T I O N

def to_letter(n):

    if len(n) == 1:
        return f"{unidad(n)}"

    elif len(n) == 2:
        return f"{decenas(n)}"

    elif len(n) == 3:
        return f"{cientos(n)}"

    elif len(n) == 4:
        mil = n[0]
        ciento= n[1:]
        return f"{unidad(mil)} MIL {cientos(ciento)}"

    elif len(n) == 5:
        mil = n[0:2]
        ciento= n[2:]
        if n[2:] == "000":
            return f"{decenas(mil)} MIL{cientos(ciento)}"
        else:
            return f"{decenas(mil)} MIL {cientos(ciento)}"

    elif len(n) == 6:
        mil = n[0:3]
        ciento= n[3:]
        if n[3:] == "000":
            return f"{cientos(mil)} MIL{cientos(ciento)}"
        else:
            return f"{cientos(mil)} MIL {cientos(ciento)}"

    elif len(n) == 7:
        millon = n[0]
        mil = n[1:4]
        ciento= n[4:]
        if n[0] == "1":
            if n[1:] == "000000":
                return f"{unidad(millon)} MILLON{cientos(mil)}{cientos(ciento)}"
            elif n[1:4] == "000":
                return f"{unidad(millon)} MILLON {cientos(mil)}{cientos(ciento)}"
            else:
                return f"{unidad(millon)} MILLON {cientos(mil)} MIL {cientos(ciento)}"
        else:
            if n[1:] == "000000":
                return f"{unidad(millon)} MILLONES{cientos(mil)}{cientos(ciento)}"
            elif n[1:4] == "000":
                return f"{unidad(millon)} MILLONES{cientos(mil)}{cientos(ciento)}"
            else:
                return f"{unidad(millon)} MILLONES {cientos(mil)} MIL {cientos(ciento)}"

    elif len(n) == 8:
        millon = n[0:2]
        mil = n[2:5]
        ciento= n[5:]
        if n[1:] == "0000000":
            if n[2:5] == "000":
                return f"{decenas(millon)} MILLONES{cientos(mil)}{cientos(ciento)}"
            else:
                return f"{decenas(millon)} MILLONES {cientos(mil)} MIL {cientos(ciento)}"
        else:
            if n[2:5] == "000":
                return f"{decenas(millon)} MILLONES {cientos(mil)}{cientos(ciento)}"
            else:
                return f"{decenas(millon)} MILLONES {cientos(mil)} MIL {cientos(ciento)}"
