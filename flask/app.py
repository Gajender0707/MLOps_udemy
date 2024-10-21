from flask import Flask,render_template,redirect,request,url_for

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        name=request.form["name"]
        return name
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/dishes")
def dishes():
    return render_template("dishes.html")

@app.route("/score/<marks>")
def score(marks):
    if int(marks)>33:
        return redirect(url_for("dishes"))
    if int(marks)<10:
        return redirect(url_for("about"))
    return render_template("score.html",marks=marks)






if __name__=="__main__":
    app.run(debug=True)