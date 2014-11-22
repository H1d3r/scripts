#!/usr/bin/python
# Find/Replace SID with username.

import re

print '[+] Doing things!'

### Opens files, sets variables
sids = open("userAndSID.txt","r+")
perms = open('permissions','r+')
newperms = open('updatedPermissions','w+')

replacements = {}

### Adds user and sid from input file into replacements dictionary.
for line in sids:
	user, sid = line.split('\t')
	replacements.update({sid.rstrip():user.rstrip()})



for x in perms.readlines():
	for ruser, rsid  in replacements.items():
		line = line.replace(rsid, ruser)
	newperms.write(line)



#### Closes files ####

sids.close()
perms.close()
newperms.close()


#### Failed Code ####

'''
####
for line in perms:
	for ruser, rsid  in replacements.iteritems():
		line = line.replace(rsid, ruser)
	newperms.write(line)

####
indata = perms.read()
newperms.write(indata)

for aline in newperms:
	print aline

for line in sids:
	user, sid = line.split('\t')
	print user, sid

####
for line in perms:
	for src, target in replacements.iteritems():
		line = line.replace(src, target)
		print line
	newperms.write(line)

'''
