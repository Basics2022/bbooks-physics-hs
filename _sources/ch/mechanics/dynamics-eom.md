(physics-hs:mechanics:dynamics:eom)=
# Equazioni cardinali della dinamica per sistemi chiusi

Le equazioni cardinali della dinamica mettono in relazione le variazioni delle grandezze inerziali con le azioni agenti sul sistema.

Usando i princìpi della meccanica di Newton e la conservazione della massa per sistemi chiusi, è possibile ricavare le equazioni cardinali della dinamica, che governano il moto di un sistema meccanico.

Per ogni sistema chiuso le equazioni cardinali assumono la stessa forma, quando vengono espresse in termini di quantità di moto, quantità del momento angolare ed energia cinetica del sistema. Questo viene qui dimostrato per un [punto materiale](physics-hs:mechanics:dynamics:eom:points) per un [sistema di punti materiali](physics-hs:mechanics:dynamics:eom:points), e per [un corpo rigido con distribuzione di massa continua in un moto piano](physics-hs:mechanics:dynamics:eom:rigid-2d) **todo**, ma è valido per un sistema meccanico qualsiasi.

In particolare, per moti regolari e derivabili (e quindi senza urti impulsivi) le 3 equazioni cardinali del moto sono:

- **bilancio della quantità di moto**: la derivata nel tempo della quantità di moto di un sistema chiuso è uguale alla risultante delle forze esterne agenti sul sistema,

  $$\dot{\vec{Q}} = \vec{R}^{ext} \ ;$$

- **bilancio del momento della quantità di moto**: la derivata nel tempo del momento della quantità di moto di un sistema chiuso rispetto a un punto $H$, a meno di un "termine di trasporto della quantità di moto", è uguale alla risultante dei momenti esterni rispetto al polo $H$

  $$\dot{\vec{L}}_H + \dot{\vec{x}}_H \times \vec{Q} = \vec{M}^{ext}_H \ ;$$

- **bilancio dell'energia cinetica**: la derivata nel tempo dell'energia cinetica di un sistema chiuso è uguale all potenza totale agente sul sistema, uguale alla somma della potenza delle azioni interne e delle azioni interne al sistema,

  $$\dot{K} = P^{tot} = P^{ext} + P^{int} \ .$$
