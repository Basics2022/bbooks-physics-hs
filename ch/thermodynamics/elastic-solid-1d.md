(physics-hs:thermodynamics:matter:elastic:1d)=
# Solidi elastici

## Solido elastico lineare 1-dimensionale

**Legge costitutiva lineare con espansione termica.**
Sia data la legge costitutiva elastica che esprime la lunghezza della trave $L$ in funzione dell'azione assiale $f$ e della differenza di temperatura $T-T_0$ rispetto alla temperatura di riferimento $T_0$,

$$L(f,T) - L_0 = \frac{1}{K} f + \alpha L_0 (T-T_0) \ ,$$

assumendo che la costante elastica isoterma $K$, e il coefficiente di dilatazione termica a carico costante $\alpha$ siano costanti, parametri caratteristici del materiale e della configurazione di riferimento. Sotto queste ipotesi, è possibile invertire la relazione per scrivere l'azione assiale in funzione dell'allungamento e della temperatura,

$$f(\Delta L, \, \Delta T) = K \Delta L - \alpha \, L_0 \, K \, \Delta T \ .$$

**Potenziali termodinamici.**

$$dE = T dS + f dL  \qquad , \qquad \text{energia interna} $$
$$dH = T dS - L df  \qquad , \qquad \text{entalpia, $H = E - f \, L$} $$ 
$$dF =-S dT + f dL  \qquad , \qquad \text{Helmholtz, $F = E + T \, S$} $$ 
$$dG =-S dT - L df  \qquad , \qquad \text{Gibbs, $G = H + T \, S$} $$ 

**Energia libera di Helmholtz.**

$$d E = \delta Q^{ext} - \delta L^{int} = T \, dS + f \, dL$$

La variazione dell'energia libera di Helmholtz, $F := E - TS$,

$$dF = d E - T \, dS - S \, dT = f \, dL - S \, dT \ ,$$

permette di riconoscere l'azione assiale e l'entropia come le derivate parziali di $F$,

$$
f = \left(\frac{\partial F}{\partial L} \right)_T
\qquad , \qquad
S = - \left(\frac{\partial F}{\partial T} \right)_L
$$

Integrando la relazione dell'azione assiale, si ottiene

$$F(\Delta L, \Delta T) = \dfrac{1}{2} \, K \, \Delta L^2 - \alpha \, L_0 \, K \, \Delta T \, \Delta L + F_0(T) \ ,$$

avendo introdotto la funzione $F_0(T)$, dipendente al massimo dalla temperatura $T$, come risultato dell'integrazione in $L$.
Dall'espressione dell'energia libera di Helmholtz si può poi ricavare l'espressione dell'entropia

$$
S(\Delta L, \Delta T) = - \left(\frac{\partial F}{\partial T} \right)_L = \alpha \, L_0 \, K \, \Delta L - F_0'(T) \ .
$$

**Calori specifici.**
Il calore specifico a lunghezza costante viene calcolato direttamente usando l'espressione dell'entropia,

$$C_L = T \left(\frac{\partial S}{\partial T} \right)_L = - T \, F_0''(T) \ .$$

Assumendo che il calore specifico $C_L$ sia costante, l'integrazione ci fornisce un'espressione della funzione $F_0'(T)$,

$$F_0'(T) - F_0'(T_0) = - C_L \ln \left( \dfrac{T}{T_0} \right) \ ,$$

che consente di esprimere l'entropia in fuznione del calore specifico,

$$S(\Delta L, \, \Delta T) = \alpha \, L_0 \, K \, \Delta L + C_L \ln \left( 1 + \dfrac {\Delta T}{T_0} \right) + S_0$$

Usando la legge costitutiva per esprimere l'allungamento in funzione dell'azione assiale e dell'incremento di temperatura,

$$S(f, \, \Delta T) = \alpha \, L_0 \, K \, \left( \dfrac{1}{K} \, f + \alpha \, L_0 \, \Delta T \right) + C_L \ln \left( 1 + \dfrac {\Delta T}{T_0} \right) + S_0 \ ,$$

è possibile calcolare il calore specifico a carico costante,

$$\begin{aligned}
C_f & = T \left(\frac{\partial S}{\partial T} \right)_f = \\
    & = T \, \left[ K \, ( \alpha \, L_0 )^2 + \frac{C_L}{T}\right] \\
    & = T K \, ( \alpha \, L_0 )^2 + C_L \ .
\end{aligned}$$



