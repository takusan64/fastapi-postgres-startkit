from pydantic import BaseModel

class res_model(BaseModel):
  country_id: int
  country_code: str
  name_label: str