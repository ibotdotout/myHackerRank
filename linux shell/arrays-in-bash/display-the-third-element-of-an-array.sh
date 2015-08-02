#!/bin/bash

while read line
do
  List=("${List[@]}" $line) # add new item
done

echo ${List[3]}
