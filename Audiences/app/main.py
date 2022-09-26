from fastapi import FastAPI
from .core import db
from typing import Any, Dict
from .crud.save_data import SaveData

app = FastAPI()

@app.post("/fb_audience/")
def test(request: Dict[Any,Any]):
    
    fb_audience = db.Db.fb_table()
    cur,conn = db.Db.connect()
    SaveData(cur,conn).fb_save_data(fb_audience)
    db.Db.disconnect(cur, conn)

    return request

@app.post("/gg_audience/")
def test(request: Dict[Any,Any]):
    
    gg_audience = db.Db.gg_table()
    cur,conn = db.Db.connect()
    SaveData(cur,conn).gg_save_data(gg_audience)
    db.Db.disconnect(cur, conn)

    return request

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8080, debug=True, reload=True)