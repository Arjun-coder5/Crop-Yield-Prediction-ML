from flask import Flask, request, render_template, redirect, Response
import numpy as np
import pickle
import sqlite3
from datetime import datetime

# Load model
dtr = pickle.load(open('dtr.pkl', 'rb'))
preprocessor = pickle.load(open('preprocessor.pkl', 'rb'))

app = Flask(__name__)

# ---------------- DB ----------------
def init_db():
    conn = sqlite3.connect('predictions.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            country TEXT,
            crop TEXT,
            year INTEGER,
            rainfall REAL,
            pesticides REAL,
            temperature REAL,
            prediction TEXT,
            created_at TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def save_to_db(data):
    conn = sqlite3.connect('predictions.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO history 
        (country, crop, year, rainfall, pesticides, temperature, prediction, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()
    conn.close()

# ---------------- ROUTES ----------------

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        Year = int(request.form['Year'])
        rainfall = float(request.form['average_rain_fall_mm_per_year'])
        pesticides = float(request.form['pesticides_tonnes'])
        temp = float(request.form['avg_temp'])
        Area = request.form['Area']
        Item = request.form['Item']

        features = np.array([[Year, rainfall, pesticides, temp, Area, Item]], dtype=object)
        transformed = preprocessor.transform(features)
        prediction = dtr.predict(transformed)[0]

        prediction_value = round(float(prediction), 2)

        save_to_db((
            Area, Item, Year, rainfall, pesticides, temp,
            str(prediction_value),
            datetime.now().strftime("%d %b %Y, %I:%M %p")
        ))

        return render_template('index.html', prediction=prediction_value)

    except Exception as e:
        return f"Error: {e}"


# ---------------- HISTORY ----------------

@app.route('/history')
def history():
    conn = sqlite3.connect('predictions.db')
    c = conn.cursor()
    c.execute('SELECT * FROM history ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    return render_template('history.html', rows=rows)


@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('predictions.db')
    c = conn.cursor()
    c.execute('DELETE FROM history WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect('/history')


@app.route('/clear')
def clear():
    conn = sqlite3.connect('predictions.db')
    c = conn.cursor()
    c.execute('DELETE FROM history')
    conn.commit()
    conn.close()
    return redirect('/history')


# ---------------- API ----------------

@app.route('/api/predict', methods=['POST'])
def api_predict():
    data = request.json

    features = np.array([[ 
        data['Year'],
        data['rainfall'],
        data['pesticides'],
        data['temperature'],
        data['Area'],
        data['Item']
    ]], dtype=object)

    transformed = preprocessor.transform(features)
    prediction = dtr.predict(transformed)[0]

    return {"prediction": round(float(prediction), 2)}


# ---------------- CSV DOWNLOAD ----------------

@app.route('/download')
def download():
    conn = sqlite3.connect('predictions.db')
    c = conn.cursor()
    c.execute('SELECT * FROM history')
    rows = c.fetchall()

    def generate():
        yield 'id,country,crop,year,rainfall,pesticides,temp,prediction,date\n'
        for r in rows:
            yield ','.join(map(str, r)) + '\n'

    return Response(generate(), mimetype='text/csv',
                    headers={"Content-Disposition": "attachment;filename=history.csv"})


if __name__ == "__main__":
    app.run(debug=True)