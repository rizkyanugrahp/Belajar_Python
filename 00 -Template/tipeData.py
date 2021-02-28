## tipe data

# tipe data: angka satuan/tidak berkoma(integer)
data_integer = 10
print("data :", data_integer)
print("- bertipe : ", type(data_integer))
# disini diketahui bahwa di python tipe data integer akan 
# otomatis atau tidak perlu di deklarasikan.

#tipe data: angka dengan koma (float)
data_float = 1.5
print("data :", data_float)
print("- bertipe : ", type(data_float))
# sama seperti integer float juga otomatis 

# tipe data: kumpulan karakter (string)
data_string = "Rizky Anugrah Pratama"
print("data :", data_string)
print("- bertipe : ", type(data_string))

# tipe data: biner true/false (boolean)
data_bool = True
print("data :", data_bool)
print("- bertipe : ", type(data_bool))

## tipe data khusus+

# bilangan kompleks 
data_complex = complex(5,6)
print("data :", data_complex)
print("- bertipe : ", type(data_complex))

# tipe data bahasa C

from ctypes import c_double, c_char

data_c_double = c_double(10.5)
print("data :", data_c_double)
print("- bertipe : ", type(data_c_double))

