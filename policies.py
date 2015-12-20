from SR_71 import command, log

log("Installing Policies / Services", TASK)
command("rundll32 syssetup,SetupInfObjectInstallAction DefaultInstall 128 .\policies.inf")
