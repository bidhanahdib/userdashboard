
from main import maindash
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


