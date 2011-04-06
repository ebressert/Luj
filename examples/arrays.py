from time import time
import random, os
import subprocess as sp
import luj
import numpy 

def squared(a):
    command = """
    a = py_obj
    for i=1, 100000 do
        for j, k in ipairs(a) do
            if j % 2 == 0 then
                a[j] = a[j] - 0.01
            end
        end
    end
    out = a
    """
    out = luj.lua(command, python_obj = a, lua_obj = 'out', lua_call = 'luajit')
    return out

def pysquared_arr(a):
    s = a.shape
    a = a.ravel()
    for i in xrange(100000):
        
        for i in xrange(len())
        if i % 2 ==0:
            a = a - 0.01
    return a
    
start = time()
a = numpy.arange(8000).reshape((20,20,20))
b = pysquared(a)
print "Python function execution in %.3f seconds" % (time() - start)

start = time()
a = numpy.arange(8000).reshape((20,20,20))
b = squared(a)
print "Luj with luajit in %.3f seconds" % (time() - start)

