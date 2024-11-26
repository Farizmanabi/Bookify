from book import ManageBook
from transaction import Transaction

def main():
    print("=== Selamat Datang di Bookify ===")
    manage = ManageBook()
    transactions = Transaction()

    while True:
        print("\n=== Menu Utama ===")
        print("1. Lihat Daftar Buku")
        print("2. Tambahkan Buku ke Keranjang")
        print("3. Edit Buku dalam Keranjang")
        print("4. Hapus Buku dari Keranjang")
        print("5. Reset Semua Transaksi")
        print("6. Lihat Detail Pemesanan")
        print("7. Hitung Total Pembayaran")
        print("8. Bayar Pesanan")
        print("9. Keluar dari Program\n")

        choice = input("Pilih opsi: ")

        # Read book from book.py -> read_book()
        if choice == "1":
            manage.read_book()
        
        # Add book from transaction.py -> tambah_buku()
        elif choice == "2":
            manage.read_book()
            book_id = input("Masukkan ID buku yang ingin ditambahkan ke keranjang: ")
            buku_ditemukan = next((book for book in manage.book_list if book.book_id == book_id), None)
            if buku_ditemukan:
                jumlah = int(input("Masukkan jumlah buku yang ingin dibeli: "))
                transactions.tambah_buku(buku_ditemukan, jumlah)
            else:
                print(f"Buku dengan ID '{book_id}' tidak ditemukan.")

        # Edit book from transaction.py -> edit_buku()
        elif choice == "3":  
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
        elif choice == "4":
            book_id = input("Masukkan ID buku yang ingin dihapus dari keranjang: ")
            transactions.hapus_buku(book_id)
        
        # Reset book from transaction.py -> reset_keranjang()
        elif choice == "5":
            transactions.reset_keranjang()

        # Read book from transaction.py -> reset_keranjang()
        elif choice == "6":
            transactions.lihat_keranjang()
            
        # SUM all transaction from transaction.py -> hitung_total()
        elif choice == "7":
            transactions.hitung_total()
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
