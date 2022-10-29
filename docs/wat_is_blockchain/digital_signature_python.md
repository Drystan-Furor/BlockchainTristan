# Digital Signature in Python

## Hoe maak je een digitale handtekening in Python met ecdsa SigningKey
De ecdsa-bibliotheek van Python biedt een gebruiksvriendelijke implementatie van ECDSA (Elliptic Curve Digital Signature Algorithm). Met ecdsa kunnen we gemakkelijk openbare en privé sleutelparen genereren, digitale berichten ondertekenen en de integriteit van digitale berichten verifiëren. De bibliotheek kan worden geïnstalleerd met behulp van het volgende pip-commando:
```cli
pip install ecdsa
```

---
## Digitale handtekeningen
Digitale handtekening is een asymmetrische cryptografische techniek die wordt gebruikt om de authenticiteit van digitale berichten of documenten te valideren. Het maakt gebruik van het concept van openbare/private sleutelparen waarbij de twee sleutels wiskundig zijn gekoppeld, wat beveiligingseigenschappen biedt die superieur zijn aan handgeschreven handtekeningen. De persoon die een digitaal document of bericht ondertekent, gebruikt zijn persoonlijke sleutel en de enige manier om de handtekening te ontsleutelen is door de openbare sleutel van dezelfde persoon te gebruiken. Als we het digitale bericht met succes ontsleutelen met behulp van de openbare sleutel van de persoon, is het wiskundig bewezen dat dezelfde persoon het bericht heeft ondertekend. Digitale handtekeningen spelen een belangrijke rol in cryptocurrency.

---
## Een digitale handtekening maken

In het onderstaande voorbeeld laten we zien hoe u digitale handtekeningen maakt.
```python
from ecdsa import SigningKey
private_key = SigningKey.generate() # uses NIST192p
signature = private_key.sign(b"Avans+ authorizes this shot")
print(signature)
```

In het bovenstaande voorbeeld importeren we eerst het SigningKey-object uit de ecdsa-bibliotheek. De methode Genereer() van SigningKey maakt een privésleutel voor ons aan. Standaard gebruikt de methode Genereer() de curve $\ NIST192p$. Als u een langere curve wilt gebruiken die meer zekerheid biedt, kunt u de parameter curve=<curvename> toevoegen in de methode Genereer(). We kunnen dan het teken () gebruiken dat toegankelijk is voor private_key om alle digitale gegevens te ondertekenen als een bytestring en een digitale handtekening terug te krijgen (ook een bytestring).

```
{
  "author": "Jeroen",
  "email": "Jeroen-Hendriks@outlook.com",
}
```