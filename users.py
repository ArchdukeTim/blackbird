import shlex, subprocess, re
command_line = "wmic UserAccount get Name"
args = shlex.split(command_line)
p = subprocess.Popen(args, stdout=subprocess.PIPE)
(out, err) = p.communicate()
a = re.findall(r"[\w']+", out.decode())
print(a)

