println """\
        ____               _           __     _____
       / __ \\_________    (_)__  _____/ /_   |__  /
      / /_/ / ___/ __ \\  / / _ \\/ ___/ __/    /_ <
     / ____/ /  / /_/ / / /  __/ /__/ /_    ___/ /
    /_/   /_/   \\____/_/ /\\___/\\___/\\__/   /____/
                    /___/
    Hort 503, Spring 2018
    =================================================
         """
         .stripIndent()
/*
 * Author: John Hadish
 *
 * Summary: Final Project for Hort 503
 * Blast workflow
 */

// This is the command to run the project in idev session on Kamiak:
// srun nextflow run Project03.nf -profile standard

/*
 * This splits the file into chunks of 5000 (extra credit)
 */
Channel
  .fromPath( params.fasta_path )
  .splitFasta( by: params.sequence_size, file: true )
  .set{ SPLIT_FILES }


/*
 * This Blasts each chunk against the swissprotdb. The user can change this
 * in the "nextflow.config" file
 */
process blastp{
  module 'blast'

  input:
    file(fasta) from SPLIT_FILES
  output:
    file "blast_result.txt" into BLAST_RESULTS
  """
  blastp \
  -query $fasta \
  -db ${params.db_path} \
  -outfmt "6 qacc sacc stitle pident length mismatch gapopen qstart qend sstart send evalue bitscore" \
  -out "blast_result.txt"
  """
}


/*
 * This collects all of the blast outputs and puts them into a new file
 * called "Combined_Blast" in the "Final_Files" directory
 */
BLAST_RESULTS
  .collectFile(name: "Combined_Blast.txt", storeDir: "Final_Files")
  .set{ COMBINED_BLAST }


/*
 * This uses bash commands (awk, sort and uniq) to generate a summary
 * of the results in tab deliminated form.
 */
process summarize{
  publishDir "Final_Files", mode: "link"
  input:
    file(Combined_Blast) from COMBINED_BLAST
  output:
    file "Summary.txt" into SUMMARY
  """
  awk '{ print \$1 }' $Combined_Blast | sort | uniq -c \
  | sort -k1 -n -r | awk '{ print \$2, \$1}' OFS='\t' > Summary.txt
  """
}
