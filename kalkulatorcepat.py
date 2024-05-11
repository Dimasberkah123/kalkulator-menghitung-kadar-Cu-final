import streamlit as st
import pandas as pd

# Fungsi untuk mengatur warna background
def set_background_color(color):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Fungsi utama aplikasi
def main():
    # Pemilihan warna background
    color = st.color_picker("Pilih warna untuk background:", "#FFFFFF")
    set_background_color(color)

if __name__ == '__main__':
    main()
    
def main():
    st.sidebar.header("Navigasi")
    selected = st.sidebar.selectbox("Pilih halaman:", ["Pendahuluan", "Tentang Cu", "Batas Maksimal Kadar Cu", "Petunjuk Penggunaan Aplikasi","Kalkulator Cepat Menghitung Kadar Cu (untuk sampel padatan)", "Kalkulator Cepat Menghitung Kadar Cu (untuk sampel cairan)"])

    if selected == "Pendahuluan":
        show_pendahuluan()
    elif selected == "Tentang Cu":
        show_TentangCu()
    elif selected == "Batas Maksimal Kadar Cu":
        show_BatasMaksimalKadarCu()
    elif selected == "Kalkulator Cepat Menghitung Kadar Cu (untuk sampel padatan)":
        calculate_cu_content()
    elif selected == "Petunjuk Penggunaan Aplikasi":  
        show_penggunaan_aplikasi()  
    elif selected == "Kalkulator Cepat Menghitung Kadar Cu (untuk sampel cairan)":
        calculate_cu_liquid()

def show_BatasMaksimalKadarCu():
    # Tabel informasi tambahan
    st.markdown("<h1 style='color:red'>❗𓇼𓂃Batas Maksimal Kadar Cu</h1>", unsafe_allow_html=True)
    default_kalkulatorcepat = {
        "Permen": "2.0 mg/kg",
        "Susu formula": "20.0 mg/kg",
        "Susu UHT": "0.02 mg/kg",
        "Tepung Terigu": "10 mg/kg",
        "Produk Siap Konsumsi": "20 mg/kg", 
        "Makanan Hasil Laut": "1.0 mg/kg", 
        "Sayuran Segar": "2.0 mg/kg",
        "Kopi": "30 mg/kg",
        "Air mineral": "0.02 mg/L",
        "Pasta coklat": "15.0 mg/kg",
        "Keju": "0.02 mg/kg",
        "Yogurt": "0.20 mg/kg",
        "Minuman berperisa berkarbonisasi": "0.05 mg/kg",
        "Eskrim": "20.0 mg/kg",
        "Baso ikan beku": "0.3 mg/kg",
        "Kripik kulit ikan": "0.3 mg/kg"
    }

    df = pd.DataFrame({
        "Sampel Produk": list(default_kalkulatorcepat.keys()),
        "Maksimal Kadar Cu": list(default_kalkulatorcepat.values())
    })

    # Garis pembatas berwarna-warni
    st.markdown(
        '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
        unsafe_allow_html=True
    )

    st.write("Berikut beberapa daftar maksimal kadar Cu pada produk pangan menurut SNI:")
    st.dataframe(df)

