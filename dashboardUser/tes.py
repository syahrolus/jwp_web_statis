import os

path = '.'

files = os.listdir(path)

tdn_ambil_akhir = "</main><!-- End #main -->\n"
ambil_akhir = tdn_ambil_akhir+""
tdn_ambil_awal = '<main id="main" class="main">'
ambil_awal = ""
isi = ""

file_nav = open("main_nav.html")
tmp2 = 0
tmp3 = 0
for i in file_nav:
    tmp = i
    if tmp3 == 0:
        ambil_awal += tmp
    if tdn_ambil_awal in tmp:
        tmp3 = 1
    if tmp2 == 1:
        ambil_akhir += tmp
    if tdn_ambil_akhir in tmp:
        tmp2 = 1
# print(ambil_awal)
# print('********')
# print(ambil_akhir)


tmp = 0
for f in files:
    if f.endswith(".html"):
        if os.stat(f).st_size < 1:  
            file_new = open(f,"w")
            file_new.write(ambil_awal+isi+"\n"+ambil_akhir)
            isi = ""
        else:
            file = open(f, "r")
            for i in file:
                if tdn_ambil_awal in i:
                    tmp = 1
                if tdn_ambil_akhir in i:
                    tmp = 0
                if tmp == 2:
                    isi += i
                if tmp == 1:
                    tmp += 1  
            file_new = open(f,"w")
            file_new.write(ambil_awal+isi+"\n"+ambil_akhir)
            isi = ""
