# Análise de anúncios de venda de carros

Aplicação web interativa para exploração de um conjunto de dados de anúncios de venda de carros nos Estados Unidos.

## Descrição

O painel permite visualizar a distribuição e as relações entre as principais variáveis dos anúncios através de dois gráficos gerados com plotly-express:

- **Histograma** da quilometragem (`odometer`), que mostra como se distribuem os veículos anunciados.
- **Gráfico de dispersão** entre quilometragem e preço (`price`), que permite observar a relação entre o desgaste do veículo e o valor pedido.

Cada gráfico é gerado ao clicar no botão correspondente.

## Aplicação publicada

https://vehicles-dashboard-b89w.onrender.com

Nota: a aplicação está alojada no plano gratuito do Render, pelo que fica inativa após um período sem utilização. O primeiro acesso pode demorar cerca de um minuto a carregar.

## Estrutura do projeto

- `app.py` — código da aplicação Streamlit
- `notebooks/EDA.ipynb` — análise exploratória dos dados
- `vehicles_us.csv` — conjunto de dados
- `requirements.txt` — dependências do projeto
- `.streamlit/config.toml` — configuração do servidor

## Bibliotecas utilizadas

pandas, plotly-express, streamlit

## Executar localmente

    python -m venv vehicles_env
    source vehicles_env/bin/activate
    pip install -r requirements.txt
    streamlit run app.py
