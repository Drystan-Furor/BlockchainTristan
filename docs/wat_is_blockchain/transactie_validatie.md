# Transaction Validation
> Transactie Validatie

## KeyPairs (openbaar en privé)

>Het bitcoin-netwerk vereist dat alle gebruikers keypairs hebben. Een sleutelpaar bestaat uit één publieke en één private sleutel.

Private keys zijn een enkel 256-bits nummer. Je kunt er zelf een maken of laten genereren. Van deze private key, wordt een public key gegenereerd met behulp van het Elliptic Curve Digital Signature Algorithm (ECDSA). De resulterende reeks getallen met een public key kan niet omgekeerd worden gebruikt om een private key te vinden. Dit nieuwe keypair wordt gebruikt om gegevens te coderen/decoderen en om gegevens te vergrendelen waarbij alleen de private key kan worden gebruikt om deze te ontgrendelen.

---
## Basisverificatieproces

> Bitcoin authenticeert transacties en afzenders met digitale handtekeningen die zijn gemaakt met behulp van sleutelparen. De afzender wil dat het juiste bitcoinbedrag naar de juiste persoon (portemonnee) wordt overgemaakt en de ontvanger wil ervoor zorgen dat de gegevens correct zijn en afkomstig zijn van de afzender.

![418e78d8287c2c81880ba387a0981579.png](:/0fddf61ffae147fe86a69e89cfb6132a)

1. De afzender heeft de te verzenden gegevens verzameld.
2. Met behulp van de hash-functie wordt een 256-bit hash gemaakt.
3. De afzender ondertekent de hash met zijn privésleutel, versleutelt deze en maakt een digitale handtekening

- Op dit punt worden gegevens, de openbare sleutel en de digitale handtekening aan de ontvanger verstrekt.

4. Wanneer de openbare sleutel wordt toegepast op de digitale handtekening, wordt stap 3 gerespecteerd en is de hash van stap 2 het resultaat.
5. De gegevens en de hash-functie worden toegepast en het resultaat is de hash (moet hetzelfde zijn als stap 2).
6. De resultaten van stap 4 en 5 worden vergeleken, en indien correct, wordt de transactie geauthenticeerd; als dit niet het geval is (de gegevens zijn onjuist of de gebruikte openbare sleutel is onjuist), wordt deze afgewezen als een valse transactie.

---
## The Bitcoin Transaction(receiving)

Je besluit je oldtimer te verkopen en een koper (we noemen hem Nakamura) biedt aan je te betalen met bitcoin, dus je moet een bitcoin-adres opgeven. Je maakt een adres aan door jouw public key te hashen, wat resulteert in een“PubKeyHash” en dat omzetten naar een bitcoin-adres dat begint met een 1 of 3 met het base58check-formaat.

![2fbe87fc5173134f1e37a5b9eac1f697.png](:/4938d48b423144e0bbc9fa76825c276f)
*U kunt de PublicKeyhash reverse engineeren vanaf het adres, maar u kunt de public key niet eens verkrijgen van de PublicKeyHash.*

Met het opgegeven adres maakt Nakamura (uw autokoper) een transactie-output met daarin:

- Index (een transactie-ID) en locatie om te helpen bij toekomstige transacties
- Het totale bedrag in satoshis (de kleinste eenheid van bitcoin)
- PubKey Script vergrendelt het bedrag in uw PubKeyHash

Wanneer u uiteindelijk de tien bitcoins wilt uitgeven, wordt uw privésleutel gebruikt om het PubKey-script te voeden en de ontvangen Bitcoin te ontgrendelen.
![47be62012e376ef945e2f3e9be97337b.png](:/b69c2fc1f7f84405b980a2faabc6a406)

De transactie moet worden gevalideerd en gedolven door de miners (meestal binnen 10 minuten, maar soms langer) om te worden voltooid, en dan geeft uw wallet de storting van tien bitcoins aan. De wallet "bevat" het geld niet zoals een echte portemonnee; alleen een uitvoer die een niet-uitgegeven transactie-uitvoer (UTXO) wordt genoemd. UTXO's worden ontgrendeld wanneer u een deel of alle bitcoin naar een ander adres stuurt en een nieuwe UTXO maakt.

Het bitcoin-netwerk is geen accountgebaseerd systeem, maar een matrix van UTXO's. De portefeuilles bevatten sleutels om die UTXO's te ontgrendelen en over te dragen aan anderen.

