import math
import timeScraper

seconds = list()
minutes = list()
hours = list()
h = 300
k = 300

def degreeToRadians(deg):
	rads = deg* 0.0174533
	return rads

def clockRunning():
	clockRun = False	
	angle = angle1 = 6
	angle2 = 0.5
	r = 280

	secs = mins = hrs = count = 0
	c1 = 600
	d1 = 300
	r1 = 280
	r2 = 200
	c2 = 500
	d2 = 300

	while not clockRun:
		
		A = degreeToRadians(angle)
		c = h + r*math.cos(A)		#cosA returns cos of A radians
		d = k + r*math.sin(A)

		if len(seconds) < 60:
			seconds.append((int(c),int(d)))

		angle += 6
		count += 1

		secs+=1

		if secs == 1:
			secs = 0
			mins += 1
			A1 = degreeToRadians(angle1)
			c1 = h + r1*math.cos(A1)
			d1 = k + r1*math.sin(A1)
			if len(minutes) < 60:
				minutes.append((int(c1),int(d1)))
			angle1 += 6
			
		if mins == 1:
			mins = 0
			hrs += 1
			A2 = degreeToRadians(angle2)
			c2 = h + r2*math.cos(A2)
			d2 = k + r2*math.sin(A2)
			hours.append((int(c2), int(d2)))
			if len(hours) == 360:
				clockRun = True
			angle2 += 1

clockRunning()

hh = timeScraper.hh
mm = timeScraper.mm
ss = 0

#hh = int(input("Enter HH: "))
hh = (hh-3)*30
if hh < 0:
	hh = 360+hh
	
#mm = int(input("Enter MM: "))
hh = hh+(mm/2)
#ss = int(input("Enter SS: "))