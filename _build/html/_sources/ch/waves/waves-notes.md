(physics-hs:waves:notes)=
# Note

(physics-hs:waves:notes:elementary-sol)=
## Soluzioni particolari

(physics-hs:waves:notes:elementary-sol:free)=
### Moti liberi
#### Vibrazione di una corda con estremi vincolati 

$$
\begin{cases}
  m \ddot{u} - \sigma_0 u'' = 0 \quad x \in [0,L] \\
  u(0,t) = 0 \\
  u(L,t) = 0 \\
\end{cases}
$$

La velocità di propagazione delle perturbazioni è $c = \sqrt{\frac{\sigma_0}{m}}$.

````{dropdown} Onde $\ $ stazionarie - modi propri di vibrare
Si applica il metodo di separazione delle variabili $u(x,t) = f(x) g(t)$,

$$m f \ddot{g} - \sigma_0 f'' g = 0 \ ,$$
$$\frac{m}{\sigma_0}\frac{\ddot{g}}{g} = \frac{f''}{f} = C$$

e scegliendo solo i valori di $c$ che forniscono soluzioni non triviali compatibili con i vincoli, $C = - k^2$. L'equazione per la parte spaziale della soluzione diventa quindi

$$f''(x) + k^2 f(x) = 0 \ .$$

La soluzione generale di questa equazione è

$$f(x) = A \cos (kx) + B \sin (kx) \ ,$$

e l'imposizione delle condizioni al contorno consentono di trovare i valori ammissibili di $A$, $B$ e una condizione su $k$,

$$\begin{cases}
  0 = f(0) = A \\
  0 = f(L) = k B \sin (kL) \\
\end{cases}$$

e quindi per avere soluzioni non banali, deve essere soddisfatta la condizione 

$$\sin(kL) = 0 \ .$$

I valori della costante $k$ ammissibili per ottenere soluzioni non banali sono quindi

$$k_n = n \frac{\pi}{L} \ , \qquad n \in \mathbb{N} \ .$$

Quindi esiste una forma spaziale $f_n(x) = A_n \sin \left( k_n x \right)$ per ogni valore di $n \in \mathbb{N}$. Ad ogni forma $f_n(x)$ è associata una parte temporale $g_n(t)$,

$$g_n(t) = a_n \cos\left( \omega_n t \right) + b_n \sin\left( \omega_n t \right) \ ,$$

con $\omega_n = c \, k_n$.

La forma generale della soluzione del problema può quindi essere scritta come combinazione di onde stazionarie,

$$u(x,t) = \sum_{n} \left[ \alpha_n \cos\left( \omega_n t \right) + \beta_n \sin\left(\omega_n t\right) \right] \sin\left( k_n x \right) \ .$$

con $k_n = n\frac{\pi}{L}$ e $\omega_n = c k_n = n c \frac{\pi}{L}$.

I coefficienti $\alpha_n$, $\beta_n$ vengono calcolati applicando le condizioni iniziali del problema

$$\begin{aligned}
  u_0(x) = u(x,0)       & = \sum_{n} \alpha_n  \sin\left( k_n x \right) \\
  v_0(x) = \dot{u}(x,0) & = \sum_{n} \omega_n \beta_n  \sin\left( k_n x \right) \\
\end{aligned}$$

e quindi risultano essere i coefficienti delle **serie di Fourier** della posizione e della velocità iniziale. Nel caso di configurazione iniziale in quiete, $\dot{u}(x,0) = 0$, i coefficienti $\beta_n$ sono nulli, $\beta_n = 0$.

````
````{dropdown} Onde $\ $ viaggianti

Si usano le proprietà delle funzoni trigonometriche,

$$\begin{aligned}
 \cos(\alpha \mp \beta) & = \cos \alpha \cos \beta \pm \sin \alpha \sin \beta \\
 \sin(\alpha \mp \beta) & = \sin \alpha \cos \beta \mp \cos \alpha \sin \beta \\
\end{aligned}$$

e 

