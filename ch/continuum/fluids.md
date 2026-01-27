(continuum:fluids)=
# Fluidi

Un fluido può essere definito come uno stato della materia che non è in grado di sostenere sforzi di taglio in quiete. Una porzione di fluido in quiete scambia per contatto solo reazioni normali alla sua superficie. La forza elementare scambiata dalla sezione di superficie elementare $\Delta S$ in $\vec{r}$, con normale $\hat{n}(\vec{r})$ uscente dalla superficie della porzione di fluido considerata è

$$\Delta \vec{F} = - p(\vec{r}) \hat{n}(\vec{r}) \Delta S \ ,$$

dove $p(\vec{r})$ è la pressione nel punto considerato. Il versore normale dà la direzione della forza, il segno meno dà il verso (l'azione esercitata da un fluido su una superficie esterna è sempre di spinta, e per il terzo principio della dinamica lo stesso vale per l'azione esercitata da una superficie esterna sul fluido), mentre la pressione può essere interpretata dal punto di vista meccanico come il valore assoluto della forza per unità di superficie. La pressione ha quindi come unità di misura il Pascal, $\text{Pa} = \frac{\text{N}}{\text{m}^2}$.

(fluids:statics)=
## Statica dei fluidi

(fluids:statics:stevino)=
### Legge di Stevinio

...

$$P + \rho g z = \text{const}$$

...

(fluids:statics:archimedes)=
### Legge di Archimede

Un corpo di volume $V$ immerso in un fluido di densità $\rho_f$ e soggetto a un campo gravitazionale uniforme $\vec{g} = - g \hat{z}$, riceve dal fluido una spinta dal basso verso l'alto di intensità *pari al peso del volume del fluido spostato*, cioè la forza di Archimede è

$$\vec{F}^{\text{Arch}} = \rho_f V g \hat{z} \ .$$


(fluids:dynamics)=
## Dinamica dei fluidi

(fluids:dynamics:bernoulli)=
### Bilancio di quantità di moto, energia e teorema di Bernoulli

(fluids:dynamics:bernoulli)=
### Azioni fluidodinamiche su un corpo in moto in un fluido

**todo** *Pillole di analisi dimensionale, per ricavare la formula $\vec{F} = \frac{1}{2} \rho |\vec{v}|^2 S \vec{c}_F(Re, M, \dots)$*

(fluids:dynamics:stokes)=
#### Legge di Stokes
L'interazione tra un fluido e un corpo di piccole dimensioni in moto relativo rispetto al fluido con *velocità relativa* $\vec{v}_{rel}$ rispetto alla velocità del fluido locale si manifesta come una forza di resistenza aerodinamica. Per un corpo sferico di raggio $R$, la formula di Stokes fornisce un'espressione *esatta* (*esatta all'interno del modello usato*) di questa forza

$$\vec{F} = - 6 \pi \mu R \vec{v}_{rel} \ .$$

La formula di Stokes fornisce un'espressione della resistenza aerodinamcia lineare rispetto alla velocità relativa.

**todo** *Commentare effetto di \text{Re}. Cogliere l'occasione per un po' di analisi dimensionale per ottenere la formula $\vec{F} = \frac{1}{2} \rho |\vec{v}|^2 \vec{c}_F(\text{Re}, \text{M})$...*


