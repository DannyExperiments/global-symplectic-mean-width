# Reproducibility

Run from the repository root with Python 3.9 or newer. The verification code uses the standard library and exact rational arithmetic.

~~~sh
python3 -I scripts/verify_repository.py
python3 -I verification/src/replay.py
~~~

Compare with [the recorded replay](verification/logs/replay.txt). The checks cover 108 exact polar and covariance fixtures, 17,496 support and reciprocal-image calculations, all six square explorer settings and a determinant-one disk example. The manuscript proves the general statement.

[PDF build](paper/BUILD.md) · [Visualization build](visualization/README.md)
