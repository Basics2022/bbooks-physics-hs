(physics-hs:electromagnetism:electric-current)=
# Corrente elettrica

- corrente elettrica:
  - descrizione microscopica: materiale elettricamente neutro, con $e^-$ liberi di conduzione
  - def come flusso di carica: dalla descrizione micro alla descrizione macroscopica, media, ("fenomenologica"?)

Localmente, è possibile definire una **densità "macroscopica" di corrente elettrica** come la media pesata delle velocità delle cariche, $\vec{v}$.

$$\lim_{\Delta V(P) \rightarrow 0} \dfrac{\sum_{k \in \Delta V(P)} q_k}{\Delta V} = \rho(P)$$
$$\lim_{\Delta V(P) \rightarrow 0} \dfrac{\sum_{k \in \Delta V(P)} q_k \vec{v}_k}{\Delta V_P} = \vec{j}(P)$$

La **corrente elettrica** attraverso una superficie $S$ viene definita come il flusso di carica elettrica attraverso la superficie $S$,

$$i = I_{S} = \Phi_{S}(\vec{j}) \ .$$

````{list-table}
:header-rows: 0
* - ![](../../media/electric-current.png)
  - ![](../../media/electric-current-solids.png)
````

**Oss. Corrente elettrica in materiali neutri**: è possibile avere corrente elettrica anche in materiali elettricamente neutri, anche localmente. Ad esempio, nell'ipotesi di avere due sostanze diverse con carica $\rho^+$, $\rho^-$ e velocità media delle due sostanze $\vec{v}^+$, $\vec{v}^-$, la corrente densità di corrente elettrica è

$$\vec{j} = \rho \vec{v} = \rho^+ \vec{v}^+ + \rho^- \vec{v}^- \ . $$

Nel caso in cui il materiale sia neutro, la densità di carica elettrica è nulla, $0 = \rho = \rho^+ + \rho^- =$ e quindi $\rho^+ = - \rho^-$ e la densità di corrente elettrica può essere scritta come $\vec{j} = \rho^- (\vec{v}^- - \vec{v}^+)$.

**Oss. Corrente elettrica in solidi conduttori neutri.** I solidi hanno una struttura microscopica con gli atomi disposti in un reticolo, senza libertà di movimento. Nei solidi conduttori, gli elettroni "più esterni" della struttura atomica non sono localizzati attorno al singolo atono, ma sono "condivisi" e libersi di muoversi tra tutti gli atomi del solido: queste cariche elettriche libere di muoversi permettono una buona conduzione di corrente elettrica, e vengono chiamati **elettroni di conduzione**

Senza "forzanti esterne", come ad esempio campi elettrici, il moto degli elettroni di conduzione non ha direzioni privilegiate: poiché il moto delle cariche libere è casuale senza direzioni privilegiate, la velocità media è nulla (la velocità è una grandezza vettoriale!) e la corrente elettrica è nulla. Se le velocità delle cariche libere ha una direzione preferenziale, la loro velocità media, $\vec{v}^-$, e quindi la corrente elettrica, non è nulla. Assumendo che le cariche elettriche positive abbiano velocità media nulla rispetto all'osservatore $\vec{v}^+ = \vec{0}$, la densità di corrente elettrica diventa $\vec{j} = \rho^- \vec{v}^-$.
<!--
```{figure} ../../media/electric-current-solids.png
---
width: 30%
align: right
---
```
-->
<!--
La corrente elementare attraverso la superficie elementare $\Delta S$ è
V
$$\Delta i = \Phi_{\Delta S}(\vec{j}) = \vec{j} \cdot \hat{n} \Delta S = \frac{\sum_k q_k \vec{v}_k}{\Delta V} \cdot \hat{n} \Delta S = $$
-->
## Strumenti: misura e generazione
**todo**
  - strumenti per misurare corrente e tensione: amperometro e voltmetro
  - generatori di "spinta": generatori di tensione
  - resistenza al moto: la resistenza elettica

## Legge di conservazione della carica elettrica
Il principio di conservazione della carica elettrica

