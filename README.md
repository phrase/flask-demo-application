# flask-demo-application

A simple Flask demo application showing [PhraseApp](https://phraseapp.com/) In-Context-Editor integration. Built on top of [Flaskr](http://flask.pocoo.org/docs/0.10/tutorial/introduction/), the Flask tutorial app.

For a full step-by-step tutorial, check out our blog post: [Localization For Flask Applications](https://phraseapp.com/blog/posts/python-localization-flask-applications/)

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
* [PhraseApp](https://phraseapp.com)
* [PhraseApp Documentation](https://help.phraseapp.com)
* [Step-by-Step Tutorial for Flask localization and PhraseApp integration](https://phraseapp.com/blog/posts/python-localization-flask-applications/)
