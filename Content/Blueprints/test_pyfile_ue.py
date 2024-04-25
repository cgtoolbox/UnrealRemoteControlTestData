#
# Test file to be run by tests\test_remote_execution.py of the upyrc wrapper.
# Github depot: https://github.com/cgtoolbox/UnrealRemoteControlWrapper
#

import sys
import unreal

unreal.log("Executed from file !")
localvar = "File localvar"
unreal.log(localvar)

if len(sys.argv) > 1:
    print(f"From cmd arguments: {sys.argv[1]} {sys.argv[2]}")