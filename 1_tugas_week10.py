from pymongo import MongoClient

# Membuat koneksi ke MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Memilih database
db = client['aplikasi']

# Memilih koleksi (collection)
collection = db['biodata']

def tambah_kontak(nama, telepon, email):
    kontak = {
        'nama': nama,
        'telepon': telepon,
        'email': email
    }
    result = collection.insert_one(kontak)
    print(f"Kontak ditambahkan dengan ID: {result.inserted_id}")

def lihat_semua_kontak():
    kontak_list = collection.find()
    for kontak in kontak_list:
        print(kontak)

def cari_kontak(nama):
    kontak = collection.find_one({'nama': nama})
    if kontak:
        print(kontak)
    else:
        print(f"Kontak dengan nama {nama} tidak ditemukan.")

def update_kontak(nama, telepon, email):
    result = collection.update_one({'nama': nama}, {'$set': {'telepon': telepon, 'email': email}})
    if result.modified_count > 0:
        print(f"Kontak dengan nama {nama} telah diperbarui.")
    else:
        print(f"Kontak dengan nama {nama} tidak ditemukan.")

def hapus_kontak(nama):
    result = collection.delete_one({'nama': nama})
    if result.deleted_count > 0:
        print(f"Kontak dengan nama {nama} telah dihapus.")
    else:
        print(f"Kontak dengan nama {nama} tidak ditemukan.")

def menu():
    print("\n=== Menu ===")
    print("1. Tambah Kontak")
    print("2. Lihat Semua Kontak")
    print("3. Cari Kontak")
    print("4. Update Kontak")
    print("5. Hapus Kontak")
    print("0. Keluar")

if __name__ == "__main__":
    while True:
        menu()
        pilihan = input("Masukkan pilihan (0-5): ")

        if pilihan == '0':
            print("Keluar dari program.")
            break
        elif pilihan == '1':
            nama = input("Nama: ")
            telepon = input("Telepon: ")
            email = input("Email: ")
            tambah_kontak(nama, telepon, email)
        elif pilihan == '2':
            print("\nMenampilkan semua kontak:")
            lihat_semua_kontak()
        elif pilihan == '3':
            nama = input("Nama kontak yang dicari: ")
            cari_kontak(nama)
        elif pilihan == '4':
            nama = input("Nama kontak yang ingin diperbarui: ")
            telepon = input("Telepon baru: ")
            email = input("Email baru: ")
            update_kontak(nama, telepon, email)
        elif pilihan == '5':
            nama = input("Nama kontak yang ingin dihapus: ")
            hapus_kontak(nama)
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
