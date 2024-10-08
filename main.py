
from fastapi_users import FastAPIUsers
from fastapi import FastAPI, Depends
from src.auth.base_config import auth_backend
from src.auth.base_config import User
from src.auth.manager import get_user_manager
from src.auth.schemas import UserRead, UserCreate

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend




app = FastAPI(
    title="Authentic test"
)


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"






