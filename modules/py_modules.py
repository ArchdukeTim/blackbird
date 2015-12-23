from SR_71 import command, log, Log_Types, query_yes_no
import os
from colorama import Back, Style

            
class Updates:
    def run(self):
        update = command("wuapp.exe")
        if update == 1:
            log("Could not start windows update", Log_Types.ERROR)
            return False;
        if query_yes_no("Have you configured windows update?"):
            log("Started Windows Update", Log_Types.SUCCESS)

class Users:
    def run(self):
        users = command("wmic UserAccount get Name")
        if users == 1:
            log("Could not iterate over user accounts", Log_Types.ERROR)
            return False
        del users[0]
        for user in users:
            if any("Built-in" in x for x in command("net user %s" % user)):
                command("net user %s CyberPatriot1!" % user)
                command("net user %s /ACTIVE NO" % user)
                continue
            
            user = user.replace(" ", "")
            cuser = Back.RED + user +Style.RESET_ALL
            if query_yes_no("Is %s an authorized user?" % cuser):
                print("Allowing user %s to stay" % cuser)
                command("net user %s CyberPatriot1!" % user)
            else:
                print("Removing user  %s" % cuser)
            
            if any("*Administrators" in x for x in command("net user %s" % user)):
                if not query_yes_no("Is %s an authorized administrator?" % cuser):
                    print("Removing %s " % cuser +" from Administrators")
                    command("net localgroup administrators %s /delete" % user)
                    
                    
class Policies:
    def run(self):
        log("Installing Policies / Services", Log_Types.TASK)
        cwd = os.getcwd()
        os.chdir(os.path.expanduser("~")+os.path.normpath("/Desktop/\CyberPatriot Tools/")) 
        print(os.getcwd())

class Firewall:
    def run(self):
        command("netsh advfirewall set allprofiles state on") # turn on firewall for all types
        command("netsh advfirewall set allprofiles logging filename %systemroot%\system32\LogFiles\Firewall\pfirewall.log") # set log file
        command("netsh advfirewall set allprofiles logging maxfilesize 4096") # set log file size
        command("netsh advfirewall set allprofiles logging droppedconnections enable") # set logging for dropped packets
        command("netsh advfirewall set allprofiles logging allowedconnections enable") # set logging for connected packets
        command("netsh advfirewall set allprofiles firewallpolicy blockinboundalways,allowoutbound")
        
        command("secedit /configure /db %temp%\\temp.sdb /cfg Policies_Services_Template.inf")

class Remote:
    def run(self):
        command("reg add \"HKEY_LOCAL_MACHINE\\SYSTEM\CurrentControlSet\Control\Terminal Server\" /v fDenyTSConnections /t REG_DWORD /d 1 /f")
        command("reg add \"HKEY_LOCAL_MACHINE\\SYSTEM\CurrentControlSet\Control\Remote Assistance\" /v fAllowToGetHelp /t REG_DWORD /d 0 /f")
        

class Shares:
    def run(self): 
        shares = command("net share")
        shares = shares[2:-1]
        print(shares)
        for share in shares:
            print (share.split(' ', 1)[0])
            command("net share %s /DELETE" % share)
