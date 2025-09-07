# `hap-counter.py` 

Given read alignments (in BAM format with haplotype tags) and a set of variants (in phased VCF format) computes support for ALT and REF alleles across reads assigned to individual haplotypes.

# Installation

```bash
git clone git@github.com:iam28th/hap-counter.git --recurse-submodules
# submodules contain specification and test files, 
# omit if they are not necessary

cd hap-counter
python hap-counter.py --help
```

The only dependency is pysam, which can be installed with pip.

# Usage

```bash
python hap-counter.py --bam alignments.bam --vcf variants.vcf
```

Assumes indexes (`.bai` for `.bam` and `.tbi` for `.vcf`) are present. Produces output in `.tsv` format, e.g.:

```csv
chrom   pos     h1_REF  h1_ALT  h2_REF  h2_ALT
chr16   28001380        11      4       3       12
chr16   28002343        11      5       3       12
chr16   28003017        12      4       3       13
chr16   28003087        12      4       3       11
chr16   28004800        13      4       3       9
...
```
where:
- `chrom` - chromosome name
- `pos` - position on chromosome
- `h<H>_<A>` with `H` in `{1,2}` and `A` in `{'ALT, 'REF'}` (last 4 columns) - number of primary alignments with `HP==H` supporting allele `A`

# Limitations
- requires both `.vcf` and `.bam` files to be sorted by position
- currently only calculates support for SNVs
