# UTxO

> The term UTXO stands for "Unspent Transaction Output".

It is basically a type of cryptocurrency recording method that is used to represent the number of tokens that a person receives after they make a transaction on the blockchain.

As the name suggests, UTXO is **the "unspent" output of the transaction.**
> To put it simply, if you spend 5 BTC to buy an item for 3 BTC, then you will receive a new UTXO with a value of 2 BTC. We'll discuss this more in a bit.

---
The concept of UTXO was first created and used by Satoshi Nakamoto on the Bitcoin blockchain. Later, the system was adopted by all forks of Bitcoin, including Bitcoin Cash (BCH), Litecoin (LTC), Zcash (ZEC), as well as several others that are not Bitcoin forks like Monero and Cardano. The purpose of UTXO is partly to check whether or not a certain wallet holds sufficient balance to make a requested transaction.

> For instance, if owner A wants to send 5 BTC to owner B, the network needs to know if owner A has at least 5 BTC in his wallet. If the balance is insufficient, it would be impossible to make the transaction.

Other than that, UTXO is also used **to make sure that no funds are spent twice**, hence eliminating the double-spending issue. Every UTXO can only be spent once, so if you spend the specific UTXO, you won't be able to use it again in the future. For each UTXO spent, one or more new UTXOs are created as a result of the transaction. The new UTXO will be sent to the appropriate wallet.

Put simply, you can think of UTXO as an indivisible and unique chunk of native tokens that are controlled by the owner's private keys.
