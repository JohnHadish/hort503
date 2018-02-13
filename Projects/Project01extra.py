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

    #This is the vector that this function makes. It has 4 lines added to it
    rtype = []

    for i in range(4):
        rtype.append((fq.readline()).rstrip())

    return(rtype)

#May need to add sommething that returns "false"




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

    quality_string = read[3]
    sequence_string = read[1]
    length = len(quality_string)
    ##I want to get the length of the string that is healthy, return that number, and do some cutting
    Trim_Off = 0
    for letter in quality_string:
        Decimal_Q = ord(letter) - 33
        if Decimal_Q < min_q:
            Trim_Off += 1
        else:
            break


    if (length - Trim_Off) >= min_size:
        read[1] = sequence_string[Trim_Off:]
        read[3] = quality_string[Trim_Off:]
        return(read)
    else:
        return(False)


def trim_read_back(read, min_q, min_size):
    """This does the same thing as 'trim_read_front', except that it trims the
    back. I acheive this by just reversering the strings, sending them to the
    trim_read_front, getting them back, and put them back in the correct order.
    """

    #These are the vectors that this function uses to keep this function readable.
    #Ignore the numbers, they are just for positions (it doesnt like when you
    #reverse and call from an empty vector.)
    reverse_read = [0,1,2,3]
    final_read = [0,1,2,3]

    #This function checks to see if after the forward trim the read was removed.
    #If not, it will reverse it and send it back to get cut agian.
    #Otherwise it will basically push it down the line, assigning it "False" again
    if read != False:
        #Here is the actual reversing if the string.
        for number in range(4):
            reverse_read[number] =  read[number][::-1]
        #Here is where it gets sent to be trimmed again, just this time in reverse.
        reverse_read_trimmed = trim_read_front(reverse_read, min_q, min_size)
    else:
        reverse_read_trimmed = False

    #The string we get back must then be flipped again so it is going forwards before
    #We return it. If it did not pass the trimming test, then it received a False
    #And gets pushed through
    if reverse_read_trimmed != False:
        for number in range(4):
            final_read[number] =  reverse_read[number][::-1]
    else:
        final_read = False

    #Returns the front and back trimmed read to main
    return(final_read)


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
##script, Fastq_In, Fastq_Trimed, min_q, min_size = argv



    print(f"Opening {Fastq_In} file for reading...")
    fq = open(Fastq_In)
    print(f"Opening {Fastq_Trimed} file for writing...")
    fq_Trimed = open(Fastq_Trimed, "w")

    #This counts how many lines are in fq. It has to open up Fastq_In to do this
    #It then rewinds the file to the first position
    Total_Reads = int(sum(1 for line in fq)/4)
    fq.seek(0)


    Reads_Removed = 0

    for read in range(Total_Reads):
        rtype = get_read(fq)


        #Trims the front
        front_trimmed = trim_read_front(rtype, int(min_q), int(min_size))


        #Trims the back
        final_trimmed = trim_read_back(front_trimmed, int(min_q), int(min_size))


        if final_trimmed != False:
            final_write = "\n".join(final_trimmed)
            fq_Trimed.write(final_write + "\n")
        elif final_trimmed == False:
            Reads_Removed += 1
        else:
            print("Error, This file is corrupt")


    print(Total_Reads, "reads were found")
    print(Reads_Removed, "reads were removed")
    print(Total_Reads - Reads_Removed, "reads were trimmed and kept")
    print("Done.")


# Begin the program by calling the main function.
main(argv)
