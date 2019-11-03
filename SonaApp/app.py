from flask import Flask
from flask.views import MethodView
from flask_smorest import Api, Blueprint, abort


# Schemas
from schemas.MainMenuInfo import MainMenuInfoSchema
from schemas.Schedule import ScheduleSchema
from schemas.StudyInfo import StudyInfoSchema
from schemas.StudyPage import StudyPageSchema

# Wrapper to use
from SonaWrap.Wrapper import SonaWrap

# initialize app
app = Flask('SonaApi')
app.config['OPENAPI_VERSION'] = '3.0.2'
app.config['OPENAPI_URL_PREFIX'] = "/openapi"
app.config['OPENAPI_REDOC_PATH'] = "/viewRe"
app.config['OPENAPI_SWAGGER_UI_PATH'] = "/viewUi"
app.config['OPENAPI_SWAGGER_UI_VERSION'] = "3.18.3"

api = Api(app)


#get blueprints and register them
from SonaApp.routes.auth import authBlp
from SonaApp.routes.studyPage import spBlp

api.register_blueprint(authBlp)
api.register_blueprint(spBlp)