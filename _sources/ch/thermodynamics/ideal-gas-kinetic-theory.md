(physics-hs:thermodynamics:matter:gases:ideal:kinetic-theory)=
# Teoria cinetica dei gas

Nel 1738, Daniel Bernoulli pubblica il *Hydrodynamica* nel quale fornisce un primo modello microscopico di un gas, pensato come un insieme di un numero enorme **todo** di particelle elementari (molecole), e il legame tra le grandezze macroscopiche e la media delle grandezze microscopiche.

Considerando: **todo**
- un volume retto di lati $\Delta L_x$, $\Delta L_y$, $\Delta L_z$, $\Delta V = \Delta L_x \, \Delta L_y \, \Delta L_z$
- che contiene un numero $\Delta N$ di particelle identiche che non interagiscono tra di loro ma solo con urti elastici con le pareti rigide del volume

La forza sulla parete del volume con normale in direzione $x$, può essere calcolata come rapporto tra l'impulso esercitato dalla parete e l'intervallo di tempo tra 2 urti della stessa molecola con la stessa parete,

$$\Delta F_{x,i} = -\frac{\Delta I_{x,i}}{\Delta t_i} = \frac{2 m_m v_{x,i}}{\frac{2 \Delta L_x}{v_{x,i}}} = m_m \frac{v_{x,i}^2}{\Delta L_x}$$

La forza media per unità di superficie sulla parete è

$$\frac{\Delta F_{x,i}}{\Delta S_x} = \frac{\Delta F_{x,i}}{\Delta L_y \Delta L_z} = \dfrac{m_m v_{x_i}^2}{\Delta L_x \, \Delta L_y \, \Delta L_z} = \dfrac{m_m v_{x_i}^2}{\Delta V}$$

L'energia cinetica della $i$-esima particella è

$$
K_i = \frac{1}{2} m_m |\vec{v}_i|^2 = 
\frac{1}{2} m_m \left( v_{x,i}^2 + v_{y,i}^2 + v_{z,i}^2  \right) = 
$$

L'energia dell'insieme delle particelle contenute nel volume è uguale alla somma delle loro energie cinetiche

$$K = \sum_i K_i = \sum_i \frac{1}{2} m_m \left( v_{x,i}^2 + v_{y,i}^2 + v_{z,i}^2 \right) \ .$$

Assumendo che la velocità delle particelle abbia una distribuzione isotropa nello spazio, ossia che non ci siano direzioni preferenziali, la media dei quadrati delle singole componenti cartesiane è uguale

$$\langle \Delta K \rangle = \langle K_1 \rangle \, \Delta N = \Delta N \frac{3}{2} m_m v_{rms}^2 \ .$$

**todo** L'energia cinetica può essere scritta in funzione della temperatura, $T$,

$$\frac{\langle \Delta K \rangle}{\Delta N} = \dfrac{3}{2} m_m v^2_{rms} = \frac{3}{2} k_B \, T \ ,$$

questa espressione prevede che l'energia cinetica di una molecola sia direttamente proporizonale alla temperatura e al numero di gradi di libertà della particella, qui $f = 3$, tramite la costante di proporzionalità $k_B = \dots$, la **costante di Boltzmann**.

La forza media esercitata dalle $\Delta N$ molecole sulla superficie con normale $x$ può essere quindi scritta come

La **costante di Avogadro** (**todo** da dove arriva? Esperimenti sui gas a pari volume e condizioni TD, fatti da?? Gay-Lussac?? Charles?? Controllare video di Bressanini e altre fonti) permette di convertire il numero di molecole $N$ nel numero di moli $n$, $\Delta N = N_A \, \Delta n$, e calcolare la massa di una mole, la massa molare, una volta nota la massa di una molecola $M_m = N_A m_m$

$$P 
  & = \dfrac{\Delta N}{\Delta V} m_m \, v_{rms}^2 = \\  
  & = \dfrac{\Delta N}{\Delta V} k_B \, T
    = \dfrac{\Delta n}{\Delta V} \underbrace{N_A k_B}_{= R_u} \, T \\
  & = \dfrac{m_m \Delta N}{\Delta V} \dfrac{k_B}{m_m} \, T
    = \dfrac{\Delta m }{\Delta V} \dfrac{k_B}{m_m} \, T  
    = \dfrac{\Delta m }{\Delta V} \underbrace{\dfrac{N_A \, k_B}{M_m}}_{=\frac{R_u}{M_m} = R} \, T   \ , $$

avendo introdotto la definizione della **costante universale** $R_u = N_A \, k_B$ come prodotto del numero di Avogadro e la costante di Boltzmann, e una costante del gas considerato come rapporto tra la costante universale e la sua massa molare, $R = \dfrac{R_u}{M_m}$.

<span style="color:red">Valori numerici; cenni storici</span>



