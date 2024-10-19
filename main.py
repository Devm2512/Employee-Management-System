import streamlit as st
import mysql.connector
import pandas as pd
import datetime
st.title('Welcome to HRMS')
st.write('Hello, This is a training project by Dewang Moghe')
choice = st.sidebar.selectbox("Menu",("Home","Employee login","Administrator",'Holiday Calender'))
if (choice=="Home"):
    st.image('https://snacknation.com/wp-content/uploads/2022/12/Employee-Management-Software-e1670371925164.png')
    st.header('Welcome')
    st.write('Hello, This is a training project by Dewang Moghe')
elif(choice=="Employee login"):
    st.image('https://www.phppayroll.com/wp-content/uploads/employee-management-system.jpg')
    if 'login' not in st.session_state:
        st.session_state['login']=False
    Employee_id = st.text_input("Enter Employee ID")
    Password  = st.text_input("Enter Password")
    btn = st.button("Login")
    if btn:
        mydb = mysql.connector.connect(host="localhost",user="root",password="Dev@2512",database="employee")
        c = mydb.cursor()
        c.execute("select * from pro_info")
        for r in c:
            if(r[0]==Employee_id and r[1]==Password):
                st.session_state['login']=True
                break
        if st.session_state['login']==False:
            st.subheader("Incorrect Id or Password")
    if st.session_state['login']==True:
         st.subheader("Login Successful")
         choice2 = st.sidebar.selectbox('Features',('None','Sign In attendenace','Sign Out attendance','View all Employee','Leave reuest','Raise a Query'))
         if (choice2 == 'Sign In attendenace'):
             date = str(datetime.datetime.now())
             no_id = st.text_input('Enter employee id')
             btn10 = st.button("Sign In")
             if btn10:
                 mydb = mysql.connector.connect(host="localhost",user="root",password="Dev@2512",database="employee")
                 c = mydb.cursor()
                 c.execute("insert into SignInOutRecord values(%s,%s)",(no_id,date))
                 mydb.commit()
         elif (choice2 == 'Sign Out attendance'):
             date = str(datetime.datetime.now())
             noid = st.text_input('Please enter employee id')
             btn11 = st.button("Sign Out")
             if btn11:
                 mydb = mysql.connector.connect(host="localhost",user="root",password="Dev@2512",database="employee")
                 c = mydb.cursor()
                 c.execute("insert into SignOutRecord values(%s,%s)",(noid,date))
                 mydb.commit()
         elif(choice2 =="View all Employee"):
             mydb = mysql.connector.connect(host="localhost",user="root",password="Dev@2512",database="employee")
             c = mydb.cursor()
             c.execute("select * from pro_info")
             l=[]
             for r in c:
                 l.append(r)
             df = pd.DataFrame(data=l,columns=['empid','Designation','salary','department','manager'])
             st.dataframe(df)
         elif(choice2=='Leave reuest'):
             name = st.text_input('Enter Employees name')
             Leave = st.text_input('Enter the number of leaves')
             typo = st.selectbox('Select',('Sick','Personal','Maternal','Short Leave'))
             btn2 = st.button('Send Request')
             if(btn2):
                 mydb = mysql.connector.connect(host="localhost",user="root",password="Dev@2512",database="employee")
                 c = mydb.cursor()
                 c.execute("insert into Persons values(%s,%s,%s)",(name,Leave,typo))
                 mydb.commit()
         elif(choice2 == 'Raise a Query'):
             emp_id = st.text_input('Enter Employees ID ')
             name = st.text_input('Enter Employees Name ')
             Designation = st.text_input('Enter Designation ')
             Category = st.selectbox('Select',('Admin','Finance and Accounts','Human Resources','IT'))
             if Category == 'Admin':
                 SubCategory = st.selectbox('Select',('Admin Openings','Opening a Bank Account','ID card lost and New ID Cards','Hygiene','Courier'))
                 Query = st.text_input('Write the Query')
                 btn20 = st.button('Send Query')
                 if btn20:
                     mydb = mysql.connector.connect(host="localhost",user="root",password="Dev@2512",database="employee")
                     c = mydb.cursor()
                     c.execute("insert into Admin_Query values(%s,%s,%s,%s,%s,%s)",(emp_id,name,Designation,Category,SubCategory,Query))
                     mydb.commit()
             elif Category == 'Finance and Accounts':
                 SubCategory = st.selectbox('Select',('Income tax related Issues','Reimbursement related queries','Salary Related Queries'))
                 Query = st.text_input('Write the Query')
                 btn21 = st.button('Send Query')
                 if btn21:
                     mydb = mysql.connector.connect(host="localhost",user="root",password="Dev@2512",database="employee")
                     c = mydb.cursor()
                     c.execute("insert into Finanace_Query values(%s,%s,%s,%s,%s,%s)",(emp_id,name,Designation,Category,SubCategory,Query))
                     mydb.commit()
             elif Category == 'Human Resources':
                 SubCategory = st.selectbox('Select',('Attendance Query','General Query','HRMS','Leave Related Queries','Medical Insurance Query','Payroll Query'))
                 Query = st.text_input('Write the Query')
                 btn22 = st.button('Send Query')
                 if btn22:
                     mydb = mysql.connector.connect(host="localhost",user="root",password="Dev@2512",database="employee")
                     c = mydb.cursor()
                     c.execute("insert into HR_Query values(%s,%s,%s,%s,%s,%s)",(emp_id,name,Designation,Category,SubCategory,Query))
                     mydb.commit()
             elif Category == 'IT':
                 SubCategory = st.selectbox('Select',('Email Related issues','Hardware','Internet related issues','New software Installation','others'))
                 Query = st.text_input('Write the Query')
                 btn23 = st.button('Send Query')
                 if btn23:
                     mydb = mysql.connector.connect(host="localhost",user="root",password="Dev@2512",database="employee")
                     c = mydb.cursor()
                     c.execute("insert into IT_Query values(%s,%s,%s,%s,%s,%s)",(emp_id,name,Designation,Category,SubCategory,Query))
                     mydb.commit()
