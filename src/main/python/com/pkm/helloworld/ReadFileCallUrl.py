import os
import sys
import urllib2


inputFile = os.path.join(sys.path[0], "schools.txt")
print("Refreshing Cache for schools found in: {0}".format(inputFile))

with open(inputFile, "r") as fp:
	for cnt, line in enumerate(fp):
		print(">>>>\n>>>>\n>>>>Refresh Cache for SchoolId={0}".format(line).rstrip("\n"))
		contents = urllib2.urlopen("https://sfs.iprod.afford.com/RCW/Home/RefreshDataCache?schoolId={0}".format(line)).read()
		print(">>>>{0}".format(contents))

print("Done Refreshing Cache")
