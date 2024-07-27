import streamlit as st
import pandas as pd

# Set page title and icon
st.set_page_config(page_title="Web Apps", page_icon=":blue[Menilai Tingkat Pencemaran Air Limbah]")

# Create a header section
st.write("Aplikasi ini dibuat oleh kelompok 8 kelas PLI")

st.title("SELAMAT DATANG DI WEB APPS PENENTUAN INDEKS KUALITAS AIR LIMBAH")

st.markdown("<h1 style='color: blue'>Web Apps Penentuan Indeks Kualitas Air Limbah Menggunakan Metode Storet</h1>", unsafe_allow_html=True)
st.write('----------------------------')

# Membuat Sidebar
with st.sidebar:
    selected_tab = st.selectbox("Pilih Tab", ["Home", "Metode Storet", "Baku Mutu Air Limbah", "Our Team"])

# Menampilkan konten sesuai dengan tab yang dipilih
if selected_tab == "Home":

    st.markdown("<style>h2{color: #0047AB;}</style>", unsafe_allow_html=True)
    st.write("Penentuan Indeks Kualitas Air Limbah penting untuk ditentukan agar dapat mengetahui Status Mutu air.")   
    st.header("Indeks kualitas air (IKA)")
    st.write("Indeks kualitas air (IKA) memberikan nilai tunggal yang mengekspresikan keseluruhan kualitas air pada suatu lokasi dan waktu tertentu berdasarkan beberapa parameter kualitas air.")
    st.write("IKA dapat ditentukan menggunakan 6 metode, yaitu:")
    st.write('- Metode Storet')
    st.write('- Metode IP')
    st.write('- Metode CCME')
    st.write('- Metode CCME WQI')
    st.write('- Metode IDW')
    st.write('- Metode NSF-WQI')

    st.divider()

    st.header("Metode Storet")
    st.write("Penentuan status mutu air dengan metode Storet adalah dengan membandingkan data kualitas air dengan baku mutu yang disesuaikan dengan peruntukannya.")
    st.write('Metode storet menggunakan pendekatan kuantitatif untuk menilai kualitas air berdasarkan parameter fisika, kimia dan biologi. Nilai tiap parameter ini kemudian dibandingkan dengan standar kualitas air yang di tetapkan. Hasil perbandingan tersebut akan menghasilkan Indeks Kualitas Air yang mencerminkan kondisi perairan (kategori baik, sedang, atau tercemar)')
    st.write("Metode Storet merupakan cara untuk menentukan status mutu air dengan menggunakan sistem nilai dari “US-EPA (Environmental Protection Agency)” dengan mengklasifikasikan mutu air dalam empat kelas, yaitu:")
    st.write("- Kelas A = tidak tercemar, skor 0")
    st.write("- Kelas B = tercemar ringan, skor -1 - (-10) ")
    st.write("- Kelas C = tercemar sedang, skor -11 - (-30)")
    st.write("- Kelas D = tercemar berat, skor lebih dari - 30")

    st.divider()
   
    st.header("Cara Penggunaan Aplikasi")
    st.write("- Untuk menggunakan aplikasi, silahkan tekan tombol > pada bagian kiri atas.")
    st.write("- Untuk menentukan IKA menggunakan cara storet silahkan pilih menu Metode Storet")
    st.write("- Untuk melihat baku mutu silahkan pilih menu Baku Mutu Air Limbah")

