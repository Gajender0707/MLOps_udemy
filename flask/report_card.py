from flask import Flask,render_template,redirect,request,url_for

app=Flask(__name__)


# @app.route("/show_data",methods=["GET","POST"])
# def show_data():

#     return render_template("show_data.html")

@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        science=request.form["science"]
        maths=request.form["maths"]
        c=request.form["c"]
        data_science=request.form["datascience"]
        student_data={
            "science":science,
            "maths":maths,
            "c":c,
            "data_science":data_science
        }
        return redirect(url_for("home",data=student_data))
    return render_template("student_data.html")

if __name__=="__main__":
    app.run(debug=True)