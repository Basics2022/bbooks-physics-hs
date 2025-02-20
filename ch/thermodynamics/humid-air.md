(physics-hs:thermodynamics:matter:humid-air)=
# Aria umida

## Definizioni
L'**aria atmosferica** può essere pensata come una miscela di aria secca (a sua volta miscela di gas N$_2$ al 78%, O$_2$ al 21%, Ar circa all'1%, e altre tracce di gas) i cui rapporti rimangono inalterati in intervalli ragionevoli di condizioni termodinamiche) e di vapore acqueo, acqua allo stato di vapore.

Viene definita **pressione parziale**, $p_i$, dovuta a un componente $i$ di una miscela, la pressione che ci sarebbe nel sistema se ci fosse solo il componente scelto nell'intero volume del sistema. La **legge di Dalton** sulle pressioni parziali afferma che la pressione in una miscela di gas è la somma delle pressioni parziali dei suoi componenti,

$$p = \sum_i p_i$$

Le quantità estensive possono essere scritte come somma delle quantità riferite a ogni singolo componente (nell'**ipotesi** che non ci siano interazioni? Ad esempio, l'energia della miscela di 2 componenti è uguale alla somma dei contributi di energia associati ai singoli componenti)

$$E = \sum_i E_i \quad , \quad H = \sum_i H_i \quad , \quad \dots$$

## Aria secca e vapore acqueo
Nell'ipotesi che i componenti in fase gassosa possano essere modellati con la legge dei gas ideali.

La massa molare media dell'**aria secca** $M_m^{a.s.}$ e la costante specifica del gas $R^{a.s.}$ sono

$$\begin{aligned}
M_m^{a.s.}
  & = 0.78 \, M_{m, N_2} + 0.21 \, M_{m, O_2} + 0.01 \, M_{m, Ar} = \\ 
  & = 0.78 \cdot 28 \frac{kg}{kmol} + 0.21 \cdot 32 \frac{kg}{kmol} + 0.01 \cdot 40 \frac{kg}{kmol} = 28.96 \frac{kg}{kmol}
\end{aligned}$$

$$R^{a.s.} = \frac{R}{M_m^{a.s.}} = \frac{8314 \frac{J \, kmol}{K}}{ 28.96 \frac{kg}{kmol} } = 287.1 \frac{J}{kg \, K}$$

La massa molare media del **vapore acqueo** $M_m^{v}$ e la costante specifica del gas $R^{v}$ sono

$$\begin{aligned}
M_m^{v} = M_{m, H_2 O} = 2 \cdot 1 \frac{kg}{kmol} + 16 \frac{kg}{kmol} = 18 \frac{kg}{kmol}
\end{aligned}$$

$$R^{v} = \frac{R}{M_m^{v}} = \frac{8314 \frac{J \, kmol}{K}}{ 18 \frac{kg}{kmol} } = 461.9 \frac{J}{kg \, K}$$

## Regola delle fasi di Gibbs
La regola delle fasi di Gibbs prevede che un sistema con $C=2$ componenti indipendenti, aria secca e vapore acqueo, e $P$ fasiè determinato dal valore di

$$F = C - P + 2 = 4 - P $$

variabili intensive. Nel caso ci sia una fase sola, $P=1$, il sistema è determinato da $F = 3$ variabili intensive indipendenti, come ad esempio pressione, temperatura e composizione; nel caso coesistano $P=2$ fasi, il sistema è determinato da $F = 2$ variabili intensive indipendenti, poiché si aggiunge un vincolo tra pressione e temperatura in condizioni di equilibrio di più fasi, che può essere scritto come uguaglianza tra i potenziali chimici del componente nelle due fasi,

$$\mu_{l}(P,T) = \mu_{v}(P,T) \ .$$

## Misure di umidità
### Umidità specifica o titolo, $x$

Rapporto tra frazione di vapore acqueo e aria secca nello stesso volume di aria umida,

$$x = \frac{m_v}{m_a}$$

Assumendo che la fase gassosa si comporti come miscela di gas ideali, si può scrivere

$$x = \frac{m_v}{m_a} = \frac{\rho_v}{\rho_a} = \frac{R_a \, T}{p_a} \frac{p_v}{R_v \, T} = \frac{287.1}{461.9} \frac{p_v}{p_a} = 0.622 \, \frac{p_v}{p_a} = 0.622 \, \frac{p_v}{p - p_v} \ ,$$

ricordando che $p = p_v + p_a$

### Umidità relativa
L'umidità relativa è il rapporto tra la massa di vapore $m_v$ contenuta nell'aria umida rispetto alla massa di vapore $m_{v,sat}$ che sarebbe contenuta nel sistema nella condizionie di saturazione alla stessa temperatura,

$$\varphi = \frac{m_v}{m_{v,sat}}$$

$$\varphi = \frac{m_v}{m_{v,sat}} = \frac{\rho_v}{\rho_{v,sat}} = \frac{R_v \, T}{p_{v,sat}} \frac{p_v}{R_v \, T} = \frac{p_v}{p_{v,sat}} \ ,$$

e quindi 

$$x = 0.622 \, \frac{p_v}{p - p_v} = 0.622 \, \frac{ \varphi p_{v,sat} }{p - \varphi p_{v,sat}}$$

## Entalpia dell'aria umida
Nell'ipotesi che l'aria umida si comporti come miscela ideale, la sua entalpia è la somma dell'entalpia di aria secca e vapore acqueo,

