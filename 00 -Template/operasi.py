#operasi aritmatika

a = 10  
b = 3

# operasi pertamabahan +
hasil = a + b
print(a,'+',b,'=',hasil)

# operasi pengurangan - 
hasil = a - b
print(a,'-',b,'=',hasil)

# operasi perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)

# operasi pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)

# operasi perpangkatan (eksponen)**
hasil = a ** b
print(a,'**',b,'=',hasil)

# operasi sisa bagi (modulus) %
hasil = a % b
print(a,'%',b,'=',hasil)

# operasi floor division //
hasil = a // b
print(a,'//',b,'=',hasil)

# prioritas operasi, operational precendence
'''
    1. ()
    2. exsponen **
    3. perkalian dan teman-temanya * / ** % //
    4. pertamabahan dan pengurangan + -
'''
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // y
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',y,'=',hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)
# kurung akan mengabil langkah pertama
hasil = (x + y) * z
print('(',x,'+',y,')*',z,'=',hasil)