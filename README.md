# Project Title

Sample python API to generate database query from known input format.
Currently, only SQL query is managed but we can image managing mongo queries later.
How we can warn the api which query is requested ? I imagine to have a specific HTTP HEADER [ONGOING]

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

To run this sample, we are going to create an image with Docker. Make sure you have latest stable version of Docker installed. Please checkout the following official [guide](https://docs.docker.com/engine/)

Otherwise, we recommend using the latest version of Python in order to use Flask which supports Python 3.6 and newer.


### Installing

A step by step series of examples that tell you how to get a development env running

Please install requirements:

```
pip3 install -r requirements.txt
```

Then you will be able to run it locally:
```
python3 -m flask run
```

Or

Use Docker to have all in container:
```
docker build -t MY_FAMOUS_NAME .
```
Then run it
```
docker run -d -p 5000:5000 --name MY_FAMOUS_CONTAINER MY_FAMOUS_NAME
```

You will be able to do a CURL request in order to test it:
```
curl -X POST 'http://127.0.0.1:5000/generate' -H 'Content-Type: application/json' -d '{"fields": ["name"],"filters":{"field":"name","value":1,"predicate":"contains"}}'
```
You should receive:
```
SELECT name FROM tows WHERE name LIKE "%1%"
```
## Running the tests

```
python3 -m unittest test_app.py
```
```
....
----------------------------------------------------------------------
Ran 4 tests in 0.003s
OK
```
## Built With

* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Flask is a micro web framework written in Python
* [Cerberus](https://docs.python-cerberus.org/en/stable/) - powerful, simple and lightweight data validation 

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
