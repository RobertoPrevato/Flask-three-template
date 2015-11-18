# Flask-three-template
Project template for Python Flask three-tier web applications, using Aurelia web framework.
<img src="http://ugrose.com/ug.png" width="300" height="300" alt="UgRoslein" title="UgRoslein - ugrose.com" align="right" />

## Features
* Integration with [Aurelia](http://aurelia.io/) web framework.
* Project skeleton ready to use, to start a three tier web application using Flask for its presentation layer.
* Localization strategy, using Flask-Babel.
* Authentication and authorization strategies, including anonymous authentication.
* Login mechanism protected against brute forcing (stores login attempts in DB).
* DB based sessions strategy.
* MongoDB collections for accounts, sessions, login attempts.
* Example files for production deployment using Nginx and uWSGI servers.
* Skeleton for data access layers for MongoDB.
* Skeleton for unit testing.
* Custom error pages.
* Application db logger, to store and retrieve messages and exceptions logs in database

## Getting started
In order to use the Flask-Aurelia template, it`s necessary to install the software required by Aurelia (e.g. NodeJs, gulp; jspm).
Refer to the official [Aurelia getting started guide](http://aurelia.io/get-started.html).

## Branches
* [empty-project](https://github.com/RobertoPrevato/flask-three-template/tree/empty-project): empty template without any authentication strategy.
* [master](https://github.com/RobertoPrevato/flask-three-template/tree/master): template with custom authentication and authorization strategy.
* [spa-humbular](https://github.com/RobertoPrevato/flask-three-template/tree/spa-humbular): template with Humbular Single Page Application strategy.
* [spa-aurelia](https://github.com/RobertoPrevato/flask-three-template/tree/spa-aurelia): Single Page Application template using Aurelia framework.

## How to prepare the environment
* Python.
* [Flask](http://flask.pocoo.org/).
* [Flask-Babel](https://pythonhosted.org/Flask-Babel/).
* pymongo.
* pycrypto.

Refer to the [dedicated wiki page](https://github.com/RobertoPrevato/flask-three-template/wiki/Preparing-the-environment), for instructions about how to prepare the environment and install the dependencies.

## Servers setup
* Basic settings file for Nginx.
* Settings file for uWSGI.
* Development server ready to use: Flask itself.

## Grunt integration
* JavaScript bundling and minification strategy.
* LESS compilation.

## CRUD architecture
The branch spa-humbular includes a strategy to implement SPA administrative sides with CRUD functionalities.
As a working example, the user management feature has been used.

![crud-architecture](http://ugrose.com/content/demos/humbular/images/crud-architecture.gif)

For detailed information, refer to the [dedicated wiki page](https://github.com/RobertoPrevato/flask-three-template/wiki/CRUD-architecture-for-SPA).
