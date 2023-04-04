import os
import datetime
import logging
import platform
import socket
import re
import uuid
import json
import glob
import time
import sqlite3
import pandas as pd
import csv


from . import log


def sql_to_csv(arguments):
    # TODO: Rework this is super ugly
    db = sqlite3.connect(arguments.file)
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    logger = logging.getLogger(log.logger_name)
    for table_name in tables:
        table_name = table_name[0]
        logger.info(table_name)
        table = pd.read_sql_query("SELECT * from %s" % table_name, db)
        table.to_csv(f"{os.path.basename(arguments.file)}-{table_name}.csv", index_label="index")
    cursor.close()
    db.close()


def csv_compare(arguments):
    # TODO: Rework this is super ugly
    left = {}
    right = {}

    logger = logging.getLogger(log.logger_name)

    with open(arguments.left_file, newline='') as left_csv:
        left_reader = csv.reader(left_csv, delimiter=",", quotechar=" ")
        for row in left_reader:
            left[row[1]] = row[2]

    with open(arguments.right_file, newline='') as right_csv:
        right_reader = csv.reader(right_csv, delimiter=",", quotechar=" ")
        for row in right_reader:
            right[row[1]] = row[2]

    for key in left:
        try:
            if left[key] != right[key]:
                logger.info(f"DIFF [{key}]:\n\t {left[key]} [{arguments.left_file}]\n\t {right[key]} [{arguments.right_file}]")
        except Exception as e:
            logger.error(f"ERROR: key {key}")