$$\begin{aligned}
 \cos \alpha \sin \beta & = \frac{1}{2} \left( \sin(\alpha+\beta) - \cos(\alpha-\beta) \right) \\
 \sin \alpha \sin \beta & = \frac{1}{2} \left( \cos(\alpha-\beta) - \cos(\alpha+\beta) \right) \\
\end{aligned}$$

La soluzione dell'equazione può quindi essere riscritta come

$$\begin{aligned}
 u(x,t)
 & = \sum_n \left[\frac{\alpha_n}{2}\left( \sin(\omega_n t + k_n x) - \sin(\omega_n t - k_n x)  \right) \right. + \\
 & \qquad + \left.\frac{\beta_n }{2}\left( \cos(\omega_n t - k_n x) - \cos(\omega_n t + k_n x)  \right) \right] = \\ 
 & = \sum_n \left[\frac{\alpha_n}{2}\left( \sin(k_n (c t + x)) - \sin(k_n(c t - x))  \right) \right. + \\
 & \qquad + \left.\frac{\beta_n }{2}\left( \cos(k_n (c t - x)) - \cos(k_n(c t + x))  \right) \right] \ .
\end{aligned}$$

Nel caso di condizione iniziale in quiete, tutti i coefficieti $\beta_n$ sono nulli. La soluzione è uguale a due contributi uguali - e uguali a metà della condizione iniziale - che si muovono in direzione opposta a velocità $\mp c$,

$$\begin{aligned}
  u(x,t) 
  & = \sum_n \frac{\alpha_n}{2} \sin(k_n(x+ct)) + \sum_n \frac{\alpha_n}{2} \sin(k_n(x-ct)) = \\
  & = \frac{1}{2} u_0(x+ct) + \frac{1}{2} u_0(x-ct) \ ,
\end{aligned}$$

avendo riconosciuto il contributo delle due onde viaggianti

$$\begin{aligned}
  \frac{1}{2} u_0(x+ct) & = \sum_n \frac{\alpha_n}{2} \sin(k_n(x+ct)) && \text{(onda viaggiante verso sinistra)} \\
  \frac{1}{2} u_0(x-ct) & = \sum_n \frac{\alpha_n}{2} \sin(k_n(x-ct)) && \text{(onda viaggiante verso destra)}
\end{aligned}$$

````

<!--
<iframe src="../../_static/animations/waves-packet.html" width="800" height="600" frameborder="0"></iframe>
<iframe src="../../_static/animations/waves-mode-1.html" width="800" height="600" frameborder="0"></iframe>
<iframe src="../../_static/animations/waves-mode-2.html" width="800" height="600" frameborder="0"></iframe>

<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <iframe src="../../_static/animations/waves-packet.html" width="100" height="100" frameborder="0"></iframe>
  <iframe src="../../_static/animations/waves-mode-1.html" width="100" height="100" frameborder="0"></iframe>
  <iframe src="../../_static/animations/waves-mode-2.html" width="100" height="100" frameborder="0"></iframe>
</div>
-->

<!-- flex-wrap: wrap; -->
<div style="display: flex; gap: 0; overflow-x: auto; min-width: 2400px;">
  <div style="width: 480px; height: 560px; overflow: hidden;">
    <div style="transform: scale(0.8); transform-origin: top left; width: 700px; height: 700px;">
      <iframe src="../../_static/animations/waves-packet.html" width="800" height="800" frameborder="0" style="border: 0;"></iframe>
    </div>
  </div>
  <div style="width: 480px; height: 560px; overflow: hidden;">
    <div style="transform: scale(0.8); transform-origin: top left; width: 800px; height: 800px;">
      <iframe src="../../_static/animations/waves-mode-1.html" width="800" height="800" frameborder="0" style="border: 0;"></iframe>
    </div>
  </div>
  <div style="width: 480px; height: 560px; overflow: hidden;">
    <div style="transform: scale(0.8); transform-origin: top left; width: 800px; height: 800px;">
      <iframe src="../../_static/animations/waves-mode-2.html" width="800" height="800" frameborder="0" style="border: 0;"></iframe>
    </div>
  </div>
</div>

