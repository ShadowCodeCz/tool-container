import argparse
import logging
import logging.config

from . import cli
from . import log


def main():
    parser = argparse.ArgumentParser(
        description="Tool container",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("-l", "--logger_level", default="DEBUG")
    subparsers = parser.add_subparsers()

    sql_to_csv_parser = subparsers.add_parser('sql2csv')
    sql_to_csv_parser.add_argument("-f", "--file", required=True)
    sql_to_csv_parser.set_defaults(func=cli.sql_to_csv)


    csv_compare_parser = subparsers.add_parser('csv-compare')
    csv_compare_parser.add_argument("-l", "--left-file", required=True)
    csv_compare_parser.add_argument("-r", "--right-file", required=True)
    csv_compare_parser.set_defaults(func=cli.csv_compare)

    arguments = parser.parse_args()
    logging.config.dictConfig(log.default_logger_configuration(arguments.logger_level))
    arguments.func(arguments)

