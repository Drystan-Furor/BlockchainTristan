# UTxO

> De term UTXO staat voor "Unspent Transaction Output".

Het is in feite een soort cryptocurrency-opnamemethode die wordt gebruikt om het aantal tokens weer te geven dat een persoon ontvangt nadat hij een transactie op de blockchain heeft gedaan.

Zoals de naam al doet vermoeden, is UTXO **de "niet-uitgegeven" output van de transactie.**
> Simpel gezegd, als u 5 BTC uitgeeft om een artikel voor 3 BTC te kopen, ontvangt u een nieuwe UTXO met een waarde van 2 BTC. We zullen dit zo meer bespreken.

---
Het concept van UTXO werd voor het eerst gemaakt en gebruikt door Satoshi Nakamoto op de Bitcoin-blockchain. Later werd het systeem overgenomen door alle vorken van Bitcoin, inclusief Bitcoin Cash (BCH), Litecoin (LTC), Zcash (ZEC), evenals verschillende andere die geen Bitcoin-vorken zijn, zoals Monero en Cardano. Het doel van UTXO is onder meer om te controleren of een bepaalde portemonnee voldoende saldo heeft om een gevraagde transactie uit te voeren.

> Als eigenaar A bijvoorbeeld 5 BTC naar eigenaar B wil sturen, moet het netwerk weten of eigenaar A ten minste 5 BTC in zijn portemonnee heeft. Als het saldo onvoldoende is, is het onmogelijk om de transactie uit te voeren.

Afgezien daarvan wordt UTXO ook gebruikt **om ervoor te zorgen dat geld niet twee keer wordt uitgegeven**, waardoor het probleem van dubbele uitgaven wordt geëlimineerd. Elke UTXO kan maar één keer worden uitgegeven, dus als u de specifieke UTXO uitgeeft, kunt u deze in de toekomst niet meer gebruiken. Voor elke uitgegeven UTXO worden als gevolg van de transactie een of meer nieuwe UTXO's gecreëerd. De nieuwe UTXO wordt naar de juiste portemonnee gestuurd.

> Simpel gezegd, je kunt UTXO zien als een ondeelbaar en uniek stuk native tokens dat wordt beheerd door de privésleutels van de eigenaar.

Een UTXO is een niet-uitgegeven transactie-output. Bij een geaccepteerde transactie in een geldig blockchain-betalingssysteem (zoals Bitcoin), kunnen alleen niet-uitgegeven outputs worden gebruikt als input voor een transactie. Wanneer een transactie plaatsvindt, worden invoer verwijderd en worden uitvoer gemaakt als nieuwe UTXO's die vervolgens in toekomstige transacties kunnen worden verbruikt.