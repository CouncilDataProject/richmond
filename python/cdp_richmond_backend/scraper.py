#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from typing import List

from cdp_backend.pipeline.ingestion_models import EventIngestionModel
from cdp_scrapers.legistar_utils import LegistarScraper

###############################################################################


def get_events(
    from_dt: datetime,
    to_dt: datetime,
    **kwargs,
) -> List[EventIngestionModel]:
    scraper = LegistarScraper(
        client="richmondva",
        timezone="America/New_York",
        ignore_minutes_item_patterns=[
            "Citizens were encouraged to provide their comments in writing",
            "This meeting will be held in-person",
            "Special Guidelines for Public Access and Citizen",
            "To access or participate, or both",
            "The Honorable",
            "Absent",
            "A copy of the material provided has been filed",
            "CERTIFICATION OF CLOSED MEETING",
            "the Council has convened in closed meeting on this date",
        ],
    )

    return scraper.get_events(begin=from_dt, end=to_dt)
