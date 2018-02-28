#!/bin/bash
PHONEBOOK_ENTRIES="bash_phonebook_entries"
endline="\n"
if [ "$#" -lt 1 ]; then
	    exit 1

elif [ "$1" = "new" ]; then
	if [ ! -e $PHONEBOOK_ENTRIES ] || [ ! -s $PHONEBOOK_ENTRIES ]; then
		echo "" > $PHONEBOOK_ENTRIES
	fi
	echo "$2 $3 $4" >> $PHONEBOOK_ENTRIES
elif [ "$1" = "list" ]; then
	if [ ! -e $PHONEBOOK_ENTRIES ] || [ ! -s $PHONEBOOK_ENTRIES ]; then
		echo "phonebook is empty"
	else
		cat $PHONEBOOK_ENTRIES
	fi
elif [ "$1" = "remove" ]; then
	grep -v $2 $PHONEBOOK_ENTRIES > temp.txt
	echo "temp.txt"
	rm $PHONEBOOK_ENTRIES
	cat temp.txt > $PHONEBOOK_ENTRIES
	rm temp.txt
elif [ "$1" = "clear" ]; then
	rm $PHONEBOOK_ENTRIES
else
	grep $2 $PHONEBOOK_ENTRIES

fi
 
