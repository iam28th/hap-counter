import pysam


def is_snv(variant: pysam.libcbcf.VariantRecord) -> bool:
    return (
        len(variant.ref) == 1 and len(variant.alts) == 1 and len(variant.alts[0]) == 1
    )
