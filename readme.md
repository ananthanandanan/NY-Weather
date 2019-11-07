### This is simple weather app
**What it does do**
it takes the user input ,and gets the data and stores the city in database ,finally showing the weather of the desired city.




## How to build 

clone the weather app.


### Getting Started

+ First install the python,if you not have already done so.

```console
$ apt-get update

$ apt-get install python3.7
```

+ Now install the virtual environment .This is great because allows you to work on a specific project without affecting other projects. So for that you have to install the pip (package manager) ,then install the ***virtual env*** .

```console
    $ sudo apt-get install python-pip
```

+ Now to install the virtualenv 

```console
$ pip install virtualenv
```
+ Create a virtualenv 


```console
$ virtualenv first_project
```
If you want a specific python type.

```console
$ virtualenv -p /usr/bin/python3.7 first_project
```
+ Now to activate the virtualenv:

```console
$ .first_project/bin/activate
```
+ Install Django

```console
$ pip install django
```

+ Start the project 

```console
$ django-admin starproject weather_app

```


+ Sign up to the Open Weather app and you will get an secret key ie: your API key 

### Insert API key

+ Insert the API key to the variable ***api_key***

+ Now you can host the weather app

