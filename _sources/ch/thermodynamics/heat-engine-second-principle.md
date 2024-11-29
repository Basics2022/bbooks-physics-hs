(physics-hs:thermodynamics:heat-engine:second-principle)=
# Secondo principio della termodinamica per cicli termodinamici

Esistono due enunciati equivalenti del secondo principio della termodinamica per una macchina termica che realizza un ciclo termodinamico.

(physics-hs:thermodynamics:heat-engine:second-principle:kelvin)=
## Enunciato di Kelvin
```{prf:proposition} Enunciato di Kelvin
Una macchina termodinamica non può trasformare in lavoro tutto il calore assorbito da una sorgente a temperatura costante.
```


$$d E^{tot} = \delta Q^{ext} + \delta L^{ext} = \delta Q^{ext} - \delta L$$

$$\begin{aligned}
  0 & = \oint_{\gamma} \dfrac{d E^{tot}}{T_1} = \\
    & = \oint_{\gamma} \dfrac{\delta Q^{ext}}{T_1} - \oint_{\gamma} \dfrac{\delta L}{T_1} \le & \delta Q^{ext} \left(\dfrac{1}{T_1} - \dfrac{1}{T} \right) \le 0 \\
    & \le \oint_{\gamma} \dfrac{\delta Q^{ext}}{T} - \dfrac{L}{T_1} \le \\
    & \le \underbrace{ \oint_{\gamma} d S}_{=0} - \dfrac{L}{T_1} \ ,
\end{aligned}$$

che implica

$$L \le 0 \ ,$$

cioè che una macchina termica che scambia calore unicamente con una sorgente a temperatura costante produce un lavoro negativo, ossia assorbe lavoro esterno, e cede calore.

(physics-hs:thermodynamics:heat-engine:second-principle:planck)=
## Enunciato di Planck
```{prf:proposition} Enunciato di Planck
Non è possibile trasferire calore da una sorgente a temperatura $T_2$ a una sorgente a temperatura maggiore $T_1 > T_2$ con una macchina termica che non assorba lavoro.
```
**todo** dim
