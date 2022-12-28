import flask 
from flask import request
import DB
import Categories
import Items



class StartPoint():
    __app = flask.Flask(__name__)

    @classmethod
    @__app.route("/")
    def Home():
        return flask.render_template("Home.html")

    @classmethod
    @__app.route("/categories")
    def categories():
        return flask.render_template("Categories.html", myCategories = Categories.Categories.GetAllCategories())
    
    
    @classmethod
    @__app.route("/Items")
    def items():
        return flask.render_template("Items.html", myItems= Items.Items.GetAllItems())


    @classmethod
    def Start(cls):
         cls.__app.run(debug=True)

    @classmethod
    @__app.route("/categories/add", methods = ['POST', 'GET'])
    @__app.route("/categories/edit/<id>", methods = ['POST', 'GET'])
    def AddCategory(id: int = None):
        theRequest = flask.request
        if id == None: # Add
            if theRequest.method == 'POST':
                s = Categories.Categories()
                s.Name = theRequest.form['Name']
                s.Save()
                return flask.redirect("/categories")
                
            else:
                return flask.render_template( 'CtgData.html', s = None)
        else: # Edit
            if request.method == "POST":
                s = Categories.Categories(id)
                s.Name = theRequest.form['Name']
                s.Save()
                return flask.redirect("/categories")
            else:
                s1 = Categories.Categories.GetAllCategories(id = id)[0]
                return flask.render_template("CtgData.html", s = s1)

    @classmethod
    @__app.route("/items/add", methods = ['POST', 'GET'])
    @__app.route("/items/edit/<id>", methods = ['POST', 'GET'])
    def AddItem(id: int = None):
        theRequest = flask.request
        if id == None: # Add
            if theRequest.method == 'POST':
                s = Items.Items()
                s.itmName = theRequest.form['itmName']
                s.itmPrice= theRequest.form['itmPrice']
                s.Saveitm()
                return flask.redirect("/Items")
                
            else:
                return flask.render_template( 'Itemdata.html', s = None)
        else: # Edit
            if request.method == "POST":
                s = Items.Items(id)
                s.itmName = theRequest.form['itmName']
                s.itmPrice = theRequest.form['itmPrice']
                s.Saveitm()
                return flask.redirect("/Items")
            else:
                s1 = Items.Items.GetAllItems(id = id)[0]
                return flask.render_template("Itemdata.html", s = s1)
                

    @classmethod
    
    @__app.route("/items/delete/<id>", methods = ['POST', 'GET'])
    def DeleteItem(id: int = None):
        theRequest = flask.request
        if request.method == "POST":
                s = Items.Items(id)
                s.itmName = theRequest.form['itmName']
                s.itmPrice = theRequest.form['itmPrice']
                s.Deleteitm()
                return flask.redirect("/Items")
        else:
                s1 = Items.Items.GetAllItems(id = id)[0]
                return flask.render_template("deleteitem.html", s = s1)
                
    @classmethod
    @__app.route("/categories/delete/<id>", methods = ['POST', 'GET'])
    def Deletecat(id: int = None):
        theRequest = flask.request
        if request.method == "POST":
                s = Categories.Categories(id)
                s.Name = theRequest.form['Name']
                s.Deletectg()
                return flask.redirect("/categories")
        else:
                s1 = Categories.Categories.GetAllCategories(id = id)[0]
                return flask.render_template("deletectg.html", s = s1)        
        


if __name__ == "__main__": 
    StartPoint.Start()