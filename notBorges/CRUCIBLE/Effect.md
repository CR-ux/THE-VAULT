---
permalink: Effect
---
**Seq. Ontology	Effect**
**Classic	Note & Example	Impact**
[coding_sequence_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001580)	CDS	The variant hits a CDS.	MODIFIER
[chromosome](http://www.sequenceontology.org/browser/current_svn/term/SO:0001580)	CHROMOSOME_LARGE DELETION	A large part (over 1% or 1,000,000 bases) of the chromosome was deleted.	HIGH
[duplication](http://www.sequenceontology.org/browser/current_svn/term/SO:1000035)	CHROMOSOME_LARGE_DUPLICATION	Duplication of a large chromoome segment (over 1% or 1,000,000 bases).	HIGH
[inversion](http://www.sequenceontology.org/browser/current_svn/term/SO:1000036)	CHROMOSOME_LARGE_INVERSION	Inversion of a large chromoome segment (over 1% or 1,000,000 bases).	HIGH
[coding_sequence_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001580)	CODON_CHANGE	One or many codons are changed 
e.g.: An MNP of size multiple of 3	LOW
[inframe_insertion](http://www.sequenceontology.org/browser/current_svn/term/SO:0001821)	CODON_INSERTION	One or many codons are inserted 
e.g.: An insert multiple of three in a codon boundary	MODERATE
[disruptive_inframe_insertion](http://www.sequenceontology.org/browser/current_svn/term/SO:0001824)	CODON_CHANGE_PLUS CODON_INSERTION	One codon is changed and one or many codons are inserted 
e.g.: An insert of size multiple of three, not at codon boundary	MODERATE
[inframe_deletion](http://www.sequenceontology.org/browser/current_svn/term/SO:0001822)	CODON_DELETION	One or many codons are deleted 
e.g.: A deletion multiple of three at codon boundary	MODERATE
[disruptive_inframe_deletion](http://www.sequenceontology.org/browser/current_svn/term/SO:0001826)	CODON_CHANGE_PLUS CODON_DELETION	One codon is changed and one or more codons are deleted 
e.g.: A deletion of size multiple of three, not at codon boundary	MODERATE
[downstream_gene_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001632)	DOWNSTREAM	Downstream of a gene (default length: 5K bases)	MODIFIER
[exon_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001791)	EXON	The variant hits an exon (from a non-coding transcript) or a retained intron.	MODIFIER
[exon_loss_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001572)	EXON_DELETED	A deletion removes the whole exon.	HIGH
[exon_loss_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001572)	EXON_DELETED_PARTIAL	Deletion affecting part of an exon.	HIGH
[duplication](http://www.sequenceontology.org/browser/current_svn/term/SO:1000035)	EXON_DUPLICATION	Duplication of an exon.	HIGH
[duplication](http://www.sequenceontology.org/browser/current_svn/term/SO:1000035)	EXON_DUPLICATION_PARTIAL	Duplication affecting part of an exon.	HIGH
[inversion](http://www.sequenceontology.org/browser/current_svn/term/SO:1000036)	EXON_INVERSION	Inversion of an exon.	HIGH
[inversion](http://www.sequenceontology.org/browser/current_svn/term/SO:1000036)	EXON_INVERSION_PARTIAL	Inversion affecting part of an exon.	HIGH
[frameshift_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001589)	FRAME_SHIFT	Insertion or deletion causes a frame shift 
e.g.: An indel size is not multple of 3	HIGH
[gene_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001564)	GENE	The variant hits a gene.	MODIFIER
[feature_ablation](http://www.sequenceontology.org/browser/current_svn/term/SO:0001879)	GENE_DELETED	Deletion of a gene.	HIGH
[duplication](http://www.sequenceontology.org/browser/current_svn/term/SO:1000035)	GENE_DUPLICATION	Duplication of a gene.	MODERATE
[gene_fusion](http://www.sequenceontology.org/browser/current_svn/term/SO:0001565)	GENE_FUSION	Fusion of two genes.	HIGH
[gene_fusion](http://www.sequenceontology.org/browser/current_svn/term/SO:0001565)	GENE_FUSION_HALF	Fusion of one gene and an intergenic region.	HIGH
[bidirectional_gene_fusion](http://www.sequenceontology.org/browser/current_svn/term/SO:0002086)	GENE_FUSION_REVERESE	Fusion of two genes in opposite directions.	HIGH
[rearranged_at_DNA_level](http://www.sequenceontology.org/browser/current_svn/term/SO:0000904)	GENE_REARRANGEMENT	Rearrengment affecting one or more genes.	HIGH
[intergenic_region](http://www.sequenceontology.org/browser/current_svn/term/SO:0000605)	INTERGENIC	The variant is in an intergenic region	MODIFIER
[conserved_intergenic_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0002017)	INTERGENIC_CONSERVED	The variant is in a highly conserved intergenic region	MODIFIER
[intragenic_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0002011)	INTRAGENIC	The variant hits a gene, but no transcripts within the gene	MODIFIER
[intron_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001627)	INTRON	Variant hits and intron. Technically, hits no exon in the transcript.	MODIFIER
[conserved_intron_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0002018)	INTRON_CONSERVED	The variant is in a highly conserved intronic region	MODIFIER
[miRNA](http://www.sequenceontology.org/browser/current_svn/term/SO:0000276)	MICRO_RNA	Variant affects an miRNA	MODIFIER
[missense_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001583)	NON_SYNONYMOUS_CODING	Variant causes a codon that produces a different amino acid 
e.g.: Tgg/Cgg, W/R	MODERATE
[initiator_codon_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001582)	NON_SYNONYMOUS_START	Variant causes start codon to be mutated into another start codon (the new codon produces a different AA). 
e.g.: Atg/Ctg, M/L (ATG and CTG can be START codons)	LOW
[stop_retained_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001567)	NON_SYNONYMOUS_STOP	Variant causes stop codon to be mutated into another stop codon (the new codon produces a different AA). 
e.g.: Atg/Ctg, M/L (ATG and CTG can be START codons)	LOW
[protein_protein_contact](http://www.sequenceontology.org/browser/current_svn/term/SO:0001093)	PROTEIN_PROTEIN_INTERACTION_LOCUS	Protein-Protein interacion loci.	HIGH
[structural_interaction_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0002093)	PROTEIN_STRUCTURAL_INTERACTION_LOCUS	Within protein interacion loci (e.g. two AA that are in contact within the same protein, prossibly helping structural conformation).	HIGH
[rare_amino_acid_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0002008)	RARE_AMINO_ACID	The variant hits a rare amino acid thus is likely to produce protein loss of function	HIGH
[splice_acceptor_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001574)	SPLICE_SITE_ACCEPTOR	The variant hits a splice acceptor site (defined as two bases before exon start, except for the first exon).	HIGH
[splice_donor_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001575)	SPLICE_SITE_DONOR	The variant hits a Splice donor site (defined as two bases after coding exon end, except for the last exon).	HIGH
[splice_region_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001630)	SPLICE_SITE_REGION	A sequence variant in which a change has occurred within the region of the splice site, either within 1-3 bases of the exon or 3-8 bases of the intron.	LOW
[splice_region_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001630)	SPLICE_SITE_BRANCH	A varaint affective putative (Lariat) branch point, located in the intron.	LOW
[splice_region_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001630)	SPLICE_SITE_BRANCH_U12	A varaint affective putative (Lariat) branch point from U12 splicing machinery, located in the intron.	MODERATE
[stop_lost](http://www.sequenceontology.org/browser/current_svn/term/SO:0001578)	STOP_LOST	Variant causes stop codon to be mutated into a non-stop codon 
e.g.: Tga/Cga, */R	HIGH
[5_prime_UTR_premature start_codon_gain_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001988)	START_GAINED	A variant in 5'UTR region produces a three base sequence that can be a START codon.	LOW
[start_lost](http://www.sequenceontology.org/browser/current_svn/term/SO:0002012)	START_LOST	Variant causes start codon to be mutated into a non-start codon. 
e.g.: aTg/aGg, M/R	HIGH
[stop_gained](http://www.sequenceontology.org/browser/current_svn/term/SO:0001587)	STOP_GAINED	Variant causes a STOP codon 
e.g.: Cag/Tag, Q/*	HIGH
[synonymous_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001819)	SYNONYMOUS_CODING	Variant causes a codon that produces the same amino acid 
e.g.: Ttg/Ctg, L/L	LOW
[start_retained](http://snpeff.sourceforge.net/SnpEff_manual.html)	SYNONYMOUS_START	Variant causes start codon to be mutated into another start codon. 
e.g.: Ttg/Ctg, L/L (TTG and CTG can be START codons)	LOW
[stop_retained_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001567)	SYNONYMOUS_STOP	Variant causes stop codon to be mutated into another stop codon. 
e.g.: taA/taG, */*	LOW
[transcript_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001576)	TRANSCRIPT	The variant hits a transcript.	MODIFIER
[feature_ablation](http://www.sequenceontology.org/browser/current_svn/term/SO:0001879)	TRANSCRIPT_DELETED	Deletion of a transcript.	HIGH
[regulatory_region_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001566)	REGULATION	The variant hits a known regulatory feature (non-coding).	MODIFIER
[upstream_gene_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001631)	UPSTREAM	Upstream of a gene (default length: 5K bases)	MODIFIER
[3_prime_UTR_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001624)	UTR_3_PRIME	Variant hits 3'UTR region	MODIFIER
[3_prime_UTR_truncation](http://www.sequenceontology.org/browser/current_svn/term/SO:0002015) +[exon_loss](http://www.sequenceontology.org/browser/current_svn/term/SO:0001572)	UTR_3_DELETED	The variant deletes an exon which is in the 3'UTR of the transcript	MODERATE
[5_prime_UTR_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001623)	UTR_5_PRIME	Variant hits 5'UTR region	MODIFIER
[5_prime_UTR_truncation](http://www.sequenceontology.org/browser/current_svn/term/SO:0002013) + [exon_loss_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001572)	UTR_5_DELETED	The variant deletes an exon which is in the 5'UTR of the transcript	MODERATE
[sequence_feature](http://www.sequenceontology.org/browser/current_svn/term/SO:0002013) + [exon_loss_variant](http://www.sequenceontology.org/browser/current_svn/term/SO:0001572)	NEXT_PROT	A 'NextProt' based annotation. Details are provided in the 'feature type' sub-field (ANN), or in the effect details (EFF).	MODIFIER