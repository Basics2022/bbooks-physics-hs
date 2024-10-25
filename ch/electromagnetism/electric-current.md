(physics-hs:electromagnetism:electric-current)=
# Corrente elettrica

- corrente elettrica:
  - descrizione microscopica: materiale elettricamente neutro, con $e^-$ liberi di conduzione
  - def come flusso di carica: dalla descrizione micro alla descrizione macroscopica, media, ("fenomenologica"?)

Localmente, è possibile definire una **densità "macroscopica" di corrente elettrica** come la media pesata delle velocità delle cariche, $\vec{v}$.

**todo**. **Obs - corrente elettrica nei solidi**: è possibile avere corrente elettrica anche in materiali elettricamente neutri, anche localmente. Ad esempio, nell'ipotesi di avere due sostanze diverse con carica $\rho^+$, $\rho^-$ e velocità media delle due sostanze $\vec{v}^+$, $\vec{v}^-$, la corrente densità di corrente elettrica è

$$\vec{j} = \rho \vec{v} = \rho^+ \vec{v}^+ + \rho^- \vec{v}^- \ . $$

Nel caso in cui il materiale sia neutro, la densità di carica elettrica è nulla, $0 = \rho = \rho^+ + \rho^- =$ e quindi $\rho^+ = - \rho^-$ e la densità di corrente elettrica può essere scritta come $\vec{j} = \rho^- (\vec{v}^- - \vec{v}^+)$. Assumendo che le cariche elettriche positive siano ferme rispetto all'osservatore $\vec{v}^+ = \vec{0}$, la densità di corrente elettrica diventa $\vec{j} = \rho^- \vec{v}^-$.

La **corrente elettrica** attraverso una superficie $S$ viene definita come il flusso di carica elettrica attraverso la superficie $S$,

$$i = I_{S} = \Phi_{S}(\vec{j}) \ .$$

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

**Legge di Ohm** in forma locale: 

$$
\vec{j}(P) = \sigma(P) \, \vec{e}(P)
\qquad \ , \qquad
\vec{e}(P) = \rho_R(P) \, \vec{j}(P)
$$

**Prima legge di Ohm** <span style="color:red"> "per cavi" </span> **todo** *trovare titolo decente*

$$d V = i \, d R$$

**Seconda legge di Ohm** <span style="color:red"> "per cavi" </span> **todo** *trovare titolo decente*

$$d R = \dfrac{\rho_R}{A} \, d \ell$$

### gas
### vuoto?
### semiconduttori
 cenni all'elettronica: diodi, transistor, ...


## Circuiti elettrici
- dalle leggi fisiche alle leggi di Kirchhoff, ipotesi (validità e non-validità dell'approccio circuitale)
- componenti:
  - resistenze
  - condensatori
  - generatori
- regimi di funzionamento in DC, (trascurando gli effetti EM: no campi magnetici esterni, *ogni circuito è una spira*...):
  - stazionario
    - bilancio di energia: "generatori" di energia elettrica, "perdite" nelle resistenze
      - approfondimenti:
        - pile <span style="color:red"> Collegamento ad altre parti: termodinamica? chimica?</span>
  - transitorio:
    - esempio: carica/scarica condensatore
