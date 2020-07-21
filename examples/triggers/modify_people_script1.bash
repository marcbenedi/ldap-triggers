#!/bin/bash

# $1 contains USER name

# $2 contains GROUP name

# The rest of arguments, if any, are the other accounts

echo $1 $2

for G in ${@:3}
do
        echo $G
done