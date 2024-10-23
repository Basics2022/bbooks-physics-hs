(physics-hs:thermodynamics:matter:gases:ideal:expressions)=
# Espressioni diverse dell'equazione di stato dei gas perfetti

Formule alternative dell'equazione di stato dei gas perfetti

- $n$ numero di moli, $R$ costante universale dei gas
  
  $$P \, V = n \, R \, T$$

- il numero di moli $n$ può essere scritto come rapporto della massa $m$ del sistema e la massa molare $M_m$ del gas considerato,

  $$m = M_m \, n$$

  Usando questa espressione per sostituire $n$ nella legge dei gas perfetti, e dividendo per $V$ si può trovare una nuova espressione dell'equazione di stato di un gas perfetto,

  $$\begin{aligned}
    P   = \dfrac{m}{V} \, \dfrac{R}{M_m} \, T     
        = \rho \, R_g \, T \ ,
  \end{aligned}$$

  avendo riconosciuto la densità come rapporto tra massa e volume del sistema $\rho = \frac{m}{V}$ e definito la costante    del gas specifica per il gas considerato come rapporto della costante universale e la massa molare, $R_g = \frac{R}{M_m}$

- la relazione di Avogadro lega il numero di moli $n$ e il numero di molecole $N$ (**todo** *può essere solo una comoda unità di conto? Da dove arriva?...),

  $$N = N_A \, n \ ,$$

  essendo $N_A \approx 6.022 \cdot 10^{23} \text{mol}^-1$ il **numero di Avogadro**. La legge di stato dei gas perfetti può quindi essere riscritta come

  $$P \, V = N \, \frac{R}{N_A} \, T = N \, k_B \, T \ , $$

  dove è stata introdotta la costante di Boltzmann, $k_B = \frac{R}{N_A} \approx 1.38 \cdot 10^{-23} \frac{\text{J}}{\text{K}}$.

  La costante di Boltzmann (**todo** *introdotta da Planck e da lui dedicata a Boltzmann*) è il fattore di conversione tra l'energia dovuta all'agitazione termica del sistema e la sua temperatura, come mostrato nella sezione dedicata alla [teoria cinetica dei gas](physics-hs:thermodynamics:matter:gases:ideal:kinetic-theory).


