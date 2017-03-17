#!/usr/bin/env python

import os
import pwd
import sys
import time
from Pegasus.DAX3 import *

# The name of the DAX file is the first argument
if len(sys.argv) < 3:
        sys.stderr.write("Usage: %s DAXFILE <control-file> [prms-outputfile]\n" % (sys.argv[0]))
        sys.exit(1)
daxfile = sys.argv[1]
controlFile = sys.argv[2]
outputFile = "prms.output" if len(sys.argv) < 4 else sys.argv[3]

USER = pwd.getpwuid(os.getuid())[0]

dax =ADAG("prms-wf")

# Add some workflow-level metadata
dax.metadata("creator", "%s@%s" % (USER, os.uname()[1]))
dax.metadata("created", time.ctime())

control_f = File(controlFile)
prmsOutput = File(outputFile)

prms = Job("prms")
prms.addArguments("-C",control_f)
prms.setStdout(prmsOutput)
prms.uses(control_f, link=Link.INPUT)
prms.uses(prmsOutput, link=Link.OUTPUT, transfer=True, register=False)
dax.addJob(prms)

f = open(daxfile, "w")
dax.writeXML(f)
f.close()