$$\dot{Q}_V = - \Phi_{\partial V}(\vec{j}) = - I_{\partial V}$$

- **todo** esempi/esercizi con misura della corrente e della carica elettrica, con strumenti di misura (misura o modello di strumento, come bilance)

## Conduzione

### Conduzione nei solidi "di Ohm"

In un materiale di Ohm, il campo elettrico $\vec{e}$ è proporzionale alla densità di corrente elettrica $\vec{j}$. Per un solido isotropo, senza direzioni preferenziali, la **forma locale - differenziale - della legge di Ohm** è
**Legge di Ohm** in forma locale: 

$$
\vec{j}(P) = \sigma(P) \, \vec{e}(P)
\qquad \ , \qquad
\vec{e}(P) = \rho_R(P) \, \vec{j}(P)
$$

essendo la resistività $\rho_R$, e la conduttanza $\sigma = \frac{1}{\rho_R}$ le costanti di proporzionalità, caratteristiche del materiale.

In un cavo conduttore, nell'ipotesi di grandezze uniformi sulla sezione - o riferendosi alle grandezze medie -, si può integrare la legge in forma locale su un tratto di cavo elementare, di lunghezza $d \ell$,

$$\begin{aligned}
 \underbrace{e \, d \ell}_{- d v} \, A & = \rho_R \, \underbrace{j \, A}_{i} \, d \ell \\
 \rightarrow \quad dv & = - \dfrac{\rho_R \, d \ell}{A} \, i = - dR \, i \ , 
\end{aligned}$$

avendo introdotto la differenza di potenziale elementare $d v$ tra gli estremi del tratto di cavo elementare, proporzionale alla corrente che transita nel cavo tramite la **resistenza elettrica** elementare $dR$. Queste relazioni che caratterizzano i materiali di Ohm sono le due leggi di Ohm:

 - **Prima legge di Ohm.** La differenza di potenziale agli estremi di un cavo di lunghezza elementare è proporzionale alla corrente, tramite la resistenza elettrica elementare,

   $$dv = - dR \, i \ ,$$

 - **Seconda legge di Ohm.** La resistenza elettrica di un cavo è direttamente proporzionale alla resistività del materiale, alla lunghezza del cavo, e inversamente proporzionale alla sezione del cavo,

   $$dR = \frac{\rho_R \, d\ell}{A} \ .$$

(physics-hs:electromagnetism:electric-current:gas)=
### Conduzione nei gas
**todo** *blabla*
- spiegazione (immediata utilizzando modello atomistico della materia): campo elettrico elevato "strappa" $e^-$ dagli atomi dei gas (rarefatti). Un atomo inizialmente neutro viene **ionizzato**: gli elettroni hanno carica negativa, lo ione (l'atomo al quale sono stati sottratti gli elettroni) ha carica positiva. Queste due entità hanno ora carica elettrica netta, e subiscono l'accelerazione dovuta all'interazione con un campo elettrico: il loro moto si sviluppa quindi in due direzioni diverse:
  - 
  - 
Esperimenti:
- Goldstein (1886) si concentra sul moto delle cariche positive: tubi di Crookes con sostanze diverse producono "particelle" (**todo** *Goldstein aveva in mente la natura discreta di quello che stava osservando? In quali termini si esprimeva?*) con rapporto $\frac{\text{carica}}{\text{massa}}$ caratteristici della sostanza, ma diversi da sostanza a sostanza. Spiegazione di oggi: gli ioni di sostanze diverse hanno massa e carica che dipendono dalla sostanza di partenza
- [Thomson](modern:experiments:thomson:electron) (1897) si concentra sul moto delle cariche negative, scoprendo che il rapporto $\frac{\text{massa}}{\text{carica}}$ è indipendente dalla sostanza contenuta nel tubo di Crookes. Viene scoperto/introdotto il concetto di elettrone, come unità di carica "elementare".
- Rontgen e i raggi X **todo** *link a Rontgen: raggi X, Becquerel: fosforescenza, emissione di raggi e radioattività naturale; coniugi Curie*

### Conduzione nei semiconduttori
 cenni all'elettronica: diodi, transistor, ...


