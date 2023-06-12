from flask import Flask, render_template, redirect, request, flash, jsonify
from flask_mysqldb import MySQL
from datetime import datetime
from collections import defaultdict
app = Flask(__name__)


app.secret_key = "caircocoders-ednalan"
       
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'work'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


@app.route('/base')
def base():
     return render_template('base.html')

   
    
@app.route('/product')
def product():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM product ORDER BY id")
    product = cur.fetchall()
    return render_template('product.html', product=product)


@app.route("/product/ajax_add",methods=["POST","GET"])
def product_ajax_add():
    cur = mysql.connection.cursor() 
    if request.method == 'POST':
        txtname = request.form['txtname']
        txtdate = request.form['txtdate']
        print(txtname)
        if txtname == '':
            msg = 'Please Input name'  
        elif txtdate == '':
           msg = 'Please Input Date'  
        else:     
            cur.execute("INSERT INTO product (productName,date) VALUES (%s,%s)",[txtname,txtdate])
            mysql.connection.commit()       
            cur.close()
            msg = 'New record created successfully'   
    return jsonify(msg) 
    


@app.route("/product/ajax_update",methods=["POST","GET"])
def product_ajax_update():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        string = request.form['string']
        txtname = request.form['txtname']
        txtdate = request.form['txtdate']
        
        print(string)
        cur.execute("UPDATE product SET productName = %s, date = %s WHERE id = %s ", [txtname, txtdate, string])
        mysql.connection.commit()       
        cur.close()
        msg = 'Record successfully Updated'   
    return jsonify(msg)  




@app.route("/product/ajax_delete",methods=["POST","GET"])
def product_ajax_delete():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        getid = request.form['string']
        print(getid)
        cur.execute('DELETE FROM product WHERE id = {0}'.format(getid))
        mysql.connection.commit()       
        cur.close()
        msg = 'Record deleted successfully'   
    return jsonify(msg)



@app.route('/location')
def location():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM location ORDER BY id")
    location = cur.fetchall()
    return render_template('location.html', location=location)


@app.route("/location/ajax_add",methods=["POST","GET"])
def location_ajax_add():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        txtname = request.form['txtname']
        txtdate = request.form['txtdate']
        print(txtname)
        if txtname == '':
            msg = 'Please Input name'  
        elif txtdate == '':
           msg = 'Please Input Date'  
        else:     
            cur.execute("INSERT INTO location (locationName,Date) VALUES (%s,%s)",[txtname,txtdate])
            mysql.connection.commit()       
            cur.close()
            msg = 'New record created successfully'   
    return jsonify(msg) 
    


@app.route("/location/ajax_update",methods=["POST","GET"])
def location_ajax_update():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        string = request.form['string']
        txtname = request.form['txtname']
        txtdate = request.form['txtdate']
        print(string)
        cur.execute("UPDATE location SET locationName = %s, Date = %s WHERE id = %s ", [txtname, txtdate, string])
        mysql.connection.commit()       
        cur.close()
        msg = 'Record successfully Updated'   
    return jsonify(msg)  




@app.route("/location/ajax_delete",methods=["POST","GET"])
def location_ajax_delete():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        getid = request.form['string']
        print(getid)
        cur.execute('DELETE FROM location WHERE id = {0}'.format(getid))
        mysql.connection.commit()       
        cur.close()
        msg = 'Record deleted successfully'   
    return jsonify(msg)



@app.route('/movements')
def mov():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM product ORDER BY id")
    product = cur.fetchall()
    result1 = cur.execute("SELECT * FROM location ORDER BY id")
    location = cur.fetchall()
    result = cur.execute("SELECT * FROM movements ORDER BY id")
    movements = cur.fetchall()
    return render_template('movement.html', movements=movements, products=product, locations=location)


@app.route("/delete-mov/<int:id>")
def deleteMovement(id):
    cur = mysql.connection.cursor()
    getid = id
    print(getid)
    cur.execute('DELETE FROM movements WHERE id = {0}'.format(getid))
    mysql.connection.commit()       
    cur.close()
    return redirect("/movements")


