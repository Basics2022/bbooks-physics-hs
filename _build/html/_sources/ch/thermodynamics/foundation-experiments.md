(physics-hs:thermodynamics:foundation:experiments)=
# Esperienze ed esperimenti

## Dilatazione sostanze

## Esperienza di Torricelli 

## Prime esperienze sui gas
Boyle

## Equilibrio termico
...

## Scale di temperatura
- Scale empiriche: costruite con scelte arbitrarie senza nessun significato fisico profondo
- Scala termodinamica: la temperatura assoluta è direttamente legata all'agitazione dei componenti elementari della materia

### Scale empiriche
Metodo generale per la definizione delle scale di temperatura: scelta di due temperature di riferimento, facilmente riproducibili nei limiti di errori tollerati; suddivisione in parti uguali dell'intervallo ed estensione oltre questi limiti, tipicamente in 100 o 60 (o suoi multipli) parti.
- 1702, Romer:
  - estremo inferiore,  $0 \, \text{°Ro}$: temperatura eutettica del cloruro di ammonio;
  - estremo superiore, $60 \, \text{°Ro}$: temperatura di ebollizione dell'acqua
  successivamente si accorse che la solidificazione dell'acqua avveniva circa a $7.5 \, \text{°Ro}$ e decise di usare questa condizione per definire l'estremo inferiore, in modo tale da rendere più facile la taratura dello strumento
- 1709-15, Fahrenheit:
  - definizione originale della scala:
    - estremo inferiore,   $0 \, \text{°F}$: temperatura eutettica del cloruro di ammonio; le malelingue sostengono la temperatura più bassa registrata negli inverni di Danzica, città allora prussiana in cui viveva mentre metteva a punto gli strumenti
    - estremo superiore,   $96 \, \text{°F}$: temperatura media del corpo umano
  - le scelte rocambolesche e definite in maniera imprecisa non costituivano delle condizioni facilmente replicabili per la costruzione e/o taratura di nuovi strumenti. Vennero scelte quindi le condizioni di solidificazione ($32 \, \text{°F}$) e di evaporazione ($212 \, \text{°F}$) dell'acqua a pressione ambiente al livello del mare, in modo tale da suddividere tale intervallo in 180 sotto-intervalli
- 1731, de Réaumur:
  - estremi: solidificazione ($0 \, \text{°Re}$) ed evaporazione ($80 \, \text{°Re}$) dell'acqua a temperatura ambiente. Perché 80 intervalli tra queste due condizioni? Perché il termometro costruito da Reaumur usava come principio fisico l'espansione dell'etanolo, e il volume dell'etanolo varia dell'8% tra le due condizioni di riferimento scelte.
- 1742, Celsius:
  - estremi: solidificazione ($100 \, \text{°C}$) ed evaporazione ($0 \, \text{°C}$) dell'acqua a temperatura ambiente. Perché questa definizione "invertita" rispetto alle altre? Perché no, si potrebbe rispondere. Per rendere più pratica la misura e adeguarsi al verso delle altre scale, un anno dopo la morte di Celsius, la scala fu invertita da Linneo (**todo** lo stesso Linneo, biologo, che si dilettava con la classificazione di piante e animali, padre della classificazione scientifica degli organismi viventi, usata tuttora)

### Scala termodinamica
Scala di temperatura assoluta
- Esperimenti sui gas, estrapolando i dati sperimentali delle [leggi di Charles](physics-hs:thermodynamics:matter:gases:ideal:experiments:charles) e di [Gay-Lussac](physics-hs:thermodynamics:matter:gases:ideal:experiments:gay-lussac)
- 1848, Kelvin *On an Absolute Thermometric Scale*.

## Teoria cinetica dei gas
1738, D.Bernoulli *Hydrodynamica*

