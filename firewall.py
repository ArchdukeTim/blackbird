from SR_71 import command, log
log("--------FIREWALL--------")
command("netsh advfirewall set allprofiles state on") # turn on firewall for all types
log("Turned on firewall")
command("netsh advfirewall set allprofiles logging filename %systemroot%\system32\LogFiles\Firewall\pfirewall.log") # set log file
log("Set log file")
command("netsh advfirewall set allprofiles logging maxfilesize 4096") # set log file size
log("Set log file size")
command("netsh advfirewall set allprofiles logging droppedconnections enable") # set logging for dropped packets
log("Set logging for droped packets")
command("netsh advfirewall set allprofiles logging allowedconnections enable") # set logging for connected packets
log("Set logging for connected packets")
command("netsh advfirewall set allprofiles firewallpolicy blockinboundalways,allowoutbound")
log("Block inbounds, allow outbound")