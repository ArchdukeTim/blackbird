import sys, enum,shlex, subprocess, re, os
from collections import Counter

class Color(enum.Enum):
    def __str__(self):
        return str(self.value)
    RED = '\033[0;31m'
    GREEN ='\033[0;32m'
    YELLOW ='\033[1;33m'
    CYAN ='\033[0;36m'
    BCYAN ='\033[1;36m'
    PURPLE ='\033[0;35m'
    GRAY ='\033[0;37m'
    MAGENTA ='\033[0;37m'
    NC ='\033[0m'
class Log_Types(enum.Enum):
    def __str__(self):
        return str(self.value)
    WARNING = Color.YELLOW
    ERROR = Color.RED
    SUCCESS = Color.GREEN
    TASK = Color.GRAY
    PROMPT = Color.CYAN
    
def log(message, mtype):
    print("[%sSR-71%s] [%s%s%s] %s" % (Color.MAGENTA, Color.NC, mtype, mtype.name, Color.NC, message))
def query_yes_no(question, default="yes"):
    '''Ask a yes/no question via raw_input() and return their answer.
    :param question: is a string that is presented to the user.
    :param default: is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    '''
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)
    
    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")
def command(command):
    
    args = shlex.split(command)
    p = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    (out, err) = p.communicate()
    if p.returncode != 0:
        return p.returncode
    out = out.decode()
    outputList = out.splitlines()
    outputList = list(filter(None, outputList))
    return outputList


def verify_forensic():
    for i in os.listdir(os.path.expanduser("~")+"\\Desktop\\"):
        if "Forensic" in i:
            lines =  open(os.path.expanduser("~")+"\\Desktop\\"+i).read()
            if lines.count("<Type Answer Here>") == 3:
                log("Forensics Question [%s] Not Answered" % i, Log_Types.ERROR)
                return False
    return True
# if not verify_forensic():
#     if not query_yes_no("Do you want to continue?", default = "no"):
#         sys.exit()
        
    
