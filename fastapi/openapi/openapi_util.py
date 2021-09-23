import json

def create_openapi_jsonfile(app):
  try:
    openapi_data = app.openapi()
    with open('openapi.json', 'w') as f:
      json.dump(openapi_data, f, ensure_ascii=False, indent=2)
    print("Created OpenAPI JSON File")
  except Exception:
    print("Created OpenAPI Error")
    raise