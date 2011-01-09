dict_funcs = {}

# Adopted from http://lua-users.org/wiki/SplitJoin
dict_funcs['string_split'] = """
function split(str, pat)
   local t = {}
   local fpat = "(.-)" .. pat
   local last_end = 1
   local s, e, cap = str:find(fpat, 1)
   while s do
      if s ~= 1 or cap ~= "" then
          table.insert(t,cap)
      end
      last_end = e+1
      s, e, cap = str:find(fpat, last_end)
   end
   if last_end <= #str then
      cap = str:sub(last_end)
      table.insert(t, cap)
   end
   return t
end

"""

dict_funcs['numpy_parse'] ="""
function numpy_parser(data)
    tmp1 = split(data,string.char(10))
    tmp2 = {}
    tbl = {}
    for key1, item1 in pairs(tmp1) do
        tmp2 = split(item1,',')
        tbl[key1] = {}
        for key2, item2 in pairs(tmp2) do
            tbl[key1][key2] = item2
        end
    end
    return tbl
end

"""

dict_funcs['string_join'] = """
function join(tbl)
    return table.concat(tbl, string.char(10))
end

"""

# dict_funcs['out_type'] = """
# 
# 
# 
# """

def grab_func(name):
    return dict_funcs[name]
