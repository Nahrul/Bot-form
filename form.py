import sys
import time
import os
import datetime
from itertools import permutations
import webbrowser




print("Hallo selamat datang di program saya")

nama_entry = "&entry.1246283301="
tahun = "&entry.1504050475_year="
bulan = "&entry.1504050475_month="
tanggal = "&entry.1504050475_day="
zona = "&entry.1624782304=WIB"
jam_masuk = "&entry.1700089040_hour="
menit_masuk = "&entry.1700089040_minute="
shift_entry = "&entry.477209646="
jam_keluar = "&entry.673082708_hour="
menit_keluar = "&entry.673082708_minute="
cabang = "&entry.996150919=CIREBON"

kva_pln = "&entry.1982930308=250"
kva_pln_catatan = "&entry.1050631306"
status_pln = "&entry.187354536=Normal"
unit_trafo = "&entry.126579681=3+Unit"
trafo1 = "&entry.393804010=250"
trafo2 = "&entry.1390830960=66"
trafo3 = "&entry.1703077705=60"
status_trafo1= "&entry.1955105236=OK"
status_trafo2 = "&entry.1260958791=OK"
status_trafo3 = "&entry.1778973206=OK"

jumlah_genset = "&entry.1012263950=3+Unit"
genset1 = "&entry.644464405=175"
genset2 = "&entry.261934755=60"
genset3 = "&entry.491270146=60"
status_genset1 = "&entry.371318830=Stand+by+Auto"
status_genset2 = "&entry.262897399=Stand+by+Auto"
status_genset3 = "&entry.299357963=Stand+by+Auto"

jenis_panel = "&entry.1734933449=LMVDP"
beban_r = "&entry.1623101554="
beban_s = "&entry.1236883645="
beban_t = "&entry.461319217="
beban_n = "&entry.378859242="

fire_alarm = "&entry.1408683710=Aktif"

pompa_jokie = "&entry.307490925=Stand+by+Auto"
pompa_dorong = "&entry.1960544484=Stand+by+Auto"
pompa_sumur = "&entry.1574900219=ON"

area_cctv = "&entry.204335889=OFFICE,DC,TC"
jumlah_on = "&entry.518888431="
jumlah_off = "&entry.57560343="

jumlah_coldroom = "&entry.1612360139=3"
suhu_coldroom1 = "&entry.598921574="
preasure_coldroom1 = "&entry.450528536="
suhu_coldroom2 = "&entry.1808231313="
preasure_coldroom2 = "&entry.1146489042="
suhu_coldroom3 = "&entry.628255825="
preasure_coldroom3 = "&entry.1215854966="
status_coldroom1 = "&entry.1498269812="
status_coldroom2 = "&entry.1531822471="
status_coldroom3 = "&entry.1892158262="

total_kwh = "&entry.1822776012="
area_kwh = "&entry.917804643=OFFICE"

area_air = "&entry.448978164=OFFICE,DC"
total_air = "&entry.681409772="

pemeliharaan = "&entry.2018189608="
perbaikan = "&entry.55438860="
permintaan = "&entry.132101497="
kejadian = "&entry.1688875228="
catatan = '&entry.1850401002=Operasional+Normal'



