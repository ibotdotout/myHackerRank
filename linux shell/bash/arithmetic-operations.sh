#!/bin/bash

read exp
printf "%.3f\n" ` echo  "scale = 4 ; $exp " | bc -l`
