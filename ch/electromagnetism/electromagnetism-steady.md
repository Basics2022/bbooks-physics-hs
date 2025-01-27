(physics-hs:electromagnetism:electromagnetism-steady)=
# Magnetismo ed elettromagnetismo in regime stazionario

(physics-hs:electromagnetism:electromagnetism-steady:experience)=
## Esperienze elementari su campo magnetico
- cos'è? come costruire un campo magnetico? o avere multipli di un campo magnetico?

(physics-hs:electromagnetism:electromagnetism-steady:experience-faraday)=
## Esperienza di Faraday
L'esperienza di Faraday riconosce che su un tratto elementare $d \vec{\ell}$ di un cavo elettrico percorso da corrente $i$ in un campo magnetico $\vec{b}$ agisce una forza elementare

$$d \vec{F} = - i \, \vec{b} \times d \vec{\ell} \ .$$ (eq:faraday:force)

Riconoscendo che il risultato è frutto dell'applicazione del modello di [conduttore con sezione piccola](physics-hs:electromagnetism:circuits-electric:electric-cable) si può riscrivere l'espressione della forza in termini di densità di corrente elettrica usando la relazione {eq}`eq:cable:current-current-density`, e cercando la densità volumentrica di forza $\vec{f}$, tale che $d \vec{F} = \vec{f} dV = \vec{f} A d \ell$,

$$\vec{f} A d \ell = - j A \vec{b} \times \vec{\ell} = - \rho v A \vec{b} \times \hat{t} \ell = - A \vec{b} \times \vec{j} d \ell$$

e quindi

$$\vec{f} = - \vec{b} \times \vec{j} \ .$$

**todo** ha senso associarla a Faraday? Nessuno la conosceva prima? Galvani, Volta,... come misuravano la corrente elettrica?

(physics-hs:electromagnetism:electromagnetism-steady:experience-faraday:galvanometer)=
### Il galvanometro

Il galvanometro è uno strumento utilizzato per la misura della corrente elettrica. Sfrutta l'azione meccanica osservata nell'esperienza di Faraday

Il momento meccanico generato dalla corrente nel cavo elettrico equilibria un momento generato da componenti meccanici "noti", realizzabili e tarabili con la precisione richiesta.

**todo** *Serve questo riferimento qui?*
- spostare a fine capitolo
- azioni elettro-meccaniche:..., cenni al motore elettrico in corrente continua? serve accoppiamento $\vec{e} \leftrightarrow \vec{b}$ di Faraday? No in corrente continua

(physics-hs:electromagnetism:electromagnetism-steady:experience-oersted-ampere)=
## Esperienze di Oersted e Ampere

- interazione tra corrente elettrica e campo magnetico, in regime stazionario:
  - esperienze di Oesrted e Ampére:

**Legge di Ampére.** Forza (<span style="color:red">**todo** per unità di lunghezza; usare notazione vettoriale per indicare la direzione della forza</span>) scambiata tra due cavi percorsi da corrente elettrica

$$\frac{F}{L} = \frac{\mu}{2 \pi} \frac{i_1 \, i_2}{d}$$
Confrontando la legge di Ampére con l'esperienza di Faraday, è possibile ricavare l'espressione del campo magnetico prodotto da un cavo infinito percorso da corrente elettrica,

$$b = \frac{\mu}{2 \pi} \frac{i}{d}$$

**todo** *immagini*

(physics-hs:electromagnetism:electromagnetism-steady:biot-savart)=
## Legge di Biot-Savart
La legge di Biot-Savart permette di generalizzare i risultati dell'esperienza di Ampére. Il contributo elementare al campo magnetico $\vec{b}(\vec{r}_0)$ nel punto dello spazio $\vec{r}_0$ dovuto a un cavo elettrico[^ref:electric-cable] di lunghezza elementare $d \ell$ posizionato nel punto dello spazio $\vec{r}$ e percorso da corrente elettrica $i$ è dato dalla formula

$$d \vec{b}(\vec{r}_0) = - \frac{\mu}{4 \pi} i(\vec{r}) \frac{ \vec{r}_0 - \vec{r} }{| \vec{r}_0 - \vec{r} |^3} \times d \vec{\ell}(\vec{r}) \ .$$ (eq:biot-savart:differential)

Di conseguenza, il contributo dovuto alla corrente in un cavo elettrico descritto dal percorso $\gamma(\vec{r})$ è la somma dei contributi elementari {eq}`eq:biot-savart:differential`, per fenomeni continui l'integrale

$$\vec{b}(\vec{r}_0) = - \frac{\mu}{4 \pi} \int_{\gamma(\vec{r})} i(\vec{r})  \frac{ \vec{r}_0 - \vec{r} }{| \vec{r}_0 - \vec{r} |^3}\times d \vec{\ell}(\vec{r}) \ .$$ (eq:biot-savart:integral)

[^ref:electric-cable]: Fare riferimento alla sezione sul [cavo elettrico](electric-current:cable), e l'approssimazione circuitale di cavi elettrici.

