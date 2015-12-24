from SR_71 import command, log, log, Log_Types, query_yes_no
import os
from colorama import Fore, Style


class Updates:
    task = "Updates"
    def run(self):
        command("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\" /v AUOptions /t REG_DWORD /d 0 /f")
        update = command("wuapp.exe")
        if update == 1:
            log("Could not start windows update", Log_Types.ERROR)
            return 1;
        if query_yes_no("Have you configured windows update?"):
            pass

class Users:
    task = "Users"
    def run(self):
        users = command("wmic UserAccount get Name")
        if users == 1:
            log("Could not iterate over user accounts", Log_Types.ERROR)
            return False
        del users[0]
        for user in users:
            #log(user, Log_Types.WARNING)
            user = user.rstrip().replace(" ", "\ ")
            if any("Built-in" in x for x in command("net user %s" % user)):
                command("net user %s CyberPatriot1!" % user)
                command("net user %s /ACTIVE NO" % user)
                continue

            user = user.replace(" ", "")
            cuser = Fore.RED + user +Style.RESET_ALL
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
    task = "Policies"
    def run(self):
        cwd = os.getcwd()
        try:
            os.chdir(os.path.expanduser("~")+os.path.normpath("/Desktop/\CyberPatriot Tools/"))
        except(FileNotFoundError):
            log("Failed to locate CyberPatriot Tools on desktop", Log_Types.ERROR)
            return 1;
        command("secedit /configure /db %temp%\\temp.sdb /cfg Policies_Services_Template.inf")
        log("Loaded security policy. Check Appendices for specific settings", Log_Types.LOG)

class Firewall:
    task = "Firewall"
    def run(self):
        command("netsh advfirewall set allprofiles state on") # turn on firewall for all types
        log("Turned on firewall", Log_Types.LOG)
        command("netsh advfirewall set allprofiles logging filename %systemroot%\system32\LogFiles\Firewall\pfirewall.log") # set log file
        log("Set log file", Log_Types.LOG)
        command("netsh advfirewall set allprofiles logging maxfilesize 4096") # set log file size
        log("Set log file size", Log_Types.LOG)
        command("netsh advfirewall set allprofiles logging droppedconnections enable") # set logging for dropped packets
        log("Set logging for droped packets", Log_Types.LOG)
        command("netsh advfirewall set allprofiles logging allowedconnections enable") # set logging for connected packets
        log("Set logging for connected packets", Log_Types.LOG)
        command("netsh advfirewall set allprofiles firewallpolicy blockinboundalways,allowoutbound")
        log("Block inbounds, allow outbound", Log_Types.LOG)

class IllegalMedia:
    task = "Illegal Media"
    def run(self):
        self.removeFileType("mp3")
        self.removeFileType("mp4")
        self.removeFileType("jpg")
        self.removeFileType("jpeg")

    def removeFileType(self, fileType):
        if query_yes_no("do you wish to remove all %s files?" % fileType):
            command("del /s *.%s" % fileType)

class Remote:
    task = "Remote"
    def run(self):
        command("reg add \"HKEY_LOCAL_MACHINE\\SYSTEM\CurrentControlSet\Control\Terminal Server\" /v fDenyTSConnections /t REG_DWORD /d 1 /f")
        command("reg add \"HKEY_LOCAL_MACHINE\\SYSTEM\CurrentControlSet\Control\Remote Assistance\" /v fAllowToGetHelp /t REG_DWORD /d 0 /f")


class Shares:
    task = "Shares"
    def run(self):
        shares = command("net share")
        shares = shares[2:-1]
        print(shares)
        for share in shares:
            print (share.split(' ', 1)[0])
            command("net share %s /DELETE" % share)
