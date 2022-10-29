

# Elliptic Curve Digital Signature Algorithm (ECDSA)
> dit document bevat [KaTeX notation](https://katex.org/), bekijk het in [Joplin](https://joplinapp.org/).

![Elliptische curve digitale handtekening algoritme](https://trustica.cz/wp-content/uploads/2018/06/frame-16644.png "ECDSA")

In cryptografie biedt het Elliptic Curve Digital Signature Algorithm (ECDSA) een variant van het Digital Signature Algorithm (DSA) dat elliptische kromme cryptografie gebruikt.
---
---
## Sleutel- en handtekeninggrootte
Net als bij cryptografie met elliptische krommen in het algemeen, is de bitgrootte van de privésleutel die nodig wordt geacht voor ECDSA ongeveer twee keer zo groot als het beveiligingsniveau, in bits.
> Bij een beveiligingsniveau van 80 bits, wat inhoudt dat een aanvaller maximaal ongeveer $\ 2^{80}$ bewerkingen nodig heeft om de privésleutel te vinden, zou de grootte van een privésleutel van ECDSA 160 bits zijn. Aan de andere kant is de handtekeninggrootte hetzelfde voor zowel DSA als ECDSA: ongeveer $\ 4t$ bits, waarbij *t* het beveiligingsniveau is, gemeten in bits, dat wil zeggen ongeveer 320 bits voor een beveiligingsniveau van 80 bits.

## Sleutelgeneratie
We genereren asymmetrische sleutels met behulp van de algoritmen voor sleutelovereenkomsten die cryptografie met elliptische krommen biedt. **Elliptische curve Diffie-Hellman (ECDH)** is een veelgebruikt algoritme voor sleutelovereenkomsten. Het proces van publiek-private sleutelgeneratie in ECDH als volgt:

- Privésleutel: De privésleutel is een willekeurig gekozen getal $\ n_{p}$ zodat $\ n_{p}$ ligt in het interval 1 tot $\ n_o -1$, waarbij $\ n_o$ de volgorde is van de subgroep van de elliptische krommepunten, gegenereerd door het generatorpunt $\ G$

- Openbare sleutel: de openbare sleutel wordt gegeven als $\ P = n_pG$, waarbij $\ n_p$ de privésleutel is die hierboven willekeurig is geselecteerd, $\ G$ het generatorpunt van de elliptische curve is en $\ P$ de publieke sleutel.



---
## Algoritme voor het genereren van handtekeningen
Stel dat [Alice](https://en.wikipedia.org/wiki/Alice_and_Bob) een ondertekend bericht wil sturen naar [Bob](https://en.wikipedia.org/wiki/Alice_and_Bob). In eerste instantie moeten ze het eens zijn over de krommeparameters $\ CURVE,G,n$ Naast het veld en de vergelijking van de kromme hebben we $\ G$ nodig, een basispunt van de eerste orde op de kromme; $\ n$ is de vermenigvuldigingsvolgorde van het punt $\ G$


| Parameter |                                                                                                                                                                                             |
|:---------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| $\ CURVE$ | het elliptische krommeveld en de gebruikte vergelijking                                                                                                                                     |
|   $\ G$   | elliptische kromme basispunt, een punt op de kromme dat een [subgroep van grote priemgetallen $\ n$](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography#Domain_parameters) genereert |
|   $\ n$   | integer volgorde van $\ G$ , betekent dat $\ n \times G=O$, waarbij $\ O$ het identiteitselement is                                                                                         |
| $\ d_{A}$ | de privésleutel (willekeurig geselecteerd)                                                                                                                                                  |
| $\ Q_{A}$ | de openbare sleutel $\ d_{A} \times G$ (berekend met een elliptische curve)                                                                                                                 |
|   $\ m$   | het te verzenden bericht                                                                                                                                                                    |

![ecdsa](https://i.pinimg.com/originals/e5/67/23/e56723a709b473328852a42c3f53561a.jpg)


## Handtekening generatie
Het algoritme voor het genereren van handtekeningen is gebaseerd op het ElGamal-handtekeningschema. Het neemt de privésleutel van de afzender en het te verzenden bericht als invoer en genereert de handtekening als uitvoer. De werking van het algoritme is als volgt:

1. **Message hash**: We berekenen de hash $\ h$ van het bericht $\ m$
   met hashfuncties zoals MD-5, SHA-256 en Keccak-256, als volgt:
   $$
   h = hash (m)
   $$
2. **Willekeurig getal**: We kiezen een willekeurig getal $\ k$, variërend van 1 tot $\ n-1$, waarbij $\ n$ een priemgetal is dat de volgorde van de subgroep van elliptische krommepunten voorstelt gegenereerd door het generatorpunt $\ G$
3. **Willekeurig punt**: We berekenen het willekeurige punt $\ R$ op de elliptische kromme door het willekeurige getal $\ k$ te vermenigvuldigen met het generatorpunt $\ G$, als volgt:
   $$
   R = kG
   $$
4. **x-coördinaat:** We selecteren de $\ x$ *-coördinaat* van het hierboven gegenereerde willekeurige punt, als volgt:
   $$
   r = R.x
   $$
5. **Handtekeningbewijs**: We passen de volgende vergelijking toe om het handtekeningbewijs $\ s$ als volgt te berekenen:
   $$
   s = k^{−1}\times (h+r\times n_p)\,(mod\,n)
   $$
- De handtekening bestaat uit twee gehele waarden berekend boven $\ r$ en $\ s$

---
![generate a public ley](https://th.bing.com/th/id/R.c3aae197b37d83f7380f189958e1fa13?rik=LIqwfUGepL7ckQ&riu=http%3a%2f%2fi.stack.imgur.com%2felA8D.png&ehk=b2iNEiR7PxvpGjG3vHeJEha9LUMtN3QgAVaVj1O%2bjo0%3d&risl=&pid=ImgRaw&r=0)

---

## Handtekeningverifiëring
Het handtekeningverificatie-algoritme neemt het bericht en de handtekening $\ r,s$ als invoer en retourneert een booleaanse waarde die aangeeft of de handtekening is geverifieerd. Het handtekeningverificatie-algoritme werkt als volgt:

1.**Berichthash**: We berekenen de hash $\ h$ van het bericht $\ m$ met dezelfde hashfunctie die we gebruikten tijdens het genereren van handtekeningen, als volgt:
$$
h = hash (m)
$$
2. **Modulaire inverse:** We berekenen de modulaire inverse van de handtekening als volgt:
   $$
   s_{inverse} = s^{-1} (mod \, n)
   $$
3. **Willekeurig punt**: we herberekenen het willekeurige punt
   $\ R'$ zoals in het proces voor het genereren van handtekeningen, waarbij $\ P$ de openbare sleutel van de afzender is, als volgt:
   $$
   R’ = (h \times s_{inverse}) \times G + (r \times s_{inverse}) \times P
   $$
4. **x-coördinaat**: We krijgen de $\ x$ *-coördinaat* van het herberekende willekeurige punt, als volgt:
   $$
   r' = R'.x
   $$
5. **Verifiëren**: we verifiëren het resultaat door de recent berekende $\ r’$ . te matchen
   met de $\ r$ die als onderdeel van de handtekening kwam, als volgt:
   $$
   r’ == r
   $$

![ontwerp](https://th.bing.com/th/id/OIP.iodCEU8FmCJER0wHR-wAeAHaE2?pid=ImgDet&rs=1)

---
## Uitgebreide ECDSA
We kunnen de openbare sleutel genereren uit de handtekening die is berekend door het ECDSA-algoritme. Het berekeningsproces van de openbare sleutel retourneert 0, 1 of 2 punten op de elliptische curve die de openbare sleutel vertegenwoordigen tegen de handtekening. Dit zorgt echter voor onduidelijkheid.

Extended ECDSA pakt dit probleem aan door een extra deel $\ v$ aan de handtekening toe te voegen, waardoor de handtekening $\ {r,s,v}$ wordt. Hierdoor kunnen we de publieke sleutel met meer zekerheid berekenen. De uitgebreide ECDSA verwijdert niet alleen dubbelzinnigheid, maar heeft ook meer toepassingen.

## Gebruik van uitgebreide ECDSA
Uitgebreide ECDSA-implementatie is met name handig in omgevingen met beperkte opslag of bandbreedte. In situaties waar het moeilijk of duur is om openbare sleutels op te slaan of te verzenden, kunnen we uitgebreide ECDSA gebruiken.

> Blockchain is een omgeving die beperkt is in bandbreedte en opslag. Door uitgebreide ECDSA te gebruiken, wordt het verzenden of opslaan van de openbare sleutel vermeden. Ethereum gebruikt het om transacties te ondertekenen.

![a signing mechanism of ECDSA](https://www.researchgate.net/publication/341061276/figure/download/fig1/AS:962414149373966@1606468822740/a-Signing-mechanism-of-elliptic-curve-digital-signature-algorithm-b-Verification.png)

```
{
  "author": "Tristan",
  "email": "artstristan@gmail.com",
}
```
