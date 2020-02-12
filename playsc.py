import argparse
from src import useChrome
import time
import re
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--trackurl", "-u", type=str, required=True)
parser.add_argument("--time", "-t", type=int, required=False)
args = parser.parse_args()

while True:
    if not args.trackurl:
        useChrome.browser.close()
        print("missing track url")
        parser.print_help
        break

    if not re.match(r'^https://soundcloud.com', args.trackurl):
        useChrome.browser.close()
        print("url does not match requirement, use a url to a public song")
        print('eg: --track https://soundcloud.com/darude/sandstorm-radio-edit')
        break

    useChrome.browseTrackPage(args.trackurl)
    useChrome.clickPlayButtonOnTrackPage()

    if not args.time:
        time.sleep(30)
        useChrome.browser.close()
        break
    else:
        time.sleep(args.time)
        useChrome.browser.close()
        break