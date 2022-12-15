import urllib.request
import scipy as sc, numpy as np, re, matplotlib.pyplot as plt


def h(n,x):
    return sc.special.spherical_jn(n, x) + 1j * sc.special.spherical_yn(n, x)


def a(n,x):
    return sc.special.spherical_jn(n, x)/h(n, k*r)


def b(n,x):
    return (x * sc.special.spherical_jn(n-1, x) - n * sc.special.spherical_jn(n, x)) / (x * h(n - 1, x) - n * h(n, x))


def sigma(povtor, x):
    sigm = 0
    for n in range(1,povtor):
        sigm = sigm + np.power(-1,n)*(n+0.5)*(b(n,x)-a(n,x))
        print('n= ',n)
    return sigm

url = 'https://jenyay.net/uploads/Student/Modelling/task_02.xml'
urllib.request.urlretrieve(url, 'datresh.xml')
with open('datresh.xml', 'r') as file:
    book = file.readlines()
var = int(input('Введите ваш вариант: '))
var +=1
shkala = int(input('Введите приближение(число шагов): '))
print(book[var])
print(re.findall('\d+[.]*\d*e*[-]*\d*', book[var]))
book1 = re.findall('\d+[.]*\d*e*[-]*\d*', book[var])
D = float(book1[1])
print('D= ',D)
fmin = float(book1[2])
print('fmin= ',fmin)
fmax = float(book1[3])
print('fmax= ',fmax)
r = D/2
print('r= ',r)
f = np.linspace(fmin,fmax,shkala)
print('f= ',f)
lamda = 3*10**8/f
print('lamda= ',lamda)
k = 2*np.pi/lamda
print('k= ',k)
result = lamda**2/np.pi*abs(sigma(70,k*r))**2
print('sigma = ',result)
plt.plot(2*np.pi*r/lamda,result/(np.pi*r**2))
plt.show()
plt.plot(f,result)
plt.show()

# creating json file
'import json as js'

with open('result.json', 'w', encoding='utf8') as file:
    file.write('{\n')
    for i in range(shkala):
        slova = {"freq": f[i], "lambda": lamda[i], "rcs": result[i]}
        if i+1!=shkala:
            file.write('        {},\n'.format(slova))
        if i+1==shkala:
            file.write('        {}\n'.format(slova))
    file.write('    ]\n}')