class Emp:
    count=0;
    def __init__(self,salary,desig):
        self.name=input("Enter your name:- ");
        self.age=input("Enter your age:- ");
        self.salary=salary;
        self.desig=desig;
        f1=open("empp.txt","a");
        f1.write(self.name+"|"+str(self.age)+"|"+str(self.salary)+"|"+self.desig+"\n");
        f1.close();
        Emp.count+=1;
               
    @staticmethod
    def display():
        f2=open("empp.txt","r");
        for record in f2:
            rec=record.split("|");
            print("\n Name : ",rec[0]);
            print("Age :",rec[1]);
            print("Salary :",rec[2]);
            print("Designation : ",rec[3]);


    def displayEmp(self):
        print("\n Name : ",self.name);
        print("Age : ",self.age);
        print("Salary : ",self.salary);
        print("Designation : ",self.desig);

    def __str__(self):
        print("\n Name : ",self.name);
        print("Age :",self.age);
        print("Salary :",self.salary);
        print("Designation : ",self.desig);


    

class Clerk(Emp):
    def __init__(self):
        super().__init__(8000,"Clerk");

    def raiseSalary(self):
        self.salary+=2000;
    
        
class Programmer(Emp):
    def __init__(self):
        super().__init__(25000,"Programmer");

    def raiseSalary(self):
        self.salary+=5000;
        
class Manager(Emp):
    def __init__(self):
        super().__init__(80000,"Manager");

    def raiseSalary(self):
        self.salary+=10000;

class EmpRaiseSalary:  #ducktyping
    @staticmethod
    def incr(obj):
        obj.raiseSalary();

           

