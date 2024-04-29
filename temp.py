def dot_product(u,v):
    equal_length= len(u) == len(v)
    if equal_length:
        sum=0
        for i in range(len(u)):
            s = u[i] * v[i]
            sum += s
        return sum
    else:
        return print("The dot product is not defined with vector of non equal sizes")

def proj(v,u):
    s = dot_product(v,u)/dot_product(u,u)
    print(s)
    for i in range(len(u)):
        u[i] *= s
    return u

if __name__ == '__main__':
    u = [1, 2, 0, 3]
    v = [4, 0, 5, 8]
    print(proj(v, u))
