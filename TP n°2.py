# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:09:54 2021

@author: Toniocstl
"""
import tp2annexe as a
def point_fixe(g,x0,epsilon,Nitermax):
    n=0
    xold = x0
    erreur = g(xold) - xold
    while abs(erreur)> epsilon and n<Nitermax:
        xnew = g(xold)
        erreur = xnew - xold
        xold = xnew
        print(n)
        n+=1
    return xnew 

print('xnew=',point_fixe(a.g12,1, 1e-10,5e4))
