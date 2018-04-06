"""A Python script that performs simple read trimming of a FASTQ file.

.. module:: Project01
   :platform: Unix, Windows
   :synopsis: This script receives as input a FASTQ file and a set of arguments
      that control trimming. A new FASTQ file is generated containing only
      trimmed reads that meet the given requirements.

.. moduleauthor:: John Hadish

"""

from sys import argv
script, Fastq_In, Fastq_Trimed, min_q, min_size = argv



def get_read(fq):
    """Extract a single read from a FASTQ file.

    Reads in a FASTQ file are stored in 4 lines that contain the
    sequence_id, nucleotide sequence, a second id, and a series of
    characters represeting quality scores.

    :param fq: A file handle for the FASTQ file
    :type fq: An io.TextIOBase object (created using the open() function).

    :return: a list containing 4 strings: the sequence ID, nucleotide sequence,
        second ID, and the quality score sequence. If there are no more
        sequences in the FASTQ file then this function returns False.
    :rtype: a list with four elements
    """

    #This is where an individual read will be stored
    rtype = []

    #This adds the info to the above vector, removoinf the returns at the end with
    #".rstrip"
    for i in range(4):
        rtype.append((fq.readline()).rstrip())

    return(rtype)





def trim_read_front(read, min_q, min_size):
    """Trims the low quality nucleotides from the front of a reads' sequences.

    This function examines the quality score of each nucleotide sequence
    starting from the first position of the sequence. When it encouters a
    high quality score it stops trimming and returns an updated read.

    :param read: A list containing for elements in this order: the sequence ID,
        the nucleotide sequence string, a secondary identifier string, and a
        quality score string.
    :type read: a list

    :param min_q:  The minimum quality score that a nucleotide must have to
        not be trimmed (e.g. 20).
    :type min_q:  integer

    :param min_size:  The minimum size that the sequence must have after
        trimming to keep the read (e.g. 25).
    :type min_size: integer

    :return: a list just like the the get_read() function returns but with the
       low-quality reads (and corresponding quality scores) trimmed off the
       front of the string. If the remaining trimmed read is smaller than the
       desired minimum read length then this function returns False.
    :rtype: a list with four elements
    """
    #This pulls out the 4th line of each file (quality_string) and the 2nd
    #(sequence_string)
    quality_string = read[3]
    sequence_string = read[1]

    #This determines how long the sequence is
    length = len(quality_string)

    #This keeps track of how much we should trim off.
    Trim_Off = 0

    #checks each letter in the quality string, and checks if its value (ord -
    #33 for fastq files) is below the cutoff (typically set to 30)
    for letter in quality_string:
        Decimal_Q = ord(letter) - 33
        if Decimal_Q < min_q:
            Trim_Off += 1
        #It stops when it finds the first letter with quality score >= than minimum
        else:
            break

    #This checks to see if the length is above the minimum length, and then if it
    #is, it will remake the sequence and send it back. If not it returns False.
    if (length - Trim_Off) >= min_size:
        read[1] = sequence_string[Trim_Off:]
        read[3] = quality_string[Trim_Off:]
        return(read)
    else:
        return(False)




def main(argv):
    """The main function of this script.

    After trimming is completed, the fucntion prints out three status lines. The
    first indicates the total number of reads that were found. The second
    indicates how many reads were removed for being too short after trimming and
    the third indicates how many reas were trimmed and kept.

    The script will create a new FASTQ file of just the trimmed reads and name
    it according to the argument provided by the user when running the script.

    :param argv:  The incoming arguments to this script as
       provided by the sys.argv variable.  There must be four total arguments
       provided to the script must be in the following order

       - The filename for the input FASTQ file
       - The filename for the new output FASTQ file that this script creates
       - An integer for the minimum quality score. Anything below this at the
         beginning of each read's nucleotide sequence is trimmed off.
       - An integer indicating how large a read's nucleotide sequence must
         be after trimming in order to keep it.
    """
    #This opens the files:
    print(f"Opening {Fastq_In} file for reading...")
    fq = open(Fastq_In)
    print(f"Opening {Fastq_Trimed} file for writing...")
    fq_Trimed = open(Fastq_Trimed, "w")

    #This counts how many lines are in fq (the fast q file).
    #It has to open up Fastq_In to do this
    #It then rewinds the file to the first position once it is done counting
    Total_Reads = int(sum(1 for line in fq)/4)
    fq.seek(0)

    #This Tracks how many reads have been removed.
    Reads_Removed = 0

    #This runs the other functions with their required inputs
    for read in range(Total_Reads):
        rtype = get_read(fq)

        front_trimmed = trim_read_front(rtype, int(min_q), int(min_size))

        if front_trimmed != False:
            final_trimmed = "\n".join(front_trimmed)
            fq_Trimed.write(final_trimmed + "\n")

        elif front_trimmed == False:
            Reads_Removed += 1
        else:
            print("Error, This file is corrupt")

    #This prints off stats about the run.
    print(Total_Reads, "reads were found")
    print(Reads_Removed, "reads were removed")
    print(Total_Reads - Reads_Removed, "reads were trimmed and kept")
    print("Done.")

# Begin the program by calling the main function.
main(argv)
