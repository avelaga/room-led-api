# Flask backend for my room leds
To run:
- Install the dependencies with the command, 'pip install -r requirements.txt'
- From the root of the repo, run 'export FLASK_APP=api.py' to set the file that flask will direct to
- Run 'flask run -h 0.0.0.0 -p 8000' to start the server

The server will now be running at <ip/hostname>:8000 on the local network.

The hue endpoint takes a required parameter, hue, that must be an int.
You can do this by accessing the get endpoint - '/?hue=<:number>'

### To start at boot with the use of screen:
- Run `nano startup` at the home directory to create a script
- Copy in this - 
```#!/bin/bash```
```cd /home/pi/room-led-api && export FLASK_APP=api.py && flask run -h 0.0.0.0 -p 8000```
- Run `sudo nano /etc/rc.local` to edit a file that runs at boot and add `sudo su - pi -c "screen -dm -S pistartup ~/startup"` at the end right before `exit 0`. This starts a detached screen named pistartup and then runs the script startup in it.
