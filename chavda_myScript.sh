#!/bin/bash
if [ "$#" -ne 2 ]; then
  echo "You must enter exactly 2 command line arguments. Ex: myScript.sh [directory] output_file"
else
  if [ -d "$1" ]; then #check if its a directory or not
    if [ -r "$1" ]; then #check if the directory is readable
      output="$2" #create the output.html file in the directory to scan
      echo "<html>" >> $output #write the <html> tag in the output file
      echo "<ul>" >> $output #write the <ul> tag
      cd "$1"
      for i in *; do #search for all directories
        if [ -d "$i" ]; then #if its a directory only
          echo "<li>"$1$i"</li>" >> $output #write the directory path on output file
          cd "$i"
          echo "<ul>" >> $output #create another <ul> tag
          k=$(echo $1$i | sed -e 's/ /%20/g') #removing any space in the name of the current directory
          echo "<li><a href="$k">.</a></li>" >> $output #hypertext link to go to current directory
          echo "<li><a href="$(dirname "$k")">..</a></li>" >> $output #hypertext link to go to parent directory
          for j in *; do #search everything in level deep than the main directory
            if [ -f "$j" ]; then #if its a file
              l=$(echo $j | sed -e 's/ /%20/g') #removing any space in the name of the file
              echo "<li><a href="$k/$l">$j</a></li>" >> $output #adding a hypertext link to that file
            fi
            if [ -d "$j" ]; then #if its a sub-directory
              l=$(echo $j | sed -e 's/ /%20/g') #removing any space in the name of the sub-directory
              echo "<li><a href="$k/$l">$j/</a></li>" >> $output #adding a hypertext link to that sub-directory
            fi
          done
          cd ..
          echo "</ul>" >> $output #end <ul> tag
        fi
      done
      cd ..
      for i in "$1"*; do #find all files in the directory to be scanned
      	if [ -f "$i" ]; then #if its a file
          if cmp -s "$i" "$output"; then
      	    # exclude the html created before from getting included in the scan
      	    :
      	  else
      	    l=$(echo $i | sed -e 's/ /%20/g') #removing any space in the name of the file
            echo "<li><a href="$l">$i</a></li>" >> $output
          fi
        fi
      done
      echo "</ul>" >> $output
      echo "</html>" >> $output
    else
      echo "Directory not readable"
    fi
  else
    echo "No such directory"
  fi
fi