## Calore latente e calore specifico
1750-60, J.Black. I suoi studi sul calore aiutano a distinguere i concetti di temperatura e di calore **todo**
- sistemi fisici sul quale non viene compiuto lavoro, scambiano tra di loro calore per raggiungere l'equilibrio termico
  - la quantità di calore "entrante" in un sistema, ne fa variare la temperatura. La variazione di temperatura nel sistema è inversamente proporzionale alla sua massa,

    $$m \, c_x \, d T = \delta Q \ ,$$

    la costante di proporzionalità è definita **calore specifico**. **todo** *controllare commenti su stato termodinamico ${\cdot}_x$ del sistema*

  - la quantità di calore scambiata tra due sistemi è uguale e opposta: $d Q_{ij} = - d Q_{ji}$.
    Mettendo a contatto due sistemi che non manifestano cambiamenti di fase, isolati dall'ambiente, si ottiene quindi

    $$\begin{cases}
      d E_i = m_i \, c_i \, d T_i = \delta Q_{ij} \\
      d E_j = m_j \, c_j \, d T_j = \delta Q_{ji} = - \delta Q_{ij}
    \end{cases}
    $$

    $$\rightarrow \qquad 0 = d E_i + d E_j = m_i \, c_i \, d T_i + m_j \, c_j \, d T_j$$

    **todo** *definire energia interna e aggiungere riferimento alla sezione "Princìpi della termodinamica"*

- i cambiamenti di fase avvengono a temperatura costante. Ad esempio, l'apporto di calore a un sistema in equilibrio contenente ghiaccio alla temperatura di solidificazione non ne fa aumentare la temperatura, ma la massa liquida. L'aumento della temperatura. Una volta completata la trasformazione di fase, l'apporto di calore causa una variazione di temperatura,

    $$\delta Q = \begin{cases}
      d m_{l} \, L_{sl}                 \quad & , \quad {\delta m_l < m} \\
      d m_{l} \, L_{sl} + m \, c \, d T \quad & , \quad {\delta m_l = m} \ .
    \end{cases}$$

    Viene definito **calore latente di fusione** il coefficiente $L_{sl}$ di proporzionalità tra il calore entrante nel sistema durante la trasformazione di fase e la quantità di massa liquefatta $\delta m_l$.

## Esperienze sui gas, ed equazione di stato dei gas perfetti
- Boyle: $PV = \text{const.}$
- Charles: $V \propto T$
- Gay-Lussac: $P \propto T$
- Avogadro: $V \propto n$

L'equazione di stato dei gas perfetti riassume questi risultati

$$\dfrac{P V}{T n} = R = \text{const.}$$


## Lavoro, ... **todo**

```{margin}
**todo**<br> Diatriba sulla priorità sulla formulazione del principio di conservazione dell'energia: von Meyer; Joule; successivamente Hemlholtz; Tyndall - scienziato e uno dei primi alpinisti - uno dei pochi a riconoscere il contributo di von Meyer
```

- Rivoluzione industriale
- 1798, B.Thompson, *An Inquiry Concerning the Source of the Heat Which is Excited by Friction*, oggi può essere interpretato come un lavoro che identificava l'attrito come fenomeno di dissipazione dell'energia meccanica "utile"/"macroscopica" e della sua conversione in calore;
- 1824, S.Carnot, *Riflessioni sulla forza motrice del fuoco* 
- 1840-42, J.von Meyer, medico, chimico e fisico, intuisce il principio di conservazione dell'energia, *"che non può essere né creata né distrutta"* **ref** *Remarks on the Forces of Nature*, 1841
- 1842-45, J.P.Joule *The Mechanical Equivalent of Heat*
- 1850, R.Clausius

## Formalismo e prìncipi della termodinamica classica
**todo**

- usando il formalismo di Gibbs:
  - funzioni di stato (energia interna,...), regola delle fasi, spazio di fase,...
- si possono formulare i prìncipi della termodinamica

## Meccanica statistica
- Maxwell
- Gibbs
- **Boltzmann**


