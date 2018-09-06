
# coding: utf-8

# In[11]:


import time
import numpy as np
import pandas as pd
import speech_recognition as sr

rlno=[]
name=[]
dob=[]
stream=[]
year=[]
grade=[]


# In[12]:


def speechip():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        print("You said: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return
    speech=r.recognize_google(audio)
    return speech


# In[13]:


def options():
    #ch=input("Enter into operation(y/Y or n/N): ")
    print('speak "YES" to continue "NO" to discontinue')
    ch=speechip()
    while(ch=='yes' or ch=='YES'):
        #v=int(input("Enter your Action:"))
        print('speak:Action-1: Create Database \nAction-2. Modify Database \nAction-3. Delete Database')
        v=speechip()
        if v=="Create Database" or v=="create database":
            createDatabase()
        elif v=="Modify Database" or v=="modify database":
            modifyDatabase()
        elif v=="Delete Database" or v=="delete database":
            deleteDatabase()        
        else:
            exit(0)
        #ch=input("Continue?(y/Y or n/N): ")
        print('Continue? speak "YES" or"NO"')
        ch=speechip()


# In[14]:


def modifyDatabase():
    print("1. Entire Modification \n2. Partial Modification \n3. Exit \n:")
    #ch1=int(input("Enter Choice:"))
    print('speak your choice:')
    ch1=speechip()
    if ch1==1:
        entireModify()
        #options()
    elif ch1==2:
        partialModify()
        options()
    else:
        options()


# In[15]:


def insertdata(rlno,name,dob,stream,year,grade):
    #Creating database
    filedf=pd.DataFrame({
        'UNIVERSITY ROLL NUMBER': rlno,
        'NAME': name,
        'D.O.B': dob,
        'STREAM': stream,
        'YEAR': year,
        'GRADE': grade
     })
    #print(filedf)
    filedf.to_csv("C:/Users/Subhadeep Chakrabort/Desktop/Student's Database management using Speech recognition/DataSheet1.csv")
    return


# In[16]:


def createDatabase():
    #ch=input("Insert data?(y/Y or n/N): ")
    print('Insert data: speak YES or NO')
    ch=speechip()
    while(ch=='yes' or ch=='YES'):
        print("Speak UNIVERSITY ROLL NUMBER: ")
        rl=speechip()
        rlno.append(rl)
        print("Speak Name: ")
        nm=speechip()
        name.append(nm)
        print("Speak Date of Birth: ")
        db=speechip()
        dob.append(db)
        print("Speak Stream: ")
        st=speechip()
        stream.append(st)
        print("Speak Year: ")
        yr=speechip()
        year.append(yr)
        print("Speak Grade: ")
        gd=speechip()
        grade.append(gd)
        
        insertdata(rlno,name,dob,stream,year,grade)
        #ch=input("Continue?(y/Y or n/N): ")
        print('Continue: speak YES or NO')
        ch=speechip()
        options()


# In[17]:


def entireModify():
    #n=input("Enter UNIVERSITY ROLL NUMBER to Modify respective database:")
    print('Enter UNIVERSITY ROLL NUMBER to Modify respective database:')
    n=speechip()
    file=pd.read_csv("C:/Users/Subhadeep Chakrabort/Desktop/Student's Database management using Speech recognition/DataSheet1.csv")
    namear=np.array(file['UNIVERSITY ROLL NUMBER'].tolist())
    namear.flatten()
    namelist=namear.tolist()
    ind=namelist.index(n)
    
    #modpt=file.ix[nameind]
    #modlist=modpt.tolist()
    #Process
    #ch=input("Insert data?(y/Y or n/N): ")
    print('Insert data:speak YES or NO') 
    ch=speechip()
    while(ch=='yes' or ch=='YES'):
        print("Speak UNIVERSITY ROLL NUMBER: ")
        rl=speechip()
        rlno[ind]=rl
        print("Speak Name: ")
        nm=speechip()
        name[ind]=nm
        print("Speak Date of Birth: ")
        db=speechip()
        dob[ind]=db
        print("Speak Stream: ")
        st=speechip()
        stream[ind]=st
        print("Speak Year: ")
        yr=speechip()
        year[ind]=yr
        print("Speak Grade: ")
        gd=speechip()
        grade[ind]=gd
        
        insertdata(rlno,name,dob,stream,year,grade)
        #ch=input("Continue?(y/Y or n/N): ")
        print('Continue:speak YES or NO') 
        ch=speechip()
        options()


# In[18]:


def partialModify():
    #n=input("Enter UNIVERSITY ROLL NUMBER to Modify respective database:")
    print('Enter UNIVERSITY ROLL NUMBER to Modify respective database:')
    n=speechip()
    file=pd.read_csv("C:/Users/Subhadeep Chakrabort/Desktop/Student's Database management using Speech recognition/DataSheet1.csv")
    namelist=file['UNIVERSITY ROLL NUMBER'].tolist()
    #print(namear)
    #namear.flatten()
    
    ind=namelist.index(n)
    print(namelist)
    print(ind)
    #modpt=file.ix[nameind]
    #modlist=modpt.tolist()
    #ch2=input("Custom Modification, (y/Y or n/N)?")
    print('Custom Modification:speak YES or NO?')
    ch2=speechip()
    while ch2=='yes' or ch2=='YES':
        #sect=int(input("1. UNIVERSITY ROLL NUMBER\n2. Name \n3. DOB \n4. Stream \n5. Year \n6. Grade \n:"))
        print('speak 1. UNIVERSITY ROLL NUMBER\n2. Name \n3. DOB \n4. Stream \n5. Year \n6. Grade \n: ')
        sect=speechip()
        if sect==1:
            print("Speak UNIVERSITY ROLL NUMBER: ")
            rl=speechip()
            print(rlno)
            rlno[ind]=rl
            print(rlno)
        elif sect==2:
            print("Speak Name: ")
            nm=speechip()
            name[ind]=nm
        elif sect==3:
            print("Speak Date of Birth: ")
            db=speechip()
            dob[ind]=db
        elif sect==4:
            print("Speak Stream: ")
            st=speechip()
            stream.append(st)
        elif sect==5:
            print("Speak Year: ")
            yr=speechip()
            year.append(yr)
        elif sect==6:
            print("Speak Grade: ")
            gd=int(speechip())
            grade.append(gd)
        
        insertdata(rlno,name,dob,stream,year,grade)
        #ch=input("Continue?(y/Y or n/N): ")
        print('Continue:speak YES or NO?')
        ch=speechip()
        return
            
            


# In[21]:


def deleteDatabase():
    #n=input("Enter UNIVERSITY ROLL NUMBER to Delete respective database:")
    print('Enter UNIVERSITY ROLL NUMBER to Delete respective database:')
    n=speechip()
    file=pd.read_csv("C:/Users/Subhadeep Chakrabort/Desktop/Student's Database management using Speech recognition/DataSheet1.csv")
    namear=np.array(file['UNIVERSITY ROLL NUMBER'].tolist())
    namear.flatten()
    namelist=namear.tolist()
    ind=namelist.index(n)
    print(ind)
    #ch2=input("Custom Modification, (y/Y or n/N)?")
    print('Custom Modification:YES or NO?')
    ch2=speechip()
    col=[]
    r1=file['UNIVERSITY ROLL NUMBER'].tolist()
    n1=file['NAME'].tolist()
    d1=file['D.O.B'].tolist()
    s1=file['STREAM'].tolist()
    y1=file['YEAR'].tolist()
    g1=file['GRADE'].tolist()
    while ch2=='yes' or ch2=='YES':
        del r1[ind]
        del n1[ind]
        del d1[ind]
        del s1[ind]
        del y1[ind]
        del g1[ind]
        rlno=r1
        name=n1
        dob=d1
        stream=s1
        year=y1
        grade=g1
        insertdata(rlno,name,dob,stream,year,grade)
        #ch=input("Continue?(y/Y or n/N): ")
        print('Continue:YES or NO?')
        ch=speechip()
        return
    


# In[22]:


print("~~~~~~~~~~~~~Welcome to Smart Database Management System~~~~~~~~~~~~")

for i in range(4):
    if i==3:
        print("You have exceeded maximum try for",i,"times !!! Sorry!!")
        break
    print("!!!!!!!!!!!!!!!Speak password to open Database!!!!!!!!!!!!!!!!!!!!!!")
    password=speechip()
    if password=='project':
        #print("This will: \nAction-1: Create Database \nAction-2. Modify Database \nAction-3. Delete Database ")
        print('Go to the option window')
        options()
    else:
        print("Password Error!!!!! Try again!!!!!")

#filedf.to_csv("C:/Users/Subhadeep Chakrabort/Desktop/Student's Database management using Speech recognition/DataSheet1.csv")
filedf=pd.read_csv("C:/Users/Subhadeep Chakrabort/Desktop/Student's Database management using Speech recognition/DataSheet1.csv")
r,c=filedf.shape
filedf.head(r)

