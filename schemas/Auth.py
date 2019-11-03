from marshmallow import Schema,fields

class CredentialsSchema(Schema):
    username = fields.Str()
    password = fields.Str()

class TokenSchema(Schema):
    token = fields.Str()

class AuthHeaderSchema(Schema):
    token = fields.Str()