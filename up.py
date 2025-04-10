from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        return f"Terima kasih, {name}! Email kamu adalah {email}."
    return '''
        <form method="POST">
            Nama: <input type="text" name="name"><br>
            Email: <input type="email" name="email"><br>
            <input type="submit" value="Kirim">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
