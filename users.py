import sys
from SR_71 import query_yes_no, Color, command, log, Log_Types

users = command("wmic UserAccount get Name")
if users == 1:
    log("Could not iterate over user accounts", Log_Types.ERROR)
    sys.exit()
del users[0]
for user in users:
    if any("Built-in" in x for x in command("net user %s" % user)):
        command("net user %s CyberPatriot1!" % user)
        command("net user %s /ACTIVE NO" % user)
        continue
    
    user = user.replace(" ", "")
    cuser = Color.RED.value + user + Color.NC.value
    if query_yes_no("Is %s an authorized user?" % cuser):
        print("Allowing user %s to stay" % cuser)
        command("net user %s CyberPatriot1!" % user)
    else:
        print("Removing user  %s" % cuser)
    
    if any("*Administrators" in x for x in command("net user %s" % user)):
        if not query_yes_no("Is %s an authorized administrator?" % cuser):
            print("Removing %s " % cuser +" from Administrators")
            command("net localgroup administrators %s /delete" % user)

