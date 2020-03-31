# E.pauciflora_NLR
This project aims to identify the NBS-LRR (NLR) homologues in E. pauciflora. 



- - -

module load hmmer/3.3
module load bedtools/2.25.0
module load clustal-omega/1.2.4
module load python/3.7.2

- - -

nhmmer EG_nonTIRhmm EP_genome.fna > EP_nonTIRout

nhmmer EG_TIRhmm EP_genome.fna > EP_TIRout

- - -

python make_bed.py < EP_nonTIRout > EP_nonTIRout.bed

python make_bed.py < EP_TIRout > EP_TIRout.bed

- - -

bedtools getfasta -fi EP_genome.fna -bed EP_nonTIRout.bed -s -fo EP_nonTIR.fasta

bedtools getfasta -fi EP_genome.fna -bed EP_TIRout.bed -s -fo EP_TIR.fasta

- - -

clustalo -i EP_nonTIR.fasta -o clustalo_EP_nonTIR.sto --outfmt=st --force

clustalo -i EP_TIR.fasta -o clustalo_EP_TIR.sto --outfmt=st --force

- - -

hmmbuild EP_specific_nonTIR.hmm clustalo_EP_nonTIR.sto

hmmbuild EP_specific_TIR.hmm clustalo_EP_TIR.sto

- - -

nhmmer EP_specific_nonTIR.hmm EP_genome.fna > EP_specific_nonTIRout

nhmmer EP_specific_TIR.hmm EP_genome.fna > EP_specific_TIRout

- - -

python make_bed.py < EP_specific_nonTIRout > EP_specific_nonTIRout.bed
python counter.py < EP_specific_nonTIRout.bed


python make_bed.py < EP_specific_TIRout > EP_specific_TIRout.bed
python counter.py < EP_specific_TIRout.bed

cat EP_specific_nonTIRout.bed EP_specific_TIRout.bed | python combine_bed.py > EP_specific_combined.bed
python counter.py < EP_specific_combined.bed

- - -

bedtools getfasta -fi EP_genome.fna -bed EP_specific_combined.bed -s -fo EP_specific_combined.fasta

- - -

cat EP_specific_combined.fasta | fold -w 60
