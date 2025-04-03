(physics-hs:modern:quantum:basics)=
# Introduzione alla meccanica quantistica

(physics-hs:modern:quantum:basics:probability)=
## Interpretazione probabilistica

Interpretazione probabilistica di alcuni esperimenti:
- doppia fenditura
- intensità delle righe degli spettri di emissione

(physics-hs:modern:quantum:basics:measurements)=
## Misura
- interazione sistema-strumento
- lo strumento è tipicamente un sistema macroscopico che funziona nel regime ben descritto dalla fisica classica
- ...


(physics-hs:modern:quantum:basics:uncertainty)=
## Indeterminazione di Heisenberg
Non è possibile conoscere contemporaneamete il valore di alcune coppie di grandezze fisiche, dette complementari o coniugate. Alcuni esempi sono:
- stessa componente di posizione e quantità di moto
  
    $$\sigma_{x_i} \sigma_{p_i} \ge \frac{\hbar}{2}$$

- diverse componenti del momento della quantità di moto (sia momento totale, sia orbitale, sia di spin)
- ...

(physics-hs:modern:quantum:basics:spin)=
## Spin, esperimento di Stern-Gerlach
Le particelle subatomiche manifestano due tipi di momento angolare:
- il momento angolare orbitale, $\hat{\mathbf{L}}$
- momento angolare intrinseco, di **spin**, $\hat{\mathbf{S}}$

Il momento angolare totale è la somma di questi due contributi, $\hat{\mathbf{J}} = \hat{\mathbf{L}} + \hat{\mathbf{S}}$


## Alcuni esempi 1-dimensionali
### Moto libero di un sistema puntiforme
Moto libero, incertezza tra posizione e quantità di moto porta a "diffusione della probabilità"

### Barriera e buca di potenziale
Contronto e differenze con meccanica classica:
- collisione con una parete - barriera di potenziale
- moto libero in una scatola - buca di potenziale

Effetti:
- effetto tunnel

Buca di potenziale, sistema finito:
- valori di energia discreti

Barriera di potenziale, dominio infinito:
- valori di energia continui
- ...

### Oscillatore armonico
- valore di energia discreti

## Atomo di Idrogeno, $H$

## Sistemi di elementi identici
- In meccanica quantistica, non è possibile distinguere elementi identici in sistemi che contengono più elementi
- Stato di un sistema

   $$\Psi(\mathbf{q}_1, \mathbf{q}_2, \dots \mathbf{q}_n) \ ,$$

   è indistinguibile con uno scambio di due elementi identici. Quindi in seguito a uno scambio di argomenti della funzione d'onda, la funzione d'onda non cambia a meno di un cambio di fase (in principio arbitrario, e ininfluente sulla fisica del problema),

   $$\Psi(\mathbf{q}_1, \dots, \mathbf{q}_a, \dots, \mathbf{q}_b, \dots, \mathbf{q}_n) = e^{j \alpha} \Psi(\mathbf{q}_1, \dots, \mathbf{q}_b, \dots, \mathbf{q}_a, \dots, \mathbf{q}_n) \ .$$

   Un secondo scambio degli stessi argomenti comporta che 
   
   $$\Psi(\mathbf{q}_1, \dots, \mathbf{q}_a, \dots, \mathbf{q}_b, \dots, \mathbf{q}_n) = e^{j 2 \alpha} \Psi(\mathbf{q}_1, \dots, \mathbf{q}_a, \dots, \mathbf{q}_b, \dots, \mathbf{q}_n) \ .$$

   Questa relazione è soddisfatta per qualsiasi valore della funzione d'onda nel caso in cui $e^{j 2 \alpha} = 1$, e quindi $e^{i \alpha} = \pm 1$.

   La funziona d'onda che rappresenta lo stato di un sistema composto da più elementi identici deve quindi essere o simmetrica o anti-simmetrica rispetto a uno scambio di indici:
   - funzione d'onda simmetrica, i **bosoni**

     $$\Psi(\mathbf{q}_1, \dots, \mathbf{q}_a, \dots, \mathbf{q}_b, \dots, \mathbf{q}_n) = \Psi(\mathbf{q}_1, \dots, \mathbf{q}_b, \dots, \mathbf{q}_a, \dots, \mathbf{q}_n) \ .$$

   - funzione d'onda anti-simmetrica, i **fermioni**

     $$\Psi(\mathbf{q}_1, \dots, \mathbf{q}_a, \dots, \mathbf{q}_b, \dots, \mathbf{q}_n) = - \Psi(\mathbf{q}_1, \dots, \mathbf{q}_b, \dots, \mathbf{q}_a, \dots, \mathbf{q}_n) \ .$$

```{prf:definition} Principio di esclusione di Pauli - per fermioni
:label: pauli-principle

**Principio di esclusione di Pauli** Due fermoni della stessa natura non possono trovarsi nello stesso stato. La relazione di anti-simmetria della funzione d'onda per i fermioni corrisponde a una generalizzazione della condizione 

$$f(x,y) = - f(y,x) \ .$$

In questo caso, se i due argomenti della funzione assumono lo stesso valore (analogia con due fermioni che si trovano nello stesso stato) allora segue che

$$f(x,x) = - f(x,x) \ ,$$

relazione che implica $f(x,x) = 0$. Poiché il modulo quadro di $\Psi$ rappresenta la densità di probabilità di uno stato del sistema, se $\Psi(\mathbf{q}_i) = 0$, allora

$$p(\dots, \mathbf{q}_i, \dots, \mathbf{q}_i, \dots) = |\Psi(\dots, \mathbf{q}_i, \dots, \mathbf{q}_i, \dots)|^2 = 0 \ ,$$

e quindi **la probabilità che due fermioni si trovino nello stesso stato è nulla**.

```

**todo** La natura dei fermioni è legata allo [spin]() frazionario

```{prf:example} Gli elettroni sono fermioni
:label: fermions-electrons

Gli elettroni sono fermioni. Questo comportamento degli elettroni è alla base della spiegazione della struttura atomica, e dell'occupazione di orbitali differenti.

```

```{prf:example} Bosoni in una buca di potenziale
```

```{prf:example} Fermioni in una buca di potenziale
```