**Coefficienti termodinamici: costanti elastiche, coefficiente di dilatazione.**
Dall'espressione della legge costitutiva, si definiscono la costante elastica isoterma

$$\frac{1}{K} := \left(\frac{\partial L}{\partial f}\right)_T \ ,$$

e il coefficiente di dilatazione termica a carico costante

$$\alpha_f := \frac{1}{L_0} \left(\frac{\partial L}{\partial T}\right)_f \ .$$

La costante elastica adiabatica,

$$\frac{1}{K_{ad}} := \left(\frac{\partial L}{\partial f}\right)_S \ ,$$

può essere calcolata derivando la funzione che esprime la lunghezza $L$ in funzione delle variabili indipendente $f$, $S$ che si può ricavare sostituendo il legame $\Delta T(\Delta L, \, F)$ della relazione costitutiva nell'espressione dell'entropia, per ottenere

$$S = \alpha \, L_0 \, K \, \Delta L + C_L \ln \left( 1 + \frac{1}{T_0} \frac{1}{\alpha \, L_0 \, K} \left( K \, \Delta L - f \right) \right) + S_0$$

la cui derivata $\frac{\partial}{\partial f}\big|_S$ vale

$$0 = \alpha \, L_0 \, K \left(\frac{\partial L}{\partial f}\right)_S + C_L \dfrac{1}{1 + \frac{K \, \Delta L - f}{\alpha \, T_0 \, L_0 \, K}}\frac{1}{\alpha \, L_0 \, K \, T_0} \left( K \left(\frac{\partial L}{\partial f}\right)_S - 1\right) \ .$$

Introducendo la definizione della costante elastica in condizioni adiabatiche, $K_{ad}(T; K, \alpha)$, 

$$\dfrac{K}{K_{ad}} \left[ \frac{(\alpha \, L_0)^2 \, T \, K }{C_L} + 1 \right] = 1$$

si trova la relazione tra le costanti elastiche isoterma e adiabatica,

$$\begin{aligned}
  K_{ad} & = K \left( 1 + \frac{(\alpha \, L_0)^2 \, T \, K }{C_L} \right)     
           = K \frac{1}{1 - \dfrac{(\alpha \, L_0)^2 \, K \, T }{C_f}} \ . 
\end{aligned}$$

**Energia interna.**
L'energia interna del sistema può essere ricavata da $E = F + T \, S$,

$$\begin{aligned}
  E & = \dfrac{1}{2} \, K \, \Delta L^2 - \alpha \, L_0 \, K \, \Delta T \, \Delta L + F_0(T) + T \left( \alpha \, L_0 \, K \, \Delta L + C_L \ln \left( 1 + \dfrac{\Delta T}{T_0} \right) + S_0 \right) = \\
    & = \frac{1}{2} \, K \, \Delta L^2 + F_0(T) + T \, C_L \, \ln \left( 1 + \dfrac{\Delta T}{T_0} \right) + T \, S_0 \ .
\end{aligned}$$

E' quindi possibile riconoscere $E_0 := E(\Delta L = 0, \Delta T = 0) = F_0(T_0) + T_0 \, S_0$.
La variazione di quest'ultima relazione nei confronti delle variabili $\Delta L$, $\Delta T$,

$$\begin{aligned}
  d E & = K \Delta L \, d L + \underbrace{F_0'(T)}_{- C_L \ln \left(\frac{T}{T_0}\right) - S_0} dT + C_L \, d T \left[ \ln \left(\frac{T}{T_0}\right) + 1 \right] + S_0 \, d T = \\
      & = K \Delta L \, d L + C_L \, d T
\end{aligned}$$

può essere espressa in funzione degli incrementi $d L$, $d S$, grazie all'incremento della relazione che lega le tre variabili $S, L, T$,

$$d S = \alpha \, L_0 \, K \, d L + \frac{C_L}{T} \, dT \ ,$$

in

$$\begin{aligned}
  d E & = K \Delta L \, d L + C_L \, dT = \\
      & = K \Delta L \, d L + \, T \, ( dS - \alpha \, L_0 \, K \, dL ) = \\
      & = ( K \Delta L - K \, \alpha \, L_0 \, T ) \, d L + \, T \, dS  \ .
\end{aligned}$$

**todo**
<span style="color:red">Controllare! Non torna l'espressione della forza: c'è solo la temperatura, ma ci dovrebbe essere la differenza di temperatura rispetto a quella di riferimento?</span>
