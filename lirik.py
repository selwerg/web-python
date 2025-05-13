import sys
import time

def jalanin_lirik():
    lirik = [
        ("Telah lama ku menantimu...", 0.1),
        ("Diam sendiri menunggu", 0.1),
        ("Setengah hati mencinta", 0.2),
        ("Ku sakit karenamu", 0.1),
        ("Sungguh aku tak bisa", 0.2),
        ("Sampai kapanpun tak bisa", 0.2),
        ("Membenci dirimu", 0.1),
        ("sesungguhnya aku tak mampu", 0.1),
        ("Sulit untuk ku bisa", 0.1),
        ("Sangat sulit ku tak bisa", 0.2),
        ("Memisahkan segala", 0.1),
        ("cinta dan benci yang ku rasa", 0.2),
    ]

    # Delay antar baris (bisa kamu sesuaikan lagi sesuai ritme lagunya)
    delay = [0.5, 0.5, 0.7, 3.0, 0.8, 0.6, 0.3, 0.6, 0.4, 0.6, 0.1, 0.3]

    print("\n== Cinta dan Benci - Geisha ==")
    time.sleep(1.5)

    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')

    print("// Code by Ray")

# Panggil fungsi jika dijalankan langsung
if __name__ == "__main__":
    jalanin_lirik()
