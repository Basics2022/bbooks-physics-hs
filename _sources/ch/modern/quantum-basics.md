(physics-hs:modern:quantum:basics)=
# Introduzione alla meccanica quantistica

In questa sezione si presentano le idee fondamentali che hanno portato allo sviluppo della meccanica quantistica come una meccanica per l'atomo e altri sistemi di dimensioni microscopiche, la natura probabilistica delle leggi fisiche nell'ambito della meccanica quantistica, il ruolo fondamentale della misura nello sviluppo di una teoria, i limiti che vincolano la nostra conoscenza, e alcuni esempi che mettano in luce alcune differenze tra la fisica dei sistemi microscopici descritta dalla meccanica quantistica rispetto alla fisica di sistemi macroscopici governati dalla meccanica classica.



(physics-hs:modern:quantum:basics:origin)=
## Origine della meccanica quantistica

Il primo obiettivo nella formulazione di una teoria della meccanica dei sistemi micrsocopici/atomici è la previsione corretta degli spettri discreti di emissione/assorbimento degli atomi, in termini di frequenza e intensità della radiazione emessa/assorbita.

```{dropdown} Consigli mutlimediali

- CURIUSS - Il Principio di Intederminazione {cite}`curiuss-heisenberg`

```

```{dropdown} **todo**
- *Separare meccanica matriciale (Heisenberg), da meccanica ondulatoria (Schrodinger), da equivalenza (Dirac)*
- *Aggiungere link ad articoli*
```

- 1925: W.Heisenberg deduce una teoria per la meccanica dell'elettrone usando solo le quantità fisiche **osservate**, cioè le freqeunze e le intensità della radiazione emessa o assorbita dagli atomi. La formulazione di Heisenberg è una meccanica matriciale, anche se non sapeva cosa fossero le matrici. L'algebra matriciale non era un sapere scontato all'inizio del secolo, ma per fortuna di Heisenberg lui era una persona fuori dal comune, mentre nel gruppo di ricerca di Gottingen guidato da M.Born, lo stesso M.Born e P.Jordan erano molto ferrati in materia
  - conservazione dell'energia
  - energia del sistema può assumere solo valori discreti, quantizzati
  - non-commutatività delle operazioni con le matrici. Questa non-commutatività è strettamente legata alla [relazione di indeterminazione](physics-hs:modern:quantum:basics:uncertainty)

- 1926: E.Schrodinger formula una teoria ondulatoria della meccanica quantistica, non relativistica. L'equazione è un'equazione d'onda per una funzione complessa $\psi(x,t): E \times T \rightarrow \mathbb{C}$, alla quale si fatica ad attribuire un significato. L'intuizione di M.Born attribuisce un'[interpretazione probabilistica](physics-hs:modern:quantum:basics:probability) alla funzione d'onda $\psi(x,t)$, o meglio al suo modulo $|\psi(x,t)|^2$: questa funzione può essere interpretata come densità di probabilità nello spazio, che rappresenta la probabilità di trovare una particella nella posizione dello spazio $x$ al tempo $t$.

- 1926-1928: P.Dirac è un fottuto stramaledetto genio. Ventenne, ha già ri-formulato la teoria di Heisenberg-Born-Jordan, e dimostrato l'equivalenza tra le formulazioni di Heisenberg-Born-Jordan e di Schrodinger; mentre l'equazione di Schrodinger presenta dei limiti nella previsione dei risultati, P.Dirac sviluppa l'equazione d'onda per la meccanica quantistica in regime relativistico, cioè in accordo con la [teoria della relatività ristretta](physics-hs:modern:einstein:special) di A.Einstein. Questa equazione apre un mondo:
  - incorpora la possibilità della distruzione della massa con la creazione di energia (e viceversa), e quindi getta le basi per le teorie quantistiche dei campi in cui può variare il numero dei componenti
  - prevede l'esistenza di valori di energia negativa[^energy-negative], e dell'antimateria

