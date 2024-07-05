def lb_a_kg(libras):
    kilogramos = libras * 0.4536
    return kilogramos

def kg_a_lb(kilogramos):
    libras = kilogramos / 0.4536
    return libras

def ftin_a_m(feets, inches):
    meters = feets * 0.3048 + inches * 0.0254
    return meters

def m_to_ft(meters):
    feets = meters / 0.3048
    in_to_m = meters % 0.3048 
    inches = in_to_m / 0.0254
    return feets, inches

def imc(peso, altura):
    return peso / altura ** 2

print(ftin_a_m(m_to_ft(1.86)))
print("{:.2f}".format(imc(peso = kg_a_lb(80), altura= m_to_ft(1.86))))