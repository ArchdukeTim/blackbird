import sys
from SR_71 import query_yes_no, Color, command, log, Log_Types

users = command("wmbic UserAccount get Name")
if users == 1:
    log("Could not iterate over user accounts", "error")
    sys.exit()
del users[0]
for user in users:
    user = user.replace(" ", "")
    cuser = Color.RED.value + user + Color.NC.value
    if query_yes_no("Is %s an authorized user?" % cuser):
        print("Allowing user %s to stay" % cuser)
        #command("net user %s CyberPatriot1!" % user) Uncomment for testing
    else:
        print("Removing user  %s" % cuser)
    if any("*Administrators" in x for x in command("net user %s" % user)):
        if not query_yes_no("Is %s an authorized administrator?" % cuser):
            print("Removing %s " % cuser +" from Administrators")
            #command("net localgroup administrators %s /delete" % user) Uncomment for testing

#command("net user Adminstrator /ACTIVE NO")
#command("net user Guest /ACTIVE NO")
