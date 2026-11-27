# Problem and proof

Ahn and Kerman ask whether a toric convex body has minimum mean width over its linear symplectic orbit. The theorem assumes only quarter-turn invariance \(JK=K\), with \(J(x,y)=(-y,x)\), and requires that \(K\subset\mathbb R^{2n}\) be compact, convex and have nonempty interior. Width is
\[
M(K)=2\int_{S^{2n-1}}h_K(u)\,d\sigma(u),
\qquad h_K(w)=\sup_{a\in K}\langle a,w\rangle .
\]
Here \(\sigma\) is spherical probability measure.

For \(P^TJP=J\), write \(P=US\) with \(S=(P^TP)^{1/2}\) positive and \(U\) orthogonal. The identity \(PJP^T=J\) gives \((P^TP)J(P^TP)=J\), and conjugating the positive square root by the orthogonal matrix \(J\) gives \(J^{-1}SJ=S^{-1}\). The width of \(PK\) is the width of \(SK\).

For a standard Gaussian \(G\), homogeneity and independence of length and direction give \(\mathbb E h_K(SG)=(\mathbb E\|G\|/2) M(SK)\). The \(J\)-invariance of the support and the Gaussian, together with the reciprocal identity, give \(\mathbb E h_K(S^{-1}G)=\mathbb E h_K(SG)\). The convex support comparison uses the two arguments with the same \(G\). It gives \(\mathbb E h_K(SG)\ge \mathbb E h_K(CG)\) for \(C=(S+S^{-1})/2\).

The matrix \(C\) has all eigenvalues at least one. Let \(Y\) be centered Gaussian of covariance \(C^2-I\) and independent of \(G\). The Gaussian \(G+Y\) has the same law as \(CG\). Conditional Jensen then gives \(\mathbb E h_K(CG)\ge \mathbb E h_K(G)\). If \(S\ne I\), the noise is nonzero. Since \(J^2=-I\) and \(K\) has nonempty interior, it contains a centered ball of radius \(r>0\). The Jensen gap at \(G=0\) is at least \(r\mathbb E\|Y\|>0\). The gap as a function of the base point is continuous and nonnegative, so its expectation over \(G\) is strictly positive. Thus equality requires \(S=I\), which is equivalent to orthogonality of \(P\) and suffices for equality.

Toric symmetry contains the simultaneous quarter-turn. On the Lagrangian bidisk, this quarter-turn swaps the two real coordinate disks up to sign and preserves the product. Both cases satisfy the theorem. See the [manuscript](../paper/manuscript.pdf) for references, full proof and examples.
