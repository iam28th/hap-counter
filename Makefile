
BAM := spec/test_data/giab_2023.05.hg002.haplotagged.chr16_28000000_29000000.processed.30x.bam
VCF := spec/test_data/giab_2023.05.hg002.wf_snp.chr16_28000000_29000000.vcf.gz
OUT := output.tsv

# runs program on example data
.PHONY: test
test:
	python hap-counter.py --bam $(BAM) --vcf $(VCF) --output $(OUT)

.PHONY: clean
clean:
	rm -f $(OUT)
