include <starmap.scad>;

/**
 * Draw rods for each star, sized by the apparent magnitude from Earth
 *
 * Gnu Public License 3.0  https://www.gnu.org/licenses/gpl-3.0.en.html
 */

rodRadius = 100;
rodInnerRadius = 95;
baseRodRadius = 2;
minimumRodRadius = 0.5; // Minimum radius for magnitude 6.5 stars
starFirst = 0;
starCount = 8911;

$fn = 20;

/**
 * Draw a rod representing a star
 * @param ra the Right Ascension of the star
 * @param dec the declination of the star
 * @param mag the apparent magnitude of the star
 */

module starRod(ra, dec, mag) {
    theta = 15 * ra; // Degrees
    phi = 90 - dec; // Degrees from vertical

    delta = baseRodRadius - minimumRodRadius;
    radius = baseRodRadius - (mag / 6.5) * delta;

    rotate(a = [0, 0, theta])
    rotate(a = [phi, 0, 0])
    translate([0,0,rodInnerRadius])
    cylinder(h=rodRadius - rodInnerRadius, r=radius, center=false);
}

/**
 * Add rods for a given number of stars
 * @param starFirst the index of the first star to output
 * @param starCount the number of stars
 */

module starRods(starFirst, starCount) {
    for (star = [starFirst:starFirst + starCount - 1]) {
	if (star <= 8911) {
        	starRod(stars[star][0], stars[star][1], stars[star][2]);
	}
    }
}

/* 
difference() {
    sphere(r=90, center= true, $fn=100);
    sphere(r=85, center= true);
    starRods(starFirst, starCount);
}
*/

starRods(starFirst, starCount);
