from fastapi import APIRouter, HTTPException, Depends
from router import router_countries
from openapi import response as openapi_res
from openapi import query as openapi_query
from utils.errors import Error_400

router = APIRouter()

# endpoint /countries
# return 登録されたした国情報を取得 [object]
@router.get(
  '/countries',
  response_model=openapi_res.Response_Model,
  tags=["country"],
  responses=Error_400.openapi_response
)
def get_country(query:openapi_query.Query_Model = Depends()):
  try:
    res = router_countries.get_country(query.country_id)
    return res
  except Exception:
    raise HTTPException(status_code=Error_400.status_code, detail=Error_400.detail)