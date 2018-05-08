#!/bin/sh

count=32
stars=8911

increment=`expr $stars / $count + 1`

start=0
for i in `seq 1 $count`; do
#	openscad-nightly -o star_rods.$i.stl -D "starFirst=$start" -D "starCount=$increment" star_rods.scad &
	start=`expr $start + $increment`
done

wait

echo "solid Star_Rods" > star_rods.stl
for file in star_rods.*.stl; do
	head -n -1 $file | tail -n +2 >> star_rods.stl
done
echo "endsolid Star_Rods" >> star_rods.stl

