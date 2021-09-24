from pydantic import BaseModel

class Response_Model(BaseModel):
  country_id: int
  country_code: str
  name_label: str