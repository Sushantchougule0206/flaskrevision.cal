from flask import Flask,request

# app is an object & Flask is an class name 
app=Flask(__name__) 

@app.route('/')
def welcome(): # this is a method
    return "welcome to the Flask"

@app.route('/cal',methods=["GET"])
def math_operation():
     operation=str(request.json['operation'])
     num1=int(request.json['num1'])
     num2=int(request.json['num2'])
        
     if operation=="add":
        result=num1+num2
     elif operation=="multiply":
        result=num1*num2
     elif operation=="division":
        result=num1/num2
     else:
        result=num1-num2

     return "{} of num1,num2 is {}".format(operation,result)
    
       

if __name__=='__main__':
    app.run(debug=True)