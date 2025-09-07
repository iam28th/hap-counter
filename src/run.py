import argparse
import dataclasses

import pysam

import src.pysam_utils as pysam_utils
import src.results_writer as results_writer
import src.utils as utils
from src.output_utils import get_default_output_path
from src.types import SNV_Support


def run(args: argparse.Namespace):
    # generate default output name if we need to
    output_file = args.output
    if not output_file:
        output_file = get_default_output_path()
    else:
        output_file = output_file.name

    # assume both files to be sorted by coordinate
    # and grouped by chromosome
    # (the order of chromosomes might be different though)
    with (
        pysam.VariantFile(args.vcf) as vcf,
        pysam.AlignmentFile(args.bam, "rb") as bam,
        open(output_file, "w", newline="") as csvfile,
    ):
        writer = results_writer.get_writer(csvfile)
        writer.writeheader()

        # keep a subset of reads that cover
        # currently processed variant; dynamically update this
        # subset after reading each variant
        overlapping_reads = []
        reads_iterator = None
        chrom = None
        next_read = None

        for variant in vcf:
            if not pysam_utils.is_snv(variant):
                continue

            # drop all reads that don't cover this variant
            # (i.e., end before variant.start)
            if variant.chrom != chrom:
                chrom = variant.chrom
                overlapping_reads.clear()
                reads_iterator = bam.fetch(chrom)

                # 'peek' next read
                next_read = utils.next_or_none(reads_iterator)

            else:
                overlapping_reads = [
                    r for r in overlapping_reads if r.reference_end > variant.start
                ]

            # load all reads that (might) cover this variant
            # i.e, start before variant.start
            while next_read and next_read.reference_start <= variant.start:
                # keep only overlapping primary alignments with HP tag present
                if (
                    not next_read.is_secondary
                    and next_read.has_tag("HP")
                    and next_read.reference_end > variant.start
                ):
                    overlapping_reads.append(next_read)
                next_read = utils.next_or_none(reads_iterator)

            row = get_variant_support(variant, overlapping_reads)
            writer.writerow(dataclasses.asdict(row))
            csvfile.flush()


def get_variant_support(variant, reads) -> SNV_Support:
    vs = SNV_Support(chrom=variant.chrom, pos=variant.start)

    # convert everything to upper case (just in case)
    ref_base = variant.ref.upper()
    alt_base = variant.alts[0][0].upper()

    for read in reads:
        aligned_pairs = read.get_aligned_pairs(matches_only=True)

        read_base = None

        # search for a pair where reference position matches
        # with the position of the variant
        for read_offset, ref_offset in aligned_pairs:
            if ref_offset == variant.start:
                read_base = read.query_sequence[read_offset].upper()
                break

        if read_base:
            assert read.has_tag("HP")
            if read.get_tag("HP") == 1:
                vs.h1_REF += read_base == ref_base
                vs.h1_ALT += read_base == alt_base
            else:
                vs.h2_REF += read_base == ref_base
                vs.h2_ALT += read_base == alt_base

    return vs