def show_TentangCu():
    st.markdown("<h1 style='color:pink'>..🥜𐙚⋅⋅ Apaa itu Cu ⁉️ 𝜗𝜚˚⋆</h1>", unsafe_allow_html=True)
    st.markdown('<hr style="border: none; height: 5px; background: linear-gradient(to right, yellow, green, violet);"/>',
                unsafe_allow_html=True)
    st.write("Logam Cu merupakan logam berat essensial yang dibutuhkan oleh tubuh dalam jumlah yang kecil, namun bila jumlah yang masuk ke dalam tubuh berlebihan akan berubah fungsi menjadi zat racun bagi tubuh. Keracunan Cu dapat menyebabkan gangguan pada jalur pernapasan. Pada makanan dan minuman sering terdapat unsur-unsur yang tidak mempunyai nilai nutrisi. Adanya unsur-unsur tersebut selalu dihubungkan dengan sifat-sifat yang tidak diinginkan dan kadang-kadang beracun sehingga membahayakan kesehatan konsumen. Oleh karena itu, diperlukan syarat-syarat untuk industri makanan dan minuman agar produksinya tidak membahayakan bagi konsumen, sehingga tujuan pembuatan web ini untuk menghitung kadar cemaran logam Cu yang telah dilakukan pengujian cemaran logam sesuai dengan SNI.")
    st.markdown("<h1 style='color:violet'>..🧇𐙚⋅⋅ Tujuan 𝜗𝜚˚⋆</h1>", unsafe_allow_html=True)
    st.markdown('<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, indigo);"/>',
                unsafe_allow_html=True)
    st.write('''Selain bertujuan untuk menghitung kadar agar sesuai dengan SNI. Analisis kadar tembaga pada produk pangan juga dilakukan dengan beberapa tujuan utama:

⋆˚࿔ Kepatuhan Regulasi: Banyak negara memiliki batasan maksimum untuk kadar tembaga dalam produk pangan. Analisis dilakukan untuk memastikan bahwa produk pangan memenuhi standar keamanan pangan yang ditetapkan oleh badan regulasi.

⋆˚࿔ Keamanan Konsumen: Kadar tembaga yang berlebihan dalam makanan dapat menyebabkan toksisitas tembaga pada manusia. Oleh karena itu, analisis dilakukan untuk memastikan bahwa produk pangan aman dikonsumsi dan tidak menimbulkan risiko kesehatan bagi konsumen.

⋆˚࿔ Kualitas Produk: Tembaga dapat digunakan sebagai indikator kualitas dalam beberapa produk pangan tertentu. Kadar tembaga yang rendah atau tinggi dapat menunjukkan masalah dalam proses produksi atau pemrosesan yang mempengaruhi kualitas produk.

⋆˚࿔ Nutrisi: Tembaga adalah mineral penting yang diperlukan oleh tubuh manusia dalam jumlah yang tepat. Analisis kadar tembaga membantu dalam memahami kontribusi produk pangan terhadap asupan tembaga harian dan memastikan bahwa produk tersebut memberikan nutrisi yang cukup kepada konsumen.

⋆˚࿔ Penelitian dan Pengembangan: Analisis kadar tembaga juga dilakukan sebagai bagian dari penelitian dan pengembangan produk pangan baru. Hal ini membantu dalam memahami komposisi nutrisi produk dan memungkinkan perbaikan formulasi untuk meningkatkan kualitas dan nilai nutrisi produk.


Dengan demikian, analisis kadar tembaga pada produk pangan penting untuk memastikan keamanan, kualitas, dan kepatuhan terhadap regulasi, serta untuk memahami kontribusi nutrisi produk terhadap kesehatan manusia.''')

def show_penggunaan_aplikasi():
    st.markdown("<h1 style='color:yellow'>..𐙚⋅⋅ 〃 ۫   ࣭ Petunjuk Penggunaan Aplikasi! 📢❗ 𝜗𝜚˚⋆</h1>", unsafe_allow_html=True)
    st.markdown('<hr style="border: none; height: 5px; background: linear-gradient(to right, indigo, violet);"/>',
                unsafe_allow_html=True)
    st.write('''
1. Pilih halaman yang diperlukan
2. Untuk memlilih kalkulator cepat dapat dipilih sesuai yang user inginkan
3. Masukkan volume atau bobot sampel yang akan di konversi (opsional)
4. Masukkan nilai absorbansi, slope, dan intersept
5. lalu klik kolom hitung kadar Cterukur
6. Masukkan cterukur, volume labu takar, faktor pengenceran, dan bobot sampel atau volume sampel
7. Klik kolom hitung kadar cemaran Cu''')            

