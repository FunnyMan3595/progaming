#!/usr/bin/env python
import json, sys, os

with open("save.json") as savefile:
    data = json.load(savefile)

data["runs"] += 1
runs = data["runs"]

crashes = data["crashes"]
data["crashes"] += 1

def write():
    with open("save.json", "w") as savefile:
        json.dump(data, savefile)

write()

back = " back" if runs > 1 else ""

print "Welcome%s to Progaming.  This is run #%d.  Crashes so far: %d" % (back, runs, crashes)

while True:
    print
    print "Turn %d, %d cash." % (data["turns"], data["cash"])
    order = raw_input("What now? ").lower()
    if order.startswith("w"):
        data["turns"] += 1
        data["cash"] += 1
    elif order.startswith("r") or order.startswith("q"):
        if data["cash"] < 10:
            print "Need 10 cash to recompile or quit."
            continue

        data["cash"] -= 10
        data["crashes"] -= 1
        write()
        print
        if order.startswith("r"):
            os.execv(sys.executable, [sys.executable] + sys.argv)
        else:
            sys.exit(0)
    else:
        print "Command not recognized."
