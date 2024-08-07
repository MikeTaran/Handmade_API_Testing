from pydantic import BaseModel, field_validator


class UserModel(BaseModel):
    email: str
    nickname: str
    name: str
    uuid: str

    # кастомный валидатор
    @field_validator("email","nickname", "name", "uuid")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value
# response = {
#   "email": "max@gmail.com",
#   "password": "password",
#   "name": "Max",
#   "nickname": "max"
# }
# user = UserModel(**response)
# print(user.nickname)


