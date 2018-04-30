println """\
        =========
        Project 3
        =========
         """
         .stripIndent()

// Now it is time to make this thing work:
// This splits the file into chunks of 5000 (extra credit)
Channel
  .fromPath( params.fasta_path )
  .splitFasta( by: 5000 )
  .set{ SPLIT_FILES }

process Blastp{
  input:
    fasta from SPLIT_FILES
  """
  blastp -query $fasta -db -out
  """
}