#fuction koreksi angka
def int_input(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError as e:
            print("Yang anda masukan Bukan angka!")
            
#funtion perubah int jadi str
def string(var):
    string = str(var)
    return string
            
            

nama_pelapor = int_input('\n1.Nahrul        2.risal\n3.suarno        4.noval\n5.syauqi        6.tain\n7.fauzi\n\n\nsiapakah kamu?  ')

if nama_pelapor == 1:
    nama = ('Nahrul Hayat')

elif nama_pelapor == 2:
    nama = ('Muhammad Risal')

elif nama_pelapor == 3:
    nama = ('Suarno')

elif nama_pelapor == 4:
    nama = ('Naufal Pradana')
    
elif nama_pelapor == 5:
    nama = ('Syauqi')
    
elif nama_pelapor == 6:
    nama = ('Muhammad Mustain')
    
elif nama_pelapor == 7:
    nama = ('Fauzi Anhari')
    
else:
    print('Yang anda inputkan bukan Angka/tidak ada dalam daftar')
    exit

time.sleep(1)
os.system('clear')

print('============================================================\n\n                     BMT FAST FAST HAND                \n\n============================================================')


print('Bismillahirrohmannirrohim\n')
print('Selamat Datang, ' + nama + ' \n\nOke berhubung dengan keluarnya aturan baru untuk laporan, dan menggunakan google forms yang sangat membuat saya ribet jadi mending bikin bot nya aja ygy')
print('\nLangsung aja Cekidot... :)')

time.sleep(2)
os.system('clear')


print('============================================================\n\n                     BMT FAST FAST HAND                \n\n============================================================')




v = int(input('\n\nberapa orang yg masuk? '))

print('\n1.Nahrul        2.risal\n3.suarno        4.noval\n5.syauqi        6.tain\n7.fauzi')



karyawan = permutations(['Nahrul+Hayat', 'Muhammad+Risal', 'Suarno', 'Naufal+Pradana', 'Syauqi', 'Muhammad+Mustain', 'Fauzi+Anhari'],v)

petugas = input('\nTulis aja nomernya misal(123)\nSiapa aja nih petugas nya? ')
  
g = permutations([1,2,3,4,5,6,7],v)
for i in karyawan:
     e = ''
     x=''
     breaker=False
     for y in i:
         x+=y
         x+=',+'
     for j in g:
         for d in j:
             e+=str(d)
         if e == petugas:
             breaker = True
         break
     if breaker:
         break
        
nama_entry+=x
print(nama_entry)

shift = int_input('\nSekarang sift berapa? ')

now = datetime.datetime.now()

if shift == 1:
    shift_entry = shift_entry+'Shift+1'
    tahun = tahun+str(now.year)
    bulan = bulan+str(now.month)
    tanggal = tanggal+str(now.day)
    jam_masuk = jam_masuk+'07'
    menit_masuk = menit_masuk+'00'
    jam_keluar = jam_keluar+'15'
    menit_keluar = menit_keluar+'00'
    
elif shift == 2:
    shift_entry = shift_entry+'Shift+2'
    tahun = tahun+str(now.year)
    bulan = bulan+str(now.month)
    tanggal = tanggal+str(now.day)
    jam_masuk = jam_masuk+'15'
    menit_masuk = menit_masuk+'00'
    jam_keluar = jam_keluar+'23'
    menit_keluar = menit_keluar+'00'
    
elif shift == 3:
    shift_entry = shift_entry+'Shift+3'
    tahun = tahun+str(now.year)
    bulan = bulan+str(now.month)
    tanggal_shift3 = now.day-1
    tanggal = tanggal+str(tanggal_shift3)
    jam_masuk = jam_masuk+'07'
    menit_masuk = menit_masuk+'00'
    jam_keluar = jam_keluar+'15'
    menit_keluar = menit_keluar+'00'
    kwh_kemarin = int_input('kwh kemarin brpa:  ')
    kwh_sekarang = int_input('kwh sekarang brapa:  ')
    x = kwh_sekarang - kwh_kemarin
    total_kwh += str(x)


os.system('clear')

print('SEKARANG BEBAN YA BRE KAYA LU BEBAN KELUARGA\n\n')
    
beban_r  += string(int_input('R nya brapa bre? '))
beban_s += string(int_input('S nya brapa bre? '))
beban_t += string(int_input('T nya brapa bre? '))
beban_n += string(int_input('N nya brapa bre? '))

print('\nKalo mau default langsung enter aja\n')
cctvon = input('cctv on nya brpa? (default:327) ')
cctvoff = input('cctv off nya brapa? (default:0) ')

if cctvon == '':
    jumlah_on = jumlah_on+'327'
else:
    jumlah_on += cctvon

if cctvoff == '':
    jumlah_off = jumlah_off+'0'
else:
    jumlah_off += cctvoff

    
    
os.system('clear')

print('SUHU DAN PREASURE CHILLER\n\n')
suhu_coldroom1 += string(int_input('suhu cr 1: '))
suhu_coldroom2 += string(int_input('suhu cr 2: '))
suhu_coldroom3 += string(int_input('suhu cr 3: '))
 
preasure_coldroom1 += string(int_input('preasure cr 1: '))
preasure_coldroom2 += string(int_input('preasure cr 2: '))
preasure_coldroom3 += string(int_input('preasure cr 3: '))
 
sttschiller1 = input('status cr 1: (default On)')
sttschiller2 = input('status cr 2: (default On)')
sttschiller3 = input('status cr 3: (default On)')
    
if sttschiller1 == '':
    status_coldroom1 +='ON'
    
if sttschiller2 == '':
    status_coldroom2 += 'ON'

if sttschiller3 == '':
    status_coldroom3 += 'ON'
    

print(suhu_coldroom1)


    
os.system('clear')
print('Kalo gaada tulis aja Nol(0)')

lst = []
 
# number of elements as input
print('\nPemeliharaan asset')
n = int_input("Berapa pemeliharaan nya : ")
 
# iterating till the range

for i in range(0, n):
    i = i + 1
    ele = input('pemeliharaan  '+str(i)+': ')
    ele = str(i)+'.'+ele+'%0A'

    lst.append(ele) # adding the element

pelihara = ''
for i in lst:
    x = i.replace(' ','+')
    pelihara += str(x)
    
if n == 0:
    pemeliharaan += 'nihil'
pemeliharaan = pemeliharaan+pelihara

print(pemeliharaan)





lst = []
 
# number of elements as input
print('\nPekerjaan dan Perbaikan')
n = int_input("Berapa pekerjaan nya : ")
 
# iterating till the range
for i in range(0, n):
    i = i + 1
    ele = input('pekerjaan  '+str(i)+': ')
    ele = str(i)+'.'+ele+'%0A'

    lst.append(ele) # adding the element

kerja = ''
for i in lst:
    x = i.replace(' ','+')
    kerja += str(x)
    
if n == 0:
    perbaikan +='nihil'
    
perbaikan = perbaikan+kerja

print(perbaikan)






lst = []
 
# number of elements as input
print('\nPermintaan Pekerjaan')
n = int_input("Berapa permintaan nya : ")
 
# iterating till the range

for i in range(0, n):
    i = i + 1
    ele = input('permintaan  '+str(i)+': ')
    ele = str(i)+'.'+ele+'%0A'

    lst.append(ele) # adding the element

minta = ''
for i in lst:
    x = i.replace(' ','+')
    minta += str(x)
    
if n == 0:
    permintaan += 'nihil'
    
permintaan = permintaan+minta

print(permintaan)




lst = []
 
# number of elements as input
print('\nKejadian atau Temuan')
n = int_input("Berapa kejadian nya : ")
 
# iterating till the range

for i in range(0, n):
    i = i + 1
    ele = input('kejadian  '+str(i)+': ')
    ele = str(i)+'.'+ele+'%0A'

    lst.append(ele) # adding the element

kejadian1 = ''
for i in lst:
    x = i.replace(' ','+')
    kejadian1 += str(x)

if n == 0:
    kejadian+='nihil'
    
kejadian = kejadian+kejadian1


os.system('clear')

link = 'https://docs.google.com/forms/d/e/1FAIpQLSfcPUk0OJIdPjrni3KmUdrn6c4atya0_uHvHM6yDY-lh_JFcg/viewform?usp=send_form?usp=pp_url'
link+=nama_entry+tahun+bulan+jam_masuk+jam_keluar+menit_masuk+menit_keluar+tanggal+cabang+zona+shift_entry+trafo1+trafo2+trafo3+kva_pln+kva_pln_catatan+status_pln+status_trafo1+status_trafo2+status_trafo3+unit_trafo+jumlah_genset+status_genset1+status_genset2+status_genset3+genset1+genset2+genset3+jenis_panel+beban_r+beban_s+beban_t+beban_n+fire_alarm+pompa_jokie+pompa_dorong+pompa_sumur+area_cctv+jumlah_on+jumlah_off+jumlah_coldroom+suhu_coldroom1+suhu_coldroom2+suhu_coldroom3+preasure_coldroom1+preasure_coldroom2+preasure_coldroom3+status_coldroom1+status_coldroom2+status_coldroom3+area_kwh+total_kwh+area_air+total_air+pemeliharaan+perbaikan+permintaan+kejadian+catatan
print(link)

webbrowser.open_new(link)
os.system("termux-open-url \""+link+"\"")