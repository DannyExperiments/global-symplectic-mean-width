# Mathematical audit

The checked target is the linear symplectic group and the source's normalized mean width. The proof uses compactness for the support-function Lipschitz bound and nonempty interior for a centered inscribed ball, whose existence follows from J² = −I and convexity. The reciprocal identity follows from positive square roots of positive definite matrices under orthogonal conjugation. The polar orthogonal factor preserves spherical mean width.

The midpoint comparison uses the same standard Gaussian in both reciprocal terms. The extra covariance is positive semidefinite, as C² − I = (S − S⁻¹)²/4. A centered independent Gaussian with that covariance gives the exact distributional identity. The Jensen gap is nonnegative and continuous, with strict positivity at zero for S ≠ I, so a neighborhood of strictly positive Gaussian mass forces strictness in expectation. Orthogonal symplectic matrices attain equality.

The proof gives the two corollaries by checking J-invariance directly. The disk example checks the distinction from full special-linear minimization. The [exact replay](../../verification/src/replay.py) checks finite rational algebra and both examples. The [manuscript](../../paper/manuscript.pdf) gives the proof for arbitrary dimension and convex body.
