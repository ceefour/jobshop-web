# Jobshop Web

by Hendy Irawan

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