**todo** *aggiungere immagini per Biot-Savart*

**todo** *fare una sezione nel capitolo, per descrivere l'approccio comune ai fenomeni elettromagnetici, in cui compaiono "punti potenzianti" (attivi, dove c'è la causa di un fenomeno; qui il punto $\vec{r}$ dove c'è il cavo conduttore) e "punti potenziati" (passivi, dove si osserva la conseguenza di un fenomeno; qui il punto $\vec{r}_0$ dove si misura il campo magnetico)*

### Esempi di campi magnetici generati da corrente in cavi elettrici
In questa sezione si mostra il campo magnetico prodotto dalla corrente elettrica che passa in un cavi elettrici con particolari configurazioni: il cavo rettilineo infinito, la spira circolare, il solenoide infinito rettilineo, il solenoide toroidale. Queste configurazioni possono essere considerate delle idealizzazioni di casi reali, e costituiscono una buona approssimazione nel caso in cui si possano trascurare *effetti di bordo*. (**todo** *discutere*)

Le formule vengono ricavate in [appendice](physics-hs:electromagnetism:electromagnetism-steady:notes:biot-savart), usando lla forma generale della legge di Biot-Savart, e quando possibile delle considerazioni sulla geometria e sulle simmetrie dei problemi.

**todo** *aggiungere immagini per casi particolari*

````{only} latex
- Conduttore rettilineo infinito

  $$ \vec{b}(\vec{r}) =   \frac{\mu \, i}{2 \pi \, r} \hat{\theta} \ .$$

- Spira circolare, campo magnetico sull'asse
    
  $$\vec{b}(z,r=0) = \frac{\mu \, i}{2 \, R} \frac{1}{\left[1 + \left(\dfrac{z}{R}\right)^2 \right]^{3/2}} \hat{z} $$

- Solenoide rettilineo infinito. Il campo magnetico è nullo al di fuori del solenoide e uniforme all'interno, allineato lungo l'asse e con intensità

  $$b = \mu \frac{N}{\ell} \, i$$
  $$\phi = \dots$$

- Solenoide toroidale

  $$b() = \dots$$
  $$\phi = \dots$$

````

````{only} html
```{dropdown} Filo rettilineo infinito
$$z = R \, \tan \theta$$
$$dz = R \frac{1}{\cos^2 \theta} \, d \theta$$
$$r^2 = R^2 + z^2 = R^2 \left(1+\frac{\sin^2 \theta}{\cos^2 \theta} \right) = R^2 \frac{1}{\cos^2 \theta}$$


$$\begin{aligned}
  \vec{b}(\vec{r}_0) & = - \frac{\mu}{4 \pi} i \int_{z=-\infty}^{\infty} \hat{\theta} \frac{r}{r^2} \sin \theta dz = \\
                     & = - \frac{\mu}{4 \pi} i \hat{\theta} \int_{\theta=\pi}^{0} \frac{\cos^2 \theta}{R^2} \sin \theta R \frac{1}{\cos^2 \theta} \, d \theta = \\
                     & =   \frac{\mu}{4 \pi} i \hat{\theta} \int_{\theta=0}^{\pi} \frac{1}{R} \sin \theta \, d \theta = \\
                     & =   \frac{\mu \, i}{2 \pi \, R} \hat{\theta} \ .
\end{aligned}$$
```

