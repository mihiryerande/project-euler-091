# Problem 91:
#     Right Triangles with Integer Coordinates
#
# Description:
#     The points P (x1, y1) and Q (x2, y2) are plotted at integer coordinates
#       and are joined to the origin, O (0, 0), to form ΔOPQ.
#
#     There are exactly fourteen triangles containing a right angle
#       that can be formed when each coordinate lies between 0 and 2 inclusive;
#       that is, 0 <= x1, y1, x2, y2 <= 2.
#
#     Given that 0 <= x1, y1, x2, y2 <= 50, how many right triangles can be formed?

from math import ceil, floor, sqrt


def main(n: int) -> int:
    """
    Returns the number of right triangles with integer coordinates
      that can be formed with origin O (0,0) and points P,Q
      lying within top-right quadrant of cartesian grid having coordinates at most `n`.

    Args:
        n (int): Natural number

    Returns:
        (int):
          Number of right triangles formed with origin and two other points
            in non-negative cartesian grid having coordinates at most `n`.

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(n) == int and n > 0

    # Idea:
    #     Rather than brute-forcing pairs of points P,Q,
    #       consider different ways to form right triangles using the origin and two other points.
    #     Partition such triangles into different cases which can be counted separately.
    count = 0

    # Case 1:
    #     Origin is the vertex opposite the hypotenuse.
    #     This necessarily means that points P and Q lie on the X- and Y-axes.
    #     Otherwise, angle ∠POQ would not be 90°.
    #
    #     The Y-axis point can lie at any nonzero point (0, y) -> `n` possibilities.
    #     The X-axis point can lie at any nonzero point (x, 0) -> `n` possibilities.
    #
    #     Triangle can be formed from any pair of these -> n^2 such triangles.
    count += n ** 2

    # Case 2:
    #     Origin is an endpoint of the hypotenuse.
    #     Let opposite endpoint of hypotenuse by P (x1, y1).
    #     Let point `C` (xc, yc) be the midpoint of the hypotenuse.
    #     Let length `r` be the half-length of the hypotenuse.
    #
    #     To form a right triangle with third point Q (x2, y2),
    #       Q must lie on the circle formed with center `C` and radius `r`.
    #     Simply consider points x2 in range [xc-r, xc+r].
    #     Corresponding y2 = yc ± sqrt(r^2 - (x2^2-xc^2))
    #     Find any such y2 coordinate which is an integer.

    for x1 in range(n+1):
        for y1 in range(n+1):
            if x1 == y1 == 0:
                continue
            else:
                xc = x1 / 2
                yc = y1 / 2
                r = sqrt(x1**2 + y1**2) / 2

                for x2 in range(max(ceil(xc-r), 0), min(floor(xc+r), n) + 1):  # Only check integral `x2`
                    dy = sqrt((x1**2+y1**2)/4 - (x2-xc)**2)

                    # Try upper y2
                    y2 = yc + dy
                    if 0 <= y2 <= n and (abs(y2) + abs(x2) > 0) and (abs(y2-y1) + abs(x2-x1) > 0) and int(y2) == y2:
                        count += 1

                    # Try lower y2
                    # Might be same as upper if at left/right-most point of circle
                    if dy > 0:
                        y2 = yc - dy
                        if 0 <= y2 <= n and (abs(y2) + abs(x2) > 0) and (abs(y2-y1) + abs(x2-x1) > 0) and int(y2) == y2:
                            count += 1

    return count


if __name__ == '__main__':
    max_coordinate = int(input('Enter a natural number: '))
    right_triangle_count = main(max_coordinate)
    print('Number of integral-coordinate right triangles formed with origin within distance {}:'.format(max_coordinate))
    print('  {}'.format(right_triangle_count))
