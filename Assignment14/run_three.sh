muscle3.8.31_i86linux64 -in Q9Y3D7.fasta -out Q9Y3D7.fasta.aln
hmmbuild Q9Y3D7.fasta.aln.hmm Q9Y3D7.fasta.aln
hmmsearch Q9Y3D7.fasta.aln.hmm c_elegans.PRJNA275000.WS263.genomic.fa > Q9Y3D7_hmmsearch_dmel.txt
