from SR_71 import command
command("reg add \"HKEY_LOCAL_MACHINE\\SYSTEM\CurrentControlSet\Control\Terminal Server\" /v fDenyTSConnections /t REG_DWORD /d 1 /f")
command("reg add \"HKEY_LOCAL_MACHINE\\SYSTEM\CurrentControlSet\Control\Remote Assistance\" /v fAllowToGetHelp /t REG_DWORD /d 0 /f")