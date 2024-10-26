(physics-hs:electromagnetism:electromagnetism-steady)=
# Magnetismo ed elettromagnetismo in regime stazionario

## Esperienze elementari su campo magnetico
- cos'è? come costruire un campo magnetico? o avere multipli di un campo magnetico?

## Esperienza di Faraday

$$d \vec{F} = - i \, \vec{b} \times d \vec{\ell} \ .$$

**todo** ha senso associarla a Faraday? Nessuno la conosceva prima? Galvani, Volta,... come misuravano la corrente elettrica?

### Il galvanometro

Il galvanometro è uno strumento utilizzato per la misura della corrente elettrica. Sfrutta l'azione meccanica osservata nell'esperienza di Faraday

Il momento meccanico generato dalla corrente nel cavo elettrico equilibria un momento generato da componenti meccanici "noti", realizzabili e tarabili con estrema precisione.

**todo** *Serve questo riferimento qui?*
- azioni elettro-meccaniche:..., cenni al motore elettrico in corrente continua? serve accoppiamento $\vec{e} \leftrightarrow \vec{b}$ di Faraday


## Esperienze di Oersted e Ampere

- interazione tra corrente elettrica e campo magnetico, in regime stazionario:
  - esperienze di Oesrted e Ampére:

### Legge di Ampére
Forza scambiata tra due cavi percorsi da corrente elettrica

$$F = \frac{\mu}{2 \pi} \frac{i_1 \, i_2}{d}$$

### Legge di Biot-Savart
Confrontando la legge di Ampére con l'esperienza di Faraday, è possibile ricavare l'espressione del campo magentico prodotto da un cavo percorso da corrente elettrica,

$$F = \frac{\mu}{2 \pi} \frac{i}{d}$$

**todo**
- campo magnetico prodotto da un cavo rettilineo infinito
- campo magnetico prodotto da un solenoide: lineare infinito, toroidale

## Verso le equazioni di Maxwell

### Legge di Gauss per il flusso del campo magnetico

  $$\Phi_{\partial V}(\vec{d}) = 0$$

**todo** *interpretazione: inesistenza del monopolo magnetico? linee di campo chiuse?*

### Legge di Ampére

  $$\oint_{\ell_S} \vec{e} \cdot \hat{t} = \Gamma_{\ell_S}(\vec{h}) = \Phi_{S}(\vec{j}) = i_S \ ,$$

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


## Modelli microscopici del magnetismo

## Moto di una carica elettrica in un campo elettromagnetico
Forza di Lorentz

$$\vec{F}^{Lorentz} = q \left(\vec{e}(P) + \vec{b}(P) \times \vec{v} \right)$$

Moto di una carica elettrica in un campo elettromagnetico, nell'ipotesi di effetto nullo su di essa del proprio campo elettrico

  $$m \ddot{ \vec{r} } = \vec{R}^{ext} = q \left( \vec{e}(P) + \vec{b}(P) \times \dot{\vec{r}} \right) + \vec{F}^{\text{non EM}}$$

- **todo** esempi
