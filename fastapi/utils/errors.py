from typing import Union

class ApiError(Exception):
  status_code: int = 400
  detail: str = 'API error'
  openapi_response: dict[str, Union[int, str]]

class Error_400(ApiError):
  status_code = 400
  detail = "Bad Request"
  openapi_response = {
    status_code: {
      "description": detail,
      "content": {
        "text/plain": {
          "example": detail
        }
      }
    }
  }

class Error_401(ApiError):
  status_code = 401
  detail = "Unauthorized"
  openapi_response = {
    status_code: {
      "description": detail,
      "content": {
        "text/plain": {
          "example": detail
        }
      }
    }
  }

class Error_404(ApiError):
  status_code = 404
  detail = "Not Found"
  openapi_response = {
    status_code: {
      "description": detail,
      "content": {
        "text/plain": {
          "example": detail
        }
      }
    }
  }

