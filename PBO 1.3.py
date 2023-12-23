awal=int(input('Masukkan angka awal: '))
akhir=int(input('Masukkan angka akhir: '))
x=[]
y=[]
for i in range(awal, akhir+1):
    if i%2==0:
        x.append(i)
    if i%2==1:
        y.append(i)
print('Angka genapnya adalah', x)
print('Angka ganjilnya adalah',y)