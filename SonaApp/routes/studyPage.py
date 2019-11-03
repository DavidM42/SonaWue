from flask_smorest import Blueprint
from flask.views import MethodView

from SonaWrap.Wrapper import SonaWrap

from schemas.StudyPage import StudyPageSchema
from schemas.Auth import AuthHeaderSchema

spBlp = Blueprint(
    'StudyPage', 'StudyPage', url_prefix='/studypage',
    description='Operations on studypage'
)

#This is an example blueprint to show how simple forwarding requests of sona api would be done

@spBlp.route('/')
class StudyPageView(MethodView):

    # @blp.arguments(PetQueryArgsSchema, location='query')
    #TODO decorator which gets auth header token to input here and use
    @spBlp.arguments(AuthHeaderSchema, location='headers')
    @spBlp.response(StudyPageSchema())
    def get(self, auth_header):
        """Return studyPage Info from SonaApp mobile api"""
        #TODO this way only does key error not 401 if no token given or wrong token
        sona = SonaWrap(token=auth_header["token"])

        return sona.study_page_info()
