# Flask backend for my room leds

![img](https://github.com/avelaga/room-led-controller/blob/master/example.gif)

[i followed this tutorial to set up flask with apache](https://www.bogotobogo.com/python/Flask/Python_Flask_HelloWorld_App_with_Apache_WSGI_Ubuntu14.php)

To setup and run:
- Install the dependencies with the command, `pip3 install -r requirements.txt`
- Run `sudo apt-get install libapache2-mod-wsgi python-dev` to install the WSGI package
- Eable the i2c interface with the command `sudo raspi-config`, navigating to `Interfacing Options`, and then `I2C`
- Give apache access to the i2c pins with the command `sudo adduser www-data i2c`
- If you want to enable public access, set up port forwarding on your router to forward incoming port 80 (and port 443 if you're using https) requests to the respective ports on the pi 
- If you want to use https you'll first need to buy a domain name (you can get them dirt cheap, i use [porkbun](https://porkbun.com)) and have it point to your ip. check out [this tutorial to learn how to set up https with apache on a raspberry pi](https://pimylifeup.com/raspberry-pi-ssl-lets-encrypt/)
- I had problems with pip3 not installing flask-cors in the expected directory so i had to run `sudo pip3 install -t /usr/lib/python3/dist-packages/ flask-cors` to force it to install in the correct location
- Replace the conf file at /etc/apache2/sites-available/ with flask.conf. This tells Apache to forward incoming requests to your flask server.
- Run `sudo /etc/init.d/apache2 restart` to restart the Apache server


The hue endpoint takes a required parameter, hue, that must be an int.
You can do this by accessing the get endpoint with this syntax - '/hue?hue=<:number>'
### To deploy
Ideally you [connect an http server like apache to the server](https://flask.palletsprojects.com/en/1.1.x/deploying/mod_wsgi/) but since I'm having issues getting it working I'm temporarily having it run the dev server at startup
### To start at boot with the use of screen: (not ideal)
- Install screen with `sudo apt-get install screen`
- Go into the repo and run `chmod +x ~/startup` to give the startup script execution permissions
- Run `sudo nano /etc/rc.local` to edit a file that runs at boot and add `sudo su - pi -c "screen -dm -S api ~/room-led-api/startup"` at the end right before `exit 0`. This starts a detached screen named api and then runs the script startup in it.
- Run `sudo reboot` and see if the api works at the expected url when it's back up. To verify if the screen was created properly, ssh in and run `screen -list` to see all screens. You should see one titled pistartup which you can go into with the command `screen -r api`

## UI and Arduino Controller Repos:
[React UI running on a Raspberry Pi 4 to control the LEDs](https://github.com/avelaga/room-led-ui)

[Arduino code that controls the LEDs](https://github.com/avelaga/room-led-controller)
