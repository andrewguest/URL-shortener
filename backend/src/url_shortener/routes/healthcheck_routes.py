from litestar import get


@get(path="/healthcheck", description="Healthcheck route")
async def healthcheck() -> dict:
    return {"status": "up"}
