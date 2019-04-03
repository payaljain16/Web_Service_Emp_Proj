from flask import Flask, jsonify,request;
import pickle;
from employees import *;

app=Flask(__name__);

@app.route("/", methods=['GET'])
def displayAllRecords():
    f2=open("empppp.ser","rb");
    p1=pickle.load(f2);
    result = [];
    for e in p1:
        result.append({'Name':e.name, 'Age':e.age,'Salary':e.salary,'Designation':e.desig});
    return jsonify(result);
##    print("\n Name : ",p1.name);
##    print("Age :",p1.age);
##    print("Salary :",p1.salary);
##    print("Designation : ",p1.desig);
    #return jsonify({"Name : ":p1.name,"Age : ":p1.age,"Salary : ":p1.salary,"Designation : ":p1.desig});

@app.route("/<string:num>", methods=['GET'])
def displayByName(num):
    f2=open("empppp.ser","rb");
    res="Not found.";
    p1=pickle.load(f2);
    for e in p1:
        if e.name == num:
            res={'Name':e.name, 'Age':e.age,'Salary':e.salary,'Designation':e.desig}
    return jsonify(res);

@app.route("/raise", methods=['GET'])
def raiseSalary():
    f2=open("empppp.ser","rb");
    a1=pickle.load(f2);
    f2.close();
    f1=open("empppp.ser","wb");
    for e in a1:
        EmpRaiseSalary.incr(e);
    pickle.dump(a1,f1);
    f1.close();
    f3=open("empppp.ser","rb");
    p1=pickle.load(f3);
    result = [];
    for e in p1:
        result.append({'Name':e.name, 'Age':e.age,'Salary':e.salary,'Designation':e.desig});
        f3.close();
    return jsonify(result);
    

if __name__ == '__main__':
    app.run(debug=True);
