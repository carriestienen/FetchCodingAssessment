# FetchCodingAssessment

This application calculates pixel coordinate values for an image that is to be displayed on a two dimensional surface given the dimensions of the image and the corner points of the image as it is to be displayed.

This is a flask app that accepts a JSON body at `http://localhost:5000/classify`. Expects two arguments named `dimensions` and `points` in the JSON body. 

Example request body:

```
{
    "dimensions":[3,3],
    "points":[[1, 1], [3, 1], [1, 3], [3, 3]]
}
```

### Jupyter Notebook

[Jupyter notebook with examples and plots](https://carriestienen.github.io/FetchCodingAssessment/)

This jupyter notebooks shows several examples with different dimensions and image coordinates. The examples are also plotted for viewing simplicity.

### Github Actions

Linting and unit testing done using Github actions. The html rendered jupyter notebook execution is built with github actions and hosted on GitHub pages.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

```
Docker
Python3.8 (dev mode)
```

### Installing

For local builds

```
docker build . -t classify:latest
```

This will create a docker image for this project locally.


For developer mode

```
pip install -r requirements.txt
```

### Running

For local builds

```
docker run -p 5000:5000 -it classify:latest
```

For developer mode
```
python3.8 ./server.py
```

## Test Request with CURL

```
curl --location --request POST 'http://localhost:5000/classify' \
--header 'Content-Type: application/json' \
--data-raw '{
    "dimensions":[3,3],
    "points":[[1, 1], [3, 1], [1, 3], [3, 3]]
}'
```
