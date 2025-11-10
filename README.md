I was tired of searching for something that worked for us Victorians... having see similar items for NSW and QLD was just disapopinted nothing existed for us. Having a property in central victoria I always dreamed of having a card display fire restriction data.

I tried to do something last year, got busy, and this year its done - it took 2 days of hard work, lots of issues of getting colors and fonts to work, and then making sure it worked on the mobile and PC environments

The scraping was rather easy - it being more understood by myself - python....

So anyway - I will update the docs later - I have really just placed it here - so I do not loose it - or break it... Maybe its useful for yourself! Be thrilled to see any enhancements or better code than what I have done... (Im off to do Total Fire Bans next)

Installation is pretty easy...

Configuration.yaml - all the bits to add into your configuration file
Fire_restriction_scraper.py - the python code that scrapes the CFA website to get restriction dates or find out there is none available at present.
Markdown card.yaml - just some yaml to put together a card to display the information... It turns Green if there is no restrictions and you can burn off / amber if restrictions are coming in during the next 3 weeks and red if you cannot burn off
(I think it should go Green again if at the end of the period the end date is in the past - just wait and see what happens in May next year)


Of course this is all experimental - until we are all comfortble with the logic - truth is at the CFA website - still check that - do not trust my code !!!! (Not Yet)


The only big gotcha is where to place the python script...
I used the file editor in home assistant to create a folder Scripts under config - ie. /homeassistant/config/scripts and put the fire_restirction_scraper.py there... You should be able to put it in other locations of your choosing
However in using command line to call it - you must give it a path... I am led to believe some hardware and how you run HA might change how you call it...
In my case using a Raspberry PI the call in the yaml file is:
      command: "python3 config/scripts/fire_restriction_scraper.py '{{ states('sensor.fire_municipality') }}' start"
i am led to believe in some instances you may need to change it by adding the prefix of / to the config directory....
      command: "python3 /config/scripts/fire_restriction_scraper.py '{{ states('sensor.fire_municipality') }}' start"

You will work it out !
Hope it somewhat useful for others - it took me 3 goes over several years and lots of heartache to get here - ENJOY !
