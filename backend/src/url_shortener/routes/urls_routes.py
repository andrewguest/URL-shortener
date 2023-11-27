import os
import random
import string

from litestar import Request, get, post
from litestar.response import Redirect
from pydantic import BaseModel

from ..database.redis_client import redis_client_async

BASE_URL = os.getenv("RAILWAY_PUBLIC_DOMAIN", "http://localhost:8000")


class LongURL(BaseModel):
    url: str


class ShortURL(BaseModel):
    url: str


@post(path="/url", description="Create a shortened URL for the provided long URL.")
async def create_short_url(data: LongURL, request: Request) -> ShortURL:
    """Take a long URL and create a shortened URL for it.

    Args:
        data (LongURL): The long URL to shorten.

    Returns:
        ShortURL: The shortened URL that redirects to the long URL.
    """

    # Logging
    request.logger.info(f"Request input: {data.url}")

    # Generate a unique string of 7 characters & digits for the new short URL
    random_string = "".join(random.choices(string.ascii_letters + string.digits, k=7))
    shortened_url = f"https://{BASE_URL}/{random_string}"
    redis_response = await redis_client_async.set(random_string, data.url)
    if redis_response:
        return ShortURL(url=shortened_url)


@get(
    path="/{short_url:str}",
    description="Redirect to the long URL associated with the given short URL",
)
async def redirect_to_long_url(short_url: str, request: Request) -> Redirect:
    """Redirect to the long URL associated with the given short URL

    Args:
        short_url (ShortURL): Shortened URL
    """

    # Logging
    request.logger.info(f"Path param: {short_url}")

    # Check if the short URL exists
    long_url = await redis_client_async.get(short_url)
    if long_url:
        return Redirect(long_url)
