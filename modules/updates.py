import sys
from SR_71 import query_yes_no, Color, command, log, Log_Types
update = command("wuapp.exe")
if update == 1:
    log("Could not start windows update", Log_Types.ERROR)
    sys.exit()
if query_yes_no("Have you configured windows update?"):
    log("Started Windows Update", Log_Types.SUCCESS)