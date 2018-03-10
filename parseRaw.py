#!/usr/bin/env python2.7

import sys
from totalopenstation.formats import nikon_raw_v200 as nikon
from totalopenstation.formats import UNKNOWN_STATION

if __name__ == "__main__":

	if len(sys.argv) != 2:
		print "usage: %s <input file>" % sys.argv[0]
	else:
		# open and check existence of file
		filename = sys.argv[1]
	try:
		with open(filename, 'r') as f:
			filedata = f.read()
			f.close()

		parsedData = nikon.FormatParser(filedata)
		pts = parsedData.points
		# compute and print outputs
		print "type id: (x,y,z)"
		for pt in pts:
			ptid = pt.id
			pttype = pt.properties['desc']
			# totalopenstation defaults the theodolite location to UNKNOWN_STATION
			# currently if it's location doesnt exist in the RAW file this hack
			# subtracts that location so we get all our locations assuming the
			# theodolite was at (0,0,0)
			x = pt.geometry.x - UNKNOWN_STATION.x
			y = pt.geometry.y - UNKNOWN_STATION.y

			if pttype == "ST":
				z = pt.geometry.z - UNKNOWN_STATION.z + pt.properties['ih']
			else:	
				z = pt.geometry.z - UNKNOWN_STATION.z

			if 'attrib' in pt.properties:
				print "%s %s %s: %.3f,%.3f,%.3f" % (pttype, pt.properties['point_name'], pt.properties['attrib'], x, y, z)
			else:
				print "%s %s: %.3f,%.3f,%.3f" % (pttype, pt.properties['point_name'], x, y, z)
			
	except IOError:
		print "file %s not found" % filename