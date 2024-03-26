from collections import Counter
from datetime import datetime
from urllib.parse import urlparse

from phishtank.model import Phish


def get_phishes_report(start: datetime, end: datetime) -> dict:
    phishes = Phish.get_phishes_submitted_between(end, start)

    unique_urls = set()
    base_domains = []

    for phish in phishes:
        unique_urls.add(phish.url)
        base_domains.append(get_base_domain(phish.url))

    base_domains_counter = dict(Counter(base_domains).most_common())

    return {
        "from": start,
        "to": end,
        "phishesCount": phishes.count(),
        "topLevelDomainCounts": base_domains_counter,
        "urls": unique_urls,
    }


def get_base_domain(url: str) -> str:
    domain_parts = urlparse(url).netloc.split(".")
    return ".".join(domain_parts[-2:])


def search_domain(search: str) -> dict:
    phishes = Phish.select(Phish.url, Phish.phish_detail_url).where(
        Phish.url % f"*{search}*"
    )
    phish_detail_urls = [
        phish.phish_detail_url
        for phish in phishes
        if urlparse(phish.url).netloc == search
    ]
    return {"urls": phish_detail_urls}
