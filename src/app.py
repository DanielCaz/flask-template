from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title='Home')


@app.route('/results', methods=['POST'])
def results():
    try:
        file = request.files.get('file')
        if not file:
            return f'No file provided. {request.form.keys()}', 400

        file_contents = file.read().decode('utf-8')

        return render_template('results.html', title='Results', file_contents=file_contents)
    except UnicodeDecodeError as e:
        return f'Error reading file: {e}', 400
    except Exception as e:
        return f'Internal Server Error: {e}', 500
