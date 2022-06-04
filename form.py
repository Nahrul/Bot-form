import sys
import time
import os
import datetime
from itertools import permutations
import webbrowser



# entry.1251386738: ASY
# entry.11845914: CIREBON
# entry.1737599555: WIB
# entry.458820389: Shift 1
# entry.666255708_hour: 07
# entry.666255708_minute: 00
# entry.1320728560_hour: 15
# entry.1320728560_minute: 00
# entry.1136196154_year: 2022
# entry.1136196154_month: 6
# entry.1136196154_day: 2
# entry.1386643190: Nahrul, Hayat

# entry.1425743504: 150
# entry.1811372098: 66
# entry.1465374572: 50
# entry.1503625449: Normal

# entry.1623498328: 3 Unit

# entry.1644025321: 250
# entry.105937284: 66
# entry.124466718: 60
# entry.331132565: 
# entry.1076685182: OK
# entry.1125670931: OK
# entry.1537648042: OK

# entry.836916224: 3 Unit

# entry.34499611: 175
# entry.680599205: 60
# entry.1190301583: 60
# entry.1447459752: 
# entry.352239030: 
# entry.2031781778: 
# entry.1028900588: Stand by Auto
# entry.1539680982.other_option_response: hehe
# entry.1539680982: __other_option__
# entry.2068862473: Stand by Manual

# entry.955785228: LVMDP
# entry.1263609799: 
# entry.766600094: 
# entry.670855053: 10
# entry.1819587166: 11
# entry.1021302425: 12
# entry.1275826288: 13
# entry.1324114517: 
# entry.2141508875: 
# entry.1350190396: 
# entry.1184945300: 
# entry.1229371084: 
# entry.1856053227: 
# entry.30180668: 
# entry.2098291707: 

# entry.209873353: Stand by Auto
# entry.926069726: Nihil
# entry.787116222: Stand by Manual

# entry.840879772: Pompa air sumur office: 1 unit (normal)
# Pompa transfer office dan dc: 2 unit (normal)
# Pompa sumur pos 1 : 1 unit (normal)
# Pompa transfer tc dan pos 1 : 1 unit (normal)
# Pompa sumur bmt : 1 unit (normal)
# entry.216921219: ON

# entry.1033210631: •  CCTV Office 45CH   :  ON
# •  CCTV Recruit  8CH:  ON
# •  CCTV Collect 24CH : ON
# •  CCTV TC 11CH   : ON
# •  CCTV DC 216CH   : ON
# •  CCTV DC PRS 19CH :  ON
# •  CCTV Posko 4CH    : ON
# entry.1450700688: 327
# entry.249967045: 1

# entry.666490678: 1
# entry.553580392: 30
# entry.665166214: 2
# entry.2052590279: 20
# entry.2010845976: 3
# entry.1394288064: 301

# entry.29450866: office: 60kwh
# dc : 1kwh
# tc : 2kwh
# entry.399026465: 10000

# entry.970325908: office : 12m3
# DC : 18m3
# tc : 12m3
# entry.1548278604: 7000

print("Hallo selamat datang di program saya")

regional = "&entry.1251386738=ASY"
nama_entry = "&entry.1386643190="
tahun = "&entry.1136196154_year="
bulan = "&entry.1136196154_month="
tanggal = "&entry.1136196154_day="
zona = "&entry.1737599555=WIB"
jam_masuk = "&entry.666255708_hour="
menit_masuk = "&entry.666255708_minute="
shift_entry = "&entry.458820389="
jam_keluar = "&entry.1320728560_hour="
menit_keluar = "&entry.1320728560_minute="
cabang = "&entry.11845914=CIREBON"

kva_pln1 = "&entry.1425743504=250"
kva_pln2 = "&entry.1811372098=66"
kva_pln3 = "&entry.1465374572=60"
kva_pln_catatan = "&entry.1050631306"
status_pln = "&entry.1503625449=Normal"
unit_trafo = "&entry.1623498328=3+Unit"
trafo1 = "&entry.1644025321=250"
trafo2 = "&entry.105937284=66"
trafo3 = "&entry.124466718=60"
status_trafo1= "&entry.1076685182=OK"
status_trafo2 = "&entry.1125670931=OK"
status_trafo3 = "&entry.1537648042=OK"

jumlah_genset = "&entry.836916224=3+Unit"
genset1 = "&entry.34499611=175"
genset2 = "&entry.680599205=60"
genset3 = "&entry.1190301583=60"
status_genset1 = "&entry.1028900588=Stand+by+Auto"
status_genset2 = "&entry.1539680982=Stand+by+Auto"
status_genset3 = "&entry.2068862473=Stand+by+Auto"

jenis_panel = "&entry.955785228=LVMDP"



beban_r = "&entry.670855053="
beban_t = "&entry.1021302425="
beban_s = "&entry.1819587166="
beban_n = "&entry.1275826288="

fire_alarm = "&entry.181359338=Aktif"



