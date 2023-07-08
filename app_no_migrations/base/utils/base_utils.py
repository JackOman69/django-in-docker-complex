import datetime

class DateFormats:
    DEFAULT = '%Y-%m-%d'
    WITH_T = '%Y-%m-%dT%H:%M:%S'
    WITH_TIME = '%Y-%m-%d %H:%M:%S'
    WITH_TIME_NO_SECONDS = '%Y-%m-%d %H:%M'
    TIME = '%H:%M:%S'
    TIME_NO_SECONDS = '%H:%M'
    FULL_DATE_DESCRIPTION = "%A %d %B"
    MOYCLASS = "%Y-%m-%dT%H:%M:%S.%fZ"
    STATISTICS_MONTH = "%m.%Y"
    DOTS_WITH_TIME = "%d.%m.%Y %H:%M:%S"
    DOTS_WITH_TIME_NO_SECONDS = "%d.%m.%Y %H:%M"
    HUMAN = "%d.%m.%Y"


def date_converter(obj):
    if isinstance(obj, datetime.date):
        return obj.strftime(DateFormats.DEFAULT)
    if isinstance(obj, datetime.datetime):
        return obj.strftime(DateFormats.WITH_TIME)
    if isinstance(obj, datetime.time):
        return obj.strftime(DateFormats.TIME_NO_SECONDS)
