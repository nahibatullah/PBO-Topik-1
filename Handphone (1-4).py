class Handphone:
    def __init__(self, merek, model, tahun, kapasitas_baterai):
        self.merek = merek
        self.model = model
        self.tahun = tahun
        self.kapasitas_baterai = kapasitas_baterai
        self.status_daya = 100
        self.dinyalakan = False
    def nyalakan(self):
        if self.status_daya > 0:
            self.dinyalakan = True
            print(f"{self.merek} {self.model} telah dinyalakan.")
        else:
            print("Baterai kosong. Silakan isi daya terlebih dahulu.")
    def matikan(self):
        self.dinyalakan = False
        print(f"{self.merek} {self.model} telah dimatikan.")
    def isi_daya(self, jumlah):
        self.status_daya = min(100, self.status_daya + jumlah)
        print(f"Handphone diisi daya. Status baterai sekarang: {self.status_daya}%")
    def info(self):
        status = "Menyala" if self.dinyalakan else "Mati"
        print(f"Handphone: {self.merek} {self.model}")
        print(f"Tahun: {self.tahun}")
        print(f"Baterai: {self.status_daya}% dari {self.kapasitas_baterai}mAh")
        print(f"Status: {status}")
