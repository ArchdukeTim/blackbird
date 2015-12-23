import sys
from SR_71 import query_yes_no, Color, command, message, Log_Types
update = command("wuapp.exe")
if update == 1:
    ("Could not start windows update", Log_Types.ERROR)
    sys.exit()
if query_yes_no("Have you configured windows update?"):
    message("Started Windows Update", Log_Types.SUCCESS)