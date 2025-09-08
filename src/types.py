from src.compat import dataclass


@dataclass
class ReadStruct:
    """
    Used to cache results of expensive calls,
    such as  read.get_aligned_pairs
    """

    read = None
    aligned_pairs = None


@dataclass(slots=True)
class SNV_Support:
    """
    Represents one row of the output
    """

    chrom: str
    pos: int  # 0-based

    # ruff: noqa:N815
    h1_REF: int = 0
    h1_ALT: int = 0
    h2_REF: int = 0
    h2_ALT: int = 0

    @staticmethod
    def get_fieldnames() -> list[str]:
        fns = ["chrom", "pos", "h1_REF", "h1_ALT", "h2_REF", "h2_ALT"]
        # sanity check
        assert all(fn in dir(SNV_Support) for fn in fns)
        return fns