```{dropdown} Spira circolare - campo magnetico sull'asse
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

````

<!--
Nell'ipotesi in cui il raggio $R$ dell'anello sia molto maggiore del raggio della sezione del toro, si può approssimare il campo come uniforme, $b =$
-->



(physics-hs:electromagnetism:magnetism:micro)=
## Modelli microscopici del magnetismo

**todo** *correnti di Ampére. Una carica elettrica in movimento (passare da Biot-Savart a carica, da corrente a carica discreta) genera un campo magnetico; un'$e^-$ in moto attorno al nucleo - qualsiasi cosa sia, sia l'elettrone, sia il suo movimento - quindi genera un campo magnetico, comportandosi come una spira (o un dipolo magnetico); a questo contributo, si aggiunge un momento magnetico intrinsceco di* **spin**, *come dimostrato dall'[esperimento di Stern-Gerlach](modern:experiments:stern-gerlach).*

*L'allineamento dei momenti magnetici degli atomi appartenenti a una vasta regione di un mezzo macroscopico si manifesta come magentismo del mezzo*

**todo** *aggiungere dettagli, temperatura di Curie,...*


(physics-hs:electromagnetism:lorentz)=
## Moto di una carica elettrica in un campo elettromagnetico
Il moto di una corpo puntiforme di massa $m$ e carica elettrica $q$ in una regione dello spazio nel quale è presente un campo elettromagnetico $\vec{e}(P, t)$, $\vec{b}(P,t)$ è soggetto a una forza esterna,

$$\vec{F}^{Lorentz}(t) = q \left[\vec{e}(P,t) - \vec{b}(P,t) \times \vec{v}_P(t) \right]$$ (eq:force:lorentz)

definita **forza di Lorentz**.

Nell'ipotesi di risultante nulla degli effetti del campo elettromagnetico generato da un sistema su se stesso[^motion:electromagnetic-field], l'equazione dinamica che governa il moto del sistema è

  $$m \ddot{ \vec{r}_P } = \vec{R}^{ext} = q \left[ \vec{e}(P) + \vec{b}(P) \times \dot{\vec{r}_P} \right] + \vec{F}^{\text{non EM}}$$

[^motion:electromagnetic-field]: Il campo elettromagnetico generato dalla carica nell'istante $t$ non influenza il moto della carica stessa allo stesso istante. Perché evidenziare il tempo $t$? Perché il campo EM si propaga nello spazio e nel tempoe quindi il moto di una carica al tempo $t$ può essere influenzato dal campo elettromagnetico generato da una carica - anche se stessa (se c'è riflessione...) - in qualche istante precedente.

Esempi dell'applicazioni della legge di Lorentz si ritrovano negli esperimenti condotti a cavallo della 1900 nell'indagine sulla struttura della materia e sui suoi componenti elementari, come:
- l'[esperimento di Thomson](modern:experiments:thomson:electron)
- ...
- **todo** esempi


(physics-hs:electromagnetism:electromagnetism-steady:maxwell)=
## Verso le equazioni di Maxwell

Fare riferimento a:
- [equazioni di Maxwell per l'elettrostatica](physics-hs:electromagnetism:electrostatics:maxwell)
- [equazioni di Maxwell e principi dell'elettromagnetismo classico in regime stazionario](physics-hs:electromagnetism:electromagnetism-steady:maxwell)
- [equazioni di Maxwell e principi dell'elettromagnetismo classico](physics-hs:electromagnetism:electromagnetism-general:maxwell)

(physics-hs:electromagnetism:electromagnetism-steady:maxwell:gauss-b)=
### Legge di Gauss per il flusso del campo magnetico

  $$\Phi_{\partial V}(\vec{b}) = 0$$ (eq:gauss:b)

**todo** *interpretazione: inesistenza del monopolo magnetico? linee di campo chiuse?*

(physics-hs:electromagnetism:electromagnetism-steady:maxwell:ampere)=
### Legge di Ampére in regime stazionario

  $$\oint_{\ell_S} \vec{h} \cdot \hat{t} = \Gamma_{\ell_S}(\vec{h}) = \Phi_{S}(\vec{j}) = i_S \ ,$$ (eq:ampere:steady)

  essendo $\ell_S = \partial S$ il contorno - chiuso - della superficie $S$.

Non abbiamo ancora finito l'indagine sui fenomeni elettromagnetici. Le equazioni che abbiamo trovato finora:
- sono **incomplete**, nel senso che non riescono a descrivere il fenomeno fisico dell'[induzione elettromagnetica](physics-hs:electromagnetism:electromagnetism-general:em-induction), e di questo non possiamo accorgercene senza ulteriori esperienze
- tra di loro **incongruenti**, contraddittorie, e di questo possiamo accorgercene confrontando la legge di Ampére in regime stazionario {eq}`eq:ampere:steady` con l'[equazione di bilancio della carica elettrica](physics-hs:electromagnetism:charge-conservation) {eq}`eq:current:charge-equation`. La legge di Ampéere in regime stazionario {eq}`eq:ampere:steady` per una superficie chiusa $S = \partial V$ si riduce a 

   $$\Phi_{\partial V}(\vec{j}) = 0 \ ,$$

   poiché il contorno $\partial \ell$ di una superficie chiusa $S = \partial V$ non ha estensione, non esiste. Confrondando questa equazione con la legge di bilancio della carica elettrica,

   $$\dot{Q}_V = - \Phi_{\partial V}(\vec{j}) \ ,$$

   si sarebbe tentati di concludere che $\dot{Q}_V \equiv 0$ per ogni volume $V$, cioè non è possibile cambiare la carica elettrica contenuta in qualsiasi volume $V$. Questa conclusione dimostra una chiara incongruenza con l'esperienza, e la sua [soluzione da parte di Maxwell](physics-hs:electromagnetism:electromagnetism-general:ampere-maxwell) sarà un contributo decisivo per formulare un insieme di princìpi fisici consistente dei fenomeni elettromagnetici, e riconoscerne il carattere ondulatorio.



Sono necessarie quindi due "correzioni" delle equazioni, per includere fenomeni **non stazionari**, in generale più difficili da cogliere: una correzione sarà necessaria per poter descrivere l'induzione elettromagnetica, l'altra per rendere l'equazione di Ampére compatibile con il [principio di conservazione della carica elettrica](). Questi due interventi vengono discussi nel capitolo successivo e sono legati ai nomi di due giganti della scienza, rispettivamente M.Faraday e J.C.Maxwell.

