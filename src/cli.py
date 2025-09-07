import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="hap-counter",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        allow_abbrev=False,
        description="Computes support for ALT and REF alleles from alignment",
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
        help="A file with aligned reads which must be indexed beforhand. The reads are assumed sorted by coordinate.",
        required=True,
    )

    parser.add_argument(
        "--vcf",
        type=argparse.FileType("r"),
        help="Variants in phased VCF format (optionally gzipped). For now only SNVs are processed",
        required=True,
    )

    parser.add_argument(
        "--output",
        type=argparse.FileType("w"),
        help="Output path (when omitted, is generated from timestamp).",
    )

    return parser.parse_args()
