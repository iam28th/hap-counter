import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="hap-counter",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        allow_abbrev=False,
        description="Computes support for ALT and REF alleles from aligned reads",
        epilog="To report issues: https://github.com/iam28th/hap-counter",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        help="increase output verbosity",
        action="store_true",
        required=False,
    )

    parser.add_argument(
        "--bam",
        type=argparse.FileType("r"),
        # TODO: check that corresponding .bai is present in action kwarg
        help="a file with aligned reads which must be indexed beforehand; the reads are assumed sorted by coordinate",
        required=True,
    )

    parser.add_argument(
        "--vcf",
        type=argparse.FileType("r"),
        help="variants in phased VCF format, optionally gzipped; for now only SNVs are processed",
        required=True,
    )

    parser.add_argument(
        "--output",
        type=argparse.FileType("w"),
        help="output path; when omitted, is generated from PID and timestamp",
    )

    return parser.parse_args()
