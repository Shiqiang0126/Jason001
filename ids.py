p =['name', ['saving', 100.0]]
print ('''p =['name', ['saving', 100.0]''')
p0 = p
p1 = p[:]
p2 = list(p)
print("id of p,p0,p1,p2:",id(p),id(p0),id(p1),id(p2))
print("id[x] of p,p0,p1,p2:",[id(x) for x in p],[id(x) for x in p0],[id(x) for x in p1],[id(x) for x in p2])
p0[0] = "name0"
print("after p0[0] = 'name0'")
print("id[x] of p,p0,p1,p2:",[id(x) for x in p],[id(x) for x in p0],[id(x) for x in p1],[id(x) for x in p2])
p1[0] = "name1"
print('after p1[0] = "name1"')
print("id[x] of p,p0,p1,p2:",[id(x) for x in p],[id(x) for x in p0],[id(x) for x in p1],[id(x) for x in p2])
p1[1][1] = 200.0
print('after p1[1][1] = 200.0')
print("id[x] of p,p0,p1,p2:",[id(x) for x in p],[id(x) for x in p0],[id(x) for x in p1],[id(x) for x in p2])
p[1][1] = 500.0
print('after p[1][1] = 500.0')
print("id[x] of p,p0,p1,p2:",[id(x) for x in p],[id(x) for x in p0],[id(x) for x in p1],[id(x) for x in p2])
print(p,p0,p1,p2)
p2[1][0] = "saving 2"
print('after p2[1][0] = "saving 2')
print("id[x] of p,p0,p1,p2:",[id(x) for x in p],[id(x) for x in p0],[id(x) for x in p1],[id(x) for x in p2])
print(p,p0,p1,p2)
