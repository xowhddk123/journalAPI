from routers import users_router
from models import *
from fastapi import FastAPI


app = FastAPI()

app.include_router(users_router)


# 서버를 실행하기 위한 코드 (로컬 테스트용)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port_num)
