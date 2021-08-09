
userdb = [{'userid': 1, 'username': 'Bidhan'}]
userdetails = {}

def createuser (wuserid, wusername, wuserphone, wuseradd): 
    userdetails = {
        "userid": wuserid,
        "username": wusername,
        "phone no.": wuserphone,
        "address": wuseradd
    }
    userdb.append(userdetails)
    #return userdetails
    #print(userdb)
    print(userdetails)
    print("\n" + "User details added successfully!!! ")
    maindash()

def showusers():
    print("\n" + "All User informations!!!! " + "\n")
    print(userdb)
    maindash()

def userdel(deluserid):
    for i in userdb:
        #print(i)
        xuserid = i['userid']
        xusername = i['username']
        #print(xuserid)
        #print(xusername)
        if xuserid == deluserid:
            userdb.remove({'userid': deluserid, 'username': xusername})
            print("Deleted user information:")
            print("\n" + "user "  + xusername + " deleted successfully!!!")

        #print(userdb)
    maindash()

def userget(getuserid):
    for i in userdb:
        #print(i)
        xuserid = i['userid']
        xusername = i['username']
        #print(xuserid)
        #print(xusername)
        print("user information!!!" + "\n")
        if xuserid == getuserid:
            print({'userid': getuserid, 'username': xusername})
    maindash()


def updateuser(id, updateuser):
    for count,values in enumerate(userdb):
        print(count, values)
        for i in values:
            if values[i] == id:
                dbindex = count        
                userdb[dbindex] = {'userid': id, 'username': updateuser}
                print("\n" + "user "  + updateuser + " updated successfully!!!")
    
    maindash()








def dash(userinput):
    switcher = {
        1: "Add user",
        2: "Show users"
    }
    print(switcher.get(userinput))
    #return switcher.get(userinput, "Invalid user input")
    maindash()
    

def maindash():
    print("\n")
    print("--------------------")
    print("USER DASHBOARD")
    print("--------------------")
    print("CHOOSE ANY:" + "\n" + "1: Add customer" + "\n" + "2: show users" + "\n" +"3: Delete user by ID" + "\n" + "4: Get user info by UID" + "\n"+ "5: Update username by UID")
    print("choose: ", end=" ")
    userinput = int(input())
    if userinput == 1:
        print("\n" + "Enter user id:", end= " ")
        input_userid = int(input())
        print("Enter username:", end=" " )
        input_username = input()
        print("Enter user phone no:", end=" " )  
        input_userphone = int(input())
        print("Enter user address :", end=" " )  
        input_useraddress = input()
        createuser(input_userid, input_username, input_userphone, input_useraddress)
    elif userinput == 3:
        print("Enter user id to delete:", end=" ")
        input_deleteid = int(input())
        userdel(input_deleteid)
    elif userinput == 4:
        print("Enter user id to get user info: ", end=" ")
        input_get = int(input())
        userget(input_get)
    elif userinput == 5:
        print("Update UID of user", end=" ")
        input_updateuid = int(input())
        print("Enter username to update")
        input_updateusername = input()
        updateuser(input_updateuid, input_updateusername)



    else:
        dash(showusers())


maindash()

# print("Enter userid: ")
# wuserid = int(input())
# print("Enter username:")
# wusername = input()
# createuser(wuserid, wusername)


# print("\n")
# print("Enter userid: ")
# wuserid = int(input())
# print("Enter username:")
# wusername = input()
# createuser(wuserid, wusername)
# print(userdb)




