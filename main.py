#AAP10_Angerer
#Changed by Patrick
#FIR-Filter Programm
from time import time
pow = 3023
mod = 12191769932823784859
seed = time()
def random() -> int:
    global seed
    seed = (1 + (seed * pow)) % mod
    return seed
def mac(coeff, values):
    return sum([coeff[i] * values[i] for i in range(len(coeff))])
coeff  = [1/256 for x in range(256)]
values = [0     for x in range(256)]
for i in range(2048):
    values[1:] = values[:-1]
    values[0] = random() % 100
    print(" " * int(mac(coeff, values)), "*", sep='')