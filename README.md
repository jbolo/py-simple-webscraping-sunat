# py-simple-webscraping-sunat
Process that downloads a list of clients from the sunat website and saves it in a mysql database.

To build, make sure you have Python 3.11 installed. Then install `poetry`:

```sh
pip install -U poetry
```

Then install all the necessary packages (make sure to change to the root directory of the project):

```sh
poetry install
```

You can execute the process with the following command:
```sh
python extract.py
```

Dont forget create your database and set the database credentials on your environment: MYSQL_HOSTNAME, MYSQL_USERNAME and MYSQL_PASSWORD. Also, create the database sunat and the table padron_reducido_ruc.

