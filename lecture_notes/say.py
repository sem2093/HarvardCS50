import cowsay
import sys

# have a cow say hello

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])

# have a trex say hello

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])
  
# import goodbye from sayings.py

import sys

from saying import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])