[^energy-negative]: Mentre in meccanica classica l'energia è una quantità definita a meno di una costante additiva, questa arbitrarietà scompare nella teoriadi A.Einstein. **todo** *aggiungere riferimento e dettagli*

(physics-hs:modern:quantum:basics:probability)=
## Interpretazione probabilistica

```{epigraph}
<!--the theory produces a good deal but hardly brings us closer to the secret of the Old One. I am at all events convinced that -->

Sono convinto che Dio non gioca a dadi

-- A.Einstein
```

```{epigraph}
Smettila di dire a Dio cosa fare

-- M.Born

```

Questo scrive[^einstein-god-dice] A.Einstein in una corrispondenza {cite}`born1916albert` con M.Born e N.Bohr nel 1926,

[^einstein-god-dice]: Le frasi di A.Einstein dalle quali è stata tagliata la citazione sono "la teoria produce dei buoni risultati, ma difficilmente ci porterà più vicini al segreto di Dio. Sono fermamente convinto che Dio non giochi a dadi". Chi è interessato è conosce il tedesco {cite}`born1916albert`, o chi si accontenta della traduzione in inglese {cite}`bromberg1972twentieth` trova i riferimenti; per chi vuole ricordarsi l'importanza delle fonti, ma in fondo è un ciarlatano, si consiglia una ricerca "Einstein fake quotes" sul vostro motore di ricerca preferito. Inoltre non èvero che A.Einstein non conoscesse la matematica - anche se c'era chi la conosceva meglio, e gli diede una mano soprattutto per la [teoria della relatività generale](physics-hs:modern:einstein:general)...: Einstein fu bocciato la prima volta all'ammissione all'ETH, il Politecnico di Zurigo, per la prova di francese. Aveva 16 anni. Entrò l'anno successivo.

Interpretazione probabilistica di alcuni esperimenti:
- doppia fenditura
- intensità delle righe degli spettri di emissione

(physics-hs:modern:quantum:basics:measurements)=
## Misura
- interazione sistema-strumento
- lo strumento è tipicamente un sistema macroscopico che funziona nel regime ben descritto dalla fisica classica
- ...


(physics-hs:modern:quantum:basics:uncertainty)=
## Indeterminazione di Heisenberg
Non è possibile conoscere contemporaneamete il valore di alcune coppie di grandezze fisiche, dette complementari o coniugate. Alcuni esempi sono:
- stessa componente di posizione e quantità di moto
  
    $$\sigma_{x_i} \sigma_{p_i} \ge \frac{\hbar}{2}$$

- diverse componenti del momento della quantità di moto (sia momento totale, sia orbitale, sia di spin)
- ...

(physics-hs:modern:quantum:basics:spin)=
## Spin, esperimento di Stern-Gerlach
Le particelle subatomiche manifestano due tipi di momento angolare:
- il momento angolare orbitale, $\hat{\mathbf{L}}$
- momento angolare intrinseco, di **spin**, $\hat{\mathbf{S}}$

Il momento angolare totale è la somma di questi due contributi, $\hat{\mathbf{J}} = \hat{\mathbf{L}} + \hat{\mathbf{S}}$


## Alcuni esempi 1-dimensionali
### Moto libero di un sistema puntiforme
Moto libero, incertezza tra posizione e quantità di moto porta a "diffusione della probabilità"

### Barriera e buca di potenziale
Contronto e differenze con meccanica classica:
- collisione con una parete - barriera di potenziale
- moto libero in una scatola - buca di potenziale

Effetti:
- effetto tunnel

Buca di potenziale, sistema finito:
- valori di energia discreti

Barriera di potenziale, dominio infinito:
- valori di energia continui
- ...

### Oscillatore armonico
- valore di energia discreti

## Atomo di Idrogeno, $H$

