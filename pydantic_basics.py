import uuid
from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, validator, EmailStr
from pydantic.alias_generators import to_camel

class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    @computed_field
    def username(self) -> str:
        return f"{self.first_name} {self.last_name}"
    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl


class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str = "Playwright course"
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
    preview_file: FileSchema = Field(alias="previewFile")
    created_by_user: UserSchema = Field(alias="createdByUser")

course_default_model = CourseSchema(
    id='course_id',
    title='API',
    maxScore=100,
    minScore=10,
    description='<UNK> <UNK> <UNK> <UNK> <UNK>',
    estimatedTime='3 week',
    previewFile=FileSchema(
        id="id-1234569",
        filename="my_file.txt",
        directory="my_directory",
        url="http://localhost:8000/course"
    ),
    createdByUser=UserSchema(
        email="user@gmail.com",
        lastName="Bond",
        firstName="Zara",
        middleName="Alisa",
        id="user-id"
    )
)
print(course_default_model)

course_dict = {
    'id': 'string',
    'title': 'string',
    'maxScore': 100,
    'minScore': 10,
    'description': 'string',
    'previewFile': {
        'id': "id-1234569",
        'filename': "my_file.txt",
        'directory': "my_directory",
        'url': "http://localhost:8000/course"
    },
    'estimatedTime': '1 week',
    'createdByUser': {
        'email': "user@gmail.com",
        'lastName': "Bond",
        'firstName': "Zara",
        'middleName':"Alisa",
        'id': "user-id"
    }
}
course_dict_model = CourseSchema(**course_dict)
print(course_dict_model)

course_json_str = '''
{
    "id": "string",
    "title": "string",
    "maxScore": 100,
    "minScore": 10,
    "description": "string",
    "previewFile": {
        "id": "id-1234569",
        "filename": "my_file.txt",
        "directory": "my_directory",
        "url": "http://localhost:8000/course"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName":"Alisa",
        "id": "user-id"
    }
}
'''
course_json_model = CourseSchema.model_validate_json(course_json_str)
print(course_json_model)
print(course_json_model.model_dump(by_alias=True))
print(course_json_model.model_dump_json(by_alias=True))

user = UserSchema(
    email= "user@gmail.com",
    lastName= "Bond",
    firstName= "Zara",
    middleName= "Alisa",
    id="user-id"
)

print(user.get_full_name(), user.username)
