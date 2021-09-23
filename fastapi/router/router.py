from fastapi import APIRouter, HTTPException, Depends
from router import router_countries
from openapi import response as openapi_res
from openapi import query as openapi_query
from utils.errors import error_400

router = APIRouter()

# endpoint /countries
# return 登録されたした国情報を取得 [object]
@router.get(
  '/countries',
  response_model=openapi_res.res_model,
  tags=["country"],
  responses=error_400.openapi_response
)
def get_country(query:openapi_query.query_model = Depends()):
  try:
    res = router_countries.get_country(query.country_id)
    return res
  except Exception:
    raise HTTPException(status_code=error_400.status_code, detail=error_400.detail)