$$H = \sum_i H_i
  = H_{as} + H_v = m_{as} h_{as} + m_v h_v
  = m_{as} \left( h_{as} + \frac{m_v}{m_{as}} h_v \right)
  = m_{as} \left( h_{as} + x \, h_v \right)
$$

Nell'ipotesi di gas ideale biatomico (come N$_2$ e O$_2$ di cui è composta al 99%), l'entalpia specifica dell'aria secca è proporzionale alla temperatura,

$$h_a = c_{p,a} T \ ,$$

con $c_{p,a} = \frac{7}{2} R^{a.s.} = \frac{7}{2} \, 287.1 \frac{J}{kg \, K} = 1005 \frac{J}{kg \, K}$.

L'entalpia del vapore temperatura $T$ è l'energia necessaria a pressione $P$ costante a vaporizzare un kg di acqua satura alla temperatura di $T_{l,sat}(P)$ e del calore necessario a portare il valore alla temperatura $T$

$$H_v = m_v \, \left( r(P) + c_{p,v} \, (T-T_{l,sat}(P) \right) \ , $$

essendo $r$ il calore latente di vaporizzazione alla pressione $P$, e $c_{p,v}$ il calore specifico a pressione costante del vapore d'acqua.

Ad esempio, a $T = 0°C$, il calore latente di fusione e il calore specifico a pressione costante valgono $r(T = 0°C) = 2501 \, \frac{kJ}{kg}$ e $c_{p,v} = 1875 \frac{J}{kg \, K}$ a $T = 0°C$.

**todo** *controllare! Errore? Esistono tabelle con valori tabulati che descrivono il comportamento non-ideale?* Nel caso il vapore d'acqua si comportasse come un gas ideale con una molecola tri-atomica con atomi non allineati, con $f = 6$ gradi di libertà rigidi che contribuiscono all'energia interna, si avrebbe $c_{v,v} = 3 R^{v}$, $c_{p,v} = 4 R^{v} = 4 \cdot 461.9 \frac{J}{kg \, K} = 1847.6 \frac{J}{kg \, K}$.


## Tabelle 
- delle condizioni di saturazione, T, p, $\rho$, h, s, in condizioni di liquido o vapore saturo
- del vapore surriscaldato
- del liquido sottoraffreddato

## Diagrammi
- diagramma di Mollier, o psicrometrico: assi $x$, $h$, solitamente costruito alla pressione $P_0 = 1 \, atm$
- diagramma ASHRAE: assi $T$ di bulbo secco, $x$

## Temperature e misure di umidità
- Temperatura di bulbo secco
- Temperatura di rugiada: temperatura di saturazione, attraverso un processo di raffreddamento a $p$ e $x$ costanti
- Temperatura di bulbo bagnato: temperatura alla quale si porta l'acqua in condizioni di scambio di calore convettivo forzato (? $v \in [3, 40] \, m/s$) con l'aria; l'aria lambisce la garza, l'acqua tende a evaporare assorbendo calore (dall'aria?); all'equilibrio, l'acqua è a $T_{H_2} < T_{a}$
- Temperatura di saturazione adiabatica: coincide con la temperatura di bulbo bagnato?

## Trasformazioni dell'aria umida
- Miscelamento adiabatico di due portate di aria umida
  - Sistema aperto in regime stazionario, senza lavoro o calore apportato al sistema; bilanci di:
    - massa a.s.
    - massa v
    - energia (flussi di entaplia)
- Riscaldamento sensibile di una portata di aria umida
- Raffreddamento sensibile di una portata di aria umida
  - Sistema aperto in regime stazionario, con scambi di calore
    - bilancio massa è banale
    - bilancio energia $\dot{Q} = \dot{m} \Delta h$
- Raffreddamento con deumidificazione
  - Sistema aperto in regime stazionario, con scambi di calore; $\dot{m}_L$ di solito trascurabile
    - bilancio di massa, e approssimazioni $0 = \dot{m}_1 + \dot{m}_L - \dot{m}_2$, $\dot{m}_1 \sim \dot{m}_2$
    - bilancio di energia $Q_{12} = \dot{m}(h_2 - h_1) + \dot{m}_l h_l$
- Umidificazione dell'aria per iniezione di acqua
  - Sistema aperto in regime stazionario, con scambi di calore
    - approssimazione della massa di aria secca $\sim$ massa aria umida: $m_{i} = m_{i,a} + m_{i,v} \sim m_{i,a}$
    - massa volume: $\dot{m}_{v,1} + \dot{m}_v = \dot{m}_{v,2}$
    - massa aria: $\dot{m}_{a,1} = \dot{m}_{a,2}$
    - bilancio di energia: $\dot{m}_{1} h_1 + \dot{m}_v h_v = \dot{m}_2 h_2$

(physics-hs:thermodynamics:matter:humid-air:vapor-pressure)=
## Tensione di vapore
Esempi:
- cuocere la pasta in montagna: pressione minore, temperatura di ebollizione minore
- evaporazione di una pozzanghera: l'acqua della pozzanghera evapora anche se la temperatura dell'ambiente è inferiore alla temperatura di ebollizione dell'acqua

## Esercizi
- Evaporazione di una pozzanghera; evapo-traspirazione: metodi di Penman-Monteith,...
- Applicazioni di condizionamento


