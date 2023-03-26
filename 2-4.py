a=b=c= 10, 10, 10
print(f'{a} {b} {c} ')
print(f'{id(a)} {id(b)} {id(c)}')

a = 20

print(f'{a} {b} {c} ')
print(f'{id(a)} {id(b)} {id(c)}')

a=b=c = [1,2,3]


a.append(4)

print(f'{a} {b} {c} ')
print(f'{id(a)} {id(b)} {id(c)}')

x = 10
y = 10

print(id(x),id(y))

y+=1
y-=1

print(id(x),id(y))

y = y + 1234567890 - 1234567890

print(id(x),id(y))