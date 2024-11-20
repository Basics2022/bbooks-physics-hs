(physics-hs:thermodynamics:foundation:principles:open)=
# Sistemi aperti

In generale, l'equazione di bilancio di una grandezza fisica per un sistema aperto si ricava partendo dal bilancio della stessa grandezza fisica per un sistema chiuso e aggiungendo il contributo dei termini di flusso della grandezza fisica desiderata, attraverso la frontiera del sistema. Così, se il bilancio della grandezza fisica $F$ per il sistema chiuso all'interno del volume $V_t$ può essere scritto come

$$\dfrac{d}{dt} F_{V_t} = R^e_{V_t} \ ,$$

il bilancio della stessa grandezza fisica per un sistema aperto identificato dal volume (geometrico) $v_t$ può essere scritto come

$$\frac{d}{dt} F_{v_t} = R^e_{v_t} - \Phi_{\partial v_t}(f) \ , $$

avendo definito $f$ come la grandezza specifica di $F$ per unità di massa. Il termine di flusso attraverso la frontiera $\partial v_t$ può essere scritto come la somma dei contributi di flusso attraverso porzioni $s_{k,t}$ della superficie $\partial v_t = \cup_k s_{k,t}$,

$$\Phi_{\partial v_t}(f) = \sum_{s_{k,t}} \dot{m}_k \, f_k \ ,$$

avendo definito $\dot{m}_k = \rho_k vi^{rel}_{n,k}$ il flusso di massa attraverso la superficie $s_{k,t}$ e assumendo che la grandezza $f_k$ sia costante sulla superficie $s_{k,t}$, o che sia stato considerato il valore medio sulla superficie.

```{note}
Nel caso la grandezza $f$ non sia uniforme sulla frontiera del dominio e che vari con continuità, il termine di flusso può essere scritto al limite come sommatoria di infiniti termini attraverso superfici la cui area tende a zero, tramite un integrale di superficie, seguendo la definizione di integrale di Riemann.
```

```{note}
Un'equazione di bilancio di una grandezza fisica per un sistema aperto include anche l'equazione di bilancio della stessa grandezza fisica per un sistema aperto come caso particolare in cui il flusso di massa è nullo attraverso la frontiera del dominio, $\dot{m}_k = 0$.
```

Si considerano qui i bilanci (integrali, globali di un sistema) di alcune grandezze fisiche fondamentali in meccanica classica: massa, quantità di moto, momento della quantità di moto, energia totale.

## Bilancio di massa
Il bilancio di massa, $F = M$, $f = 1$, per un sistema aperto è

$$\frac{d}{dt} M_{v_t} = - \sum_k \dot{m}_k$$

## Bilancio della quantità di moto

<span style="color:red"> **todo** *riferimento da o a meccanica classica*</span>

## Bilancio del momento della quantità di moto

<span style="color:red"> **todo** *riferimento da o a meccanica classica*</span>

## Bilancio dell'energia totale
Il bilancio di energia totale $F = E^{tot} = E + K$, $f = e^{tot} = e + \frac{|\vec{v}|^2}{2}$,

$$\frac{d}{dt} E^{tot}_{v_t} = P^{ext}_{v_t}  + \dot{Q}^{ext}_{v_t}  - \sum_k \dot{m}_k \, e^{tot}_k \ .$$

La potenza delle azioni esterne $P^{ext}_{v_t}$ può essere scritta come somma dei contributi sulle superfici della frontiera del sistema attraverso le quali c'è flusso di massa, e le superfici impermeabili che possono essere utilizzate per estrarre lavoro dal sistema. Nel caso si possano trascurare gli effetti degli sforzi viscosi sulle superfici attraverso le quali c'è flusso di massa, la potenza delle azioni agenti sul sistema può essere scritta come

$$\begin{aligned}
  P^{ext} & = P^{ext,mech} + P^{ext,\Phi} = \\
          & = P^{ext,mech} - \sum_{k} \dot{m}_k \frac{P_k}{\rho_k} \ , 
\end{aligned}$$

e il bilancio di energia totale del sistema diventa

$$\dfrac{d}{dt} E^{tot}_{v_t} = P^{ext,mech}_{v_t} + \dot{Q}^{ext} - \sum_k \dot{m}_k h^{tot}_k \ ,$$

avendo introdotto la definizione di entalpia totale specifica, $h^{tot} = e^{tot} + \frac{P}{\rho} = e + \frac{P}{\rho} + \frac{|\vec{v}|^2}{2}$.

```{prf:example} Turbina
```
```{prf:example} Compressore
```
```{prf:example} Camera di combustione
```
