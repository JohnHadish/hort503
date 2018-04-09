#!/bin/bash

SRAs=$(cat $1)
echo $SRAs

for name in $SRAs
do
if [ ! -d $name ]
then
  mkdir $name
fi
done
