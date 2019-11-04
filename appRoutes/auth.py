from flask_smorest import Blueprint
from flask.views import MethodView

from SonaWrap.Wrapper import SonaWrap

from schemas.Auth import CredentialsSchema,TokenSchema

authBlp = Blueprint(
    'Authentication', 'Authentication', url_prefix='/auth',
    description='Operations regarding authentication'
)

@authBlp.route('/')
class AuthMethods(MethodView):
    @authBlp.arguments(CredentialsSchema())
    @authBlp.response(TokenSchema())
    def post(self, credentials):
        """Return studyPage Info from SonaApp mobile api"""
        sona = SonaWrap(username=credentials["username"], password=credentials["password"])
        #TODO better return error given by Sona 
        #TODO e.g. return in error
        #TODO also dont return 500 but 401 if wrong credentials were given
        # ['Benutzer nicht gefunden.']
        # {'ErrorCode': -4, 'Errors': ['Benutzer nicht gefunden.'], 'Result': ''}
        return {
            "token": sona.get_token()
        }
