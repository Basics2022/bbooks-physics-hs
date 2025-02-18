<!--
```{article-info}
:author: basics
:date: "{sub-ref}`today`"
:read-time: "{sub-ref}`wordcount-minutes` min read"
```
-->

(physics-hs:mechanics:inertia:continuum)=
# Inerzia e grandezze dinamiche di un sistema esteso con distribuzione continua di massa

(physics-hs:mechanics:inertia:continuum:rigid)=
## Sistemi rigidi

```{prf:example} Inerzia di una sfera
:label: inertia-sphere
:class: dropdown

Una sfera di massa $m$ ha inerzia alla rotazione

usando le coordinate cilindriche

$$I = \int_V \rho \dots = \frac{2}{5} m R^2 \ . $$

usando le coordinate sferiche

$$I = \int_V \rho \dots = \frac{2}{5} m R^2 \ . $$

con la massa

$$m = \dots = \frac{4}{3} \pi \rho R^3 \ ,$$

```

```{prf:example} Inerzia di una sfera con distribuzione di massa non uniforme
:label: inertia-sphere-non-uniform
:class: dropdown

```

```{prf:example} Inerzia di un disco uniforme
:label: inertia-disk
:class: dropdown

Un disco di massa $m$ ha inerzia alla rotazione

$$I = \int_S \sigma \left( x^2 + y^2 \right) = \int_{\theta=0}^{2\pi} \int_{r=0}^{R} \sigma r^2 \, r \, dr \, d\theta = 2 \pi \sigma \frac{R^4}{4} = \frac{1}{2} \pi \sigma R^4 = \frac{1}{2} m R^2 \ . $$

$$m = \int_S \sigma = \int_{\theta = 0}^{2 \pi} \int_{r=0}^{R} \sigma \, r \, dr \, d\theta = 2 \pi \sigma \frac{R^2}{2} = \pi \sigma R^2 \ ,$$

$$\sigma = \frac{m}{\pi R^2} \ .$$

```

```{prf:example} Inerzia di un disco uniforme
:label: inertia-disk-non-uniform-non-symmetric
:class: dropdown

```

```{prf:example} Inerzia di un anello uniforme
:label: inertia-ring
:class: dropdown

Un anello di massa $m$ ha inerzia alla rotazione

$$I = \oint_C \mu \left( x^2 + y^2 \right) = \int_{\theta=0}^{2\pi}  \mu R^2 \, R \, d\theta = 2 \pi \mu R^3 = m R^2 \ . $$

$$m = \oint_C \mu = \int_{\theta = 0}^{2 \pi} \mu \, R \, d\theta = 2 \pi \mu R $$

$$\mu = \frac{m}{2 \pi R} \ .$$

```