elif selected_tab == "Metode Storet":
    st.write('-----------------')
    st.title("Penentuan Indeks Kualitas Air")
    st.write('Penentuan indeks kualitas air dapat dihitung menggunakan metode storet')
    st.caption('Disclaimer: Baku mutu disini menggunakan acuan Baku Mutu PERMENLHK No.5 Tahun 2014 Tentang Baku Mutu Air Limbah Golongan I')
 

    st.write("Silahkan masukkan data pengujian untuk menentukan skor status mutu air.")
    st.caption("Pastikan data yang dimasukkan sudah benar")

    # Calculate Storet score
    def hitung_skor_storet(konsentrasi, baku_mutu):
        selisih = konsentrasi - baku_mutu
        if selisih <= 0:
            return 0
        elif selisih <= baku_mutu * 0.25:
            return -1 * min(selisih, 10)  # Skor dari 0 hingga -10
        elif selisih <= baku_mutu * 0.5:
            return -1 * min(selisih, 30)  # Skor dari 0 hingga -30
        elif selisih <= baku_mutu * 0.75:
            return -1 * min(selisih, 31)  # Skor dari 0 hingga -31
        else:
            return -1 * selisih  # Skor lebih rendah dari -31 jika selisih besar
    
    # Assuming `baku_mutu` is a dictionary and `baku_mutu_selected` is the key
    konsentrasi = st.number_input("Masukkan Konsentrasi")
    baku_mutu = {
        "BOD": 50,
        "COD": 100,
        "TSS": 200,
        "Minyak Lemak": 10,
        "Besi Terlarut (Fe)": 4,
        "Mangan Terlarut (Mn)": 2,
        "Barium (Ba)": 2,
        "Tembaga (Cu)": 2,
        "Seng (Zn)": 5,
        "Krom Heksavalen(Cr⁶)": 0.1,
        "Krom Total (Cr)": 0.5,
        "Cadmium (Cd)": 0.05,
        "Air Raksa (Hg)": 0.002,
        "Timbal (Pb)": 0.1,
        "Stanum (Sn)": 2,
        "Arsen (As)": 0.1,
        "Selenium (Se)": 0.05,
        "Nikel (Ni)": 0.2,
        "Kobalt (Co)": 0.4,
        "Sianida (CN)": 0.05,
        "Sulfida (H2S)": 0.5,
        "Fluorida (F)": 2,
        "Klorin Bebas (Cl2)": 1,
        "Amonia-Nitrogen (NH3-N)": 5,
        "Nitrat (NO3-N)": 20,
        "Nitrit (NO2-N)": 1,
        "Total Nitrogen": 30,
        "Senyawa aktif biru metilen": 5,
        "Fenol": 0.5
    }
    baku_mutu_selected = st.selectbox("Pilih Baku Mutu", list(baku_mutu.keys()))

    # Button to calculate Storet score
    if st.button("Hitung Skor Storet"):
        skor = hitung_skor_storet(konsentrasi, baku_mutu[baku_mutu_selected])
        st.write(f"Skor Storet: {skor}")

        # Determine pollution status
        if skor == 0:
            st.write('')
            st.write("Status Mutu Air: Tidak Tercemar")
            st.write('IKA: Kelas A')
        elif -10 < skor <= 0:
            st.write("Status Mutu Air: Tercemar Ringan")
            st.write('IKA: Kelas B')
        elif -30 < skor <= -10:
            st.write("Status Mutu Air: Tercemar Sedang")
            st.write('IKA: Kelas C')
        elif skor <= -31:
            st.write("Status Mutu Air: Tercemar Berat")
            st.write('IKA: Kelas D')

elif selected_tab == "Baku Mutu Air Limbah":
    st.title("Baku Mutu Air Limbah")
    st.write("Berikut adalah tabel baku mutu air limbah yang dapat digunakan sebagai acuan.")
    st.write("Baku Mutu Berdasarkan Acuan Peraturan Menteri Lingkungan Hidup Nomor : 05 Tahun 2014 TENTANG BAKU MUTU AIR LIMBAH Lampiran XLVII")
    st.caption('Semua hasil pengukuran tidak boleh melebihi baku mutu.')
    # Create a DataFrame for Baku Mutu Air Limbah
    baku_mutu_df = pd.DataFrame({
        'Parameter': ['BOD', 'COD', 'TSS', 'Minyak Lemak', 'Besi Terlarut (Fe)', 'Mangan Terlarut (Mn)', 
                       'Barium (Ba)', 'Tembaga (Cu)', 'Seng (Zn)', 'Krom Heksavalen(Cr⁶)', 
                       'Krom Total (Cr)', 'Cadmium (Cd)', 'Air Raksa (Hg)', 'Timbal (Pb)', 
                       'Stanum (Sn)', 'Arsen (As)', 'Selenium (Se)', 'Nikel (Ni)', 'Kobalt (Co)',
                       'Sianida (CN)', 'Sulfida (H2S)', 'Fluorida (F)', 'Klorin Bebas (Cl2)',
                       'Amonia-Nitrogen (NH3-N)', 'Nitrat (NO3-N)', 'Nitrit (NO2-N)',
                       'Total Nitrogen', 'Senyawa aktif biru metilen', 'Fenol'],
        'Baku Mutu Golongan I (mg/L)': [50, 100, 200, 10, 4, 2, 2, 2, 5, 0.1, 0.5, 0.05, 0.002, 0.1, 2, 0.1, 0.05, 0.2, 0.4,
                                         0.05, 0.5, 2, 1, 5, 20, 1, 30, 5, 0.5]
    })


    # Display the DataFrame
    st.dataframe(baku_mutu_df)

elif selected_tab=="Our Team":
    st.title('kelompok 8')
    st.header('Anggota')
    st.write('1. Farhah Yusriyyana Zatin')
    st.write('2. Ahmad Dian Alfaridz')
    st.write('3. Arum Nadya')
    st.write('4. Ainun Fadilah')
    st.write('5. Muhammad Ariel Suwandi')
    st.write('6. Mutiara Eirene Lahira')