import savepagenow
import time
import traceback
import sys

def parse_cli():
    from argparse import ArgumentParser
    parser = ArgumentParser(
        usage="""\
given this thread as an example https://www.he-man.org/forums/boards/showthread.php?168773-United-Kingdom-Collector-s-Delivery-Thread  
to save from page 17 to the end (which at time of writing is page 328), do this:
python3 archive.py --thread-id "168773-United-Kingdom-Collector-s-Delivery-Thread" --start-page 17 --end-page 328
""",
    )
    parser.add_argument('--thread-id', type=str, required=True)
    parser.add_argument('--start-page', type=int, default=1, help='(default: 1)')
    parser.add_argument('--end-page', type=int, required=True)
    parser.add_argument('--authenticate', action='store_true', help="pass this arg if you're authenticating. see here for more info: https://palewi.re/docs/savepagenow/python.html#authentication")
    args = parser.parse_args()
    return args

def make_page_url(thread_id: str, page: int) -> str:
    page_url = f'https://www.he-man.org/forums/boards/showthread.php?{thread_id}'
    # doing /page1 technically works, but most links to it probably won't look like that, so probably better to special case this
    if page != 1:
        page_url = f'{page_url}/page{page}'
    return page_url

def main():
    args = parse_cli()
    pagenum = args.start_page
    while pagenum <= args.end_page:
        page_url = make_page_url(thread_id=args.thread_id, page=pagenum)
        try:
            print(f'saving page {pagenum}...')
            archive_url = savepagenow.capture(
                target_url=page_url,
                authenticate=args.authenticate,
            )
            print(f'page {pagenum} saved at {archive_url}')
            pagenum += 1
        except Exception as exc:
            from savepagenow.exceptions import TooManyRequests, CachedPage
            match exc:
                case CachedPage():
                    # TODO make the log for this better
                    print(f'for page {pagenum}: {exc!r}')
                case TooManyRequests():
                    print('api asked us to wait, sleeping for a minute before retrying...')
                    time.sleep(60)
                case _:
                    print(f'######## failed to save page, exception included below. url used was {page_url!r}')
                    traceback.print_exception(exc, file=sys.stdout)
                    print('################################################################################')
                    pagenum += 1

if __name__ == '__main__':
    main()

