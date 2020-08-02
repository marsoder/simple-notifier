import argparse
from .exceptions import ZeroArgumentsError


def create_parser():
    parser = argparse.ArgumentParser(description="parse the arguments")
    parser.add_argument("--seconds", type=int, const=0, nargs="?", default=0,
                        help="seconds to elapse before displaying notification")
    parser.add_argument("--minutes", type=int, const=0, nargs="?", default=0)
    parser.add_argument("--hours", type=int, const=0, nargs="?", default=0,
                        help="hours to elapse before displaying notification")
    return parser


def parse_arguments(parser):
    args = parser.parse_args()

    if not args.seconds and not args.hours and not args.minutes:
        raise ZeroArgumentsError("Must specify at least one argument")

    return args

