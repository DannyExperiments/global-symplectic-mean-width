# Squeezing a square

Extract the explorer archive and open index.html. The controls run offline. Choose a squeeze factor and drag the diagram or use its left and right arrow keys to rotate the view.

The square has half-lengths 1 and 1. Stretching the first coordinate by s and shrinking the second by 1/s makes a rectangle with half-lengths s and 1/s. The two shapes use the same plot scale. Thickness is added for the rotating diagrams to show depth. The mathematics concerns their planar faces.

The area is always 4. Integrating the support function gives a mean width of 4(s + 1/s)/π, compared with 8/π for the square. At s = 2 the rectangle is 4 by 1 and its mean width is 25% larger. The explorer also displays the factor C = ((s + 1/s)/2)I and the independent Gaussian covariance C² − I from the proof.

To rebuild the GIF and offline ZIP use Python 3.9+ and Pillow 10.1+ with its bundled scalable default font. From the repository root run

~~~sh
python3 visualization/render.py
~~~

The release figure uses 72 frames of 120 ms each. The geometry and file order are deterministic for a fixed Pillow version. The figure illustrates the worked example. The manuscript proves the general result.
