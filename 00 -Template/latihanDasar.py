# Latihan Satuan Sederhana
# latihan konversi satuan temperatur

# program konversi celcius ke satuan lain

print("\n Program Konversi Temperatur\n")

# CELCIUS
celcius = float(input('Masukan Suhu Dalam Celcius : '))
print("Suhu Adalah",celcius,"Celcius")

# REAMUR
reamur = (4/5) * celcius
print("Suhu Dalam Reamur  Adalah ",reamur,"Reamur")

# FAHRENHEIT
fahrenheit = ((9/5) * celcius) + 32
print("Suhu Dalam Fahrenheit Adalah ",fahrenheit,"Fahrenheit")

# KELVIN
kelvin = celcius + 273
print("Suhu Dalam Kelvin Adalah ",kelvin,"Kelvin")

#Farenhet ke kelvin
suhu_F = eval(input('Masukan suhu dalam Fahrenheit:'))
f = ( suhu_F - 32) * 5/9 + 273.15
print('Suhu adalah:', f, 'K')
#Kelvin ke farenheit
suhu_K = eval(input('Masukan suhu dalam Kelvin:')) 
k = (suhu_K - 273.15) * 9/5 + 32
print('Suhu adalah:', k, 'F')