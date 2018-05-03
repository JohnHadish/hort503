# John Hadish Hort503 Final Project

        ____               _           __     _____
       / __ \_________    (_)__  _____/ /_   |__  /
      / /_/ / ___/ __ \  / / _ \/ ___/ __/    /_ <
     / ____/ /  / /_/ / / /  __/ /__/ /_    ___/ /
    /_/   /_/   \____/_/ /\___/\___/\__/   /____/
                    /___/
    Hort 503, Spring 2018
    =================================================

### Summary
Program that blasts a protein fasta file against a database, and summarizes the results

### Running the Program
##### Input
Edit the "nextflow.config" file if you wish to change:

* Protein fasta that will be blasted (fasta\_path) default is:  /data/hort503\_01\_s18/example-data/all.pep
* Database to blast protein fasta against (db\_path) default is: "/data/hort503\_01\_s18/example-data/swissprot"
* The number of sequences you wish to have in each file to be blasted (sequence\_size) default is" 5000 (extra credit)

##### Run
To run on Kamiak, once you have your nextflow.config file set, you must simply type the command:
```
sbatch SBATCH.sh
```
This will run the program on Dr. Ficklin's nodes and will allot 2 days for the blast. If you wish to run with different parameters, you can change them in the SBATCH.sh file

Alternatively, you can run this program in an idev session. The command is:
```
srun nextflow run Project03.nf -profile standard
```

##### Output
The program will output 4 files when run with the "sbatch SBATCH.sh" command, and 2 when run with the idev session option. 

The files are:
* **Out.out** (sbatch only) - the output file for the entire sbatch nextflow session
* **Error.err** (sbatch only) - the error file for the entire sbatch nextflow session (I hope this one is 0 bytes)
* **_Final\_Files_** - directory that contains:
    * **Summary.txt** - a tab deliminated file summarizing the number of bash hits for each gene
    * **Combined\_Blast.txt** - the combined blast results in tab deliminated form. The order is:
	
	1. Query accession
	2. Subject accession
	3. Subject title
	4. Percent identity
	5. Alignment length
	6. Number of mismatches
	7. Number of gap openings
	8. Start of alignment in query
	9. End of alignment in query
	10. Start of alignment in subject
	11. End of alignment in subject
	12. Expect value
	13. Bitscore
 
* It should also me noted that the workflow will produce a nextflow **_work_** directory that will contain all the intermediate files. You can check the **Out.out** file to see where each step is stored.

