---
permalink: 9 MONTH REPORT
---
- [x] ABSTRAXCT: use AIRG
- [x] INTRODUCTION - VIROLOGY
- [ ] INTRODUCTION - HOST GENOME: use Dave Burt’s new article, at the papers linked in the draft, and the printed papers
- [ ] PROJECT BACKGROUND: use H5N2 and H7N3 papers sent by jacqueline, and the project summary printed
- [x] METHODS
- [ ] RESULTS: just finish off everything in there
- [ ] DISCUSSION: same
- [ ] APPENDIX: snpEff summary
spikes
chr 1m 2m 4m 5m 6m 11m 14m 15m 17, 20, & 21


PROJECT BACKGROUND
include numbers of birds, W36 information 

<u>Mapping</u>
- -	Name the different algorithms and critique the methods (REFER TO TABLE)
- -	Put in GenomeBrowse diagram to show coverage for three samples – Iowa; Mexico; Mex Ped. 
<u>InDel Realignment</u>
- -	Critique the methods AND APPLICATIONS for indel realignment 
- -	Mention that Indel realignment not necessary if using GATK pipeline with GVCF haplotype caller, but that usage can improve specificity of results 
<u>Base Quality Score Recalibration</u> 
- -	Refer to table when listing software, if there is no other software than GATK then discuss in brief detail the process for GATK (1<sup>st</sup>, 2<sup>nd</sup> pass, plots)
	- o	Actually describe it well!! Use GATK forum for guidance 
	- o	<u>https://gatkforums.broadinstitute.org/gatk/discussion/44/base-quality-score-recalibration-bqsr</u>
<u>Variant/Joint Genotype Calling</u> 

- &nbsp;
	- -	<a href="https://www.nature.com/articles/srep17875" rel="noopener" class="external-link" target="_blank"><u>https://www.nature.com/articles/srep17875</u></a>
	- o	<u>SNP genotyping errors may be stratified into three groups:</u> 
		- ♣	<u>Ignoring reference allele – a homozygous SNP in the variant call,which is in fact a heterozygous SNP composed of one ref allele and one variant allele in the gold standard</u> 
		- ♣	<u>Adding reference alle – A heterozygous SNP composed of one ref allele and one varian allele in the variant call, yet a homozygous SNP in the gold standard</u>
		- ♣	<u>Other SNP calling errors</u> 





	Background reading for literature review (essential):
- -	<a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5006563/" rel="noopener" class="external-link" target="_blank"><u>https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5006563/</u></a>
- -	<a href="http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0107330" rel="noopener" class="external-link" target="_blank"><u>http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0107330</u></a>
- -	<a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4829244/%22%20%5Ct%20%22_blank" rel="noopener" class="external-link" target="_blank"><u>https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4829244/</u></a>
- -	<a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4246556/%22%20%5Ct%20%22_blank" rel="noopener" class="external-link" target="_blank"><u>https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4246556/</u></a>
- -	<a href="https://www.dropbox.com/sh/fkhh43msxkmfxl1/AADpKj820fHoupjYU3WsnBeua?dl=0&preview=01-JohnHickeyGeneralOverviewIowaMay2018.pdf%22%20%5Ct%20%22_blank" rel="noopener" class="external-link" target="_blank"><u>https://www.dropbox.com/sh/fkhh43msxkmfxl1/AADpKj820fHoupjYU3WsnBeua?dl=0&preview=01-JohnHickeyGeneralOverviewIowaMay2018.pdf</u></a>
- -	<a href="file:///C:%5C%5CUsers%5C%5CIzabela%5C%5CDownloads%5C%5Csnp1101_user_guide.pdf%22%20%5Ct%20%22_blank" rel="noopener" class="external-link" target="_blank"><u>file:///C:/Users/Izabela/Downloads/snp1101_user_guide.pdf</u></a>
- -	<a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5787230/%22%20%5Ct%20%22_blank" rel="noopener" class="external-link" target="_blank"><u>https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5787230/</u></a>
- -	<a href="https://www.cdn.ca/Articles/GEBOCT2015/2_Crampiness_Report%202%20-%20Larmer.pdf%22%20%5Ct%20%22_blank" rel="noopener" class="external-link" target="_blank"><u>https://www.cdn.ca/Articles/GEBOCT2015/2_Crampiness_Report%202%20-%20Larmer.pdf</u></a>
- -	<a href="https://gsejournal.biomedcentral.com/track/pdf/10.1186/s12711-017-0356-8?site=gsejournal.biomedcentral.com%22%20%5Ct%20%22_blank" rel="noopener" class="external-link" target="_blank"><u>https://gsejournal.biomedcentral.com/track/pdf/10.1186/s12711-017-0356-8?site=gsejournal.biomedcentral.com</u></a>
- -	<a href="https://link.springer.com/content/pdf/10.1007%2F978-1-62703-447-0.pdf" rel="noopener" class="external-link" target="_blank"><u>https://link.springer.com/content/pdf/10.1007%2F978-1-62703-447-0.pdf</u></a>
- -	<a href="https://www.ncbi.nlm.nih.gov/pubmed/17701901?dopt=Abstract" rel="noopener" class="external-link" target="_blank"><u>https://www.ncbi.nlm.nih.gov/pubmed/17701901?dopt=Abstract</u></a>
- -	<a href="https://www.ncbi.nlm.nih.gov/pubmed/23756892" rel="noopener" class="external-link" target="_blank"><u>https://www.ncbi.nlm.nih.gov/pubmed/23756892</u></a>
	GWAS:
