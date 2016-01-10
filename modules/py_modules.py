from SR_71 import command, log, log, Log_Types, query_yes_no
import os
from colorama import Fore, Style
from logging import logThreads
 
 
class Updates:
    task = "Updates"
    def run(self):
        # command("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\" /v AUOptions /t REG_DWORD /d 0 /f")
        # update = command("wuapp.exe")
        update = command("start cscript resources/update.vbs")
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
            user = user.strip()
            # log(user, Log_Types.WARNING)
            if " " in user:
                user = "\"" + user + "\""
            print(user)
            if any("Built-in" in x for x in command("net user %s" % user)):
                command("net user %s CyberPatriot1!" % user)
                command("net user %s /ACTIVE:NO" % user)
                continue
            cuser = Fore.RED + user + Style.RESET_ALL
            if query_yes_no("Is %s an authorized user?" % cuser):
                print("Allowing user %s to stay" % cuser)
                command("net user %s CyberPatriot1!" % user)
            else:
                command("net user %s /delete" % user)
                continue
 
            if any("*Administrators" in x for x in command("net user %s" % user)):
                if not query_yes_no("Is %s an authorized administrator?" % cuser):
                    print("Removing %s " % cuser + " from Administrators")
                    command("net localgroup administrators %s /delete" % user)
 
 
class Policies:
    task = "Policies"
    def run(self):
        
        command("secedit /configure /db %temp%\\temp.sdb /cfg resources/Policies_Services_Template.inf", [2,3])
        log("Loaded security policy. Check Appendices for specific settings", Log_Types.LOG)
        
        
class Programs:
    task = "Add/Remove Programs"
    def run(self):
        command("control appwiz.cpl")
        query_yes_no("Have you removed all the bad programs?") 
        
        
class Firewall:
    task = "Firewall"
    def run(self):
        command("netsh advfirewall set allprofiles state on")  # turn on firewall for all types
        log("Turned on firewall", Log_Types.LOG)
        command("netsh advfirewall set allprofiles logging filename %systemroot%\system32\LogFiles\Firewall\pfirewall.log")  # set log file
        log("Set log file", Log_Types.LOG)
        command("netsh advfirewall set allprofiles logging maxfilesize 4096")  # set log file size
        log("Set log file size", Log_Types.LOG)
        command("netsh advfirewall set allprofiles logging droppedconnections enable")  # set logging for dropped packets
        log("Set logging for droped packets", Log_Types.LOG)
        command("netsh advfirewall set allprofiles logging allowedconnections enable")  # set logging for connected packets
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
        cwd = os.getcwd()
        os.chdir(os.path.normpath("C:/Users/"))
        if query_yes_no("do you wish to remove all %s files?" % fileType):
            files = command("del /s *.%s" % fileType)
            log(files, Log_Types.LOG)
        os.chdir(cwd)
 
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
            command("net share %s /DELETE" % share)
 
class Features:
    task = "Windows Features"
    def run(self):
        log("Configuring Windows Features", Log_Types.LOG)
        command("optionalfeatures")
       
class UAC:
    task = "User Account Control"
    def run(self):
        log("Configuring UAC", Log_Types.LOG)
        command("reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 1 /f")
        command("reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v FilterAdministratorToken /t REG_DWORD /d 1 /f")
        command("reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v ConsentPromptBehaviorAdmin /t REG_DWORD /d 2 /f")
        command("reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v ConsentPromptBehaviorUser /t REG_DWORD /d 1 /f")
        command("reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableInstallerDetection /t REG_DWORD /d 1 /f")
        command("reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v ValidateAdminCodeSignatures /t REG_DWORD /d 0 /f")
        command("reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v PromptOnSecureDesktop /t REG_DWORD /d 1 /f")
        command("reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableVirtualization /t REG_DWORD /d 0 /f")
class Power:
    task = "Password on Wakeup"
    def run(self):
        command("powercfg -SETACVALUEINDEX SCHEME_MAX SUB_NONE CONSOLELOCK 0")
        command("powercfg -SETDCVALUEINDEX SCHEME_MAX SUB_NONE CONSOLELOCK 0")
        log("Password required on wakeup", Log_Types.LOG)
       
class Malware:
    task = "Install Malwarebytes"
    def run(self):
        command("start resources/mbam-setup-2.2.0.1024.exe")#include malwarebytes installer file
        #log("Press any key when malwarebytes is finished installing...", Log_Types.LOG)
        #command("set /p=", expected_errors=[0,1])
       
class Firefox:
    task = "Update Firefox "
    def run(self):
        command("start resources/Firefox_Setup_Stub_43.0.3.exe")
        #log("Press any key when firefox is finished installing...", Log_Types.LOG)
        #command("set /p=", expected_errors=[0,1])
       
class DNS:
    task = "Flush DNS Cache"
    def run(self):
        command("ipconfig /flushdns")
       
class DEP:
    task = "Turn on Data Execution Prevention"
    def run(self):
        command("bcdedit.exe /set {current} nx AlwaysOn")
       
class MBSA:
    task = "Installing Microsoft Baseline Security Analyzer"
    def __init__(self, processor_architecture):
        self.processor_architecture = processor_architecture
   
    def run(self):
        installer = None
       
        if(self.processor_architecture == 64):
            installer = r"resources\\MBSASetup-x64-EN.msi"
        else:
            installer = r"resources\\MBSASetup-x86-EN.msi"
       
        command("msiexec /i %s" % installer)
