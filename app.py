from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def show_form():
    return render_template('fortune_form.html')

@app.route('/fortune_results')
def show_results():
    name = request.args.get('name')
    chara = request.args.get('chara')
    favebluelion = request.args.get('Fave Blue Lion')
    sc6character = request.args.get('sc6character')
    if chara == "Seliph":
        print("~Seliph's Fortune~")
        print("You follow the shadows of those before you, and constantly worry")
        print("about whether you'll be able to live up to the greatness of others.")
    return render_template('results.html')



if __name__ == '__main__':
    app.run()
