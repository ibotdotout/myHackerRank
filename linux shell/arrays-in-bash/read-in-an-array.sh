#!/bin/bash

#http://en.kioskea.net/faq/1757-how-to-read-a-file-line-by-line

while read line
do
  List=("${List[@]}" $line) # add new item
done

echo ${List[@]} # print all item
