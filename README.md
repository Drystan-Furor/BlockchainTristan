# Welcome

To the Blockchain Tristan repo.

# Setup your Python virtual environments
Create a new Python virtual environment: `python -m venv _env`
## Switch to the new Python virtual environment:
Mac OS / Linux: `source _env/bin/activate`  
Windows: `_env\Scripts\activate`

Check if the new Python virtual environment is active `pip -V`  
Upgrade pip in the virtual environment: `pip install --upgrade pip`  
Install the needed dependencies: `pip install -r requirements.txt`  
Add to requirements.txt: `pip freeze > requirements.txt`

For more information see [this page](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)

# Run Flask
To run the server locally: `flask --app blockchain --debug run`  
also rename the file folder to 'blockchain' to prevent import issues :^)

# OPDR 1-2
- Why are timestamps important?  
  Because a timestamp is used to generate a hash. Therefore if the timetsamp is tempered with, the hash and by extension the blockchain will be rendered inavild.  
  Ensuring the legitimacy of transactions.

>Vraag: Waarom is de timestamp belangrijk?
- >Antwoord: een timestamp is belangrijk zodat anderen geen invloed kunnen hebben over
wanneer de data (transactie) is aangemaakt.
- > Door de timestamp mee te nemen in de hash wordt het een waarheid binnen de blockchain, dus als de timestamp
aangepast zal worden, dan kloppen de hashes en previuos hashes niet meer.

# DevOps
To satisfy the devops requirements I implemented end-to-end tests instead of unit-tests.
Because simply writing tests still has human error margins and having a 100% code coverage doesn't stop people from not implementing certain safety features. It also bogs down developement.

## Static typing
Static typing in this repository I have, using mypy.  
Check the health of the repository using: `mypy ./blockchain/*.py`
### Why?
Static typing exactly states which datatypes are expected everywhere.
This prevents easy to miss mistakes and improves overall maintainability and readability.

## E2E tests
Import the postman collection and test the endpoints via postman.
These tests cover some parts of the application from front to end and check for expected behaviour.
