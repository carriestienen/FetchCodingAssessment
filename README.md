# FetchCodingAssessment

This application calculates pixel coordinate values for an image that is to be displayed on a two dimensional surface given the dimensions of the image and the corner points of the image as it is to be displayed.

Flask app that accepts a JSON body at `http://localhost:5000/classify`. Expects two arguments named `dimensions` and `points` in the JSON body. 

Example request body:

```
{
    "dimensions":[3,3],
    "points":[[1, 1], [3, 1], [1, 3], [3, 3]]
}
```

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
