import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Fungsi untuk mengirim email
def kirim_email(pengirim, penerima, subject, html_content):
    # Konfigurasi server SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Gantilah 'password_aplikasi' dengan kode App Password yang aman dari Google
    server.login(pengirim, 'croh nynx iuwl rnby')  # Ganti dengan App Password yang benar

    # Membuat objek email
    msg = MIMEMultipart()
    msg['From'] = pengirim
    msg['To'] = penerima
    msg['Subject'] = subject

    # Menyisipkan konten HTML ke dalam email
    msg.attach(MIMEText(html_content, 'html'))

    # Mengirim email
    server.send_message(msg)
    server.quit()

# Template HTML untuk email
html_template = """
<html>
<head>
  <title>Sistem Email Otomatis</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      color: #333;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }
    .container {
      width: 100%;
      max-width: 600px;
      margin: 0 auto;
      background-color: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      border: 1px solid #ddd;
    }
    h1 {
      font-size: 24px;
      color: #333;
      margin-bottom: 10px;
      text-align: center;
    }
    hr {
      border: 0;
      border-top: 1px solid #ddd;
      margin: 20px 0;
    }
    p {
      font-size: 16px;
      line-height: 1.5;
      margin: 0 0 20px;
    }
    .button-container {
      text-align: center;
      margin-top: 20px;
    }
    .button-container a {
      color: white;
    }
    .button {
      background-color: #6a0dad;
      padding: 10px 20px;
      text-decoration: none;
      border-radius: 5px;
      font-size: 16px;
      display: inline-block;
    }
    .button:hover {
      background-color: #5a0bb5;
    }
    .footer {
      font-size: 14px;
      color: #888;
      text-align: center;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Mencoba Sistem Email Otomatis</h1>
    <p>Sistem email otomatis memudahkan pengiriman pesan secara efisien dan terjadwal. Kita bisa mendapatkan notifikasi otomatis.</p>
    <p>Keuntungan sistem ini termasuk penghematan waktu, pengurangan kesalahan manual, dan kemudahan penjadwalan email.</p>
    <div class="button-container">
      <a href="#" class="button">Pelajari Lebih Lanjut</a>
    </div>
    <div class="footer">
      &copy; 2024 Hak cipta dilindungi.
    </div>
  </div>
</body>
</html>
"""

# Menggunakan fungsi untuk mengirim email
pengirim = 'meikcztre@gmail.com'
penerima = 'sadiyahrpl@gmail.com'
subject = 'Gizel Nadira Gaus Ayubi/24'
kirim_email(pengirim, penerima, subject, html_template)
print('Email berhasil terkirim!')
