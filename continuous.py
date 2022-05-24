import time
from iss import get_next_pass

# Continuous call
def continuous_call():
    while(True):
        get_next_pass()
        time.sleep(3600)