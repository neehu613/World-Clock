# World-Clock

The user is expected to enter any place of the world, and this project displays the current time at that place using an analog clock which is explicitly drawn using pygame.
The clock runs just like an actual clock, with all the 3 hands working as expected.

Features:

1. Made use of python's BeautifulSoup to scrape an online 'time' showing website.
2. Converted the time into a pygame display, where the user is presented by an actual clock with all the hands running as expected.
This project gets the time at the place which is entered by the user, and then shows the time using an analog clock(seconds hand also works) which is built using pygame.
The implementation of the analog clock is done in the file 'clock.py'.
All the necessary calculations to bring up the clock are done in 'maths.py'
The web-scraping script 'timeScraper.py', gets the real time of the entered place.

Clock implementation involves three lists - hours, minutes and seconds, where each list has all the pairs of (x,y) co-ordinates.
These (x,y) co-ordinates are the points where the respective clock hand can be at a particular time.
Using those (x,y) co-ordinates and the clock's center (h,k), and the angle swept per unit time by each clock hand, the hands are drawn.
Using the time module, the program is made to 'sleep' every 1 second and the clock hands are updated correspondingly.

Formula used to calculate the (x, y) co-ordinates of the clock hand, given the center (h,k), the radius r and the angle A:
    <b> <br>x = h + r*math.cos(A) <br>
			  y = k + r*math.sin(A)
    </b>

<i>Run the file named 'timeScraper.py'</i>

Currently working on the weather part, which also shows the weather condition at the entered place.
