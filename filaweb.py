from flask import Flask, render_template
import pandas as pd
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    sheet_url = "https://docs.google.com/spreadsheets/d/1G2qjEZhBYi3URf9-qhCyYXV8dogyA8MMayM4YdjVcqw/pub?output=csv"
    
    df = pd.read_csv(sheet_url, header=3)
    
    data_atual = datetime.now().strftime('%d/%m/%Y')
    df = df[df['DATA'] == data_atual]

    colunas_para_ocultar = ['CR1', 'CR2', 'DOLLY', 'NF', 'OBSERVAÇÃO', 'COMENTÁRIO', 'HORA DA EMISSÃO', 'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 24', 'VICTOR', 'PENDENTE']
    colunas_presentes = [col for col in colunas_para_ocultar if col in df.columns]

    if colunas_presentes:
        df = df.drop(columns=colunas_presentes)
    else:
        print("Nenhuma das colunas a serem ocultadas foi encontrada.")
    
    return render_template('index.html', data=df.to_html(index=False))

if __name__ == '__main__':
    app.run()
