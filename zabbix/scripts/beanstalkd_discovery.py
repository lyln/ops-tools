#!/usr/bin/env python
import os
import json
t=os.popen("""netstat -nlput |awk -F":" '/beanstalkd/ {print $2}'|awk '{print $1}'|grep -v "^$" """)
ports = []
for port in  t.readlines():
        r = os.path.basename(port.strip())
        ports += [{'{#BEANSTALKDPORT}':r}]
print json.dumps({'data':ports},sort_keys=True,indent=4,separators=(',',':'))
