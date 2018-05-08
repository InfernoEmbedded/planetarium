#!/usr/bin/env python3
# encoding: utf-8
'''
 -- shortdesc

Read in the HYD V3 Database & export the star locations & magnitudes suitable
for OperSCAD consumption

@author:     Alastair D'Silva

@copyright:  2018 Alastair D'Silva. All rights reserved.

@license:    Gnu Public License 3.0  https://www.gnu.org/licenses/gpl-3.0.en.html

@contact:    alastair@d-silva.org
'''

import sys
import os
import csv
import traceback

from argparse import ArgumentParser

__all__ = []
__version__ = 0.1
__date__ = '2018-04-19'
__updated__ = '2018-04-19'

DEBUG = 0
TESTRUN = 0
PROFILE = 0

def starMagnitude(star):
    return float(star["mag"])

def main(argv=None):
    '''Command line options.'''

    program_name = os.path.basename(sys.argv[0])
    program_version = __version__
    program_build_date = "%s" % __updated__

    program_longdesc = "Convert HYG Star locations & magnitudes into OpenSCAD arrays"
    program_license = "Copyright 2018 Alastair D'Silva                                            \
                Licensed under the Gnu Public License 3.0\nhttps://www.gnu.org/licenses/gpl-3.0.en.html"

    if argv is None:
        argv = sys.argv[1:]
    try:
        # setup option parser
        parser = ArgumentParser(description=program_longdesc, epilog=program_license)
        parser.add_argument("-i", "--in", nargs=1, dest="infile", help="set input path", metavar="FILE")
        parser.add_argument("-o", "--out", nargs=1, dest="outfile", help="set output path ", metavar="FILE")

        # set defaults
        parser.set_defaults(outfile="starmap.scad", infile="HYG-Database/hygdata_v3.csv")

        # process options
        args = parser.parse_args(argv)

        print("Input = %s" % args.infile)
        print("Output = %s" % args.outfile)

        # MAIN BODY #
        stars = []

        with open(args.infile, newline='') as csvfile:
            stars_reader = csv.DictReader(csvfile, delimiter = ',')
            for star in stars_reader:
                stars.append(star)

        print("Read {} stars".format(len(stars)))

        stars.sort(key=starMagnitude)
        count = 0
        outCount = 0

        with open(args.outfile, "w+") as scadfile:
            scadfile.write("// Stars contain Right Ascension, Declination, Apparent Magnitude, sorted by apparent magnitude\n")
            scadfile.write("stars = [\n")
            starCount = len(stars)
            for star in stars:
                count = count + 1
                if star["proper"] != "Sol" and float(star["mag"]) <= 6.5:
                    if outCount > 0:
                        scadfile.write(",")
                    scadfile.write("\n\t[{}, {}, {}]".format(star["ra"], star["dec"], star["mag"]))
                    outCount = outCount + 1
            scadfile.write("\n];\n")

        print("Wrote {} visible stars to {}".format(outCount, args.outfile))

    except Exception as e:
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        traceback.print_exc(e)
        return 2


if __name__ == "__main__":
    if TESTRUN:
        import doctest
        doctest.testmod()
    if PROFILE:
        import cProfile
        import pstats
        profile_filename = '_profile.txt'
        cProfile.run('main()', profile_filename)
        statsfile = open("profile_stats.txt", "wb")
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
    sys.exit(main())

