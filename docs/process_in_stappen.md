### basic development
1. Maak een API
2. Toevoegen block aan chain en ophalen van blocks via API
3. Code coverage
4. CI workflow GitHub toevoegen
5. Toevoegen van transaction via API
6. Maak Proof of Work
7. Toevoegen block via API
8. Functies voor het valideren van de chain / blocks
9. Consensus algoritme 

### adept development
1. mining endpoint en auto start task mining -m.b.v. celery
2. Transaction class, input / output. verify, add, calculate fee
3. UTXO && UTXOPool
4. transaction validation
5. balance API, code coverage
6. Node registration
7. Block API return index/height
8. p2p node construction
9. broadcast blocks
10. Consensus algoritme 
11. block reward


### over 9000
1. [3,7 uur video's kijken tot en met video 37](https://www.youtube.com/channel/UCW7L2NGmFUEsZoPReKW_4iQ/videos)
- En voor zover nog niet gedaan lees de hoofdstukken uit het boek van Song (zie voorbereiding bijeenkomst 3) Finite Fields en ECDSA /secp
2. Sign & Validate inbouwen in Wallet, gebruik theorie Song om R en S te berekenen
3. Transacties signeren en valideren
- test voor het signeren van transactie met wallet
- test valideren transactie door node
4. Transacties broadcasten en valideren
- nodes valideren de transactie en voegen die toe aan de mempool

TODO wat moet gebeuren

```
{
  "firstName": "Max",
  "email": "max.felis11@gmail.com",
}
```
```
{
  "firstName": "Jeroen",
  "email": "Jeroen-Hendriks@outlook.com",
}
```
```
{
  "firstName": "Tristan",
  "email": "artstristan@gmail.com",
}
```