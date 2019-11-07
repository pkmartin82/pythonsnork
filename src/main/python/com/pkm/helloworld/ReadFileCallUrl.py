import os
import urllib.request

fileDir = os.path.dirname(os.path.realpath('__file__'))
inputFile = os.path.join(fileDir, "src/main/resources/schools.txt")
print("Reading a file: '{}'".format(inputFile))

with open(inputFile) as fp:
   for cnt, line in enumerate(fp):
       print("Line {}: {}".format(cnt, line))
       contents = urllib.request.urlopen("http://example.com/foo/bar/{}".format(line)).read()
