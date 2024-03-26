from datetime import datetime
from peewee import Model, BigIntegerField, CharField, TimestampField

from .db import db
from .data_loader import fetch_phish_data


class Phish(Model):
    phish_id = BigIntegerField(unique=True)
    url = CharField(index=True)
    submission_time = TimestampField(index=True)
    phish_detail_url = CharField()

    class Meta:
        database = db

    @classmethod
    def insert_many_phishes(cls, phishes: list):
        cls.insert_many(
            phishes,
            fields=[
                Phish.phish_id,
                Phish.url,
                Phish.phish_detail_url,
                Phish.submission_time,
            ],
        ).on_conflict_ignore().execute()

    @classmethod
    def get_phishes_submitted_between(cls, end: datetime, start: datetime):
        return Phish.select(Phish.url).where(
            Phish.submission_time.between(start.timestamp(), end.timestamp())
        )


def load_phish_data():
    chunked_dataframe = fetch_phish_data()

    with db.atomic():
        for chunk in chunked_dataframe:
            phishes = list(chunk.itertuples(index=False, name=None))
            Phish.insert_many_phishes(phishes)


db.create_tables([Phish])