def show_pendahuluan():
    st.markdown("""
        <style>
        @keyframes bounce {
        0%, 100% {
        transform: translateY(0);
        }
        50% {
        transform: translateY(20px);
        }
        }

        .bounce {
        animation: bounce 0.5s infinite;
        }
        </style>
        """, unsafe_allow_html=True)

# Tambahkan elemen dengan kelas "bounce" untuk menerapkan animasi bounce
    st.write('<div class="bounce">۫  ..˖💬໒꒰ྀ Halooo! >_<</div>', unsafe_allow_html=True)
    st.markdown("<h1 style='color:indigo'>'۫  ..˖💬໒꒰ྀ Selamat Datang di Kalkulator Cepat Kadar Cu❗❗6꒱ྀིঌ₊", unsafe_allow_html=True)
    st.markdown('<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
                unsafe_allow_html=True)
    st.write(''' Kalkulator Cepat Kadar Cu ini disusun oleh :
1. Andiani Putri Wijiyanti (2320507)
2. Azizah lintang Maylya (2320511)
3. Dimas Farrel Arunajati (2320519)
4. Fadhlurahman Rayyandani Shafwan (2320522)
5. Putri Chalis Lestari (2320544)
6. Ratu Amalia Zahara (2320551)''')

def calculate_cu_content():
    st.title('۫𓈒 ׄ ੭୧ Kalkulator Cepat Menghitung Kadar Cu Pada Sampel Padatan ྀ🍬 ঌ .. ')  

    st.markdown('<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
                unsafe_allow_html=True)
    st.markdown('''Kalkulator cepat ini dibuat bertujuan untuk memudahkan teman-teman menghitung 
            kadar Cu (tembaga) dalam sampel pangan yang sudah dianalisis melalui Spektrofotometer Serapan Atom (SSA).''')

    st.header('Konversi Satuan (Opsional)')
    st.write("Konversi ini digunakan untuk mengubah dari miligram ke gram dan dari mililiter ke liter")
    st.markdown('<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
                unsafe_allow_html=True)
    angka = st.number_input("Masukkan angka yang ingin di konversi:", step=0.0001)
    st.write('angka yang diinput adalah=', angka)

    hitung_angka = st.button("Hitung konversi angka")

    if hitung_angka:
        angka = angka/1000
        st.write(f"Hasil perhitungan angka = {angka}")

    st.header('Perhitungan Kadar Cterukur')
    st.markdown(
        '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
        unsafe_allow_html=True
    )

    y = st.number_input("Masukkan nilai y:", step=0.0001)
    st.write('Hasil dari absorbansi adalah=', y)
    a = st.number_input("Masukkan nilai a:", step=0.0001)
    st.write('Hasil dari intersept adalah=', a)
    b = st.number_input("Masukkan nilai b:", step=0.0001)
    st.write('Hasil dari slope adalah=', b)

    y2 = st.number_input("Masukkan nilai y2:", step=0.0001)
    st.write('Hasil dari absorbansi adalah=', y2)
    a2 = st.number_input("Masukkan nilai a2:", step=0.0001)
    st.write('Hasil dari intersept adalah=', a2)
    b2 = st.number_input("Masukkan nilai b2:", step=0.0001)
    st.write('Hasil dari slope adalah=', b2)

    hitung_x = st.button("Hitung kadar c terukur")

    if hitung_x:
        x = (y - a) / b
        x2 = (y2 - a2) / b2
        rata_rata_x = (x + x2) / 2
        st.write(f"Hasil perhitungan x = {rata_rata_x} (mg/L)")

    st.header("Cemaran Kadar Cu Dalam Sampel")

    st.markdown(
        '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
        unsafe_allow_html=True
    )

    c_terukur = st.number_input("Masukkan kadar C terukur (mg/L)", step=0.0001)
    st.write('Hasil dari konsentrasi terukur adalah=', c_terukur)
    v = st.number_input("Masukkan nilai V (L):", step=0.0001)
    st.write('Hasil dari volume adalah=', v)
    FP = st.number_input("Masukkan nilai FP:", step=0.0001)
    st.write('Hasil dari FP adalah=', FP)
    bobot_sampel = st.number_input("Masukkan nilai bobot sampel (gram):", step=0.0001)
    st.write('Hasil dari bobot sampel adalah=', bobot_sampel)

    hitung_cu = st.button("Hitung kadar cemaran Cu")

    if hitung_cu:
        kadar_cemaran_cu = (c_terukur * v * FP) / (bobot_sampel * 0.001)
        st.write(f"Hasil perhitungan kadar cemaran Cu = {kadar_cemaran_cu} ppm")

