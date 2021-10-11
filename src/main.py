import sessions, config
import argparse

def main(url=str, configPath: str="config.yaml",tor: bool= False):
    conf = config.Configuration(filePath=configPath).conf
    session = sessions.Session(
        tor=tor,
        cookies=conf["cookies"],
        headers=conf["headers"]
        ).session

    req = session.get(url)
    
    # print the text
    print(req.text)


def get_parser():
    parser = argparse.ArgumentParser(
        description="""
        Simple crawler that is able to crawl onions
        """,
        prog='PROG',
        usage='%(prog)s [options]'
    )

    parser.add_argument(
        "url",
        nargs="?",
        help="Url of the site"
    )

    parser.add_argument(
        "-t", "--tor",
        nargs="?",
        default=False,
        help="Set this option if the domain is an Onion."
    )

    parser.add_argument(
        "-c", "--configPath",
        nargs="?",
        default="config.yaml",
        help="Configuration file path."
    )
    
    return parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    main(args.url, configPath=args.configPath,tor=args.tor)
