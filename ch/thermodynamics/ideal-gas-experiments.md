(physics-hs:thermodynamics:matter:gases:ideal:experiments)=
# Esperimenti

**todo** Aggiungere immagini e grafici dei dati sperimentali per le leggi di Charles e Gay-Lussac con estrapolazione verso lo zero assoluto.

## Esperimenti e leggi

(physics-hs:thermodynamics:matter:gases:ideal:experiments:boyle)=
### Legge di Boyle
Per gas semplici, a temperatura sufficientemente elevata, e pressione sufficientemente ridotta

$$T, n \text{ const} \quad \rightarrow \quad P V = \text{const}$$

(physics-hs:thermodynamics:matter:gases:ideal:experiments:charles)=
### Legge di Charles
Per gas semplici, a temperatura sufficientemente elevata, e pressione sufficientemente ridotta

$$P, n \text{ const} \quad \rightarrow \quad \dfrac{\Delta V}{\Delta T} = V_0 \, \alpha_P = \text{const}$$

$$V = V_0 \, ( 1 + \alpha_P \, T ) \ ,$$

avendo indicato con $\alpha_0$ il coefficiente di dilatazione termica a pressione costante.

I dati sperimentali misurati mostrano un andamento lineare, e la loro estrapolazione verso il valore limite del volume $V = 0$ porta a un valore di temperatura $T = -273.15 \text{°C}$.

(physics-hs:thermodynamics:matter:gases:ideal:experiments:gay-lussac)=
### Legge di Gay-Lussac
Per gas semplici, a temperatura sufficientemente elevata, e pressione sufficientemente ridotta

$$V, n \text{ const} \quad \rightarrow \quad \frac{\Delta P}{\Delta T} = P_0 \, k_V = \text{const}$$

$$P = P_0 \, ( 1 + k_V \, T ) \ ,$$

I dati sperimentali misurati mostrano un andamento lineare, e la loro estrapolazione verso il valore limite del volume $P = 0$ porta allo stesso valore di temperatura $T = -273.15 \text{°C}$ trovato nell'esperimento di Charles.

(physics-hs:thermodynamics:matter:gases:ideal:experiments:T-kelvin)=
#### Scala di temperatura assoluta
Questa osservazione porta alla scelta di una nuova scala di temperatura, quella che diverrà la scala di temperatura termodinamica, o assoluta, di Kelvin:
- viene definito il punto a temperatura, $0 \text{ K} = -273.15 \text{°C}$
- viene mantenuta l'ampiezza del grado,

così che la legge di conversione tra il valore numerico della misura di temperatura con la scala Celsius e la scala Kelvin è

$$T[\text{K}] = T[\text{°C}] + 273.15 \ .$$

Usando la scala di temperatura assoluta, le leggi di Charles e di Gay-Lussac possono essere riscritte come **todo** (*evitare singolarità*)

$$\begin{aligned}
  V & \propto T \qquad \text{se $P, n$ const.} \\
  P & \propto T \qquad \text{se $T, n$ const.} \\
\end{aligned}$$

### Legge di Avogadro
Per gas semplici, a temperatura sufficientemente elevata, e pressione sufficientemente ridotta

$$P, T \text{ const} \quad \rightarrow \quad \frac{n}{V} = \text{const}$$

## Legge dei gas ideali
La legge dei gas ideali permette di riassumere le quattro leggi di Boyle, Charles, Gay-Lussac, Avogadro in un'unica equazione di stato,

$$\dfrac{P \, V}{n \, T} = R \ ,$$

avendo introdotto $R \approx 8.314 \frac{\text{J}}{\text{mol} \,\text{K}}$ la **costante universale dei gas**.
