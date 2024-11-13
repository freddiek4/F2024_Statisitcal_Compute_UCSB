import pymysql
import pandas as pd
from sqlalchemy import create_engine

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

user = 'root'
password = ''  # I don't think there is a password here...
host = 'localhost'
database = 'DemoDB'
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")
df.to_sql('TitanicData', con=engine, if_exists='replace', index=False)
print("Data loaded successfully into TitanicData table.")