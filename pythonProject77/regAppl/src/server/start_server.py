import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from db_manager import base_manager
from car import router as car_router
from user import router as user_router
from settings import SCRIPTS_TABLES_PATH, SCRIPTS_PRIMARY_DATA_PATH

app = FastAPI(
    title='Registration_of_applications'
)

app.include_router(car_router, prefix='/car')
app.include_router(user_router, prefix='/user')


@app.get('/')
def root():
    return RedirectResponse('/docs')


if __name__ == '__main__':
    if not base_manager.check_base():
        base_manager.create_base(SCRIPTS_TABLES_PATH, SCRIPTS_PRIMARY_DATA_PATH)
    uvicorn.run(app="start_server:app", host="127.0.0.1",  port=8000, reload=True)