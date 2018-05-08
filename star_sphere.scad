include <starmap.scad>;

/**
 * Subtract the star rods from a spherical shell
 *
 * Gnu Public License 3.0  https://www.gnu.org/licenses/gpl-3.0.en.html
 */

rodLength = 100;
shellRadius = 99;
shellThickness = 5;

difference() {
    sphere(r=shellRadius, center=true, $fn=100);
    sphere(r=shellRadius - shellThickness, center=true, $fn=100);
    import("star_rods.stl");
}
