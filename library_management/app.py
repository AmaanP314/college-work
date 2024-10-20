from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'your username', 
    'password': 'your password',  
    'database': 'library'  
}

@app.route('/')
def index():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT id, title, author, year FROM books")
    books = cursor.fetchall()
    cursor.close()
    connection.close()

    return render_template('index.html', books=books)


@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']

        # Insert into database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO books (title, author, year) VALUES (%s, %s, %s)", (title, author, year))
        connection.commit()
        cursor.close()
        connection.close()

        return redirect(url_for('index'))

    return render_template('insert.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        book_id = request.form['book_id']

        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
        connection.commit()
        cursor.close()
        connection.close()

        return redirect(url_for('index'))

    return render_template('delete.html')

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        book_id = request.form['book_id']
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']

        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("UPDATE books SET title = %s, author = %s, year = %s WHERE id = %s", (title, author, year, book_id))
        connection.commit()
        cursor.close()
        connection.close()

        return redirect(url_for('index'))

    return render_template('update.html')

if __name__ == '__main__':
    app.run(debug=True)