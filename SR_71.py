import sys, enum, shlex, subprocess, re, os, glob
from colorama import Back, Fore, Style, init
init()
from collections import Counter

from modules.py_modules import *
    

class Log_Types(enum.Enum):
    def __str__(self):
        return str(self.value)
    WARNING = Fore.YELLOW
    ERROR = Fore.RED
    FINISHED = Fore.GREEN
    TASK = Fore.CYAN
    PROMPT = Fore.LIGHTBLACK_EX
    LOG = Fore.MAGENTA
    
def log(message, mtype, write=True):
    print("[%sSR-71%s] [%s%s%s] %s" % (Fore.BLUE, Style.RESET_ALL, mtype, mtype.name, Style.RESET_ALL, message))
    log_file = open('SR-71.log', 'a')
    log_file.write('[SR-71] [%s] %s\n' % (mtype.name, message))
    log_file.closed

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
            
def command(command, expected_errors=[0]):
    args = shlex.split(command)
    #log(args, Log_Types.LOG)
    p = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    if "start" in args:
        return 0;
    out, err = p.communicate()
    if p.returncode not in expected_errors:
        code = "%s%s%s" %(Back.RED, p.returncode, Style.RESET_ALL)
        returned = "%s%s%s" %(Back.RED, out, Style.RESET_ALL)
        attempted_command = "%s%s%s" %(Back.RED, command, Style.RESET_ALL)
        log("Unexpected response: \"%s:%s\" with command \"%s\"" % (code, returned, attempted_command), Log_Types.ERROR)
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
                message("Forensics Question [%s] Not Answered" % i, Log_Types.ERROR)
                return False
    return True

class SR_71:
    def __init__(self):
        pass
    
    def run(self):
        if not verify_forensic():
            if not query_yes_no("Would you like to continue", default="no"):
                sys.exit(1);
                
        cmd_modules = glob.glob('modules/*.cmd')
        modules = [ [Updates(), Users()], 
                    [Policies(), IllegalMedia()],
                    [Firewall(), Remote(), Shares(), Features(), UAC(), Power(), Malware(), Firefox(), DNS(), DEP()]]
        
        for priorityLevel in modules:
            for py in priorityLevel:
                log("--------%s--------" % py.task, Log_Types.TASK)
                py.run()
                log(py.task, Log_Types.FINISHED)


if __name__ == '__main__':
    sr = SR_71()
    sr.run()