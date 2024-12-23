(physics-hs:electromagnetism:electromagnetism-steady:notes)=
# Note e dimostrazioni

(physics-hs:electromagnetism:electromagnetism-steady:notes:biot-savart)=
## Legge di Biot-Savart
Vengono qui dimostrate le espressioni dei campi magnetici generati da conduttori elettrici con geometria particolare, mostrati nella sezione sulla [legge di Biot-Savart](physics-hs:electromagnetism:electromagnetism-steady:biot-savart).

```{dropdown} Filo rettilineo infinito
Si usa un sistema di coordinate polari,

$$z = R \, \tan \theta$$
$$dz = R \frac{1}{\cos^2 \theta} \, d \theta$$
$$r^2 = R^2 + z^2 = R^2 \left(1+\frac{\sin^2 \theta}{\cos^2 \theta} \right) = R^2 \frac{1}{\cos^2 \theta}$$

Usando la formula di Biot-Savart {eq}`eq:biot-savart:integral`

$$\begin{aligned}
  \vec{b}(\vec{r}_0) & = - \frac{\mu}{4 \pi} i \int_{z=-\infty}^{\infty} \hat{\theta} \frac{r}{r^2} \sin \theta dz = \\
                     & = - \frac{\mu}{4 \pi} i \hat{\theta} \int_{\theta=\pi}^{0} \frac{\cos^2 \theta}{R^2} \sin \theta R \frac{1}{\cos^2 \theta} \, d \theta = \\
                     & =   \frac{\mu}{4 \pi} i \hat{\theta} \int_{\theta=0}^{\pi} \frac{1}{R} \sin \theta \, d \theta = \\
                     & =   \frac{\mu \, i}{2 \pi \, R} \hat{\theta} \ .
```

```{dropdown} Spira circolare
Sfruttando la simmetria cilindrica del problema, è possibile calcolare il campo magnetico $$ sull'asse di una spira circolare

$$\cos \phi = \frac{R}{r} \qquad , \qquad
r^2 = R^2 + z^2$$

$$\begin{aligned}
  \vec{b}(\theta) & = 2 \pi R \left( -\frac{\mu}{4 \pi} i \frac{\vec{r}}{r^3} \times \hat{\theta} \cdot \hat{z} \right) \hat{z} = \\
   & = \frac{\mu \, i}{2} \frac{R}{r^2} \cos \phi \hat{z} = \\
   & = \frac{\mu \, i}{2} \frac{R^2}{r^3} \hat{z}  = \\
   & = \frac{\mu \, i}{2} \frac{R^2}{(R^2 + z^2)^{3/2}} \hat{z}  =
       \frac{\mu \, i}{2 \, R} \frac{1}{\left(1 + \left(\frac{z}{R}\right)^2 \right)^{3/2}} \hat{z} 
\end{aligned}$$
```

```{dropdown} Solenoide rettilineo
Applicando la legge di Ampére,

$$ N \, i = \Gamma_{\gamma}(\vec{h}) = \ell \, h = \ell \, \frac{b}{\mu}$$

$$b = \mu \frac{N}{\ell} \, i$$

Il flusso del campo magnetico (uniforme) vale quindi

$$\phi = b \, A = \mu \frac{N \, A}{\ell} \, i$$
```

```{dropdown} Solenoide toroidale

Applicando la legge di Ampère,

$$N \, i = \Gamma_{\gamma}(\vec{h}) = r \, 2 \, \pi \, h = r \, 2 \, \pi \frac{b}{\mu}$$

$$b(r) = \mu \frac{N}{2 \, \pi \, r } \, i$$

Il flusso del campo magnetico attraverso le sezioni del toro vale

$$\Phi(\vec{b}) = \oint_{S} b(r) \, dS =  \mu \frac{N \, i}{2 \pi}\int_{\rho=0}^{a} \int_{\alpha=0}^{2\pi} \frac{1}{R - \rho \cos \alpha} \rho \, d \rho \, d \alpha  = $$

**todo**
```

