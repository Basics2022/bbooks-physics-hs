(physics-hs:waves:optics)=
# Ottica

**todo**
- Equazione delle onde per il campo EM

```{prf:definition} Indice di rifrazione
:label: refraction-index

L'indice di rifrazione $n_i$ di un materiale omogeneo è una proprietà del materiale che può essere definita come rapporto della velocità di propagazione della luce nel vuoto $c$ e nel materiale $c_i$,

$$n_i = \frac{c_0}{c_i} \ .$$

```

(physics-hs:waves:optics:geometric)=
## Ottica geometrica

**Approssimazione con raggi di luce.** I raggi luminosi sono qualitativamente delle linee geometriche che indicano la propagazione della luce. Essi possono essere definiti come delle curve perpendicolari in ogni punto ai fronti d'onda del campo elettromagnetico.

**todo** 
- *discutere approssimazione geometrica, con raggi luminosi; quando vale?*
- *aggiungere immagini per questa approssimazione: bridging EM field and geometrical optics, some examples: free space homogeneous medium; discontinuous medium; continuously varying in-homogeneous medium: miraggio e fata morgana*

(physics-hs:waves:optics:geometric:principles)=
### Princìpi dell'ottica geometrica
**Propagazione rettilinea in un mezzo omogeneo.** In un mezzo omogeneo, con indice di rifrazione $n$ ({prf:ref}`refraction-index`) uniforme, i raggi luminosi si propagano su traiettorie rettilinee.

**Legge di Snell - riflessione e rifrazione tra mezzi discontinui.** Per soddisfare le condizioni di continuità del campo elettromagnetico in corrispondenza di una discontinuità di proprietà fisiche, un raggio che si propaga nel mezzo 1 e incidente su una discontinuità con il mezzo 2 con un angolo $\theta{1,i}$ con la direzione normale, in generale:
- viene riflesso con lo stesso angolo 

   $$\theta_{1,r} = \theta_{1,i}$$

- viene trasmesso con angolo $\theta_{2,t}$, tale che

   $$\frac{\sin \theta_{2,t}}{\sin \theta_{1,i}} = \dfrac{n_1}{n_2} = \dfrac{c_2}{c_1} \ .$$

**todo** *Stabilire i coefficienti di riflessione e trasmissione. Scrivere sezione in physics-electromagnetism*

**Riflessione totale.** Quando $\frac{c_2}{c_1} > 1$ esiste un angolo di incidenza limite oltre al quale non avviene trasmissione nel secondo mezzo. Il valore massimo della funzione $\sin$ è 1; la condizione limite, di riflessione totale si ottiene quando 

$$1 = \sin \theta_{2,t} = \frac{c_2}{c_1} \sin \theta_{1,i} \qquad \rightarrow \qquad $$



