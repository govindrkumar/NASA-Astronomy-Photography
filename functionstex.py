# API KEY == f0Pw3meacI9F4Sj858I9deuisxs9nRmqTcqiBzUl
import requests as rq
import time
import json
import sys
from datetime import datetime, timedelta


def calculatedate():
    current_date = datetime.now()
    twentydaysbef = current_date - timedelta(days=19)

    startdate = twentydaysbef.strftime('%Y-%m-%d')
    enddate = current_date.strftime('%Y-%m-%d')

    return startdate, enddate


def inputvalid():
    while True:
        print("Rerouting back to options...")
        print("\n" * 2)

        usrinput = input(
            "List of Options\n\n1. Restart\n0. Exit\n\nSelect: ").strip()

        if usrinput == "1":
            print("Restarting...")
            return True

        elif usrinput == "0":
            print("Ending application")
            return False

        else:
            print("Sorry, not recognized. Loading options...")
            continue


def connection(url):

    try:
        resp = rq.get(url)
        resp.raise_for_status()
        return resp.json()

    except rq.exceptions.HTTPError as errorcode:
        print(f"Unexpected HTTP error: {errorcode}")
        raise

    except rq.exceptions.RequestException as e:
        print(f"Network error: {e}")
        raise

    except ValueError:
        raise ("Json Decoding Error")
