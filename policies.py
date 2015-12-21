import os
from SR_71 import command, log, Log_Types

log("Installing Policies / Services", Log_Types.TASK)
cwd = os.getcwd()
os.chdir(os.path.expanduser("~")+os.path.normpath("/Desktop/\CyberPatriot Tools/")) 
print(os.getcwd())
command("secedit /configure /db %temp%\\temp.sdb /cfg Policies_Services_Template.inf")

