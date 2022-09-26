from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from healthcheck import HealthCheck
from typing import Any, Dict
from starlette.responses import Response
from .core import db
from .core.config import USER_WEBHOOK, PASSWORD_WEBHOOK
from .crud.save_data import SaveData

security = HTTPBasic()
health = HealthCheck()
app = FastAPI()

@app.post("/fb_audience/")
def test(request: Dict[Any,Any], credentials: HTTPBasicCredentials = Depends(security)):
    
    if (credentials.username != USER_WEBHOOK) or (credentials.password != PASSWORD_WEBHOOK):
        return 'Authentication failed'

    else:
        fb_audience = db.Db.fb_table()
        cur,conn = db.Db.connect()
        SaveData(cur,conn).fb_save_data(fb_audience)
        db.Db.disconnect(cur, conn)

    return request

@app.post("/gg_audience/")
def test(request: Dict[Any,Any], credentials: HTTPBasicCredentials = Depends(security)):
    
    if (credentials.username != USER_WEBHOOK) or (credentials.password != PASSWORD_WEBHOOK):
        return 'Authentication failed'

    else:
        gg_audience = db.Db.gg_table()
        cur,conn = db.Db.connect()
        SaveData(cur,conn).gg_save_data(gg_audience)
        db.Db.disconnect(cur, conn)

    return request

@app.get("/health-check/", include_in_schema=False)
def healthcheck():
    message, status_code, headers = health.run()
    return Response(content=message, status_code=status_code, headers=headers)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8080, debug=True, reload=True)
