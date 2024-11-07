name=input("Enter your name ")
print("Welcome to KBC ",name)
question=[
        ["what is your name ","Mayank","Shubham","Aman","Rishabh",4],
        ["what is your petname ","kutta","kutti","gu","tomy",3],
        ["what is your name ","Mayank","Shubham","Aman","Rishabh",3],
        ["what is your name ","Mayank","Shubham","Aman","Rishabh",1],
        ["what is your name ","Mayank","Shubham","Aman","Rishabh",1],
        ["what is your name ","Mayank","Shubham","Aman","Rishabh",2],
        ["what is your name ","Mayank","Shubham","Aman","Rishabh",2],
    ]
money=[1000,2000,3000,5000]
for i in range(0,len(money)):
    questions=question[i]
    print(f"Question for rs.{money[i]}")
    print(questions[0])
    print(f"1.{questions[1]}        2.{questions[2]}")
    print(f"3.{questions[3]}        4.{questions[4]}")
    reply=int(input("Choose your option"))
    if(reply == questions[-1]):
        print(f"Aap jeet chuke hai rs.{money[i]}")
    else:
        print("Aap har gye")     