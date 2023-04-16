from Flask_API.api.myapi import api
from flask_restx import Resource
from Flask_API.api.database.db import all_emails, single_email, get_all_non_spam_email, get_all_spam_email
from flask import jsonify

namespace = api.namespace("emails", description="An endpoint for all spam emails")


@namespace.route("/")
class Emails(Resource):
    def get(self):
        return jsonify(all_emails())


@namespace.route("/<int:index>")
class SingleEmail(Resource):
    def get(self, index):
        return jsonify(single_email(index))


@namespace.route("/non_spam")
class NonSpamEmails(Resource):
    def get(self):
        return jsonify(get_all_non_spam_email())


@namespace.route("/spam")
class NonSpamEmails(Resource):
    def get(self):
        return jsonify(get_all_spam_email())

