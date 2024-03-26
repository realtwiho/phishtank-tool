from datetime import datetime
from typing import Union

from fastapi import APIRouter, Query

from phishtank.core import get_phishes_report, search_domain

router = APIRouter(prefix="/api/v0")


@router.get("/report")
def report(
    start: datetime = Query(alias="from"),
    end: Union[datetime, None] = Query(default_factory=datetime.now, alias="to"),
) -> dict:
    return get_phishes_report(start, end)


@router.get("/search")
def say_hello(domain: str) -> dict:
    return search_domain(domain)
