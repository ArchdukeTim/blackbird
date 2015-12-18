from SR_71 import query_yes_no, Color, command

users = command("wmic UserAccount get Name")
del users[0]
for user in users:
    user = user.replace(" ", "")
    cuser = Color.RED.value + user + Color.NC.value
    if query_yes_no("Is %s an authorized user?" % cuser):
        print("Allowing user %s to stay" % cuser)
    else:
        print("Removing user  %s" % cuser)
    if any("*Administrators" in x for x in command("net user %s" % user)):
        if not query_yes_no("Is %s an authorized administrator?" % cuser):
            print("Removing %s " % cuser +" from Administrators")
    
