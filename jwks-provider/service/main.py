from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from uuid import UUID, uuid4

app = FastAPI()


class JWKSKeyModel(BaseModel):
    kty: str
    kid: str
    alg: str
    k: str


class JWKSResponseModel(BaseModel):
    keys: List[JWKSKeyModel]


@app.get("/jwks.json")
async def root() -> JWKSResponseModel:
    return JWKSResponseModel(
        keys=[
            JWKSKeyModel(
                kty="oct",
                kid="0afee142-a0af-4410-abcc-9f2d44ff45b5",
                alg="HS256",
                k="MySekretKey",
            )
        ]
    )


@app.get("/ping")
async def ping() -> dict:
    return {
        "result": "PONG!",
    }
