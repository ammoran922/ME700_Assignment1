import sys
sys.path.append('../src')
import newtons_method as nm
import numpy as np
import pytest

def test1():
    f = lambda x: x**2 - 2  
    df = lambda x: 2*x     
    root = nm.newton_method(f, df, x0=1.0)
    print(f"test 1 root: {root}")

def test2():
    f = lambda x: 3*x**2 - 6  
    df = lambda x: 6*x     
    root = nm.newton_method(f, df, x0=1.0)
    print(f"test 2 root: {root}")

def test3():
    f = lambda x: 5*x**3 - 1  
    df = lambda x: 15*x**2     
    root = nm.newton_method(f, df, x0=1.0)
    print(f"test 3 root: {root}")

# Mechanics Problem
def test4():
    f = lambda x: 5/(2*np.pi)*np.sqrt(1/x)-1
    df = lambda x: -5 / (4*np.pi*np.power(x,3/2))     
    root = nm.newton_method(f, df, x0=1.0)
    print(f"(Oscillation Mechanics Problem) test 4 root: {root}")

# Mechanics Problem
def test5():
    f = lambda x: x**3 - 0.165*x**2 + 3.993e-4 
    df = lambda x: 3*x**2 - 0.33*x    
    root = nm.newton_method(f, df, x0=1.0)
    print(f"(Buoyant Ball Mechanics Problem) test 5 root: {root}")

def run_tests():
    test1()
    test2()
    test3()
    test4()
    test5()

run_tests()
