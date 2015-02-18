#!/bin/bash

#http://stackoverflow.com/questions/1335815/how-to-slice-an-array-in-bash

while read line
do
  List=("${List[@]}" $line) # add new item
done

echo ${List[@]:3:5} # print sliced item
