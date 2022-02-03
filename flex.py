from flask import Flask, render_template, request, flash
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html", title="Main", menu=menu)
@app.route("/about")
def about():
    return render_template("test.html", title="О сайте", menu=menu)
menu = [{"name": "Установка", "url": "install-flask"},
        {"name": "Первое приложение", "url": "first-app"},
        {"name": "Обратная связь", "url": "contact"}]
@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        answer = request.form.to_dict()
        print(answer)

if __name__=="__main__":
    app.run(debug=True)