# -*- coding: utf-8 -*-
# from urlparse import urlparse
# from werkzeug import url_quote
# from flask import Markup

class Extension(object):

    def __init__(self, name, author, description,
                 github=None, gitlab=None, bitbucket=None, docs=None, website=None,
                 approved=False, notes=None):
        self.name = name
        self.author = author
        self.description = description
        # self.description = Markup(description)
        self.github = github
        self.gitlab = gitlab
        self.bitbucket = bitbucket
        self.docs = docs
        self.website = website
        self.approved = approved
        self.notes = notes

    def to_json(self):
        rv = vars(self).copy()
        # rv['description'] = unicode(rv['description'])
        return rv

    @property
    def pypi(self):
        pass
        # return 'http://pypi.python.org/pypi/%s' % url_quote(self.name)

    @property
    def docserver(self):
        if self.docs:
            return ''
            # return urlparse(self.docs)[1]




# This list contains all extensions that were approved as well as those which
# passed listing.
extensions = [
    Extension('Flask-OpenID', 'Armin Ronacher',
        description='''
            <p>Adds <a href="http://openid.net/">OpenID</a> support to Flask.
        ''',
        github='mitsuhiko/flask-openid',
        docs='http://pythonhosted.org/Flask-OpenID/',
        notes='''
            Short long description, missing tests.
        '''
    ),
    Extension('Flask-Babel', 'Armin Ronacher',
        description='''
            <p>Adds i18n/l10n support to Flask, based on
            <a href=http://babel.edgewall.org/>babel</a> and
            <a href=http://pytz.sourceforge.net/>pytz</a>.
        ''',
        github='mitsuhiko/flask-babel',
        docs='http://pythonhosted.org/Flask-Babel/',
        approved=True,
        notes='''
            How to improve: add a better long description to the next release.
        '''
    ),
    
]

# for ext in extensions:
#     print(ext.to_json())

# v_extensions = [ext.to_json() for ext in extensions]
# print(v_extensions)

from flask import jsonify
import json

print(json.dumps( {"category":"success"}))