from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def show_form():
    return render_template('fortune_form.html')

@app.route('/fortune_results', methods=['GET'])
def show_results():
    name = request.args.get('name')
    chara = request.args.get('chara')
    favebluelion = request.args.get('Fave Blue Lion')
    sc6character = request.args.get('sc6character')
    print("Test Chara")
    print(chara)
    if chara == "Seliph":
        return render_template('seliph.html')
    if chara == "Dimitri":
        return render_template('dimitri.html')
    if chara == "Groh":
        return render_template('groh.html')
    if chara == "Fuyumi":
        return render_template('fuyumi.html')
    if chara == "Minerva":
        return render_template('minerva.html')
    if chara == "Reiko":
        return render_template('reiko.html')


if __name__ == '__main__':
    app.run()
