import os
from SR_71 import command, log, Log_Types, message

message("Installing Policies / Services", Log_Types.TASK)
cwd = os.getcwd()
os.chdir(os.path.expanduser("~")+os.path.normpath("/Desktop/\CyberPatriot Tools/"))
command("secedit /configure /db %temp%\\temp.sdb /cfg Policies_Services_Template.inf")
log("Loaded security policy. Check Appendices for specific settings")


