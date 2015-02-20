#!/bin/bash

#http://www.thegeekstuff.com/2010/06/bash-array-tutorial/

while read line
do
  List=("${List[@]}" $line) # add new item
done < $1

echo ${List[@]/*[aA]*/} # print all item
