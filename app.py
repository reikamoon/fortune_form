from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def show_form():
    return render_template('index.html')

@app.route('/fortune_results')
def show_results():
    return render_template('results.html')



if __name__ == '__main__':
    app.run()
