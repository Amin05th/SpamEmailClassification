from flask_restx import Api

api = Api(version="0.1", title="Iris classification prediction", description="Use this api based on your needs")


@api.errorhandler(Exception)
def error(e):
    return "Some Error occurred", e
