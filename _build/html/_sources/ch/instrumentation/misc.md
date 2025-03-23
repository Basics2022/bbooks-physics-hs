(instrumentation:list)=
# Esempi

## Misura posizione, velocità, accelerazione

(instrumentation:list:accelerometer)=
### Accelerometri

(instrumentation:list:accelerometer:mems)=
#### Accelerometro capacitivo, MEMS

- parte meccanica MMS. Equazioni in un sistema di riferimento non inerziale, $\tilde{x} = x + x_{out}$, con $\tilde{x}$ lo spostamento rispetto a un sistema inerziale, $x_{out}$ lo spostamento del telaio dello strumento, preso come sistema non inerziale del quale vogliamo misurare l'accelerazione, e $x$ lo spostamento relativo rispetto al telaio di una massa sospesa

  $$m \dfrac{d^2}{dt^2}(x + x_{out}) + c \dfrac{d x}{dt} + k x = 0 \, $$

  o separando lo stato $x$ dello strumento, dall'ingresso $a_{out} := \ddot{x}_{out}$,

  $$m \ddot{x} + c \dot{x} + k x = - a_{out} \ ,$$

**todo** *Per convenienza, se quel segno meno disturba, si può definire lo spostamento relativo in direzione opposta a quella usata per definire lo spostamento assoluto e ottenere quindi $m \ddot{x} + c \dot{x} + k x = a_{out}$. Riferimento all'[invarianza](physics-hs:todo:invariance)*

- parte elettrica. Lettura della variabile in uscita funzione dello spostamento relativo della massa sospesa rispetto al telaio dello strumento, $y(x)$. Questo legame viene ricavato dall'analisi del circuito elettrico dello strumento {prf:ref}`mems-accelerometer-circuit`


```{prf:example} Circuito elettrico dello strumento
:label: mems-accelerometer-circuit
**todo** A partire da un modello semplice, a modelli più complessi (con più condensatori, per aumentarne la sensitività), per poi ricondursi a problemi semplici agli effetti esterni grazie alla capacità equivalente del circuito
- discutere legame ingresso-uscita: non-lineare! (ma facilmente correggibile!!!); sensibilità
- discutere i modi per aumentare la sensibilità dello strumento
- calcolo della capacità equivalente di circuiti con più condensatori (magari con uno script...)
```


<span style="color:red">Add a sketch or a picture of a real-world MEMS accelerometer, and provide a model</span>

**Cross-referencing.** Questo strumento è stato discusso nell'introduzione agli [strumenti di misura](physics-hs:intro:measurements:order), e presentato come esempio di strumento del secondo ordine.
