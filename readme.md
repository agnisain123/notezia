<div align="center">
  <h1 align="center">Project Notezia</h1>

  <p align="center">
    A simple protected notes taking application
    <br />
    <a href="#">Live Preview</a>
    ·
    <a href="https://github.com/agnisain123/notezia/issues">Report Bug</a>
    ·
    <a href="https://github.com/agnisain123/notezia/issues">Request Feature</a>
  </p>
</div>

[![Contributors](https://img.shields.io/github/contributors/agnisain123/notezia.svg)](https://github.com/agnisain123/notezia/graphs/contributors) [![Forks](https://img.shields.io/github/forks/agnisain123/notezia.svg)](https://github.com/agnisain123/notezia/network/members) [![Issues](https://img.shields.io/github/issues/agnisain123/notezia.svg)](https://github.com/agnisain123/notezia/issues) [![Pull Request](https://img.shields.io/github/issues-pr-closed-raw/agnisain123/notezia)](https://github.com/agnisain123/notezia/pulls)


A simple protected notes-taking application

## Contents

1. [Description](#description)
1. [Project structure](#project-structure)
1. [Installation](#installation)
1. [Live demo](#live-demo)
1. [Built with](#built-with)
1. [Authors](#authors)
1. [License](#license)

## Description

This project is about a simple notes taking application where users, without requiring to register or login can save their notes using password protection.

## Project structure

```
├── env/                  virtualenv (gitignored)
├── notezia/              entry point of django application
  ├── notes/              django app named 'notes' with the code for our api
  ├── notezia/            default django application
  ├── templates/          html files go here
  ├── statics/            static assets for frontend
  ├── manage.py           entry point to the django application
└── readme.md             details and instructions about the project go here

```

## Installation

A step by step series of examples that tell you how to get a development env running locally:

1. Make sure you clone the repo and have django4.0 installed in your system and properly configured
2. Create a virtual environment using the command `virtualenv env`
3. Type `source env/bin/activate` on linux or `source env/Scripts/activate` on windows to enter the virtual env
4. Type `pip3 install -r requirements.txt` to install all required python packages
5. You may use your own database and edit the notezia/settings.py file OR follow the database config under notezia/settings.py file to create a database with the same configurations used.
5. cd to the notezia directory and run the command `python manage.py makemigrations`


## Live demo

-- To be added soon --


## Built with

- [Django](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [HTML - CSS - JS](https://developer.mozilla.org/en-US/docs/Web/HTML)

## Authors

<a href="https://github.com/agnisain123/notezia/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=agnisain123/notezia" />
</a>

## License

This project is licensed under the GNU Public License 3.0 - see the [LICENSE](LICENSE) file for details.
