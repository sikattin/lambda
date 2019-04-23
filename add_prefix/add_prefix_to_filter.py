import datetime

DATE_FORMAT = "%Y%m%d"
DAY = 1


def filter_generator(filters):
    for filter in filters:
        yield filter

def add_prefix(prefix: str, filters):
    for filter in filters:
        elements = filter.split("/")
        elements[len(elements) - 1] = "{0}_{1}". \
            format(prefix, elements[len(elements) - 1])
        yield '/'.join(elements)

# Get day 1day ago
def lambda_handler(event, context):
    filters = event['filter']
    now = datetime.datetime.now()
    date_1dayago = now - datetime.timedelta(days=DAY)
    key_prefix = date_1dayago.strftime(DATE_FORMAT)
    # generate new filters list
    newfilters = sorted(list(add_prefix(key_prefix, filter_generator(filters))))

    return newfilters
