# planetarium
Some scripts to generate a 3D printable planetarium from the HYG Star Database
http://www.astronexus.com/hyg

OpenSCAD is a bit of a pig for this task, it's single threaded & memory intensive. For this reason, the work is broken up into
separate steps.

Star_rods.sh generates the star rods for later subtraction. It breaks the work in 32 chunks, and spawns an OpenSCAD
instance for each chunk. This takes about 15 minutes on a Threadripper 1950x. The script then concatenates the result into a single
ASCII STL file.

Star_sphere.sh creates a spherical shell, and subtracts the rods from it. This runs as a single thread, takes about x hours, and
requires xxGB of RAM.


## Prerequisites
 - OpenSCAD Nightly  (Generates the STLs. Nightly possibly isn't necessary, but in what in hardcoded in the scripts, you could use the GUI instead)
 - Python3  (Generates the star map OpenSCAD array. This is already in the repository, so this is only necessary if you want to alter the array)

## Usage
```
OpenSCAD-Converter.py  # this are already done, but may be used to regenerate starmap.scad from the HYG Star Database
star_rods.sh   # Generates rods for each star
star_sphere.sh  # Subtracts rods from a spherical shell
```

## License
All code is licensed under the Gnu Public License 3.0  https://www.gnu.org/licenses/gpl-3.0.en.html
