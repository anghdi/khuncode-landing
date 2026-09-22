# Panduan leads & Meta Ads

## Yang sudah diterapkan

- Halaman `/ecommerce` fokus pada penawaran website e-commerce mulai Rp2.500.000.
- Portfolio memakai logo client asli dari public dan tautan website client.
- Biaya domain/hosting dan fitur tambahan dijelaskan sebelum pengunjung menghubungi.
- FAQ menjawab lingkup, integrasi, timeline, bahan konten, dan proses menghubungi.
- Tombol WhatsApp tetap bekerja tanpa analytics. Klik bukan lead terkonfirmasi.
- Form kontak hanya menyusun pesan WhatsApp, tidak menyimpan atau mengirim nama/catatan ke analytics.
- Versi hero mobile 640px, dimensi gambar eksplisit, dan lazy loading logo/portfolio.

## Tracking: belum aktif

Pemilik belum memiliki Meta Pixel ID dan GA4 Measurement ID. Kode saat ini hanya menyediakan hook, bukan instalasi Pixel atau GA4. Tidak ada data yang otomatis dikirim ke kedua layanan sebelum base tag dipasang.

Setelah ID tersedia:

1. Tentukan instalasi langsung atau melalui tag manager; gunakan satu jalur agar tidak terjadi duplikasi.
2. Pasang base tag dan konfigurasi preferensi consent yang sesuai sebelum memanggil tracker. Lengkapi informasi privasi sesuai implementasi nyata.
3. Uji PageView/page_view, lalu satu klik CTA per lokasi di Meta Test Events dan GA4 DebugView.
4. Kode memanggil Meta custom event `WhatsAppClick` serta GA4 `click_whatsapp`, dengan `cta_location`, `page_path`, dan label UTM valid. Jangan tambahkan nama, email, nomor telepon, atau isi pesan ke payload.
5. Jangan tandai klik sebagai `Lead` atau `Purchase`. Pesan belum tentu dikirim setelah aplikasi WhatsApp terbuka. Catat lead dan hasil diskusi di CRM atau sheet terpisah.
6. Validasi domain produksi, canonical, HTTPS, link WhatsApp, social preview, dan preferensi privasi sebelum belanja iklan.

Referensi teknis: https://developers.facebook.com/docs/meta-pixel/reference/ (akses dokumentasi mendapat HTTP 429 saat pengerjaan; validasi kembali saat pemasangan).

## URL kampanye

Gunakan `/ecommerce?utm_source=instagram&utm_medium=paid_social&utm_campaign=ecommerce_launch&utm_content=video_01` pada domain produksi.

Modul menerima label alfanumerik dengan `_`, `.`, `~`, dan `-`, maksimal 100 karakter. Hindari data pribadi dalam UTM. Label diteruskan pada link internal; tidak disimpan lintas sesi. Kunjungan baru tanpa UTM tidak diklaim sebagai kunjungan iklan.

## Pengukuran bisnis

Catat per kampanye: biaya iklan, kunjungan landing page, klik WhatsApp, percakapan masuk, lead yang sesuai layanan/anggaran, proposal, dan project jadi. Optimalkan dari kualitas percakapan serta biaya per lead yang sesuai, bukan jumlah klik semata.

Mulai eksperimen satu variabel per waktu: pesan iklan, headline, atau materi visual. Jangan membuat urgency, testimoni, rating, dan angka hasil yang belum terbukti.

## QA responsive sebelum tayang

Target lebar: 320, 375/390, 768, 1024, 1440px. Pastikan tidak ada scroll horizontal, harga tidak terpotong, CTA bawah tidak menutupi konten, menu dapat ditutup dengan Escape, form terbaca saat keyboard muncul, dan WhatsApp terbuka dari browser Instagram/Facebook. Uji zoom 200%, reduced motion, keyboard-only, dan JavaScript nonaktif.

Build dan audit HTML dilakukan lokal; pemeriksaan visual/interaksi browser belum dilakukan karena izin browser ditolak pada sesi ini. Jangan menyatakan QA lintas perangkat atau skor Lighthouse sudah lulus.

Target Core Web Vitals: LCP ≤2,5 detik, INP ≤200ms, CLS ≤0,1 pada persentil ke-75. Ini target, bukan hasil ukur website. Ukur pada URL produksi melalui PageSpeed Insights dan data pengguna nyata. Sumber: https://web.dev/articles/vitals

## Pembaruan scope

Tracking ditunda. Import modul telah dilepas dari layout dan form kontak, sehingga hook dan penerusan UTM di atas saat ini tidak berjalan. Dokumen ini menjadi rencana integrasi mendatang, bukan deskripsi tracking aktif.
