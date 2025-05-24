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

#Objek Pertama
hp1 = Handphone("Samsung", "Galaxy S23", 2023, 5000)
hp1.info()
hp1.nyalakan()
hp1.isi_daya(-20)
hp1.info()

print("\n")

#Objek Kedua
hp2 = Handphone("Apple", "iPhone 14", 2022, 4352)
hp2.info()
hp2.matikan()
hp2.isi_daya(-90)
hp2.nyalakan()
hp2.info()