- -	Https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3531285/
	Extended cleavage site in H7N3 strain in mexico 2013: <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3673898/" rel="noopener" class="external-link" target="_blank"><u>https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3673898/</u></a>
	Acquired from host not viral, 28S rRNA (first) 
 
Serology comparison of poultry workers (includes H7N3 and H5N2): <a href="https://www.cambridge.org/core/journals/epidemiology-and-infection/article/serological-comparison-of-antibodies-to-avian-influenza-viruses-subtypes-h5n2-h6n1-h7n3-and-h7n9-between-poultry-workers-and-nonpoultry-workers-in-taiwan-in-2012/E8BA167859758C3EC98261286880B08D" rel="noopener" class="external-link" target="_blank"><u>https://www.cambridge.org/core/journals/epidemiology-and-infection/article/serological-comparison-of-antibodies-to-avian-influenza-viruses-subtypes-h5n2-h6n1-h7n3-and-h7n9-between-poultry-workers-and-nonpoultry-workers-in-taiwan-in-2012/E8BA167859758C3EC98261286880B08D</u></a>


<u>VQSR</u>
<u>Variant Quality Score Recalibration</u> 
The Variant Quality Score Recalibration (VQSR) procedure (DePristo *et al.*, 2011) is a semisupervised technique that fits multidimensional Gaussian distributions to a collection of suspected true variants. Variants whose properties differ from those of the true variants are deemed more likely to be false positives. While the VQSR procedure improves the quality of variant calls, it suffers from several limitations. For example, VQSR requires tens of thousands of variants to accurately fit the distributions, and inclusion of more than a few (roughly 10) features may cause the algorithm to fail.
An alternative type of machine learning technique known as the support vector machine (SVM; Boser *et al.*, 1992; Cortes and Vapnik, 1995) addresses some of the difficulties encountered in earlier models. SVMs are numerical classification techniques designed to identify an arbitrarily defined class to which a query data point belongs, and have been previously used in bioinformatics applications from cancer subtype classification (Lee and Lee, 2002) to splice site prediction (e.g. Baten *et al.*, 2006). In a manner similar to VQSR, a vector of features is collected for all possible sites at which a variant may exist. The SVM is then trained on collections of sites known to contain true and false variants. Unlike VQSR, SVM training produces a ‘model’ that may then be used repeatedly to call variants from query datasets. SVMs can incorporate large numbers of features and, after training, an SVM does not require a large number of variants for precise calling; it may be used to classify a single query variant.

