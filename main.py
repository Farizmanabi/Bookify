from book import ManageBook
from transaction import Transaction
    
def main():
    print(r'''
          
  ____              _    _  __       
 | __ )  ___   ___ | | _(_)/ _|_   _ 
 |  _ \ / _ \ / _ \| |/ / | |_| | | |
 | |_) | (_) | (_) |   <| |  _| |_| |
 |____/ \___/ \___/|_|\_\_|_|  \__, |
                               |___/ 

          ''')
    print("===== Selamat Datang di Bookify =====")
    manage = ManageBook()
    transactions = Transaction()

    while True:
        print("\n=== Menu Utama ===")
        print("1. Lihat Daftar Buku")
        print("2. Cari buku")
        print("3. Tambahkan Buku ke Keranjang")
        print("4. Edit Buku dalam Keranjang")
        print("5. Hapus Buku dari Keranjang")
        print("6. Reset Semua Transaksi")
        print("7. Lihat Detail Pemesanan")
        print("8. Bayar Pesanan")
        print("9. Keluar dari Program\n")

        choice = input("Pilih opsi: ")

        # Read book from book.py -> read_book()
        if choice == "1":
            manage.read_book()
            
        if choice == "2":
            keyword = input("Cari buku bedasarkan (judul/penulis/kategori/tahun/harga) : ")
            manage.cari_buku(keyword)
        
        # Add book from transaction.py -> tambah_buku()
        elif choice == "3":
            while True:
                manage.read_book()
                book_id = input("Masukkan ID buku yang ingin ditambahkan ke keranjang: ")
                buku_ditemukan = next((book for book in manage.book_list if book.book_id == book_id), None)
                if buku_ditemukan:
                    jumlah = int(input("Masukkan jumlah buku yang ingin dibeli: "))
                    transactions.tambah_buku(buku_ditemukan, jumlah)
                    
                    check = input('Lanjutkan? (y/n) : ')
               
                    if check.lower() == 'n':
                        break
               
                else:
                    print(f"Buku dengan ID '{book_id}' tidak ditemukan.")
                    break

        # Edit book from transaction.py -> edit_buku()
        elif choice == "4":
            transactions.lihat_keranjang() 
            if not transactions.keranjang:
                print("Tidak ada buku yang bisa diedit.")
            else:
                old_book_id = input("Masukkan ID buku yang ingin diganti dalam keranjang: ")
                buku_lama = next((item for item in transactions.keranjang if item["buku"].book_id == old_book_id), None)

                if buku_lama:
                    new_book_id = input("Masukkan ID buku baru: ")
                    new_buku = next((book for book in manage.book_list if book.book_id == new_book_id), None)

                    if new_buku:
                        new_jumlah = int(input("Masukkan jumlah buku baru yang ingin dibeli: "))
                        transactions.edit_buku(old_book_id, new_buku, new_jumlah)
                    else:
                        print(f"Buku dengan ID '{new_book_id}' tidak ditemukan.")
                else:
                    print(f"Buku dengan ID '{old_book_id}' tidak ditemukan di keranjang.")

                transactions.lihat_keranjang()
            
        # Delete book from transaction.py -> hapus_buku()
        elif choice == "5":
            transactions.lihat_keranjang()
            if not transactions.keranjang:
                print("Tidak ada buku yang bisa dihapus.")
            else:
                book_id = input("Masukkan ID buku yang ingin dihapus dari keranjang: ")
                transactions.hapus_buku(book_id)
        
        # Reset book from transaction.py -> reset_keranjang()
        elif choice == "6":
            transactions.reset_keranjang()

        # Read book from transaction.py -> reset_keranjang()
        elif choice == "7":
            transactions.detail_pemesanan()
            
        # pay transaction from transaction.py -> bayar_pesanan()
        elif choice == "8":
            transactions.bayar_pesanan()
            
        # Keluar dari Program
        elif choice == "9":  
            print("Keluar dari program. Terima kasih telah menggunakan Bookify!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
