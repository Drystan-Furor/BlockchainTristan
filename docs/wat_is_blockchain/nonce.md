Nonce
---
> Vaak moet aan het voorlopige blok **een getal (een nonce)** toegevoegd worden dat ervoor *zorgt dat de totale hash van het blok met een bepaald aantal nullen (voorloopnullen) begint*.

De juiste nonce kan alleen worden gevonden door vele malen te proberen (Brute Force), wat resulteert in constante berekeningen door veel computers. Wanneer het juiste blok is aangekondigd, is het voor andere miners niet langer nuttig om naar hun eigen versie van het volgende blok te zoeken, maar proberen ze een nieuw blok te maken op basis van het aangekondigde blok.

![nonce](https://th.bing.com/th/id/OIP.ATTjWkO48jC7vY0zyBiKQwHaE-?pid=ImgDet&rs=1)

bloktime
---
Om de bloktijd **(de snelheid waarmee steeds een nieuw blok ontstaat)** constant te houden, wordt het aantal voorloopnullen eens in de zoveel tijd bijgesteld.
Gegeven een bepaalde rekenkracht is het een kwestie van geluk om snel zo'n blok te vinden, dus met een beperkte rekenkracht maakt men toch een evenredige kans. 

```
{
  "author": "Max",
  "email": "max.felis11@gmail.com",
}
```