#!/bin/bash

# bail on any errors
set -e

# install dependencies
sudo apt update && sudo apt install jupyter git && sudo pip3 install matplotlib pylint

# run pylint
pylint project.py -d invalid-name
pylint proj_unittest.py -d invalid-name -d wildcard-import
pylint server.py -d import-error

# run unit tests
python3 proj_unittest.py

# execute and render the results of the jupyter notebook
jupyter-nbconvert --execute --to html fetch-assignment-notebook.ipynb
cp fetch-assignment-notebook.html /tmp

# clone the repo in a temp build location
cd /tmp
git clone "https://${GH_TOKEN}@github.com/carriestienen/FetchCodingAssessment.git"

# update the contents of the gh pages branch
cd FetchCodingAssessment
git checkout jupyter-gh-pages
touch .nojekyll
mv ../fetch-assignment-notebook.html ./index.html

# update the gh pages branch
git config --global user.email "update-automation@example.com"
git config --global user.name "Pages Updater"
git add .
git commit -m "GH Pages Update $(date)"
git push origin jupyter-gh-pages
