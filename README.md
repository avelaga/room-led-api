# Flask backend for my room leds
To run:
- Install the dependencies with the command, 'pip install -r requirements.txt'
- From the root of the repo, run 'export FLASK_APP=api.py' to set the file that flask will direct to
- Run 'flask run -h 0.0.0.0 -p 8000' to start the server

The server will now be running at <ip/hostname>:8000 on the local network.

The hue endpoint takes a required parameter, hue, that must be an int.
You can do this by accessing the get endpoint - '/?hue=<:number>'


