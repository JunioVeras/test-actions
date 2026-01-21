from utils import do_something


def handler(event, context):
    if event is None:
        print("No event")

    result = do_something(event)
    return result
