# is there a car in the picture?

## What is this?
This is an api to detect if there's a vehicle in the supplied picture. Based on https://github.com/kcg2015/Vehicle-Detection-and-Tracking   

## How to use it
```bash
$ docker build -t iscar .
$ docker run -it --rm -v /path/to/images:/path/to/images -p 8000:8000 iscar
$ curl -XPOST -H 'Content-Type: application/json' -d '{"image":{"filename":"/path/to/images/car.jpg"}}'
{"object": "car", "confidence": 0.9925153255462646, "box": [141, 308, 353, 741]}

$ curl -XPOST -H 'Content-Type: application/json' -d '{"image":{"filename":"/path/to/images/no_car.jpg"}}'
{"object": false}
```
