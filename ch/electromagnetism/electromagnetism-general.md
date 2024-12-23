(physics-hs:electromagnetism:electromagnetism-general)=
# Induzione ed elettromagnetismo

(physics-hs:electromagnetism:electromagnetism-general:em-induction)=
## Legge di Faraday per l'induzione elettromagnetica

- legge di Faraday: corrente indotta

- corrente alternata:
  - principi e applicazioni:
    - trasformatori
    - generatori e motori elettrici
    - generazione/trasporto/trasformazione/consumo

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

**todo** *aggiungere immagine sul sistema del condensatore.*

$$\Gamma_{\partial S}(\vec{h}) - \dot{\Phi}_{S}(\vec{d}) = i_S $$
(physics-hs:electromagnetism:electromagnetism-general:maxwell)=
## Equazioni di Maxwell dell'elettromagnetismo

- le equazioni di Maxwell: le equazioni complete dell'elettromagnetismo

Fare riferimento a:
- [equazioni di Maxwell per l'elettrostatica](physics-hs:electromagnetism:electrostatics:maxwell)
- [equazioni di Maxwell e principi dell'elettromagnetismo classico in regime stazionario](physics-hs:electromagnetism:electromagnetism-steady:maxwell)
- [equazioni di Maxwell e principi dell'elettromagnetismo classico](physics-hs:electromagnetism:electromagnetism-general:maxwell)


