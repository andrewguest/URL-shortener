import logging
import os

from litestar import Litestar
from litestar.config.cors import CORSConfig
from litestar.logging import LoggingConfig
from litestar.openapi import OpenAPIConfig

from ..routes.healthcheck_routes import healthcheck
from ..routes.urls_routes import create_short_url, redirect_to_long_url

logging_config = LoggingConfig(
    loggers={
        "root": {"level": logging.getLevelName(logging.INFO), "handlers": ["console"]},
        "url-shortener-api": {
            "level": "INFO",
            "handlers": ["queue_listener"],
        },
    }
)
cors_config = CORSConfig(allow_origins=["*"])


def startup_events(app: Litestar) -> None:
    app.logger.info(f"Environment: {os.getenv('ENVIRONMENT')}")
    app.logger.info(f"Redis URL: {os.getenv('REDIS_URL')}")


app = Litestar(
    cors_config=cors_config,
    logging_config=logging_config,
    on_startup=[startup_events],
    openapi_config=OpenAPIConfig(title="URL Shortener service", version="0.1.0"),
    route_handlers=[healthcheck, create_short_url, redirect_to_long_url],
)
