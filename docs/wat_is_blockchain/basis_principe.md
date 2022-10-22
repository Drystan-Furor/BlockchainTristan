# Basisprincipe
![dbbcb39608291c559f7086d9247a21fc.png](https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Bitcoin_Block_Data.svg/580px-Bitcoin_Block_Data.svg.png)

De data wordt opgeslagen in zogenaamde blokken, dat zijn lijsten met transacties of andere gegevens. Het blok wordt afgesloten met de hash van alle gegevens in het dat block. De hash van het vorige blok wordt opgenomen in het volgende blok, dus de blokken zijn gerelateerd aan elkaar en aan de zogenaamde keten. Dus elk blok is als volgt opgebouwd:

- De hash van het voorgaande blok (cryptohash).
> Alleen het oudste blok van de chain (het zogenaamde Genesis block) bevat deze niet.

- Toegevoegde datarecords. Deze records kunnen door verschillende gebruikers worden toegevoegd.

> Om te verifiëren dat een bepaalde gebruiker inderdaad bepaalde informatie heeft verzonden, is deze uitgerust met een digitale handtekening die alleen door die gebruiker  kan worden gemaakt, maar door iedereen kan worden geverifieerd.

- De hash van het geheel. Deze dient als een soort serienummer.

---
![dbbcb39608291c559f7086d9247aadfghgs21fc.png](https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Blockchain.svg/300px-Blockchain.svg.png)

Van tijd tot tijd wordt er een nieuw blok gemaakt, dit wordt mining genoemd. Zodra een nieuw blok is gegenereerd, moeten alle netwerkdeelnemers of knooppunten het accepteren. Hierdoor ontstaat een soort database die alle nodes kunnen controleren op legitimiteit. Een nieuw blok wordt alleen geaccepteerd als het de hash van het laatste blok bevat en alle gegevens de juiste elektronische handtekening hebben.

Soms zijn aanvullende controles nodig, zoals bij financiële transacties waarbij iemand voldoende saldo moet hebben voordat de transactie kan worden afgerond. Een blok is alleen geldig als een meerderheid van de knooppunten het heeft geaccepteerd.

Soms treden er meningsverschillen op, bijvoorbeeld wanneer twee knooppunten (nodes) tegelijkertijd een nieuw blok hebben gemaakt en andere knooppunten een deel van het ene blok en een deel van het andere blok accepteren. Dit wordt een vork genoemd en is bijna altijd tijdelijk. Beide blokkades zijn gerechtvaardigd, dus er zijn **tijdelijk** twee versies van de waarheid. Na verloop van tijd keert de consensus echter terug en wordt de ene versie van de waarheid geaccepteerd en de andere vergeten.

Een harde vork ontstaat wanneer twee kettingen permanent parallel zijn. Dit gebeurt alleen  wanneer een deel van het netwerk besluit om over te stappen naar een nieuwe versie van de software  (met gewijzigde regels), terwijl een ander deel bij de oude versie blijft. Vanaf dit punt kan geen enkele groep elkaars blokkades accepteren. Zo ontstond  Ethereum Classic in 2016, los van Ethereum.

Een **blockchain werkt dus als een gedistribueerde database** waarbij alle nodes die actief zijn een kopie bijhouden en elkaar controleren.

Er kunnen geen wijzigingen worden aangebracht aan eerder gemaakte blokken, omdat daarmee ook de hash-waarde van het bewerkte blok verandert, en omdat de blokken door hash aan elkaar zijn gekoppeld, wordt de ketting verbroken. Wanneer een blok wordt bewerkt, moeten alle blokken die erna zijn gemaakt ook worden bewerkt om een nieuwe keten te maken.

Aangezien er meer nodes zijn, kan een dergelijk probleem worden gedetecteerd en opgelost door de aanpassingen te stoppen of het knooppunt dat deze informatie verzendt te negeren. Dit systeem zorgt voor de integriteit die de blockchain biedt.


```
{
  "author": "Tristan",
  "email": "artstristan@gmail.com",
}
```