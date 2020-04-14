Name = input("Please, Enter your Name :")

Degree = input("Plrase, Enter your Deree : ")

if int(Degree)>=90 :
    print("Execellent")
    if int(Degree)>=90 and int(Degree)<=94 :
        print("A")
    elif int(Degree)>=95 and int(Degree)<=100 : 
        print("A+")
      
elif int(Degree)>=80 :
    print("very good")
elif int(Degree)>=70 :
    print("Good")
elif int(Degree)>=50 and  int(Degree)<=60 :
    print("Pass") 
else :
    print("Fail")    