#!/usr/bin/python
import argparse
import logging
import os
import sys

from watermarks.core import setup_logger
from watermarks.core.loader import Loader


logger = logging.getLogger()


def run():
    parser = setup_parser()
    args = parser.parse_args()
    if args.verbose:
        ll = logging.DEBUG
    elif args.quiet:
        ll = logging.ERROR
    else:
        ll = None
    setup_logger(ll)
    logger.debug(args)
    r = Loader('writers')
    try:
        r.run(args)
        return 0
    except ImportError:
        logger.critical('Cannot find method "%s". Please make sure you '
                        'spelled it correctly and check your PYTHONPATH.',
                        args.method)
        return 1


def setup_parser():
    description = 'Utility for writing watermarks to images.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        'sources', metavar='PTH', nargs='+',
        help='List of files/directories that will be processed. Directories '
             'will be listed (but not recursive).'
    )
    parser.add_argument(
        '-q', '--quiet', action='store_true', help='Be quiet.'
    )
    parser.add_argument(
        '-v', '--verbose', action='store_true', help='Be verbose.'
    )
    parser.add_argument(
        '-m', '--method', required=True,
        help='Watermark method to be applied.'
    )
    parser.add_argument(
        '-w', '--watermark', required=True,
        help='Watermark image.'
    )
    parser.add_argument(
        '-d', '--dest-dir', required=True,
        help='Directory where processed files with watermarks will be stored.'
    )
    parser.add_argument(
        '--format', default='png',
        help='Format of generated images.'
    )
    parser.add_argument(
        '-s', '--suffix', default='_watermarked',
        help='Suffix of watermarked files (default: %(default)s).'
    )
    return parser


if __name__ == '__main__':
    exit(run())
