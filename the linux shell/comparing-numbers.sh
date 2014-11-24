#!/bin/bash

read x
read y

if (( $x > $y)); then
  echo "X is greater than Y"
else if (( $x < $y)); then
        echo "X is lesser than Y"
     else if (( $x == $y)); then
              echo "X is equal to Y"
          fi
     fi
fi
