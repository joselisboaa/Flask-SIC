from marshmallow import Schema, validate, fields
from api.schemas import PlainLojaSchema


class PlainClienteSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(
        required=True,
        validate=validate.Length(
            min=3, max=255, error='O nome deve ter entre {min} e {max} caracteres.'
        ),
        error_messages=dict(
            required="O campo é obrigatório.",
            null="O campo não pode ser nulo.",
            invalid="O campo só pode receber strings."
        )
    )
    endereco = fields.Str(
        required=True,
        validate=validate.Length(
            min=5, max=255, error='O nome deve ter entre {min} e {max} caracteres.'
        ),
        error_messages=dict(
            required="O campo é obrigatório.",
            null="O campo não pode ser nulo.",
            invalid="O campo só pode receber strings."
        )
    )


class ClienteSchema(PlainClienteSchema):
    loja_id = fields.Int(load_only=True, required=True,
                         error_messages=dict(
                             required="O campo é obrigatório."
                         ))
    loja = fields.Nested(PlainLojaSchema(), dump_only=True)


class ClientQuerySchemas(Schema):
    id = fields.Int()
    nome = fields.Str()
    endereco = fields.Str()
    loja_id = fields.Int()
