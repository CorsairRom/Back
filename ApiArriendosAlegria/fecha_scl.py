from dateutil import tz
from datetime import datetime


def GetfechaScl():
    scl = tz.gettz('America/Santiago') 
    today = datetime.now(tz=scl)
    return today
