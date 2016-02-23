# eveningmeeting_fun

## programme:

- turn on/off light with a script on the pi
  - relay
  - transistor
  - briefly explain the different raspberry pi pins (gpio vs static voltage out pins) and why we need the transistor.
  - We want to show that:
    - it's easy to use physical devices
  - Status: Relay can be controlled by pi, script has been commited (run gpio_part_1.py)
    
    
- build restful server (control lamp)
  - We want to show that:
    - it easy to build an API
    - e.g. /myserver/lamp/on
           /myserver/lamp/off
 - Status: Relay can be controlled by on/off commands (run gpio_part_2.py)
  
- web app to exercise api
  - We want to show that:
    - it's easy to build a backend
    - it is easy to build a little app
  - Status: We currently only have a flask script that we can use to post/get the status(gpio_part_3.py). No proper front-end yet.
   
    
- getting sensor data from the pi
    - Mention that lots of different protocols are supported by the pi: 1-wire, i2c. For all of them there is lots of information online.
    - We will not bother with recording the values into a db but can mention sqlite as an easy way to do so.
    - We want to show that:
       - you can use input data from sensors in order to control something
    - Status: We can use gpio_part_4.py to get sensor readings from a dummy sensor or the real thing. No shiny front end yet.

- listen to tweets to turn on/off the heater/lamp
  - people tweet on/off
  - average on the last 10 tweet
  - We want to show that:
    - Everything is awesome!
  - Status: Twitter voting functionality has been added in gpio_part_5.py but no shiny front end is available yet.



- more:
GPIO zero


- tell Iain to shut up about his Nest (http://www.bbc.co.uk/news/technology-35311447)


# need
- lamp (Benoit)
- an audio output cable (anniek + benoit)
- speaker (anniek)
- charging the speaker, anniek!
- router and lan cables

