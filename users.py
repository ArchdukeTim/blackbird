import shlex, subprocess, re

from SR_71 import query_yes_no, Color

#command_line = "wmic UserAccount get Name"
#args = shlex.split(command_line)
#p = subprocess.Popen(args, stdout=subprocess.PIPE)
#(out, err) = p.communicate()
#a = re.findall(r"[\w']+", out.decode())
for user in ["Tim",     "John", "Phil"]:
    if query_yes_no("Is %s an authorized user?" % user):
        print("Allowing user %s to stay" % user)
    else:
        print("Removing user "+ Color.RED.value + "%s" % user + Color.NC.value)
