from pydantic import BaseModel, HttpUrl, Field, FilePath
from tools.fakers import fake

class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")
    directory: str  = Field(default="tests")
    upload_file: FilePath

class FileSchema(BaseModel):
    """Описание структуры файла."""
    id: str
    filename: str
    directory: str
    url: HttpUrl

class CreateFileResponseSchema(BaseModel):
    """Описание структуры ответа создания файла."""
    file: FileSchema

class GetFileResponseSchema(BaseModel):
    """Описание структуры ответа получения файла."""
    file: FileSchema
