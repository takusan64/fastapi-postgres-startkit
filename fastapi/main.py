from fastapi import FastAPI, Request
from router.router import router
from middleware import middleware
from openapi import openapi_util
from openapi import metadata
import config
from database.database_util import DataBase_Util

db_util = DataBase_Util(
  host = config.DB_HOST,
  port = config.DB_PORT,
  user = config.DB_USER,
  password = config.DB_PASSWORD,
  database = config.DATABASE
)

app = FastAPI(
  title = metadata.title,
  description = metadata.description,
  version = metadata.version,
  license_info = metadata.license_info,
  openapi_tags = metadata.tags_metadata
)

# Wake up Event
@app.on_event("startup")
async def startup_event():
  try:
    openapi_util.create_openapi_jsonfile(app)
    db_util.connect_check()
  except Exception:
    print("Application startup is not completed.")
    raise

# request entry point
@app.middleware("http")
async def entry_point(request: Request, call_next):
  middleware.middleware_call()
  response = await call_next(request)
  return response

# RESR API Router
app.include_router(router)