data ={ }
while True :
    print("")
    g = input("(T)ambah, (U)bah, (H)apus, (L)ihat,(C)ari, (K)eluar: ")
    if g.lower() == "k":
        break
    elif g.lower() =="l":
        print("~~~~~~~~~~~~~~~~~~~~~~~~~Data Nilai Mahasiswa~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()
        print("======================================================================================")
        print("|  No  |      Nama     |      NIM      |   TUGAS  |   UTS   |   UAS   | Nilai Akhir  |")
        print("======================================================================================")
        i=0
        for x in data.items():
            i+=1
            print("| {6:4} | {0:13s} | {1:13} | {2:8d} |  {3:6d} | {4:7d} | {5:12.2f} | "\
                  .format(x[0],x[1][0],x[1][1],x[1][2],x[1][3],x[1][4],i))
            print("======================================================================================")

        else :
            print("======================================================================================")

    elif g.lower() == "t":
        print ("Tambah Data")
        nama  = input    ("Nama          : ")
        nim   = int(input("NIM           : "))
        tugas = int(input("Tugas         : "))
        uts   = int(input("Nilai UTS     : "))
        uas   = int(input("Nilai UAS     : "))
        nilaiakhir  = ((tugas)*30/100+(uts)*35/100+(uas)*35/100)
        data[nama] = nim, tugas, uts, uas, nilaiakhir
        
    elif g.lower() == "u":
        print("Edit Data Nilai Mahasiswa")
        nama = input         (" Masukan Nama:")
        if nama in data.keys():
            nim   = input    ("Nim               :")
            tugas = int(input("Nilai Tugas Baru  : "))
            uts   = int(input("Nilai UTS Baru    : "))
            uas   = int(input("Nilai UAS Baru    : "))
            nilaiakhir  = ((tugas)*30/100+(uts)*35/100+(uas)*35/100)
            data[nama] = nim, tugas, uts, uas, nilaiakhir
        else :
            print("Data {0} tidak ada ".format(nama))
                     
    elif g.lower() == "c":
        print("Cari Data Nilai Mahasiswa")
        nama = input(" Masukan Nama: ")
        if nama in data.keys():
            print("~~~~~~~~~~~~~~~~~~~~~~~~Data Nilai Mahasiswa~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            print("=========================================================================")
            print("|  No  |    Nama    |     NIM     |  TUGAS |  UTS |  UAS  | Nilai Akhir |")
            print("=========================================================================")
            print("| {6:4} | {0:10s} | {1:11} | {2:6d} |  {3:3d} | {4:5d} | {5:11.2f} | "\
                  .format(x[0],x[1][0],x[1][1],x[1][2],x[1][3],x[1][4],i))
            print("=========================================================================")
        else:
            print("Datanya {0} tidak ada ".format(nama))

    elif g.lower() == "h":
        print("Hapus Data Nilai Mahasiswa")
        nama = input(" Masukan Nama:")
        if nama in data.keys():
            del data[nama]
        else :
            print("Data {0} tidak ada".format(nama))  


    else:
         print ("Pilih Menu Yang Tersedia")
              
        
            
          
           
        
