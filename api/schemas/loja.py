from marshmallow import Schema, fields, validate


class PlainLojaSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(
        required=True,
        validate=validate.And(validate.Length(max=255, min=1, error="O nome deve ter entre {min} e {max} caracteres.")),
        error_messages=dict(
            required="O campo é obrigatório.",
            null="O campo não pode ser nulo.",
            invalid="O campo só pode receber strings"
        )
    )


class LojaQuerySchema(Schema):
    id = fields.Int()
    nome = fields.Str()
