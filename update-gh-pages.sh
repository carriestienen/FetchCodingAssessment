# bail on any errors
set -e

# install dependencies
apt update && apt install jupyter-nbconvert git

# execute and render the results of the jupyter notebook
jupyter nbconvert fetch-assignment-notebook.ipynb --to html
cp fetch-assignment-notebook.html /tmp

# clone the repo in a temp build location
cd /tmp
git clone "https://${GH_TOKEN}@github.com/carriestienen/FetchCodingAssessment.git"

# update the contents of the gh pages branch
cd FetchCodingAssessment
git checkout jupyter-gh-pages
touch .nojekyll
mv ../fetch-assignment-notebook.html .

# update the gh pages branch
git add .
git commit -m "GH Pages Update $(date)"
git push origin jupyter-gh-pages
