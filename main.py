from extract import extract
from transform import transform 
from load import load_csv, load_db
from logs import logs

db_name = 'data/country_pib.db'
table_name = 'pib'
file_path = 'data/country_pib.csv'

#Extrai os dados da URL e salva no DataFrame
logs('ETL process started')
df = extract()
logs('Data extracted successfully')

#Executa a função de transformação e salva no DataFrame
df = transform(df)
logs('Data transformed successfully')

#Executa a função de load_csv e salva no CSV
load_csv(df, file_path)
logs('Data loaded successfully to CSV')

#Executa a função de load_db e salva no SQLite
load_db(df, db_name, table_name)
logs('Data loaded successfully to DB')

print('ETL concluído!')