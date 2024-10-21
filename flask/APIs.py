from flask import Flask,redirect,render_template,request,jsonify


app=Flask(__name__)

## here making the json data 
todo_items=[
    {"id":1,"name":"ml","description":"this is the todo for ml"},
    {"id":2,"name":"ds","description":"this is the todo for ds"}
]


## this is for the home page 
@app.get('/')
def home():
    return "Hy welcome to the home page"

##this  is for the getting the all store items...
@app.get("/get-items")
def get_items():
    return jsonify(todo_items)



# this is for the getting the item using a perticular key like: id..
@app.get("/get-item/<int:item_id>")
def get_item(item_id):
    for item in todo_items:
        if item["id"]==item_id:
            return item
        
    return {"message":"Record Doesn't exist...."}




#this is for the adding the item.....
@app.post("/add-item")
def add_item():
    new_item=request.get_json()
    print(new_item)
    todo_items.append(new_item)
    return {"message":"new data added successfully......"}, 201



##this is for the upadating the items...
@app.put("/update-item")
def update_item():
    request_data=request.get_json()
    for item in todo_items:
        if item["id"]==request_data["id"]:
            item["name"]=request_data["name"]
            item["description"]=request_data["description"]
            return {"message":"item updated Sucessfully.."}
    return {"message":"item doesn't found...."}, 404



# this is for the Deleteing api
@app.delete("/delete-item/<int:id>")
def delete_item(id):
    for item in todo_items:
        if item["id"]==id:
            todo_items.remove(item)
            return {"message":"item deleted Sucessfully...."}
        
    return {"message":"Record doesn't found "}, 404





if __name__=="__main__":
    app.run(debug=True)