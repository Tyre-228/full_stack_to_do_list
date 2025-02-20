from marshmallow import Schema, fields

class UserSchema:
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)