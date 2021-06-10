from flask import Flask, render_template, request

app = Flask(__name__)

list1 = []
checked = []
@app.route('/', methods=["GET","POST"])
def index():
    if request.method == 'POST':
        note = request.form.get("note")
        list1.append(note)
    return render_template("home.html", notes=list1, marked=checked)


if __name__ == '__main__':
    app.run(debug=True)