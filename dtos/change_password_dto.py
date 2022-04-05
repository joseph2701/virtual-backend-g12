from config import validador,fields,validate

class ChangePasswordRequestDTO(validador.Schema):
    token=fields.String(required=True)
    password=fields.String(validate=validate.Length(min=6))

