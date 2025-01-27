(physics-hs:electromagnetism:electromagnetism-general)=
# Induzione ed elettromagnetismo

Nella sezione precedente sono stati discussi alcuni fenomeni elettromagnetici in regime stazionario, mostrando come fenomeni elettrici possano indurre fenomeni magnetici - ad esempio, un cavo percorso da corrente elettrica genera un campo magnetico nello spazio circostante - mentre non si osservano fenomeni elettrici prodotti da fenomeni magnetici.

In questa sezione, vengono discussi i fenomeni elettromagnetici in regime instazionario, mostrando la dipendenza reciproca dei fenomeni magnetici da quelli elettrici (come già mostrato nella legge di Ampére, che comunque verrà [corretta da Maxwell](physics-hs:electromagnetism:electromagnetism-general:ampere-maxwell) per un termine instazionario), e dei fenomeni elettrici da quelli magnetici: questa dipendenza, che prende il nome di [**induzione elettromagnetica**](physics-hs:electromagnetism:electromagnetism-general:em-induction), inizialmente riconosciuta da Faraday nei primi decenni del XIX secolo, è il principio fisico sul quale si basa il funzionamento di un enorme numero di applicazioni tecnologiche contemporanee, come:
- i [**generatori** elettrici](physics-hs:electromagnetism:electric-machines:motor), come quelli impiegati nelle centrali elettriche, che convertono altre forme di energia in energia meccanica e infine in energia elettrica
- i [**motori** elettrici](physics-hs:electromagnetism:electric-machines:motor), che convertono l'energia elettrica in energia meccanica), come quelli utilizzati nei sistemi di trasporto (treni, e recentemente automobili e altri mezzi) o negli elettrodomestici
- i [**trasformatori**](physics-hs:electromagnetism:circuits-magnetic:transformer), sistemi che consentono di variare la tensione e la corrente tra circuiti differenti, attualmente impiegati nei sistemi contemporanei tra le fasi di produzione, trasporto e utilizzo dell'energia elettrica: tra la produzione e il trasporto viene innalzata la tensione per ridurre le predite durante il trasporto; per motivi di sicurezza e e soddisfare le caratteristiche degli utilizzatori, la tensione viene poi ridotta all'ingresso delle città e successivamente fino agli utilizzi industriali o domestici.

(physics-hs:electromagnetism:electromagnetism-general:em-induction)=
## Legge di Faraday per l'induzione elettromagnetica

La legge di Faraday riconosce che la circuitazione del campo elettromagnetico lungo un circuito $\partial S$ non è identicamente nulla nel caso instazionario, come dimostrato dall'equazione {eq}`eq:faraday:steady` per i [fenomeni elettrostatici](physics-hs:electromagnetism:electrostatics:maxwell:faraday), ma è uguale alla derivata temporale del flusso del campo magnetico $\vec{b}$ attraverso la superficie $S$,

   $$\Gamma_{\partial S}(\vec{e}) = - \dot{\Phi}_S(\vec{b}) \ .$$ (eq:faraday)

<!--
- legge di Faraday: corrente indotta

- corrente alternata:
  - principi e applicazioni:
    - trasformatori
    - generatori e motori elettrici
    - generazione/trasporto/trasformazione/consumo
-->

(physics-hs:electromagnetism:electromagnetism-general:ampere-maxwell)=
## Correzione di Maxwell dell'equazione di Ampére

- Correzione fondamentale per ricavare equazioni di bilancio dei fenomeni elettromagnetici che prevedessero la trasmissione di perturbazioni del campo come onde: il riconoscimento dei fenomeni elettromagnetici come fenomeni ondulatori con una velocità di trasmissione paragonabile alla velocità della luce nota allora permisero di riconoscere la *luce come fenomeno elettromagnetico*, come [onda elettromagnetica](physics-hs:electromagnetism:em-waves). Alle equazioni di Maxwell, seguì la [verifica sperimentale di Hertz](physics-hs:electromagnetism:em-waves:hertz).

- La [legge di Ampére](physics-hs:electromagnetism:electromagnetism-steady:maxwell:ampere) equazione è valida **solo** in un regime elettrostatico: la forma generale dell'equazione di Ampére prevede un termine dipendente dal tempo, che è identicamente nullo nel regime elettrostatico.

- Senza questo termine, l'equazione non sarebbe consistente con la [conservazione della carica elettrica](physics-hs:electromagnetism:charge-conservation): la correzione di questa inconsistenza da parte di Maxwell è stata l'ultima azione, fondamentale, per ottenere un sistema di equazioni che governano i fenomeni elettromagnetici; la stessa modifica permette anche di riconoscere che i fenomeni EM sono fenomeni ondulatori; il calcolo della misura della velocità di propoagazione delle onde EM, confrontata con le misure disponibili della velocità della luce, permisero di riconoscere la luce come fenomeno EM

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

**todo** *aggiungere immagine sul sistema del condensatore.*



(physics-hs:electromagnetism:electromagnetism-general:maxwell)=
## Equazioni di Maxwell dell'elettromagnetismo

<!--
- le equazioni di Maxwell: le equazioni complete dell'elettromagnetismo
-->

Giunti alla fine del capitolo sui fondamenti dell'elettromagnetismo classico, si è finalmente pronti per elencare la forma generale delle equazioni fondamentali che governano i fenomeni elettromagnetici.

**Principio di conservazione della carica elettrica.** Come già discusso nel [capitolo sulla corrente elettrica](physics-hs:electromagnetism:electric-current), vale il [principio di conservazione della carica elettrica](physics-hs:electromagnetism:charge-conservation): la carica elettrica non si crea, e non si distrugge. La variazione di carica elettrica contenuta in un volume $V$ è quindi uguale al flusso di carica attraverso il suo contorno $\partial V$, come già descritto dall'equazione {eq}`eq:current:charge-equation`,

$$\dot{Q}_V = - \Phi_{\partial V}(\vec{j}) = - i_{\partial V} \ .$$ (eq:principles:charge)

**Equazioni di Maxwell in forma integrale.**

$$\begin{cases}
  \Phi_V(\partial \vec{d}) = Q_{V,f} \\
  \Gamma_{\partial S}(\vec{e}) + \dot{\Phi}_S(\vec{b}) = 0 \\
  \Phi_V(\partial \vec{b}) = 0 \\
  \Gamma_{\partial S}(\vec{h}) - \dot{\Phi}_S(\vec{d}) = \Phi_S(\vec{j}_f)
\end{cases}$$ (eq:principles:maxwell)

**Forza di Lorentz.** La forza agente su una carica elettrica di intensità $q$ in moto in un campo elettromagnetico $\vec{e}(P,t)$, $\vec{b}(P, t)$è descritta dall'espressione {eq}`eq:force:lorentz`

$$\vec{F}_P(t) = q \left[ \vec{e}(P(t), t) - \vec{b}(P(t), t) \times \vec{v}_P(t) \right] \ .$$ (eq:principles:lorentz)

Fare riferimento a:
- [equazioni di Maxwell per l'elettrostatica](physics-hs:electromagnetism:electrostatics:maxwell)
- [equazioni di Maxwell e principi dell'elettromagnetismo classico in regime stazionario](physics-hs:electromagnetism:electromagnetism-steady:maxwell)
- [equazioni di Maxwell e principi dell'elettromagnetismo classico](physics-hs:electromagnetism:electromagnetism-general:maxwell)