@app.route('/report')
def report():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM movements ORDER BY pid")
    movements = cur.fetchall()
    balancedDict = defaultdict(lambda: defaultdict(dict))
    tempProduct = ''
    cur.execute("SELECT * FROM product ORDER BY id")
    product = cur.fetchall()
    cur.execute("SELECT * FROM location ORDER BY id")
    location = cur.fetchall()
    for mov in movements:
        row = mov
        if(tempProduct == row['pid']):
            if(row['toLocation'] and not "qty" in balancedDict[row['pid']][row['toLocation']]):
                balancedDict[row['pid']][row['toLocation']]["qty"] = 0
            elif (row['fromLocation'] and not "qty" in balancedDict[row['pid']][row['fromLocation']]):
                balancedDict[row['pid']][row['fromLocation']]["qty"] = 0
            if (row['toLocation'] and "qty" in balancedDict[row['pid']][row['toLocation']]):
                balancedDict[row['pid']][row['toLocation']]["qty"] += row['Quantity']
            if (row['fromLocation'] and "qty" in balancedDict[row['pid']][row['fromLocation']]):
                balancedDict[row['pid']][row['fromLocation']]["qty"] -= row['Quantity']
            pass
        else :
            tempProduct = row['pid']
            if(row['toLocation'] ):
                    balancedDict[row['pid']][row['toLocation']]["qty"] =row['Quantity']

    return render_template('report.html',  movements=balancedDict ,products=product, locations=location)


@app.route('/index2')
def index2():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM product ORDER BY id")
    product = cur.fetchall()
    result1 = cur.execute("SELECT * FROM location ORDER BY id")
    location = cur.fetchall()
    return render_template('index2.html', products=product, locations=location)


@app.route('/movement',methods=["POST"])
def newm():
     cur = mysql.connection.cursor()
     if request.method == 'POST':
        txtname =  request.form["productId"]
        txtFrom =  request.form["fromLocation"]
        txtTo =  request.form["toLocation"]
        txtquantity= request.form['qty']
        date = datetime.now()
        print(txtFrom )
        print(txtTo )
        if txtFrom == '':
            cur.execute("INSERT INTO movements (pid,Quantity,toLocation,time) VALUES (%s,%s,%s ,%s)",[txtname,txtquantity,txtTo,str(date)])
        elif txtTo == '':
            cur.execute("INSERT INTO movements (pid,Quantity,fromLocation,time) VALUES (%s,%s,%s ,%s)",[txtname,txtquantity,txtFrom,str(date)])
        else:
           cur.execute("INSERT INTO movements (pid,Quantity,fromLocation,toLocation,time) VALUES (%s,%s,%s,%s ,%s)",[txtname,txtquantity,txtFrom, txtTo,str(date)])
        mysql.connection.commit()       
        cur.close() 
        return redirect("/index2")


@app.route('/editmovemen')
def emov():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM product ORDER BY id")
    product = cur.fetchall()
    result1 = cur.execute("SELECT * FROM location ORDER BY id")
    location = cur.fetchall()
    return render_template('edit.html', products=product, locations=location)



@app.route('/editmovemen',methods=["POST"])
def editm():
    
    if request.method == 'POST':
        id =  request.form["mid"]
        date =  request.form["time"]
        txtname =  request.form["productId"]
        txtFrom =  request.form["fromLocation"]
        txtTo =  request.form["toLocation"]
        txtquantity= request.form['qty']
        print(txtFrom )
        print(txtTo )
        cur = mysql.connection.cursor()
        if txtFrom == '':
           cur.execute("UPDATE movements SET pid = %s, Quantity = %s ,  toLocation = %s ,time= %s WHERE id = %s ", [txtname,txtquantity, txtTo,date,id])
        elif txtTo == '':
            cur.execute("UPDATE movements SET pid = %s, Quantity = %s , fromLocation = %s ,time= %s WHERE id = %s ", [txtname,txtquantity, txtFrom,date,id])
        else :
           cur.execute("UPDATE movements SET pid = %s, Quantity = %s , fromLocation = %s, toLocation = %s ,time= %s WHERE id = %s ", [txtname,txtquantity, txtFrom, txtTo,date,id])
        mysql.connection.commit()       
        cur.close()
        return redirect('/editmovemen')  
    










