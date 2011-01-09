function find_pi(n)
    c = 0
    for i = 0,n do
        x = 2 * math.random() - 1
        y = 2 * math.random() - 1
        d = x*x + y*y
        if d < 1 then
            c = c + 1
        end
    end
    return 4 * c / n
end

n = 20000000
print('pi =', find_pi(n))