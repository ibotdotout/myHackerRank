# https://www.hackerrank.com/challenges/lonely-integer-2

#!/bin/bash

read n
read -a List
echo ${List[@]} | tr ' ' '\n' | sort | uniq -u
