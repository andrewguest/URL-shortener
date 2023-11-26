from litestar import Litestar
from litestar.openapi import OpenAPIConfig

from url_shortener.routers.urls_router import create_short_url, redirect_to_long_url

app = Litestar(
    openapi_config=OpenAPIConfig(title="URL Shortener service", version="0.1.0"),
    route_handlers=[create_short_url, redirect_to_long_url],
)
