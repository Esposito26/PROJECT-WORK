from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Funzione per inizializzare il database
def init_db():
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pdf_utility TEXT,
            liked_part TEXT,
            improvement TEXT,
            pdf_errors TEXT,
            error_details TEXT,
            web_navigation TEXT,
            info_found TEXT,
            info_searched TEXT,
            web_design TEXT,
            web_suggestions TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    # Rendi la pagina index.html (anziché feedback.html)
    return render_template('index.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    pdf_utility = request.form.get('pdfUtility')
    liked_part = request.form.get('likedPart')
    improvement = request.form.get('improvement')
    pdf_errors = request.form.get('pdfErrors')
    error_details = request.form.get('errorDetails')
    web_navigation = request.form.get('webNavigation')
    info_found = request.form.get('infoFound')
    info_searched = request.form.get('infoSearched')
    web_design = request.form.get('webDesign')
    web_suggestions = request.form.get('webSuggestions')

    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO feedback (pdf_utility, liked_part, improvement, pdf_errors, error_details,
                              web_navigation, info_found, info_searched, web_design, web_suggestions)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (pdf_utility, liked_part, improvement, pdf_errors, error_details,
          web_navigation, info_found, info_searched, web_design, web_suggestions))
    conn.commit()
    conn.close()

    return redirect(url_for('home'))

@app.route('/view_feedback')
def view_feedback():
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM feedback')
    feedbacks = cursor.fetchall()
    conn.close()
    return render_template('view_feedback.html', feedbacks=feedbacks)

if __name__ == '__main__':
    init_db()  # Inizializza il database al primo avvio
    app.run(debug=True)
