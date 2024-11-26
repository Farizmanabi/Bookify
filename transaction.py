from tabulate import tabulate

class Transaction:
    def __init__(self):
        self.keranjang = []

    # CREATE - Tambahkan buku ke keranjang dengan jumlah tertentu
    def tambah_buku(self, buku, jumlah):
        for item in self.keranjang:
            if item["buku"].book_id == buku.book_id:
                item["jumlah"] += jumlah
                print(f"Jumlah buku '{buku.title}' di keranjang ditambah menjadi {item['jumlah']}.")
                return
        
        self.keranjang.append({"buku": buku, "jumlah": jumlah})
        print(f"Buku '{buku.title}' berhasil ditambahkan ke keranjang dengan jumlah {jumlah}.")

    # READ - Lihat detail buku dalam keranjang
    def lihat_keranjang(self):
        if not self.keranjang:
            print("Keranjang kosong.")
        else:
            print("Detail Keranjang:")
            table = [
                [index + 1, item["buku"].title, item["jumlah"], f"Rp{int(item['buku'].price) * item['jumlah']:,}"]
                for index, item in enumerate(self.keranjang)
            ]
            headers = ["No", "Title", "Jumlah", "Total Harga"]
            print(tabulate(table, headers, tablefmt="grid"))

        # UPDATE - Ganti buku di keranjang dengan buku baru dan jumlahnya
    def edit_buku(self, old_book_id, new_buku, new_jumlah):
        for item in self.keranjang:
            if item["buku"].book_id == old_book_id:
                # Ganti dengan buku baru dan jumlah baru
                item["buku"] = new_buku 
                item["jumlah"] = new_jumlah
                print(f"Buku dengan ID '{old_book_id}' berhasil diganti dengan buku '{new_buku.title}' (Jumlah: {new_jumlah}).")
                return
        print(f"Buku dengan ID '{old_book_id}' tidak ditemukan di keranjang.")


    # DELETE - Hapus buku dari keranjang
    def hapus_buku(self, book_id):
        for item in self.keranjang:
            if item["buku"].book_id == book_id:
                self.keranjang.remove(item)
                print(f"Buku '{item['buku'].title}' berhasil dihapus dari keranjang.")
                return
        print(f"Buku dengan ID '{book_id}' tidak ditemukan di keranjang.")

    # DELETE ALL - Reset semua transaksi
    def reset_keranjang(self):
        self.keranjang.clear()
        print("Keranjang telah direset.")

    # READ - Hitung total pembayaran
    def hitung_total(self):
        if not self.keranjang:
            print("Keranjang kosong. Tidak ada total pembayaran.")
            return 0
        else:
            total = sum(int(item["buku"].price) * item["jumlah"] for item in self.keranjang)
            table = [
                [item["buku"].title, item["jumlah"], f"Rp{int(item['buku'].price) * item['jumlah']:,}"]
                for item in self.keranjang
            ]
            headers = ["Title", "Jumlah", "Total Harga"]
            print(tabulate(table, headers, tablefmt="grid"))
            print(f"\nTotal Pembayaran: Rp{total:,}")
            return total

    # CONFIRM PAYMENT - Bayar pesanan
    def bayar_pesanan(self):
        total = self.hitung_total()
        if total > 0:
            konfirmasi = input("Lanjutkan pembayaran? (y/n): ")
            if konfirmasi.lower() == "y":
                self.reset_keranjang()
                print("Pembayaran berhasil! Terima kasih atas pesanan Anda.")
            else:
                print("Pembayaran dibatalkan.")
