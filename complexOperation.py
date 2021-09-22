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

def generateEmptyMatrix(n,m):
    '''Genera una matriz de tamaño nxm con numeros complejos de ceros'''
    colum = []
    for i in range(n):
        fil = []
        for j in range(m):
            fil.append([0,0])
        colum.append(fil)
    return (colum)
#generateEmptyMatrix(3,3)

def generaridentidad(n):
    """Genera una matriz identidad(compuesta de numeros complejos) de tamaño n"""
    ma = []
    for i in range(n):
        l = []
        for j in range(n):
            if i == j:
                l.append([1,0])
            else:
                l.append([0,0])
        ma.append(l)
    return ma
        
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

def inversoAditivo(a):
    """Retorna el inverso aditico de un numero complejo; a= complejo tipo Array"""
    res = [ a[0]*-1,a[1]*-1 ]
    return( res )
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
    return(matRes)
#sumaMatricesComplejas([ [[3,2],[4,1]],[[1,3],[2,5]] ], [ [[3,2],[4,1]],[[1,3],[2,5]] ])

def restaMatriz(matriz1,matriz2):
    """Recibe dos matrices o vectores y los resta, estos deben tener
    el mismo tamaño m x n y deben contener arreglos"""
    res = generateEmptyMatrix(len(matriz1),len(matriz1[0]))
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            res[i][j] = resta_i(matriz1[i][j],matriz2[i][j])
    return res

def inversoAditivoMatriz(matriz):
    """Recibe una matriz o un vector y halla el inverso aditiva de este(a)"""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = inversoAditivo(matriz[i][j])
    return ( matriz)
##inversoAditivoMatriz([[[3,4],[1,2]],[[3,6],[7,6]]])

def escalarXmatrizCompl(e,matriz):
    '''Retorna una matriz multiplicada por un escalar; e= int; matriz= array[array]'''
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = real_x_complejo(e,matriz[i][j])
    return(matriz)
#escalarXmatrizCompl(2,[[[3,4],[1,2]],[[3,6],[7,6]]])

def transpuestaMatriz(matriz):
    '''Retorna la transpuesta de una matriz ingresada'''
    ret = generateEmptyMatrix(len(matriz),len(matriz[0]))
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            ret[i][j] = matriz[j][i]
    return (ret)
#transpuestaMatriz([[[3,4],[1,2]],[[3,6],[7,6]]])

def conjugadaMatriz(matriz):
    '''Retorna la matriz conjugada de una ingresada'''
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = conjugado(matriz[i][j])

    return (matriz)
#conjugadaMatriz([[[3,-4],[1,2]],[[3,6],[-7,-6]],[[8,-9],[9,2]]])


def adjuntaMatriz(matriz):
    '''Halla la adjunta de una matriz calculando la conjugada y luego la transpuesta'''
    ret = transpuestaMatriz(conjugadaMatriz(matriz))
    return ( ret )
#adjuntaMatriz([[[3,4],[1,2]],[[3,6],[7,6]]])


def multiplicarMatrices(matrizA,matrizB):
    if len(matrizA[0]) == len(matrizB):
        ret = generateEmptyMatrix(len(matrizA), len(matrizB[0]))
        for i in range(len(ret)):
            for j in range(len(ret[0])):
                ret[i][j] = [0,0]
                for k in range(len(matriz2)):
                    ret[i][j] = suma_i(ret[i][j], producto_i(matrizA[i][k],matrizB[k][j]))
        if len(ret) == 1:
            return ret[i][j]
        return ret
    else:
        return 0

def productinterno(vector1,vector2):
    """Halla el producto interno de dos vectores compuesto de complejos"""
    daga = adjuntaMatriz(vector1)
    res = multiplicarMatrices(daga,vector2)
    if res[1] == 0:
        return res[0]
    return res

def normavector(vector1):
    """Halla la norma de un vector compuesto de complejos"""
    ret = productinterno(vector1,vector1)
    ret = ret ** 0.5
    return ret

def distanciavectores(vector1,vector2):
    """Halla la distancia entre dos vectores compuesto de complejos"""
    resta = restaMatriz(vector1,vector2)
    res = normavector(resta)
    return res

def truncar(matriz):
    """Trunca los valores reales en la matriz, sean de la parte real o de la
    parte imaginaria"""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            for k in range(2):
                matriz[i][j][k] = math.ceil(matriz[i][j][k])
    return matriz

def matrizUnitaria(matriz):
    """Comprueba si una matriz es unitaria"""
    daga = adjuntaMatriz(matriz)
    res = multiplicarMatrices(matriz,daga)
    res = truncar(res)
    identidad = generaridentidad(len(matriz))
    if res == identidad:
        return True
    return False

def matrizhermitiana(matriz):
    """Comprueba si una matriz es hermitiana"""    
    if adjuntaMatriz(matriz) == matriz:
        return True
    return False

def productotensor(matriz1,matriz2):
    """Halla el producto tensor de dos matrices compuestas de complejos"""
    res = generateEmptyMatrix(len(matriz1)*len(matriz2),len(matriz1[0])*len(matriz2[0]))
    m = len(matriz2)
    n = len(matriz2[0])
    for i in range(len(res)):
        for j in range(len(res[0])):
            res[i][j] = producto_i(matriz1[i//m][j//n],matriz2[i%m][j%n])
    return res








            

