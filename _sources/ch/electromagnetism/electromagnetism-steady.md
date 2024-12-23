(physics-hs:electromagnetism:electromagnetism-steady)=
# Magnetismo ed elettromagnetismo in regime stazionario

(physics-hs:electromagnetism:electromagnetism-steady:experience)=
## Esperienze elementari su campo magnetico
- cos'è? come costruire un campo magnetico? o avere multipli di un campo magnetico?

(physics-hs:electromagnetism:electromagnetism-steady:experience-faraday)=
## Esperienza di Faraday

$$d \vec{F} = - i \, \vec{b} \times d \vec{\ell} \ .$$

**todo** ha senso associarla a Faraday? Nessuno la conosceva prima? Galvani, Volta,... come misuravano la corrente elettrica?

(physics-hs:electromagnetism:electromagnetism-steady:experience-faraday:galvanometer)=
### Il galvanometro

Il galvanometro è uno strumento utilizzato per la misura della corrente elettrica. Sfrutta l'azione meccanica osservata nell'esperienza di Faraday

Il momento meccanico generato dalla corrente nel cavo elettrico equilibria un momento generato da componenti meccanici "noti", realizzabili e tarabili con la precisione richiesta.

**todo** *Serve questo riferimento qui?*
- azioni elettro-meccaniche:..., cenni al motore elettrico in corrente continua? serve accoppiamento $\vec{e} \leftrightarrow \vec{b}$ di Faraday

(physics-hs:electromagnetism:electromagnetism-steady:experience-oersted-ampere)=
## Esperienze di Oersted e Ampere

- interazione tra corrente elettrica e campo magnetico, in regime stazionario:
  - esperienze di Oesrted e Ampére:

**Legge di Ampére.** Forza (<span style="color:red">**todo** per unità di lunghezza; usare notazione vettoriale per indicare la direzione della forza</span>) scambiata tra due cavi percorsi da corrente elettrica

$$\frac{F}{L} = \frac{\mu}{2 \pi} \frac{i_1 \, i_2}{d}$$
Confrontando la legge di Ampére con l'esperienza di Faraday, è possibile ricavare l'espressione del campo magnetico prodotto da un cavo infinito percorso da corrente elettrica,

$$b = \frac{\mu}{2 \pi} \frac{i}{d}$$

**todo**
- campo magnetico prodotto da un cavo rettilineo infinito
- campo magnetico prodotto da un solenoide: lineare infinito, toroidale


(physics-hs:electromagnetism:electromagnetism-steady:biot-savart)=
## Legge di Biot-Savart
La legge di Biot-Savart permette di generalizzare i risultati dell'esperienza di Ampére. Il contributo elementare al campo magnetico $\vec{b}(\vec{r}_0)$ nel punto dello spazio $\vec{r}_0$ dovuto a un cavo elettrico[^ref:electric-cable] di lunghezza elementare $d \ell$ posizionato nel punto dello spazio $\vec{r}$ e percorso da corrente elettrica $i$ è dato dalla formula

$$d \vec{b}(\vec{r}_0) = - \frac{\mu}{4 \pi} i(\vec{r}) \frac{ \vec{r}_0 - \vec{r} }{| \vec{r}_0 - \vec{r} |^3} \times d \vec{\ell}(\vec{r}) \ .$$ (eq:biot-savart:differential)

Di conseguenza, il contributo dovuto alla corrente in un cavo elettrico descritto dal percorso $\gamma(\vec{r})$ è la somma dei contributi elementari {eq}`eq:biot-savart:differential`, per fenomeni continui l'integrale

$$\vec{b}(\vec{r}_0) = - \frac{\mu}{4 \pi} \int_{\gamma(\vec{r})} i(\vec{r})  \frac{ \vec{r}_0 - \vec{r} }{| \vec{r}_0 - \vec{r} |^3}\times d \vec{\ell}(\vec{r}) \ .$$ (eq:biot-savart:integral)

[^ref:electric-cable]: Fare riferimento alla sezione sul [cavo elettrico](electric-current:cable), e l'approssimazione circuitale di cavi elettrici.

**todo** *fare una sezione nel capitolo, per descrivere l'approccio comune ai fenomeni elettromagnetici, in cui compaiono "punti potenzianti" (attivi, dove c'è la causa di un fenomeno; qui il punto $\vec{r}$ dove c'è il cavo conduttore) e "punti potenziati" (passivi, dove si osserva la conseguenza di un fenomeno; qui il punto $\vec{r}_0$ dove si misura il campo magnetico)*

