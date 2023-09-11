#! /usr/bin/env.python3

def average(data):
    '''
    Esta función puede recibir una lista de datos
    '''
    n = len(data)
    
    i = 0
    aux = 0

    while i < n :
        aux = aux + data[i]
        i += 1
    return aux / n


def factorial(n):
    '''
    La función factorial puede calcular el producto de todos los numeros anterior de un numero natural, donde por definición 0!= 1
    '''
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def standar_desv(a,b =-1): 
    '''
    La desviación esrándar puede calcular
    y devolver la cantidad de  la dispersión estadística si el centro de los datos se mide en torno a la media 
    o a un valor dado

    '''
    n = len(a) 
    
    sums = []  
    
    i = 0    

    if type(a) != list:
        raise TypeError('Debes ingresar una lista') 
    if  n <= 1:
        raise ValueError('Para calcular el valor de la desviación es necesario tener mas de un elemento ') 
    if b > n:
        raise ValueError('El elemnto que buscas esta fuera de la lista')
    
    if b == -1: #este caso e define como el valor predeterminado
        
        while i < n:    
            sqr_dif = (a[i] - average(a))**2 
            sums.append(sqr_dif)
            i += 1 
    else :
        while i < n:    
            sqr_dif = (a[i] - a[b])**2
            sums.append(sqr_dif)
            i += 1 
    square_sum = sum(sums)
    vr = ( (1/(n-1))* square_sum  )**(1/2)
    
    return vr

def analyze_egg_signal(señal_egg):
    '''
    This function can analyze with average and standar desvitation some list about cerebla action pontential
    '''
    media_señal = average(señal_egg) 
    desv_señal = standar_desv(señal_egg) 
    
    
    print('Media de la señal EEG:', media_señal)
    print('Desviación estándar de la señal EEG :', desv_señal)
    return media_señal, desv_señal

def sin(x,n = 64):
    '''
    Esta función calcula el seno con un n veces de interaciones en la serie de Taylor
    '''
    if type(x) != float or type(n)!= int :
        raise ValueError("Debes introducir un numero real")
    if n < 0:
        raise ValueError("Debe introcur un numero mayor que 0")
    i = 0
    suma = 0
    while i < n:
       
        suma  = suma + ((-1)**i)*(x**(2*i+1))/ (factorial(2*i+1))
        i = i +1
    return suma

def cos(x,n = 64):
    '''
    Esta función calcula el coseno con un n veces de interaciones en la serie de Taylor
    '''
    if type(x) != float or type(n)!= int :
        raise ValueError("Debes introducir un numero real")
    if n < 0:
        raise ValueError("Debe introcur un numero mayor que 0")
    i = 0
    suma = 0
    while i < n:
       
        suma  = suma + ((-1)**i)*(x**(2*i))/ (factorial(2*i))
        i = i +1
    return suma
def tan(x,n=64):
    '''
    Esta función permite aproximar el valor de la tangente en un punto
    
    '''
    if -0.009 < cos(x,n) < 0.00009:
        raise ValueError('No existe la división entre zero')
    return sin(x,n) / cos(x,n)

def error (arg1,arg2):
    '''
    Esta función genera el valor del error abosulto de 2 valores
    '''
    err = abs( (arg1 - arg2/arg1)) * 100
    return err
def horner(p1,p2):
    '''
    Esta función recupera ta ta ta ta

    '''
    return 2 +2 