<a href="https://qcb.ucla.edu/wp-content/uploads/sites/14/2016/03/IntroductiontoVariantCallsetEvaluationandFilteringTutorialAppendix-LA2016.pdf" rel="noopener" class="external-link" target="_blank"><u>https://qcb.ucla.edu/wp-content/uploads/sites/14/2016/03/IntroductiontoVariantCallsetEvaluationandFilteringTutorialAppendix-LA2016.pdf</u></a>
Taken from Intro to NGS variant calling
[Previously] most variant calling [was] done on Whole Exome Sequence data (WES) and not whole genome sequence (WGA) data • WES identifies variants in ~1% of the human genome that codes for proteins • On average 12,000 variants are found in coding regions (although this number might be biased to well studied European [human] populations and will increase if looking at less well studied African genomes) [INSERT DATA FOR CHICKENS WITH REFERENCES] • WGS not commonly employed due to current cost implications and also computational data storage and analysis [but thanks to economic/industrial demand  • WGS is good for finding non-coding, regulatory and intronic variants
<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term=23341494" rel="noopener" class="external-link" target="_blank"><u>https://www.ncbi.nlm.nih.gov/pubmed/?term=23341494</u></a> ^

<u>GWAS</u> 
“Genetic studies of complex phenotypes are based on either ‘common disease–common variant’ or ‘common disease–rare variant’ hypotheses. GWAS primarily test the ‘common disease–common variant’ hypothesis, where complex phenotypes are the result of cumulative effects of a large number of common variants. In contrast, the ‘common disease–rare variant’ hypothesis posits that multiple rare variants with large effect sizes are the main determinants of heritability of the disease [<a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3956068/" rel="noopener" class="external-link" target="_blank"><u>34</u></a>]. The field is now shifting toward the study of lower frequencies of rare variants [<a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3956068/" rel="noopener" class="external-link" target="_blank"><u>37</u></a>], which can only be empowered by NGS and sophisticated bioinformatics approaches.
Machine learning to wean out false positives from SNP calls produced by GATK:
<a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1955739/" rel="noopener" class="external-link" target="_blank"><u>https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1955739/</u></a>



<p style="text-align:center;margin:0"><u>Project Background</u>
</p>
- -	phylogeography/epidemiology of H5N2 2015 outbreak in Iowa, USA (Sam Lycett) 
- -	phylogeography/epidemiology of H7N3 2013 outbreak in Mexico
- -	Create diagrams/models showing dynamics of infection - look up how to do this using software, or lift figures from Sam Lycett’s papers.
- -	The specific flock studied in the research (HYL W36) http://www.hyline.com/userdocs/pages/36_COM_ENG.pdf
- -	Then go on to discuss control measurements taken during these two outbreaks, and how future outbreaks may be benefitted by the research I am doing now (using genomic analysis to inform policy, breeding programs, vaccination strategy, genome editing etc) 



SNP1101 documentation for GWAS:
A whole genome association study is used simply to find association between genetic variants (markers) and a trait of interest across the whole genome and in a large enough group of individuals. GWAS is a powerful method to have better understanding of genetic architecture of a trait. There are well established methodologies to carry out GWAS and to interpret the results. However, there are some challenges associated with GWAS which mainly root in population and genomic data structure (e.g. stratification, cryptic relationships, ascertainment bias, genotyping/imputation errors, rare variants, multiple comparison,…). The 24 SNP1101 user’s guide (v 1.0) HiggsGene Solutions Inc. effect of each of these issues can be reduced or minimized with proper statistical methods, but independent replication of GWAS is very important for confirmation of previous findings. snp1101 can perform GWAS based on single SNP and haplotypes. Single SNP/haplotype regression

gwas{ssr| shr}
 {snp {…}} {indv {…}}
 {kinship{ped} | {{name } | {file<”gfile”><”afile”> }}{pwt<w>}  {reg_g_on_a  a <v> b <v> }}
 {aireml {max_iter<n>}}
 {wt {rel | accu}} 
{maf_range<min><max>}
 {hap_len<n>}
 {sig<s>,…}
 {mca {cwise | gwise}  {bonf | fdr | pfdr}}
 {plot {manhattan} | {qq}} 
{nthread} ;

 ssr and shr stands for single SNP regression and single haplotype regression, respectively. The kinship option allows for fitting a genomic or pedigree-based relationship matrix to account for population structure and also stratification. The aireml option estimates the variance components and updates the input variance component values. The wt option is similar to the one explained in GBLUP, and RBLUP. Minor allele frequency range is set by maf_range and SNPs with MAF out of the range are discarded. For the shr method, haplotype length should be specified by the hap_len option. User defined significance levels are specified by sig. The mca option lets you decide what kind of correction to apply for multiple testing. The correction can be done with Bonferroni (bonf), false discovery rate (fdr) or positive false discovery rate (pfdr) methods at the chromosome-wise (cwise) or genome-wise (gwise) level. Final GWAS results can be visualized by the plot command and the qq option is to investigate inflation or deflation in p-values (using qq-plot).
Flowchart of In silico [pipeline] and In vitro [functional assays] methods