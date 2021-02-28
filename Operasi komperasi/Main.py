# Operasi Konparasi

# Setiap hasil dari konparasi(perbandingan) adalah bolean
# ex: >,<,>=,<=,==,!=,is,is not

a = 4
b = 3

# lebih besar dari >
print('==== lebih besar dari (>)')
hasil = a > b 
print(a,'>',b,'=',hasil)
hasil = b > a 
print(b,'>',a,'=',hasil)

# kurang dari <
print('==== lebih kurang dari (<)')
hasil = a < b 
print(a,'<',b,'=',hasil)
hasil = b < a 
print(b,'<',a,'=',hasil)

# lebih besar dari sama dengan >=
print('==== lebih dari sama dengan (>=)')
hasil = a >= b 
print(a,'>=',b,'=',hasil)
hasil = b >= a 
print(b,'>=',a,'=',hasil)

# kurang dari sama dengan <=
print('==== kurang dari sama dengan (<=)')
hasil = a <= b 
print(a,'<=',b,'=',hasil)
hasil = b <= a 
print(b,'<=',a,'=',hasil)

# sama dengan ==
print('====  sama dengan (==)')
hasil = a == a
print(a,'==',a,'=',hasil)
hasil = b == a 
print(b,'==',a,'=',hasil)

# tidak  sama dengan !=
print('==== tidak sama dengan (!=)')
hasil = a != a
print(a,'!=',a,'=',hasil)
hasil = a != b 
print(a,'!=',b,'=',hasil)

# 'is' sebagai komperasi object identity 
print('==== object identity (is)')
x = 5 # ini adalah assignment membuat object
y = 5 
print('nilai x -',x,',id = ',hex(id(x)))
print('nilai y -',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y = ',hasil)

x = 5 # ini adalah assignment membuat object
y = 6 
print('nilai x -',x,',id = ',hex(id(x)))
print('nilai y -',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y = ',hasil)

# 'is not' sebagai komperasi object identity 
print('==== object identity (is not)')
x = 5 # ini adalah assignment membuat object
y = 5 
print('nilai x -',x,',id = ',hex(id(x)))
print('nilai y -',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is not y = ',hasil)

x = 5 # ini adalah assignment membuat object
y = 6 
print('nilai x -',x,',id = ',hex(id(x)))
print('nilai y -',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is not y = ',hasil)
