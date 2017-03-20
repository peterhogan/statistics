from time import sleep

s = 19
p = 6247
q = 8839

M = p*q

x = [s]
while True:
    xn = x[-1]**2 % M
    x.append(xn)
    print(x[-10:-1])
    sleep(0.5)