pompa_jokie = "&entry.209873353=Stand+by+Auto"
pompa_diesel = "&entry.926069726=Stand+by+Auto"
electrical_fire_pump ="&entry.787116222=Stand+by+Auto"
# pompa_dorong = "&entry.1960544484=Stand+by+Auto"
pompa_sumur = "&entry.216921219=ON"
jumlah_pompa_sumur = "&entry.840879772=Pompa+air+sumur+office:+1+unit+(normal)%0APompa+transfer+office+dan+dc:+2+unit+(normal)%0APompa+sumur+pos1+:+1+unit+(normal)%0APompa+transfer+tc+:+1+unit+(normal)%0APompa+sumur+bmt+:+1+unit+(normal)"

area_cctv = "&entry.1033210631=•++CCTV+Office+45CH+++:++ON%0A•++CCTV+Recruit++8CH:++ON%0A•++CCTV+Collect+24CH+:+ON%0A•++CCTV+TC+11CH+++:+ON%0A•++CCTV+DC+216CH+++:+ON%0A•++CCTV+DC+PRS+19CH+:++ON%0A•++CCTV+Posko+4CH++++:+ONC"
jumlah_on = "&entry.1450700688="
jumlah_off = "&entry.249967045="

jumlah_coldroom = "&entry.1070854388=3"
suhu_coldroom1 = "&entry.666490678="
preasure_coldroom1 = "&entry.553580392="
suhu_coldroom2 = "&entry.665166214="
preasure_coldroom2 = "&entry.2052590279="
suhu_coldroom3 = "&entry.2010845976="
preasure_coldroom3 = "&entry.1394288064="
status_coldroom1 = "&entry.761107784="
status_coldroom2 = "&entry.277523632="
status_coldroom3 = "&entry.1088315514="

total_kwh = "&entry.399026465="
area_kwh = "&entry.29450866="

area_air = "&entry.970325908="
total_air = "&entry.1548278604="

pemeliharaan = "&entry.1099436377="
perbaikan = "&entry.740829364="
permintaan = "&entry.864780574="
kejadian = "&entry.640345927="
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
    jam_masuk = jam_masuk+'23'
    menit_masuk = menit_masuk+'00'
    jam_keluar = jam_keluar+'07'
    menit_keluar = menit_keluar+'00'
    kwh_office_kemarin = int_input('kwh office kemarin: ')
    kwh_office_sekarang = int_input('kwh office sekarang: ')
    kwh_dc_kemarin = int_input('kwh dc kemarin: ')
    kwh_dc_sekarang = int_input('kwh dc sekarang: ')
    kwh_tc_kemarin = int_input('kwh tc kemarin: ')
    kwh_tc_sekarang = int_input('kwh tc sekarang: ')

    air_office_kemarin = int_input('air office kemarin: ')
    air_office_sekarang = int_input('air office sekarang: ')
    air_dc_kemarin = int_input('air bmt kemarin: ')
    air_dc_sekarang = int_input('air bmt sekarang: ')
    air_tc_kemarin = int_input('air tc kemarin: ')
    air_tc_sekarang = int_input('air tc sekarang: ')

    office = kwh_office_sekarang - kwh_office_kemarin
    dc = kwh_dc_sekarang - kwh_dc_kemarin
    tc = kwh_tc_sekarang - kwh_tc_kemarin

    air_office = air_office_sekarang - air_office_kemarin
    air_dc = air_dc_sekarang - air_dc_kemarin
    air_tc = air_tc_sekarang - air_tc_kemarin
    area_kwh += "Office+:+"+str(office)+"kwh%0ADc+:+"+str(dc)+"kwh%0Atc+:+"+str(tc)+"kwh"
    print(area_kwh)
    area_air += "Office+:+"+str(air_office)+"m3%0ABmt+:+"+str(air_dc)+"m3%0Atc+:+"+str(air_tc)+"m3"
    print(area_kwh)
    x = office + dc + tc
    y = air_office + air_dc + air_tc
    total_kwh += str(x)
    total_air += str(y)


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
link+=regional+nama_entry+tahun+bulan+jam_masuk+jam_keluar+menit_masuk+menit_keluar+tanggal+cabang+zona+shift_entry+trafo1+trafo2+trafo3+kva_pln1+kva_pln2+kva_pln3+kva_pln_catatan+status_pln+status_trafo1+status_trafo2+status_trafo3+unit_trafo+jumlah_genset+status_genset1+status_genset2+status_genset3+genset1+genset2+genset3+jenis_panel+beban_r+beban_s+beban_t+beban_n+fire_alarm+pompa_jokie+pompa_diesel+pompa_sumur+electrical_fire_pump+jumlah_pompa_sumur+area_cctv+jumlah_on+jumlah_off+jumlah_coldroom+suhu_coldroom1+suhu_coldroom2+suhu_coldroom3+preasure_coldroom1+preasure_coldroom2+preasure_coldroom3+status_coldroom1+status_coldroom2+status_coldroom3+area_kwh+total_kwh+area_air+total_air+pemeliharaan+perbaikan+permintaan+kejadian+catatan
print(link)

webbrowser.open_new(link)
os.system("termux-open-url \""+link+"\"")
