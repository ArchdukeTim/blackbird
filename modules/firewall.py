from SR_71 import command
command("netsh advfirewall set allprofiles state on") # turn on firewall for all types
command("netsh advfirewall set allprofiles logging filename %systemroot%\system32\LogFiles\Firewall\pfirewall.log") # set log file
command("netsh advfirewall set allprofiles logging maxfilesize 4096") # set log file size
command("netsh advfirewall set allprofiles logging droppedconnections enable") # set logging for dropped packets
command("netsh advfirewall set allprofiles logging allowedconnections enable") # set logging for connected packets
command("netsh advfirewall set allprofiles firewallpolicy blockinboundalways,allowoutbound")