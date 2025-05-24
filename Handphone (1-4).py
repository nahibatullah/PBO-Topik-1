class Handphone:
    def __init__(self, merek, model, tahun, kapasitas_baterai):
        self.merek = merek
        self.model = model
        self.tahun = tahun
        self.kapasitas_baterai = kapasitas_baterai  # dalam mAh
        self.status_daya = 100  # persentase
        self.dinyalakan = False

    # Method untuk menyalakan handphone
    def nyalakan(self):
        if self.status_daya > 0:
            self.dinyalakan = True
            print(f"{self.merek} {self.model} telah dinyalakan.")
        else:
            print("Baterai kosong. Silakan isi daya terlebih dahulu.")

    # Method untuk mematikan handphone
    def matikan(self):
        self.dinyalakan = False
        print(f"{self.merek} {self.model} telah dimatikan.")

    # Method untuk mengisi daya
    def isi_daya(self, jumlah):
        self.status_daya = min(100, self.status_daya + jumlah)
        print(f"Handphone diisi daya. Status baterai sekarang: {self.status_daya}%")

    # Method untuk menampilkan info handphone
    def info(self):
        status = "Menyala" if self.dinyalakan else "Mati"
        print(f"Handphone: {self.merek} {self.model}")
        print(f"Tahun: {self.tahun}")
        print(f"Baterai: {self.status_daya}% dari {self.kapasitas_baterai}mAh")
        print(f"Status: {status}")
