(physics-hs:thermodynamics:heat-engine:second-principle)=
# Secondo principio della termodinamica per cicli termodinamici

Esistono due enunciati equivalenti del secondo principio della termodinamica per una macchina termica che realizza un ciclo termodinamico.

(physics-hs:thermodynamics:heat-engine:second-principle:kelvin)=
## Enunciato di Kelvin
```{prf:proposition} Enunciato di Kelvin
Una macchina termodinamica che scambia calore unicamente con una sorgente a temperatura costante, in un ciclo non può assorbire calore e trasformarlo interamente in lavoro utile.
```

```{dropdown} Dall'enunciato di Clausius

Il primo principio della termodinamica è un bilancio di energia totale del sistema, in termini del calore "entrante" nel sistema $\delta Q^{ext}$ dall'ambiente esterno e del lavoro fatto sul sistema $\delta L^{ext}$ o del lavoro fatto dal sistema sull'ambiente esterno $\delta L^{sys} = - \delta L^{ext}$,

$$d E^{tot} = \delta Q^{ext} + \delta L^{ext} = \delta Q^{ext} - \delta L^{sys} \ .$$

Nel regime periodico tipico delle macchine termiche, lo stato del sistema compie un percorso chiuso $\gamma$ nel suo spazio delle fasi. Lo stato del sistema alla fine di un ciclo (e inizio di un nuovo ciclo) coincide con lo stato all'inizio del ciclo. Poiché l'energia del sistema dipende dallo stato, l'energia del sistema alla fine del ciclo termodinamico è uguale all'energia del sistema all'inizio del ciclo. Se si descrive il ciclo termodinamico con una curva chiusa $\gamma$ nello spazio delle fasi del sistema, la considerazione fatta può essere scritta $\oint_{\gamma} dE = 0$.

Si considera ora lo stato di una macchina che scambia calore con una sorgente esterna a temperatura costante $T^{ext}$. Poiché è costante, si può portare sotto segno di integrale e scrivere,

$$\begin{aligned}
  0 & = \oint_{\gamma} \dfrac{d E^{tot}}{T^{ext}} = \\
    & = \oint_{\gamma} \dfrac{\delta Q^{ext}}{T^{ext}} - \oint_{\gamma} \dfrac{\delta L}{T^{ext}} \le & \text{since } \delta Q^{ext} \left(\dfrac{1}{T_1} - \dfrac{1}{T} \right) \le 0 \\
    & \le \oint_{\gamma} \dfrac{\delta Q^{ext}}{T} - \dfrac{L}{T^{ext}} \le & \text{since } dS \ge \frac{\delta Q}{T} \\
    & \le \underbrace{ \oint_{\gamma} d S}_{=0} - \dfrac{L}{T^{ext}} \ , % \text{since $S$ funzione di stato}
\end{aligned}$$

che, insieme alla non-negatività della temperatura $T^{ext} >0$, implica che il lavoro fatto in un ciclo da una macchina che assorbe calore da una sorgente a temperatura costante è non-positivo,

$$L \le 0 \ .$$

In altri termini, una macchina termica che scambia calore unicamente con una sorgente a temperatura costante assorbe lavoro dall'ambiente esterno e cede calore, $\Delta Q^{ext} = \Delta L \le 0$.
```


(physics-hs:thermodynamics:heat-engine:second-principle:planck)=
## Enunciato di Planck
```{prf:proposition} Enunciato di Planck
Non è possibile trasferire calore da una sorgente a temperatura $T_2$ a una sorgente a temperatura maggiore $T_1 > T_2$ con una macchina termica che non assorba lavoro.
```
```{dropdown}
```
