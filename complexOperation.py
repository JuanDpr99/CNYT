import math
from sys import stdin

def suma_i(a,b):
    """Suma dos numeros complejos, a y b de tipo array"""
    c = a[0] + b[0]
    d = a[1] + b[1]
    res = [c,d]
    return res

def resta_i(a,b):
    """Resta dos numeros complejos, a y b de tipo array"""
    c = a[0] - b[0]
    d = a[1] - b[1]
    res = [c,d]
    return res

def product_i(a,b):
    """Producto entre dos números complejos, a y b de tipo array"""
    c = a[0]*b[0] - a[1]*b[1]
    d = b[0]*b[1] + a[1]*b[0]
    res = [c,d]
    return res

def div_i(a,b):
    """Cociente entre dos números complejos, a y b de tipo array"""
    c = a[0]*b[0] + a[1]*b[1]
    d = b[0]*a[1] - a[0]*b[1]
    e = b[0]**2 + b[1]**2
    if(e == 0):
        print("División entre cero es invalida")
    res = [c/e,d/e]
    return res

def module_i(a):
    """Modulo de un numero complejo, a de tipo arreglo """
    x,y = a[0], a[1]
    c = x**2 + y **2     
    return c**0.5

def conjugado(a):
    """conjugado de un numero complejo, a de tipo array"""
    c = a[1] * -1
    return [a[0],c]

def conversionPolar_Cartesiana(num):
    """Convertir un numero complejo de forma polar a cartesiana """
    r = num[0]
    theta = num[1]
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return [x,y]

def mostrar(n):
    """a es la parte real y b es la parte imaginaria
    muestra el numero complejo en forma a + bi ; n de tipo array """
    a = n[0]
    b = n[1]
    if b > 0:       
        print(a,'+',str(b)+'i')
    elif b == 0:
        print(a)
    elif b < 0:
        print(a,'-',str(abs(b))+'i')
##==========================SEGUNDA_PARTE==================================
def sumaVectoresComplejos(a,b):
    """Metodo q suma dos vectores complejos; a y b de tipo array"""
    if(len(a) == len(b)):
        vecRes = []
        for i in range(len(a)):
            res = suma_i(a[i],b[i])
            vecRes.append(res)
        print( vecRes )
            
    else:
        print("Los vectores deben tener la misma longitud")
#sumaVectoresComplejos([[3,2],[4,1]],[[1,3],[2,-5]]);

def inversoAditivo_de_complejo(a):
    """Retorna el inverso aditico de un numero complejo; a= complejo tipo Array"""
    res = [ a[0]*-1,a[1]*-1 ]
    print( res )
#inversoAditivo_de_complejo([3,2])    
        
def real_x_complejo(n,a):
    """Metodo q multiplica un número real por un número complejo; n= Real, a= Complejo tipo Array
        retorna un complejo tipo Array"""    
    c = [n*a[0],n*a[1]]
    return c
#productoEntre_Real_Complejo(3,[3,2])    

def producto_deEscalar_porVectorComplejo(n,a):
    """Metodo que multiplica un escalar por un vector complejo; n= escalar, a= vector complejo"""
    vecRes = []
    for i in range(len(a)):
        vecRes.append(real_x_complejo(n,a[i]))
    print(vecRes)
#producto_deEscalar_porVectorComplejo(3,[[3,2],[4,1]])

def sumaMatricesComplejas(matrizA,matrizB):
    """metodo q retorna la suma entre dos matrices"""
    matRes = []
    for i in range( len(matrizA) ):
        fila = []
        for j in range( len(matrizA[i]) ):            
            c = suma_i(matrizA[i][j], matrizB[i][j])
            fila.append(c)
        matRes.append( fila )
    print(matRes)
##sumaMatricesComplejas([ [[3,2],[4,1]],[[1,3],[2,5]] ], [ [[3,2],[4,1]],[[1,3],[2,5]] ])
    
   













            

