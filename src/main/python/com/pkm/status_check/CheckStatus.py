import os
import urllib.request
import json

fileDir = os.path.dirname(os.path.realpath('__file__'))
inputFile = os.path.join(fileDir, "src/main/resources/statuses.txt")
print("Reading a file: '{}'".format(inputFile))

with open(inputFile) as fp:
   for cnt, line in enumerate(fp):
       print("Line {}: {}".format(cnt, line))
       txt_contents = urllib.request.urlopen(line).read()
       print()
       print(txt_contents)
       print()
       json_contents = json.loads(txt_contents)
       print(json_contents)
       print()