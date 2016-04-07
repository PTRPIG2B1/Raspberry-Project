import os
import sys
from datetime import datetime

maintenant = datetime.now()
print "photo_"+str(maintenant.day) + "/" + str(maintenant.month) + "/" + str(maintenant.year) + "_" + str(maintenant.hour) + ":" + str(maintenant.minute) + ":" + str(maintenant.second)

