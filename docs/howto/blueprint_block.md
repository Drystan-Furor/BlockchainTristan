### Dit is een voorbeeld van een Block
> Elk block heeft een *index*, een *timestamp* (in Unix time), een *lijst van transacties*,
> een *proof*, en de *hash van het vorige block*

```
{
block = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'transactions': [
        {
        'sender': "8527147fe1f5426f9dd545de4b27ee00",
        'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
        'amount': 5,
        }
    ],
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}
```

Hier wordt het idee van de *ketting* duidelijk. elk block bevat in zichzelf the hash van het vorige block.
**Dit is cruciaal omdat dit de blockchain onveranderlijk maakt**
Als een aanvaller en eerder block corrupt maakt, dan hebben alle volgende blokken incorrecte hashes.