elif(choice=="Administrator"):
    if 'Admin Login' not in st.session_state:
        st.session_state['Admin Login']=False
    Admin_id = st.text_input("Enter Admin ID")
    Admin_Pass  = st.text_input("Enter Admin Password")
    btn3 = st.button("Admin Login")
    if btn3:
        mydb = mysql.connector.connect(host="localhost",user="root",password="Dev@2512",database="employee")
        c = mydb.cursor()
        c.execute("select * from pro_info")
        for r in c:
            if(r[0]==Admin_id and r[1]==Admin_Pass):
                st.session_state['Admin Login']=True
                break
        if st.session_state['Admin Login']==False:
            st.subheader("Incorrect Id or Password")
    if st.session_state['Admin Login']==True:
         st.subheader("Admin Login Successful")
         choice3 = st.selectbox('Features',('Select ','View Personal Information','Add New Employee'))
         if(choice3 =="View Personal Information"):
             mydb = mysql.connector.connect(host="localhost",user="root",password="Dev@2512",database="employee")
             c = mydb.cursor()
             c.execute("select * from personal_info")
             l1=[]
             for r1 in c:
                 l1.append(r1)
             df = pd.DataFrame(data=l1,columns=['Name','Age','Gender','Phone_Number','Address','Emp_id','date of birth'])
             st.dataframe(df)
         elif(choice3=='Add New Employee'):
              id_emp = st.text_input('Enter the ID of the Employee')
              Emp_name = st.text_input('Enter Employees Name')
              Emp_age = st.text_input('Enter the Age of Employee')
              Emp_gender = st.text_input('Enter the Gender of Employee')
              Emp_phone = st.text_input('Enter the Phone number')
              Emp_Address = st.text_input('Enter the Address')
              Emp_designation = st.text_input('Enter the Designation')
              Emp_salary = st.text_input('Enter the salary of the employee')
              Emp_department = st.text_input('Enter the department')
              Emp_manager = st.text_input('Enter the name of the manager for the employee ')
              btn4 = st.button('Add Employee')
              if(btn4):
                  mydb = mysql.connector.connect(host="localhost",user="root",password="Dev@2512",database="employee")
                  c = mydb.cursor()
                  c.execute("insert into personal_info values(%s,%s,%s,%s,%s,%s)",(id_emp, Emp_name, Emp_age,Emp_gender, Emp_phone,Emp_Address))
                  c.execute("insert into pro_info values(%s,%s,%s,%s,%s)",(id_emp,Emp_designation, Emp_salary, Emp_department,Emp_manager ))
                  mydb.commit()
              if st.session_state['Admin Login']==True:
                  st.subheader("Employee Added Successful")
    st.video('https://www.youtube.com/watch?v=_grpOkkd8p8')
elif(choice=='Holiday Calender'):
    mydb = mysql.connector.connect(host="localhost",user="root",password="Dev@2512",database="employee")
    c = mydb.cursor()
    c.execute("select * from Holiday_Calendar")
    l1 = []
    for r in c:
        l1.append(r)
    df1 = pd.DataFrame(data=l1,columns=['Date','Day','Name'])
    st.dataframe(df1)
