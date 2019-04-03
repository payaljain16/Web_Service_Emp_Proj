from employees import *;
import pickle;
import os.path;
import requests;

def main():
    empl=[];
    url="http://localhost:5000";
    result = requests.get(url).json();
    print(result);
    
    url2="http://localhost:5000/clerk45";
    result2 = requests.get(url2).json();
    print(result2);

    url3="http://localhost:5000/raise";
    result3 = requests.get(url3).json();
    print(result3);
    
    if os.path.exists("empppp.ser"):
        f2= open("empppp.ser","rb");
        empl=pickle.load(f2);
    else:
        empl=[];
    while True:
        print("--------------");
        print("1. CREATE");
        print("2. DISPLAY");
        print("3. RAISE SALARY");
        print("4. EXIT");
        print("-------------");
        ch1=int(input("Enter choice : "));
        if(ch1==1):
            while True:
                print("--------------");
                print("1. CLERK");
                print("2. programmer");
                print("3. MANAGER");
                print("4. EXIT");
                print("-------------");
                ch2=int(input("Enter choice : "));
                if ch2==1:
                    empl.append(Clerk());
                if ch2==2:
                    empl.append(Programmer());
                if ch2==3:
                    empl.append(Manager());
                if ch2==4:
                    break;
        if ch1==2:
            for obj in empl:
                obj.displayEmp();

        if ch1==3:
            for obj in empl:
                EmpRaiseSalary.incr(obj);

        if ch1==4:
            f1=open("empppp.ser","wb");
            pickle.dump(empl,f1);
            f1.close();
            print("Total no of employees: ",Emp.count);
            break;

                
