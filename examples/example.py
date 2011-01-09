import luj

command = """function fib_sequence(nth)
    x = {0,1}
    xx = {0,1}
    if nth == 1 then print(1) end
    
    for i = 1, nth do
        table.insert(x, x[2] + x[1])
        x = {x[2], x[3]}
        table.insert(xx,x[2])
        -- print(x[2])
    end
    return x[2]
    -- return xx
end

res = fib_sequence(py_obj)"""

py_obj = 1000
res = luj.lua(command, python_obj = py_obj, lua_obj = 'res', lua_call='luajit-2.0.0-beta5')

print res