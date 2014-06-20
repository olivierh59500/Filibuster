# encoding: utf-8
#!/usr/bin/env python
'''
This file is used for csv logging
'''

import csv
class csvlogfilegen:
  def __init__(self):
    pass

  def csvlog(self):

    with open(str(consultant)+'-'+str(location)+'-'+str(ldate)+'.csv', 'a', buffering=0) as f:
      writer = csv.writer(f)
      writer.writerow( (str(state), str(ipaddr), str(proto)+"/"+str(base_port), str(location),str(consultant), str(dft.strip('\n'))) )
      f.close()
