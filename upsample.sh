#!/bin/bash
for file in *_N.WAV; do
    #echo $file
	c=${file}
	#echo $c
	sox -v 0.9 $c -r 16000 -b 16 -c 1 n$c
	rm -rf $c
	mv n_$c $c
done

