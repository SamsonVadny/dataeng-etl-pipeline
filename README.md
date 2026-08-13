ETL Pipeline - Fake Store
Esse é um Pipeline de dados (ETL) que tem a missão de extrair, transformar e carregar os dados de productos e utilizadores de uma API pública para uma base de dados MySQL.
A sigla ETL que signifca Extract, Transform and Load se comporta da seguinte maneira.
Extract: Recolhe dados de produtos e utilizadores da API [Platzi Fake Store API](https://fakeapi.platzi.com/)
Transform:Limpa e estrutura os dados: renomeia colunas, extrai valores de campos aninhados, converte tipos de dados
Load:Grava os dados tratados em duas tabelas  de base de dados nesse caso eu usei o MySQL (`products` e `users`).
