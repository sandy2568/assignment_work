
present=0
while True:
    door_status=input("enter  c to close close the door")
    if door_status.lower()=="c":
        dup_present=int(input("enter the number of floor"))
        if (dup_present>=0) and (dup_present<6):
            way=present-dup_present
            if way<0:
                for i in range(present,dup_present):
                    print(i,".......")
            else:
                for j in range(present,dup_present,-1):
                    print(j,"......")
        present=dup_present
        print("open the door")
        print(f"{present} present floor")

    else:
        print("pls close the door")
        