<!--
<div style="display: flex; gap: 0px;">
  <div style="transform: scale(0.70); transform-origin: top left;">
    <iframe src="../../_static/animations/waves-packet.html" width="800" height="800" frameborder="0"></iframe>
  </div>
  <div style="transform: scale(0.70); transform-origin: top left;">
    <iframe src="../../_static/animations/waves-mode-1.html" width="800" height="800" frameborder="0"></iframe>
  </div>
  <div style="transform: scale(0.70); transform-origin: top left;">
    <iframe src="../../_static/animations/waves-mode-2.html" width="800" height="800" frameborder="0"></iframe>
  </div>
</div>
-->

#### Torsione di una trave con un estremo vincolato e un estremo libero

$$\begin{aligned}
  && I \ddot{u} - GJ u'' = 0 && x \in [0,L] \\
  && u(0,t) = 0 \\
  && GJu'(L,t) = 0 \\
\end{aligned}$$

La velocità di propagazione delle perturbazioni è $c = \sqrt{\frac{GJ}{I}}$.

````{dropdown} Onde $\ $ stazionarie - modi propri di vibrare
Si applica il metodo di separazione delle variabili $u(x,t) = f(x) g(t)$,

$$m f \ddot{g} - \sigma_0 f'' g = 0 \ ,$$
$$\frac{m}{\sigma_0}\frac{\ddot{g}}{g} = \frac{f''}{f} = C$$

e scegliendo solo i valori di $c$ che forniscono soluzioni non triviali compatibili con i vincoli, $C = - k^2$. L'equazione per la parte spaziale della soluzione diventa quindi

$$f''(x) + k^2 f(x) = 0 \ .$$

La soluzione generale di questa equazione è

$$f(x) = A \cos (kx) + B \sin (kx) \ ,$$

e l'imposizione delle condizioni al contorno consentono di trovare i valori ammissibili di $A$, $B$ e una condizione su $k$,

$$\begin{cases}
  0 = f(0) = A \\
  0 = GJf'(L) = GJ k B \cos (kL) \\
\end{cases}$$

e quindi per avere soluzioni non banali, deve essere soddisfatta la condizione 

$$\cos(kL) = 0 \ .$$

I valori della costante $k$ ammissibili per ottenere soluzioni non banali sono quindi

$$k_n = \frac{\pi}{2L} + n \frac{\pi}{L} = \left(\frac{1}{2} + n\right) \frac{\pi}{L} \ , \qquad n \in \mathbb{N} \ .$$

Quindi esiste una forma spaziale $f_n(x) = A_n \sin \left( k_n x \right)$ per ogni valore di $n \in \mathbb{N}$. Ad ogni forma $f_n(x)$ è associata una parte temporale $g_n(t)$,

$$g_n(t) = a_n \cos\left( \omega_n t \right) + b_n \sin\left( \omega_n t \right) \ ,$$

con $\omega_n = c \, k_n$.

La forma generale della soluzione del problema può quindi essere scritta come combinazione di onde stazionarie,

$$u(x,t) = \sum_{n} \left[ \alpha_n \cos\left( \omega_n t \right) + \beta_n \sin\left(\omega_n t\right) \right] \sin\left( k_n x \right) \ .$$

con $k_n = \left(\frac{1}{2}+n\right)\frac{\pi}{L}$ e $\omega_n = c k_n = \left( \frac{1}{2} + n \right) c \frac{\pi}{L}$.

I coefficienti $\alpha_n$, $\beta_n$ vengono calcolati applicando le condizioni iniziali del problema

$$\begin{aligned}
  u_0(x) = u(x,0)       & = \sum_{n} \alpha_n  \sin\left( k_n x \right) \\
  v_0(x) = \dot{u}(x,0) & = \sum_{n} \omega_n \beta_n  \sin\left( k_n x \right) \\
\end{aligned}$$

e quindi risultano essere i coefficienti delle **serie di Fourier** della posizione e della velocità iniziale. Nel caso di configurazione iniziale in quiete, $\dot{u}(x,0) = 0$, i coefficienti $\beta_n$ sono nulli, $\beta_n = 0$.

````

##
