# First-error summability

This page combines probability-polynomial bandwidth and Cantor propagation into the main lower theorem.

## Encode the phase by Cantor digits

Scale the middle-thirds Cantor set to the phase interval of width a. A parameter is represented by an infinite bit string v=(v_1,v_2,...). A level-k cylinder has width a3^{-k} and fair-Cantor prior mass 2^{-k}.

Choose increasing deadlines T_k with

$$
r(T_k)<\frac{a3^{-k}}2.
$$

At deadline T_k, project the reported estimate to the nearest level-k Cantor cylinder and let W_k be its kth decoded bit. Distinct level-k cylinders are separated by at least a3^{-k}; therefore on the global anytime-success event,

$$
W_k=v_k
\quad\text{for every }k.
$$

## Use physical transcript events

For prefix s in {0,1}^{k-1}, define

$$
E_{s,k}
=
\{W_1\cdots W_{k-1}=s,\; W_k=0\}.
$$

This is an ordinary event in the transcript through T_k. Its likelihood p_{s,k}(theta) is a nonnegative trigonometric polynomial of degree at most 2T_k.

If the true parameter lies anywhere in the left child s0, the single all-time success event is contained in E_{s,k}. Hence

$$
p_{s,k}(\theta)
\ge1-\alpha
\ge\frac12
$$

throughout that child.

The adjacent right child s1 has width ell_k=a3^{-k}. The local propagation lemma therefore gives

$$
\mathbb E_{\theta\mid s1}
[p_{s,k}(\theta)]
\ge
c\exp[-C(T_k a3^{-k}+1)].
$$

## The same event is a first error on the right child

Under a true s1 parameter, E_{s,k} says that all earlier bits were decoded as s and the kth bit was decoded as zero though the truth is one. Thus the first decoded error occurs at k.

The fair Cantor prior gives each right child mass 2^{-k}. Summing over all 2^{k-1} prefixes yields

$$
\Pr(\text{first error at }k)
\ge
\frac c2
\exp[-C(T_k a3^{-k}+1)].
$$

First-error events are disjoint across k. Integrating the pointwise anytime guarantee over the Cantor prior bounds the probability of any error by alpha. Absorbing fixed constants gives

$$
\boxed{
\sum_{k\ge1}
\exp[-D T_k a3^{-k}]
\le B\alpha.
}
$$

No independence across scales is used. The proof never divides by the probability of a previously correct transcript, so rare adaptive branches and coherent memory create no conditional-likelihood loophole.

## Infinite-scale consequence

Suppose

$$
L=
\limsup_{T\to\infty}
\frac{T r(T)}{\log\log T}
$$

were smaller than a sufficiently small universal constant. Choose c with 2L<c<1/D and let, for large k,

$$
T_k=
\left\lfloor
\frac{c3^k\log k}{a}
\right\rfloor.
$$

Since log log T_k/log k tends to one, the assumed small limsup implies r(T_k)<a3^{-k}/2 eventually. But

$$
\exp[-D T_k a3^{-k}]
\gtrsim
k^{-Dc},
$$

whose series diverges because Dc<1, contradicting summability.

To discard irrelevant early scales, restrict the Cantor prior to one preceding cylinder and reindex its descendants. Translation and rescaling preserve the propagation constants.

## Finite-K consequence

For K scales, write x_k=T_k a3^{-k}. Then

$$
\sum_{k=1}^{K}e^{-Dx_k}\le B\alpha.
$$

If M=max_k x_k,

$$
K e^{-DM}\le B\alpha,
$$

hence

$$
\boxed{
M\ge D^{-1}\log\frac{K}{B\alpha}.
}
$$

Jensen's inequality also gives the same order for K^{-1} sum_k x_k.

The theorem constrains simultaneous efficiency across scales. It does not identify which scale must carry the overhead, and therefore does not force a log K factor into a known final deadline.
