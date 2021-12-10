# import os

# os.system("conda list")
import test1
from log import tlog
tlog.init('./logging/a.log')



tlog.absc='saaa'
tlog.b=2
tlog.a=1
tlog.c=111
test1.main()


tlog.print_parameter()
