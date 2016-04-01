import sys
import ConfigParser

cfg = ConfigParser.ConfigParser()
cfg.read("test1.cfg")

param = sys.argv[1]
if param == "1":
	cfg.set("Section1", "width", "1920")
	cfg.set("Section1", "height","1080")
elif param == "2":
	cfg.set("Section1", "width", "1200")
	cfg.set("Section1", "height","720")
else:
	cfg.set("Section1", "width", "640")
	cfg.set("Section1", "height","480")
cfg.write(open("test1.cfg", "w"))
print cfg.items("Section1")