def calculate_cu_liquid():
    st.title('۫𓈒 ׄ ੭୧ Kalkulator Cepat Menghitung Kadar Cu Pada Sampel Cairan ྀ🫗 ঌ .. ')  
    st.markdown('<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
                unsafe_allow_html=True)
    st.markdown('''Kalkulator cepat ini dibuat bertujuan untuk memudahkan teman-teman menghitung 
            kadar Cu (tembaga) dalam sampel pangan yang sudah dianalisis melalui Spektrofotometer Serapan Atom (SSA).''')

    st.header('Konversi Satuan (Opsional)')
    st.write("Konversi ini digunakan untuk mengubah dari miligram ke gram dan dari mililiter ke liter")
    st.markdown('<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
                unsafe_allow_html=True)
    angka = st.number_input("Masukkan angka yang ingin di konversi:", step=0.0001)
    st.write('angka yang diinput adalah=', angka)

    hitung_angka = st.button("Hitung konversi angka")

    if hitung_angka:
        angka = angka/1000
        st.write(f"Hasil perhitungan angka = {angka}")

    st.header('Perhitungan Kadar Cterukur')
    st.markdown(
        '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
        unsafe_allow_html=True
    )

    y = st.number_input("Masukkan nilai y:", step=0.0001)
    st.write('Hasil dari absorbansi adalah=', y)
    a = st.number_input("Masukkan nilai a:", step=0.0001)
    st.write('Hasil dari intersept adalah=', a)
    b = st.number_input("Masukkan nilai b:", step=0.0001)
    st.write('Hasil dari slope adalah=', b)

    y2 = st.number_input("Masukkan nilai y2:", step=0.0001)
    st.write('Hasil dari absorbansi adalah=', y2)
    a2 = st.number_input("Masukkan nilai a2:", step=0.0001)
    st.write('Hasil dari intersept adalah=', a2)
    b2 = st.number_input("Masukkan nilai b2:", step=0.0001)
    st.write('Hasil dari slope adalah=', b2)

    hitung_x = st.button("Hitung kadar c terukur")

    if hitung_x:
        x = (y - a) / b
        x2 = (y2 - a2) / b2
        rata_rata_x = (x + x2) / 2
        st.write(f"Hasil perhitungan x = {rata_rata_x} (mg/L)")

    st.header("Cemaran Kadar Cu Dalam Sampel")

    st.markdown(
        '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
        unsafe_allow_html=True
    )

    c_terukur = st.number_input("Masukkan kadar C terukur (mg/L)", step=0.0001)
    st.write('Hasil dari konsentrasi terukur adalah=', c_terukur)
    v = st.number_input("Masukkan nilai V (L):", step=0.0001)
    st.write('Hasil dari volume adalah=', v)
    FP = st.number_input("Masukkan nilai FP:", step=0.0001)
    st.write('Hasil dari FP adalah=', FP)
    volume_sampel = st.number_input("Masukkan nilai volume sampel (L):", step=0.0001)
    st.write('Hasil dari volume cairan adalah=', volume_sampel)

    hitung_cu = st.button("Hitung kadar cemaran Cu")

    if hitung_cu:
        kadar_cemaran_cu = (c_terukur * v * FP) / (volume_sampel)
        st.write(f"Hasil perhitungan kadar cemaran Cu = {kadar_cemaran_cu} ppm")
        
if __name__ == '__main__':
    main()
