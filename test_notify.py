from subprocess import call
print('start test')
title = 'TestTitle'
url = 'TestUrl'

cmd = f'display notification \"{url}\" with title \"{title}\" sound name \"Glass\"'
# cmd = f'display alert \"{url}\" message\"{title}\"'
call(["osascript", "-e", cmd])

print('end test')
