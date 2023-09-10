import random
import math

matrix = [[2,1,8],[3, 'B', 7],[6,5,4]]
posx, posy = 1,1

def neighbour_function(l):
    return random.randint(0, l-1)

def cooling(t):
    return t*0.9999

def probability( fc, fn, T):
    return math.exp((fc-fn)/T)