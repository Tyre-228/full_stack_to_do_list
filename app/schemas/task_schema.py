from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    text = fields.Str(required=True, validate=validate.Length(min=1, max=128))
    completed = fields.Boolean(required=True)