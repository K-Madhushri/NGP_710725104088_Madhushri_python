def display():
    print("Welcome to python");
display();
print("Temp statement");
display();

def StudentInfo(rollno,stname,rank):
    print("Roll no:",rollno);
    print("Name:",stname);
    print("Rank:",rank);
StudentInfo(stname="abc",rank=1,rollno="st-1")

def employeeData(empid,empname,salary=30000.00):
    print("Employee ID",empid);
    print("Employee Name",empname);
    print("Salary:",salary);
employeeData("emp-1","abc",40000.00)

def data(*lst):
    print(lst);
data(10,20);
data(30,40,50,60);

def college_info(**info):
    print(info);
college_info(clg_name="NGP",Department="CSE");

def calc():
    return 10+20;
res1=calc();
print(res1);

def bookInfo():
    return "B-1","Complete reference of python",1500.00;
bookid,bookname,price=bookInfo();
print(bookid);
print(bookname);
print(price);