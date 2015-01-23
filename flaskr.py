#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Flaskr
    ~~~~~~

    A microblog example application written as Flask tutorial with
    Flask and sqlite3.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask.ext.babel import Babel, gettext as gettext_babel, ngettext as ngettext_babel

# create our little application :)
app = Flask(__name__)

# create a Bable instance for our app
babel = Babel(app)

# Check the Accept-Language header and make a smart choice
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())


# Create helpers for PhraseApp
def gettext(msgid):
    if app.config['PHRASE_ENABLED']:
        return "{{__phrase_" + msgid + "__}}"
    else:
        return gettext_babel(msgid)

def ngettext():
    if app.config['PHRASE_ENABLED']:
        return "{{__phrase_" + msgid + "__}}"
    else:
        return ngettext_babel(msgid)

# Reload Jinja gettext 
app.jinja_env.install_gettext_callables(
    gettext,
    ngettext,
    newstyle=True
)


# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default',
    LANGUAGES = {
    'en': 'English',
    'de': 'Deutsch'
    },
    PHRASE_ENABLED = True
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
               [request.form['title'], request.form['text']])
    db.commit()
    flash(gettext('New entry was successfully posted'))
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = gettext('Invalid username')
        elif request.form['password'] != app.config['PASSWORD']:
            error = gettext('Invalid password')
        else:
            session['logged_in'] = True
            flash(gettext('You were logged in'))
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash(gettext('You were logged out'))
    return redirect(url_for('show_entries'))

app.run(host='0.0.0.0', port=5000)
