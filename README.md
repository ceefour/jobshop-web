# Jobshop Web

by Hendy Irawan

## jobshop folder

jobshop folder contains prebuilt jobshop for Windows (`jobshop.exe`) and
for Linux amd64 (`jobshop`).

## Re-compiling jobshop backend

    gcc jobshop.c simlib.c -lm -o jobshop

If you get:

    simlib.c:(.text+0x15f1): undefined reference to `log'

Make sure you include `-lm`

## Launch

    pip install Flask

Better way for debug mode:

    set FLASK_APP=jobshop-web.py
    set FLASK_DEBUG=1
    flask run --host=0.0.0.0

Better way for production mode:

    set FLASK_APP=jobshop-web.py
    set FLASK_DEBUG=0
    python -m flask run --host=0.0.0.0

Old way:

    python jobshop-web.py

Open in web browser:

    http://localhost:5000/
