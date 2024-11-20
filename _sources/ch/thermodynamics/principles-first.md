(physics-hs:thermodynamics:foundation:principles:first)=
# Primo principio della termodinamica
Il primo principio della termodinamica è il bilancio di energia totale per sistemi chiusi. La variazione di energia totale $d E^{tot}$ di un sistema chiuso è dovuta al lavoro $\delta L^{ext}$ svolto sul sistema dalle azioni macroscopiche esterne e dal calore $\delta Q^{ext}$ trasmesso al sistema dall'esterno,

$$d E^{tot} = \delta L^{ext} + \delta Q^{ext} \ .$$

La termodinamica classica fornisce una descrizione macroscopica media della dinamica microscopica di un numero elevato di componenti elementari (**todo** *teoria atomica*). L'energia totale del sistema può quindi essere interpretata come somma di un contributo cinetico macroscopico e di un contenuto microscopico, cinetico e potenziale; il calore può essere interpretato come il lavoro svolto sul sistema da parte di azioni microscopiche,

<!--
```{dropdown} Energia totale
:open:

Secondo la meccanica classica di Newton, la dinamica del componente elementare $k$ del sistema è governata dalle sue equazioni del moto,

$$\begin{aligned}
  m_k \dot{\vec{v}}_k & = \vec{f}_k^e + \sum_{j\ne k} \vec{f}^i_{kj} \\ 
  \frac{d}{dt} \left( \mathbb{I}_k \cdot \vec{\omega}_k \right) & = \vec{m}_k^e + \sum_{j\ne k} \vec{m}^i_{kj} \\
\end{aligned}$$

Il centro di massa del sistema è 

$$G = \sum_k m_k P_k$$

$$E^{tot} = \frac{1}{2} \sum_i \left| \mathbf{v}_i \right|^2 + \sum_{ij} V_{ij}$$

$$\begin{aligned}
  \left\langle E^{tot} \right\rangle
  & = \left\langle \frac{1}{2} \sum_i m_i \, \left( \mathbf{v} - \delta \mathbf{v}_i \right) \cdot \left( \mathbf{v} - \delta \mathbf{v}_i  \right) +  \left( \symbf{\omega} - \delta \symbf{\omega}_i \right) \cdot \mathbb{I}_i \cdot \left( \symbf{\omega} - \delta \symbf{\omega}_i  \right) + \sum_{ij} V_{ij} \right\rangle = \\
  & = \frac{1}{2} m \mathbf{v} \cdot \mathbf{v} + \frac{1}{2} \symbf{\omega} \cdot \mathbb{I}_P \cdot \symbf{\omega} + \left\langle \frac{1}{2} \sum_i m_i \delta \mathbf{v}_i \cdot \delta \mathbf{v}_i + \delta \symbf{\omega}_i \cdot \mathbb{I}_i \cdot \delta \symbf{\omega}_i + \sum_{ij} V_{ij} \right\rangle = \\
  & = K + E \ .
\end{aligned}$$

Potenza delle forze

$$\begin{aligned}
  P & = \sum_{k} \mathbf{f}_k \cdot \mathbf{v}_k = \\
    & = \sum_{k} \mathbf{f}^{e}_k \cdot \mathbf{v}_k + \sum_{ik} \mathbf{f}^i_{ki} \cdot \left( \mathbf{v}_k - \mathbf{v}_i \right) = \\
\end{aligned}$$

```
-->

## Energia interna
```{prf:definition} Energia interna
**Gibbs** definisce l'energia interna del sistema come differenza tra la sua energia totale e l'energia cinetica "macroscopica", 

$$E = E^{tot} - K \ .$$
```

Il bilancio dell'energia interna viene ricavato come differenza dei bilanci dell'energia totale, descritto dal primo principio della termodinamica

$$d E^{tot} := \delta L^{ext} + \delta Q^{ext} \ ,$$

e il bilancio dell'energia cinetica, fornito dal teorema dell'energia cinetica ricavato in meccanica,

$$d K = \delta L^{ext} + \delta L^{int} \ .$$

Il bilancio dell'energia interna diventa quindi

$$d E = \delta Q^{ext} - \delta L^{int} \ .$$
