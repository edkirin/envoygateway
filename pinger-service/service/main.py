from fastapi import FastAPI, APIRouter, Request

api_router = APIRouter()


@api_router.get("/protected")
async def protected_route(request: Request):
    return {
        "message": "This is protected route",
        "request": {
            "url": request.url,
            "base_url": request.base_url,
            "headers": request.headers,
            "query_params": request.query_params,
            "path_params": request.path_params,
            "cookies": request.cookies,
        },
    }


@api_router.get("/unprotected")
async def unprotected_route(request: Request):
    return {
        "message": "This is unprotected route",
        "request": {
            "url": request.url,
            "base_url": request.base_url,
            "headers": request.headers,
            "query_params": request.query_params,
            "path_params": request.path_params,
            "cookies": request.cookies,
        },
    }


@api_router.get("/protected/ping")
async def protected_ping():
    return {
        "result": "Protected PONG!",
    }


@api_router.get("/unprotected/ping")
async def unprotected_ping():
    return {
        "result": "Unprotected PONG!",
    }


app = FastAPI()
app.include_router(api_router, prefix="/pinger-service")
