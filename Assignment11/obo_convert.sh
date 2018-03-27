grep -E --line-buffered '^id:|^name:|^namespace:|^def:' goslim_plant.obo | sed 's/^.*: //' | sed 'N;N;N;s/\n/\t/g' | grep '^GO:' > outfile.txt
