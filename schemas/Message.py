from pydantic import BaseModel


class Message(BaseModel):
  contenu : str
