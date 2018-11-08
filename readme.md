# Chem Caravan Web Edition
Chem Caravan is a dope game where you travel around in a Fallout 4 themed world buying and selling chems to make a profit. It's inspired by [dopewars](http://drunkmenworkhere.org/185.php), so you should check that out.

This version is a spin-off from a previous mobile app incarnation which can be found [here](https://github.com/pmaclellan/ChemCaravan).

## Setup
1. Install python 3.7.1
    * [Download Python 3](https://www.python.org/downloads/)
1. Get flask
    * `> pip install flask`
1. Get NodeJS and then Angular
    * [Download Node](https://nodejs.org/en/)
    * `> npm install -g @angular/cli`
1. Start the local server
    * `> python app.py`
1. Sell chems to kids (feature not yet supported)
    * Navigate to `127.0.0.1:5000` in browser

## Building and Serving the Angular App
The Flask server serves a compiled version of the Angular app.
1. Build the Angular app
    * `cd frontend`
    * `ng build --base-href /static/`
    * Copy the contents of `frontend/dist` into the backend. This is what will be served by the flask server. Put `index.html` into `backend/templates` and then all of the other files into `backend/static`.
    * `cd backend`
    * Launch the dev server with `python3 app.py` and then check it out in your browser at `127.0.0.1:5000`

### Front End Development
You can work on just the front end by launching the Angular app directly.
```
cd frontend
ng serve -o
```
This will launch a new browser tab with the app running in it.


Check this out for [inspiration](http://fallout.wikia.com/wiki/Happy_Trails_Caravan_Company)