# Ponderada de Matemática: Suavização Exponencial Simples

## Alphas Avaliados
Segue abaixo os alphas testados e seus respectivos RMSE (Root Mean Squared Error)

- **0,7** : 17075838,5
- **0,5** : 21147894,7
- **0,3** : 33783637,9

Com esses dados, podemos chegar a conclusão de que quanto maior o peso dado aos valores reais (alpha maior), melhores são os resultados, mostrando para gente que para a previsão de uma receita, é necessário reações rápidas a mudanças. Assim chegamos a conclusão que o melhor alpha é o de `0,7`.

## Previsão de Receita para Janeiro 2025
Seguindo com o alpha `0,7`, fazemos a previsão para janeiro de 2025, que resultou no valor de R$ 141.752

Obs.: Todo o código utilizado para realizar a atividade está em `ses.py`, para rodar o código é necessário apenas instalar as dependências em `requitements.txt`.