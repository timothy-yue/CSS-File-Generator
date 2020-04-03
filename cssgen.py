#! /usr/bin/env python3

# CSS Generator
# Read through an HTML file and create a CSS file with all the classes from
# the html file
# Usuage: ./cssgen.py <html file> <css file>

import sys
import re

#@TODO: Add parameter to determine whether it is vanilla html or React

# Error handling
if len(sys.argv) != 3:
    print("Usuage: ./cssgen.py <html file> <css file>")
    sys.exit()

htmlfile = sys.argv[1]
cssfile = sys.argv[2]

if not htmlfile[-4:] == 'html':
    print("Input file has to be an HTML file")
    sys.exit()

if not cssfile[-3:] == 'css':
    print("Output file has to be CSS file")
    sys.exit()

# Open file to read mode
f = open(htmlfile, 'r')

# Keep track of classes
classes = []

for x in f:
        # Replace all single quotes with double quotes
        santized_str = x.replace("'", '"')
        # Search for class='' structure in line 
        search = re.findall(r'class="[a-zA-Z0-9- ]*"', santized_str)
        if search:
                arr = search[0][7:-1].split(" ")
                for i in arr:
                        classes.append(i)


f.close()

# Remove duplicate from class list
classes = set(classes)

# Open file for writing
#       -will fail if css file exists
wf = open(cssfile, "x")

for c in classes:
    # @TODO: Add logic to write classes in order they appear in html
    wf.write(".{} {{ }}\n\n".format(c))

wf.close()

