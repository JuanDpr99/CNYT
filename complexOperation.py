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