### Esempi di campi magnetici generati da corrente in cavi elettrici
In questa sezione si mostra il campo magnetico prodotto dalla corrente elettrica che passa in un cavi elettrici con particolari configurazioni: il cavo rettilineo infinito, la spira circolare, il solenoide infinito rettilineo, il solenoide toroidale. Queste configurazioni possono essere considerate delle idealizzazioni di casi reali, e costituiscono una buona approssimazione nel caso in cui si possano trascurare *effetti di bordo*. (**todo** *discutere*)

Le formule vengono ricavate in [appendice](physics-hs:electromagnetism:electromagnetism-steady:notes:biot-savart), usando lla forma generale della legge di Biot-Savart, e quando possibile delle considerazioni sulla geometria e sulle simmetrie dei problemi.



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

```{Spira circolare - campo magnetico sull'asse}
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

## Verso le equazioni di Maxwell

### Legge di Gauss per il flusso del campo magnetico

  $$\Phi_{\partial V}(\vec{b}) = 0$$

**todo** *interpretazione: inesistenza del monopolo magnetico? linee di campo chiuse?*

### Legge di Ampére

  $$\oint_{\ell_S} \vec{h} \cdot \hat{t} = \Gamma_{\ell_S}(\vec{h}) = \Phi_{S}(\vec{j}) = i_S \ ,$$

  essendo $\ell_S = \partial S$ il contorno - chiuso - della superficie $S$.

- Questa equazione è valida **solo** in un regime elettrostatico: la forma generale dell'equazione di Ampére prevede un termine dipendente dal tempo, che è identicamente nullo nel regime elettrostatico.

- Senza questo termine, l'equazione non sarebbe consistente con l'equazione del bilancio della carica elettrica **todo** (aggiungere riferimento): la correzione di questa inconsistenza da parte di Maxwell è stata l'ultima azione, fondamentale, per ottenere un sistema di equazioni che governano i fenomeni elettromagnetici; la stessa modifica permette anche di riconoscere che i fenomeni EM sono fenomeni ondulatori; il calcolo della misura della velocità di propoagazione delle onde EM, confrontata con le misure disponibili della velocità della luce, permisero di riconoscere la luce come fenomeno EM

Per dimostrare l'incongruenza, è sufficiente applicare la legge di Ampére a una superficie che è il contorno di un volume chiuso, e che quindi ha contorno nullo,

$$S = \partial V  \qquad , \qquad  \partial S = \ell_S = \emptyset$$

In questo caso, la legge di Ampére diventa

$$0 = i_{\partial V} \ ,$$

mentre le leggi di conservazione della carica elettrica e la legge di Gauss per il campo elettrico

$$\begin{aligned}
  \dot{Q}_V & = - i_{\partial V} \\
  \Phi_{\partial V}(\vec{d}) & = Q_V \\
\end{aligned}$$

implicano 

$$i_{\partial V} = - \dot{Q}_V = - \dot{\Phi}_{\partial V}(\vec{d}) \ .$$

La correzione di Maxwell non è altro che l'aggiunta del termine $\dot{\Phi}_{\partial V}(\vec{d})$ all'equazione di Ampére per renderla compatibile con le altre equazioni dell'elettromagnetismo. Con questa modifica, l'**equazione di Ampére-Maxwell** diventa

$$\Gamma_{\partial S}(\vec{h}) - \dot{\Phi}_{S}(\vec{d}) = i_S $$


(physics-hs:electromagnetism:magnetism:micro)=
## Modelli microscopici del magnetismo



(physics-hs:electromagnetism:lorentz)=
## Moto di una carica elettrica in un campo elettromagnetico
Il moto di una corpo puntiforme di massa $m$ e carica elettrica $q$ in una regione dello spazio nel quale è presente un campo elettromagnetico $\vec{e}(\vec{r},t)$, $\vec{b}(\vec{r},t)$ è soggetto a una forza esterna,

$$\vec{F}^{Lorentz} = q \left[\vec{e}(P) - \vec{b}(P) \times \vec{v}_P \right]$$ (eq:force:lorentz)

definita **forza di Lorentz**.


Nell'ipotesi di risultante nulla degli effetti del campo elettromagnetico generato da un sistema su se stesso[^motion:electromagnetic-field], l'equazione dinamica che governa il moto del sistema è

  $$m \ddot{ \vec{r}_P } = \vec{R}^{ext} = q \left[ \vec{e}(P) + \vec{b}(P) \times \dot{\vec{r}_P} \right] + \vec{F}^{\text{non EM}}$$

[^motion:electromagnetic-field]: Il campo elettromagnetico generato dalla carica nell'istante $t$ non influenza il moto della carica stessa allo stesso istante. xPerché evidenziare il tempo $t$? Perché il campo EM si propaga nello spazio e nel tempoe quindi il moto di una carica al tempo $t$ può essere influenzato dal campo elettromagnetico generato da una carica in qualche istante precedente (serve riflessione?)...

- **todo** esempi
