import luj

command = """
res ={}
for key, item in pairs(py_obj) do
    --print(item)
    res[key] = item^20
end
"""

z = range(1000)
res = luj.lua(command, python_obj = z, lua_obj = 'res', lua='luajit-2.0.0-beta5')

print res