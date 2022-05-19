import time
from iss_passes_ import get_next_pass

# Continuous call
def continuous_call():
    while(True):
        time.sleep(3600)
        get_next_pass()