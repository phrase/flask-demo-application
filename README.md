# flask-demo-application (DEPRECATED)

![maintenance-status](https://img.shields.io/badge/maintenance-deprecated-red.svg)

> This repository for the demo app of Phrase Strings In-Context Editor with `Flask-Phrase` has been deprecated and is no longer maintained. Please refer to the [Flask-Phrase](https://github.com/phrase/Flask-Phrase) repository, where the demo has been moved to and will be maintained. 
 
<hr />

A simple Flask demo application showing [Phrase](https://phrase.com/) In-Context-Editor integration. Built on top of [Flaskr](http://flask.pocoo.org/docs/0.10/tutorial/introduction/), the Flask tutorial app.

For a full step-by-step tutorial, check out our blog post: [Localization For Flask Applications](https://phrase.com/blog/posts/python-localization-flask-applications/)

## Install

Clone this repository

```
git clone https://github.com/phrase/flask-demo-application
```

Install the required dependencies:

```
pip install flask flask-phrase
```

Configure your ProjectID in ```templates/layout.html```

```
projectId: "YOUR-PROJECT-ID"
````

Run the app!

```
python flaskr.py
````

## Further reading
* [Phrase](https://phrase.com)
* [Phrase Documentation](https://help.phrase.com)
* [Step-by-Step Tutorial for Flask localization and Phrase integration](https://phrase.com/blog/posts/python-localization-flask-applications/)
