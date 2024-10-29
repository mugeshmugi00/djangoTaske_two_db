from django.shortcuts import render,redirect
from . import db
from bson import ObjectId
# Create your views here.
# login page

def login(req):
    if(req.method == "POST"):
        query = req.POST
        username = query.get("username")
        password = query.get("password")
        user = db.coll.find_one({"username": username, "password": password})
        print(user,"this is user")
        if(not user):
            print("User not found, redirecting to registration.")
            return redirect("reg")
        else:
            id = str(user['_id'])
            print(id,"id is")
            print(id,user['username'])
            print("session is ",req.session)
            req.session['userId'] = id
            return redirect("home")
    return render(req, "login.html")

# register page
def reg(req):
    if(req.method == "POST"):
        print("reg block")
        query = req.POST
        username = query.get("username")
        password = query.get("password")
        confirmpassword = query.get("confirmpassword")
        if(confirmpassword == password):
            db.coll.insert_one({"username":username,"password":password})
            print("redirect block")
            return redirect("login")
    return render(req,"reg.html")
# home page
def home(req):
    print("trigger")
    session_user_id = req.session.get("userId") 

    if not session_user_id:
        return redirect("login")
    user = db.coll.find_one({"_id": session_user_id}) 

    students = db.studentcoll.find()
    courses = db.courscoll.find()
    context = {
        "students": students,
        "courses": courses,
        "user": user  
    }

    return render(req, "home.html", context)
# add student
def addstudent(req):
    users = db.coll.find()
    session = req.session.get("userId")
    if(not session):
        return redirect("login")
    if(req.method == "POST"):
        print("reg block")
        query = req.POST
        username = query.get("username")
        email = query.get("email")
        birthday = query.get("birthday")
        age = query.get("age")
        phoneNumber = query.get("phoneNumber")
        gender = query.get("gender")
        degree = query.get("degree")
        course = query.get("course")
        db.studentcoll.insert_one({"username":username,"email":email,"birthday":birthday,
                            "age":age,"phoneNumber":phoneNumber,"gender":gender,
                            "degree":degree,"course":course,})
        print("redirect block")
        return redirect("students")
    return render(req,"addStudent.html",{"users":users})
# students
def students(req):
    session = req.session.get("userId")
    if not session:
        return redirect("login") 
    print("working")
    students = db.studentcoll.find()
    datas = []
    for i in students:
        i["docId"] = str(i["_id"])
        datas.append(i)
    return render(req, "students.html", {"students": datas})

# logout
def logout(req):
    del req.session["userId"]
    print(req.session.keys())
    return redirect("login")
# about
def about(req):
    users = db.coll.find()
    session = req.session.get("userId")
    if(not session):
        return redirect("login")
    return render(req,"about.html",{"users":users})
# cours
def cours(req):
    session = req.session.get("userId")
    if not session:
        return redirect("login") 
    print("working")
    courses = db.courscoll.find()
    data = []
    for i in courses:
        i["documentId"] = str(i["_id"])
        data.append(i)
    return render(req, "cours.html", {"courses": data})  

# addCours
def addCours(req):
    users = db.coll.find()
    session = req.session.get("userId")
    if(not session):
        return redirect("login")
    if(req.method == "POST"):
        print("reg block")
        query = req.POST
        coursename = query.get("coursename")
        duration = query.get("duration")
        Specialties = query.get("Specialties")
        description = query.get("description")
        db.courscoll.insert_one({"coursename":coursename,"duration":duration,"Specialties":Specialties,"description":description,})
        print("redirect block")
        return redirect("cours")
    return render(req,"addCours.html",{"users":users})

# delet student
def deleteStudent(req, id):
    if req.method == "POST":
        print(req.method, "this is method")
        print("delete student", id)
        object_id = ObjectId(id)
        db.studentcoll.delete_one({"_id": object_id})
    return redirect("students")
# deleteCours
def deleteCours(req,id):
    if req.method == "POST":
        print(req.method,"req method cours")
        print("delete cours", id)
        objectId = ObjectId(id)
        db.courscoll.delete_one({"_id": objectId})
    return redirect("cours")