## Sistemi di elementi identici
- In meccanica quantistica, non è possibile distinguere elementi identici in sistemi che contengono più elementi
- Stato di un sistema

   $$\Psi(\mathbf{q}_1, \mathbf{q}_2, \dots \mathbf{q}_n) \ ,$$

   è indistinguibile con uno scambio di due elementi identici. Quindi in seguito a uno scambio di argomenti della funzione d'onda, la funzione d'onda non cambia a meno di un cambio di fase (in principio arbitrario, e ininfluente sulla fisica del problema),

   $$\Psi(\mathbf{q}_1, \dots, \mathbf{q}_a, \dots, \mathbf{q}_b, \dots, \mathbf{q}_n) = e^{j \alpha} \Psi(\mathbf{q}_1, \dots, \mathbf{q}_b, \dots, \mathbf{q}_a, \dots, \mathbf{q}_n) \ .$$

   Un secondo scambio degli stessi argomenti comporta che 
   
   $$\Psi(\mathbf{q}_1, \dots, \mathbf{q}_a, \dots, \mathbf{q}_b, \dots, \mathbf{q}_n) = e^{j 2 \alpha} \Psi(\mathbf{q}_1, \dots, \mathbf{q}_a, \dots, \mathbf{q}_b, \dots, \mathbf{q}_n) \ .$$

   Questa relazione è soddisfatta per qualsiasi valore della funzione d'onda nel caso in cui $e^{j 2 \alpha} = 1$, e quindi $e^{i \alpha} = \pm 1$.

   La funziona d'onda che rappresenta lo stato di un sistema composto da più elementi identici deve quindi essere o simmetrica o anti-simmetrica rispetto a uno scambio di indici:
   - funzione d'onda simmetrica, i **bosoni**

     $$\Psi(\mathbf{q}_1, \dots, \mathbf{q}_a, \dots, \mathbf{q}_b, \dots, \mathbf{q}_n) = \Psi(\mathbf{q}_1, \dots, \mathbf{q}_b, \dots, \mathbf{q}_a, \dots, \mathbf{q}_n) \ .$$

   - funzione d'onda anti-simmetrica, i **fermioni**

     $$\Psi(\mathbf{q}_1, \dots, \mathbf{q}_a, \dots, \mathbf{q}_b, \dots, \mathbf{q}_n) = - \Psi(\mathbf{q}_1, \dots, \mathbf{q}_b, \dots, \mathbf{q}_a, \dots, \mathbf{q}_n) \ .$$

```{prf:definition} Principio di esclusione di Pauli - per fermioni
:label: pauli-principle

**Principio di esclusione di Pauli** Due fermoni della stessa natura non possono trovarsi nello stesso stato. La relazione di anti-simmetria della funzione d'onda per i fermioni corrisponde a una generalizzazione della condizione 

$$f(x,y) = - f(y,x) \ .$$

In questo caso, se i due argomenti della funzione assumono lo stesso valore (analogia con due fermioni che si trovano nello stesso stato) allora segue che

$$f(x,x) = - f(x,x) \ ,$$

relazione che implica $f(x,x) = 0$. Poiché il modulo quadro di $\Psi$ rappresenta la densità di probabilità di uno stato del sistema, se $\Psi(\mathbf{q}_i) = 0$, allora

$$p(\dots, \mathbf{q}_i, \dots, \mathbf{q}_i, \dots) = |\Psi(\dots, \mathbf{q}_i, \dots, \mathbf{q}_i, \dots)|^2 = 0 \ ,$$

e quindi **la probabilità che due fermioni si trovino nello stesso stato è nulla**.

```

**todo** La natura dei fermioni è legata allo [spin]() frazionario

```{prf:example} Gli elettroni sono fermioni
:label: fermions-electrons

Gli elettroni sono fermioni. Questo comportamento degli elettroni è alla base della spiegazione della struttura atomica, e dell'occupazione di orbitali differenti.

```

```{prf:example} Bosoni in una buca di potenziale
```

```{prf:example} Fermioni in una buca di potenziale
```

## Riferimenti

```{bibliography}
:style: unsrt
:filter: docname in docnames
```
