(physics-hs:electromagnetism:electrostatics:notes)=
# Note e dimostrazioni

<!--
(physics-hs:electromagnetism:electrostatics:coulomb:notes)=
## Legge di Coulomb

(physics-hs:electromagnetism:electrostatics:charge:measurement:notes)=
### Misura della carica elettrica

(physics-hs:electromagnetism:electrostatics:e-field:notes)=
## Il campo elettrico

(physics-hs:electromagnetism:electrostatics:e-field:conservative:notes)=
### Campo conservativo

(physics-hs:electromagnetism:electrostatics:e-field:energy)=
### Energia potenziale di una distribuzione di cariche

```{dropdown} Posizionando una carica alla volta
$$\begin{aligned}
  L^{ext}_1 & = 0 \\
  L^{ext}_2 & = \frac{1}{4 \pi \varepsilon} \frac{q_1 \, q_2}{r_{12}}  \\
  L^{ext}_3 & = \frac{1}{4 \pi \varepsilon} \frac{q_1 \, q_3}{r_{13}} + \frac{1}{4 \pi \varepsilon} \frac{q_2 \, q_3}{r_{23}}  \\
            & ... \\
  L^{ext}_n & = \sum_{j=1}^{n-1} \frac{1}{4 \pi \varepsilon} \frac{q_1 \, q_n}{r_{1n}} \\
\end{aligned}$$

$$E^{pot} = L^{ext} = \sum_i L^{ext}_i = \sum_{\{i, j\}, i \ne j} \frac{1}{4 \pi \varepsilon} \frac{q_1 \, q_j}{r_{ij}} \ .$$
```

```{dropdown} Posizionando le cariche contemporanamente
Posizionando tutte le cariche contamporaneamente con una "scalatura" delle distanze, $\vec{r}_i(\alpha) = \frac{\vec{r}_i}{\alpha}$, $\alpha \in (0, 1]$, il lavoro delle forze elettriche è

$$\begin{aligned}
  dL_i(\alpha) & = \sum_{j \ne i} \vec{F}_{ij}(\alpha) \cdot d \vec{r}_i(\alpha) = \\
  & = \sum_{j \ne i} \frac{q_i \, q_j}{4 \pi \varepsilon}  \frac{1}{\left| \frac{\vec{r}_i}{\alpha} - \frac{\vec{r}_j}{\alpha}\right|^2} \hat{r}_{ji} \cdot \left(-\frac{\vec{r}_i}{\alpha^2}\right) \, d \alpha = \\
  & = - \sum_{j \ne i} \frac{q_i \, q_j}{4 \pi \varepsilon}  \frac{\hat{r}_{ji} \cdot\vec{r}_i}{\left| \vec{r}_i - \vec{r}_j\right|^2}  \, d \alpha
\end{aligned}$$

$$\begin{aligned}
 dL(\alpha) & = \sum_i d L_i = \\
  & = - \sum_{i} \sum_{j \ne i} \frac{q_i \, q_j}{4 \pi \varepsilon}  \frac{\hat{r}_{ji} \cdot\vec{r}_i}{\left| \vec{r}_i - \vec{r}_j\right|^2}  \, d \alpha = \\
  & = - \sum_{\{i,j\}, i \ne j} \frac{q_i \, q_j}{4 \pi \varepsilon}  \frac{\hat{r}_{ji} \cdot \left( \vec{r}_i - \vec{r}_j \right)}{\left| \vec{r}_i - \vec{r}_j\right|^2}  \, d \alpha = \\
  & = - \sum_{\{i,j\}, i \ne j} \frac{q_i \, q_j}{4 \pi \varepsilon}  \frac{1}{r_{ij}}  \, d \alpha  \ ,
\end{aligned}$$

e il lavoro diventa

$$
 L = \int_{\alpha = 0}^{1} dL (\alpha) =  - \int_{\alpha=0}^{1} \sum_{\{i,j\}, i \ne j} \frac{q_i \, q_j}{4 \pi \varepsilon}  \frac{1}{r_{ij}}  \, d \alpha = - \sum_{\{i,j\}, i \ne j} \frac{q_i \, q_j}{4 \pi \varepsilon}  \frac{1}{r_{ij}} \ .
$$
```
-->