---
## The Bitcoin Transaction (Sending)

Als u een hoeveelheid satoshis verzendt, maakt u een nieuwe UTXO voor die transactie en verzendt u ofwel alle bitcoin met de enkele nieuwe UTXO of wordt er een tweede nieuwe UXTO gemaakt met de rest die direct naar u wordt teruggestuurd.

Nu wil je die bitcoin van de autoverkoop uitgeven om een verzameling Pokémon-kaarten van Ash te kopen (hij heeft ze allemaal). Je creëert dus een nieuwe input en output.

![946ab162124daae4f9435e82da143c24.png](:/971c01ac4b194c61beb1da79bd8ffadd)

---
## Input:
![b216c64daeca5f84a2d9452f86565fc8.png](:/77801f78e60241b0a4f077a77145589a)

U begint met de transactie-ID en Index om de UTXO en het PubKey-script van de verkoop van de auto te vinden (blauwe rechthoek hierboven).

Vervolgens maakt u een nieuw handtekeningscript aan dat bedoeld is om het PubKey-script te bevredigen. Het Signature-script heeft een handtekening (alle transactiegegevens voor verzending naar Ash) en uw openbare sleutel. De gegevens zijn:

- Oude transactie-ID
- Oude Index
- Nakamura's PubKey-script
- Ash's PubKey-script
- Totaal satoshi's gaan naar Ash

Deze gegevens worden tweemaal gehasht met het SHA256-algoritme en ondertekend met uw privésleutel. Dit product wordt vervolgens toegevoegd aan uw openbare sleutel om het nieuwe handtekeningscript te maken. Oranje rechthoek hierboven

## Output
![2a50c4398d57054f9ec44b0559ac1360.png](:/6f7966de4954449bb94bad1c0615b70b)

Je output bevat de satoshi's die moeten worden overgedragen, een nieuwe index en een nieuw PubKey-script met het adres van Ash dat hij verstrekt om de bitcoin aan zijn adres te vergrendelen.

---
## Miners and the PubKey Script

> Wanneer de transactie naar de miners wordt verzonden, nemen ze het **Signature Script** en voeren het uit met het **PubKey Script**. Met een "true" resultaat wordt de transactie toegevoegd aan het blok en vervolgens gevalideerd.

### The PubKey Script explained
![9b97848c4f2a1f7de4717198997bf0be.png](:/8309affabd5f44d198fbb9fccf6b83e8)

Het PubKey-script gebruikt het volgende gestapelde proces van zes stappen om de transactie **(retourneer een T of F)** te verifiëren:

1. Voeg het handtekeningscript (Sig) toe en stapel er vervolgens de openbare sleutel (PubKey) op
2. OP_DUP duplicaten van het laatste dat aan de stapel is toegevoegd (de PubKey)
3. OP_HASH160 hasht de gedupliceerde openbare sleutel Pk Hash
4. PubKey (Pk) Hash van de eerste transactie (auto) wordt toegevoegd (Pk Hash in het ovaal)
5. OP_EQUALVERIFY vergelijkt de bovenste twee delen van de stapel, Pk Hash van de autotransactie (in het ovaal) en de Pk Hash van de openbare sleutel die is verstrekt aan het Signature Script (in het vierkant). Als ze hetzelfde zijn, worden ze van de stapel verwijderd (gepopt). (laat de publieke sleutel en handtekening achter)
6. OP_CHECKSIG gebruikt de openbare sleutel om de handtekening te decoderen. Het PubKey-script controleert vervolgens of er overeenstemming is tussen de digitale handtekening en de uitvoer van de gegevens die tweemaal zijn gehasht en ondertekend, waardoor de handtekening (sig) wordt gemaakt. Als ze overeenkomen, worden de Sig en PubKey verwijderd en wordt een "True" resultaat toegevoegd aan het nieuwe blok en gevalideerd op het netwerk; als "Fals" mislukt, mislukt de transactie en wordt deze niet toegevoegd.
> Ash geeft je nu je geliefde Pokémon-verzameling.

---
## Overzicht

Het Bitcoin-transactievalidatieproces is een reeks controles om ervoor te zorgen dat het netwerk nauwkeurig blijft en privacy mogelijk maakt door geen persoonlijke informatie te verzenden om transacties uit te voeren. Het transactieproces is bewezen een robuust systeem te zijn dat manipulatie kan voorkomen en vertrouwen kan geven aan de gebruikers.