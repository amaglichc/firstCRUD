from fastapi import FastAPI

from Routers.PetRouter import router as pet_router
from Routers.UserRouter import router as user_router

app = FastAPI(
    title="PetUser"
)
app.include_router(user_router)
app.include_router(pet_router)
