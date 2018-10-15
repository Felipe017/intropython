# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 17:04:06 2018

@author: Lenovo
"""
print('EXERCICIO EM AULA')
from math import pi 

def do_twice (f,x,y,z):
    f(x,y,z)
    f(x,y,z)
    
def print_spam (x,y,z):
    print(x,y*4,x,y*4,x) 
    print(z,' '*4,z,' '*4,z)
    print(z,' '*4,z,' '*4,z)
    print(z,' '*4,z,' '*4,z)
    print(z,' '*4,z,' '*4,z)
#do_twice(print_spam, pi)
print('')
def do_four (f,x,y,z):
    do_twice(f,x,y,z)
    print(x,y*4,x,y*4,x)
   
do_four(print_spam,'+','-','|')


