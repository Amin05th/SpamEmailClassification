from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

email_table = db.Table("predictions",
                       db.Column("id", db.Integer, primary_key=True),
                       db.Column("y_true", db.Integer),
                       db.Column("LogisticRegression", db.Integer),
                       db.Column("MultinomialNB", db.Integer),
                       db.Column("GaussianNB", db.Integer),
                       db.Column("BernoulliNB", db.Integer),
                       db.Column("IsolationForest", db.Integer))


def all_emails():
    emails = db.session.query(email_table).all()
    return [
        {
            "id": email[0],
            "y_true": email[1],
            "LogisticRegression": email[2],
            "MultinomialNB": email[3],
            "GaussianNB": email[4],
            "BernoulliNB": email[5],
            "IsolationForest": email[6],
        }
        for email in emails
    ]


def single_email(email_id):
    emails = db.session.query(email_table).filter_by(id=email_id)[0]
    return {
        "id": emails[0],
        "y_true": emails[1],
        "LogisticRegression": emails[2],
        "MultinomialNB": emails[3],
        "GaussianNB": emails[4],
        "BernoulliNB": emails[5],
        "IsolationForest": emails[6],
    }


def get_all_non_spam_email():
    emails = db.session.query(email_table).filter_by(y_true=0).all()
    return [
        {
            "id": email[0],
            "y_true": email[1],
            "LogisticRegression": email[2],
            "MultinomialNB": email[3],
            "GaussianNB": email[4],
            "BernoulliNB": email[5],
            "IsolationForest": email[6],
        }
        for email in emails
    ]


def get_all_spam_email():
    emails = db.session.query(email_table).filter_by(y_true=1).all()
    return [
        {
            "id": email[0],
            "y_true": email[1],
            "LogisticRegression": email[2],
            "MultinomialNB": email[3],
            "GaussianNB": email[4],
            "BernoulliNB": email[5],
            "IsolationForest": email[6],
        }
        for email in emails
    ]
