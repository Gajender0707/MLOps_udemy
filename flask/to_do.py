from flask import Flask,redirect,render_template,request,jsonify


app=Flask(__name__)

## here making the json data 
todo_items=[
    {"id":1,"name":"ml","description":"this is the todo for ml"},
    {"id":2,"name":"ds","description":"this is the todo for ds"}
]

@app.route('/')
def home():
    return "Hy welcome to the home page"

@app.route("/items",methods=["GET"])
def get_items():
    return jsonify(todo_items)

@app.route("/items/<int:item_id>",methods=["GET"])
def get_item(item_id):
    item=None
    for i in todo_items:
        if i["id"]==item_id:
            item=i
    return jsonify(item)


@app.get("/check")
def check():
    return todo_items






if __name__=="__main__":
    app.run(debug=True)