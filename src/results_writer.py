import csv

from src.types import SNV_Support


def get_writer(handle):
    return csv.DictWriter(
        handle,
        dialect="unix",
        quoting=csv.QUOTE_MINIMAL,
        delimiter="\t",
        fieldnames=SNV_Support.get_fieldnames(),
    )
