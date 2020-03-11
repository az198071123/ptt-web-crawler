from subprocess import call
call(["osascript", "-e", 'display alert \" [this is title] \" message \" [this is msg] \"'])
