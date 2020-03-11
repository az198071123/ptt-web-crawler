import sys
import traceback
try:
    1 / 0
except Exception:
    s = traceback.print_exc(file=sys.stdout)
    print(s)
