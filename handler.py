from utils import do_something
import os,sys

def handler(event, context):
    if event is None:
        print("No event")

    result = do_something(event)
    return result
