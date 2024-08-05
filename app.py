from flask import Flask, request, render_template, redirect, url_for
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Konfigurasi database
db = mysql.connector.connect(
    host="localhost",
    user="glpi_pma",
    password="Init2024##",
    database="absensi"
)

@app.route('/', methods=['GET', 'POST'])
def absensi():
    if request.method == 'POST':
        nama = request.form['nama']
        email = request.form['email']
        divisi = request.form['divisi']
        waktu_absen = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        cursor = db.cursor()
        sql = "INSERT INTO pegawai (nama, email, waktu_absen, divisi) VALUES (%s, %s, %s, %s)"
        val = (nama, email, waktu_absen, divisi)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()

        return redirect(url_for('absensi'))

    return render_template('absensi.html')

@app.route('/data', methods=['GET'])
def data():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM pegawai")
    data = cursor.fetchall()
    cursor.close()

    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
