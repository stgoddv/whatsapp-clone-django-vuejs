# Whatsapp Vuejs Django Channels Clone

A real time chat personal project built upon django, django rest framework, django channels and vuejs.

建立在django，django rest框架，django频道和vuejs之上的实时聊天个人项目。

![Demo](https://github.com/stgoddv/django-channels-tutorial/blob/develop/demo/demo.gif?raw=true)

# Table of Contents

1. [Motivation](#motivation)
2. [Installation](#installation)
3. [Features](#features)
4. [WorkInProgress](#workinprogress)
4. [Roadmap](#roadmap)
5. [Contribution](#contribution)
6. [License](#license)

### Motivation

This is an educational project trying to replicate some famous real time chat app.

The idea came up when a customer ask me to built a chat for his app. I notice that there aren't chat projects involving django channels and vueJs so I decided to make an open source chat.

It's important to emphasize that although this architecture could work in a production enviroment for small to medium size companies, this isn't really suitable for large scale deployment as whatsapp or telegram, for example. For that cases the recommended architecture and technologies are based on XAMPP.

### Installation for dev vesion

1. First create a virtual machine with python

> python3 -m venv venv

2. Activate the environment

> source venv/bin/activate

3. Install required dependencies

> pip3 install -r requirements.txt

4. Cd into django folder and apply migrations

> cd djchat && python manage.py migrate

5. Run django backend

> python manage.py runserver

6. Open a new terminal and cd into frontend folder

> cd djchat/frontend

7. Install required modules

> npm i

8. Finally run frontend dev mode

> npm run serve


### Features

Latest version: 1.0  
* Login and register forms
* Send, receive, accept and reject invitations from another users
* Profile with personal editable tagline
* Emoticons supported

Messages behaviour:  
* Message received by the server is marked with 1 check
* Message received by the other user is marked with 2 checks
* Message read by the other user is marked with a colored double check


### WorkInProgress

Currently the efforts are focused on:  
* More unit testings in backend and frontend
* Refactory of the Vuex messages architecture
* There are some things that should be communicated by channels and not by rest API


### Roadmap

* Two way registration for email verification
* Dockerization 
* JWT cookie support
* Groups support
* Block users
* Upload avatars
* Optional sound when new message arrives
* General settings panel
* Emoticons selector
* Send pictures
* Send videos
* Send links

Please understand that this is a project that I'm doing as a hobby in my little free time. Feel free to make PR if you can work on some functionality.

### Contribution

This is a pretty basic project that I did in a couple weeks. If you want to contribute improving this, adding more functionality of fixing issues I'll be glad to receive PR.

### License

MIT License

Copyright (c) 2020 Santiago Díaz de Valdés Williamson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
