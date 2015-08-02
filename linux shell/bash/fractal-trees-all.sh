# https://www.hackerrank.com/challenges/fractal-trees-all

#!/bin/sh
declare -a lv1=(1 49 0)
declare -a lv2=(2 33 31)
declare -a lv3=(3 25 15)
declare -a lv4=(4 21 7)
declare -a lv5=(5 19 3)

declare -a empty=(0 32 48 56 60 62)

function draw_arm {
    printf '1'
    for i in $(seq 1 $1); do printf '_'; done
    printf '1'
}

function draw_dash {
    for i in $(seq 1 $1); do printf '_'; done
}

function draw_body_line {
    local -n val=$1
    local lv=${val[0]}
    local start=${val[1]}
    local space=${val[2]}
    local n=$(( 16 / ( 2 ** ( lv-1 ) ) ))
    local round=$(( 2 ** ( lv-1 ) ))
    for i in $(seq 1 $n); do
      draw_dash $start
      for i in $(seq 1 $round); do
        printf '1'
        draw_dash $space
      done
      draw_dash $((start+1-space))
      echo ""
    done
}

function draw_arm_line {
    local deep=$1
    local lv=$2
    local start=$3
    for i in $(seq 1 $lv); do
      local n=$((start+i))
      local m=$((lv*2-i*2+1))
      local o=$((lv*2+i*2-3))
      draw_dash $n
      for j in $(seq 1 $((deep-1))); do
        draw_arm $m
        draw_dash $o
      done
      draw_arm $m
      draw_dash $((n+1))
      echo ""
    done
}

function empty_line {
    for i in $(seq 1 $1); do
        draw_dash 100
        echo ""
    done
}

read n

empty_line $((63-empty[n]))

if [ $n -ge 5 ]
then
    draw_arm_line 16 1 17
    draw_body_line lv5
fi

if [ $n -ge 4 ]
then
    draw_arm_line 8 2 18
    draw_body_line lv4
fi

if [ $n -ge 3 ]
then
    draw_arm_line 4 4 20
    draw_body_line lv3
fi

if [ $n -ge 2 ]
then
    draw_arm_line 2 8 24
    draw_body_line lv2
fi

if [ $n -ge 1 ]
then
    draw_arm_line 1 16 32
    draw_body_line lv1
fi
