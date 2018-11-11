#!/bin/sh

#First build the Angular project
ng build --base-href /static/

#Clean the target directories
rm ../backend/templates/*
rm ../backend/static/*

#Then copy the files over to the backend
#index.html first
mv -f dist/frontend/index.html ../backend/templates/index.html
#then the rest
mv -f dist/frontend/* ../backend/static/