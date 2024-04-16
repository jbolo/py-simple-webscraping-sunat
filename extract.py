import pandas as pd
import requests
import zipfile
import os
from pathlib import Path
from connect import engine
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s [%(levelname)s] - %(name)s - %(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

dir_home = Path(os.getcwd())
zip_filename = 'padron_reducido_ruc.zip'


def download_zipfile_from_web_sunat() -> Path:
    url = "https://www2.sunat.gob.pe/" + zip_filename
    logger.info(f"Downloading {url}")
    response = requests.get(url, timeout=(5, 500))

    if response.status_code == 200:
        zip_path = dir_home / zip_filename
        logger.info(f"Filename: {zip_path}")
        with open(zip_path, "wb") as f:
            f.write(response.content)

        logger.info(f"Downloaded {zip_path}")
        return zip_path
    else:
        logger.error(f"Error downloading {zip_path}")
        return None

def extract_zipfile(zip_path) -> pd.DataFrame:
    logger.info("Extracting")
    file_txt = "padron_reducido_ruc.txt"
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extract(file_txt)

    logger.info(f"Extracted {file_txt}")
    # for test, only read first 100 lines of text
    df = pd.read_csv(
        file_txt,
        sep='|',
        skiprows=1,
        header=None,
        names=['ruc','nombre','estado','condicion','ubigeo','tipo_via',
               'nombre_via','codigo_zona','tipo_zona','numero','interior',
               'lote','departamento','manzana','kilometro','adicional'],
        nrows=100,
        encoding="ISO-8859-1")

    logger.info(f"Read {df.shape[0]} rows")
    return df

def insert_to_database(df: pd.DataFrame):
    table = "padron_reducido_ruc"
    logger.info(f"Inserting to database table {table}")
    df.to_sql('padron_reducido_ruc', engine, if_exists='replace', index=False)
    
if __name__ == "__main__":
    zip_path = download_zipfile_from_web_sunat()
    df = extract_zipfile(zip_path)
    insert_to_database(df)
