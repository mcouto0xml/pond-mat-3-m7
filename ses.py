import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error

receita_2023 = [
    110000, 113000, 110000, 111000, 112000, 115000,
    115000, 120000, 112000, 112000, 114000, 125000
]
receita_2024 = [
    126000, 131000, 131000, 134000, 135000, 137000,
    140000, 139000, 135000, 135000, 137000, 144000
]

# Combinar série
dados = receita_2023 + receita_2024
datas = pd.date_range("2023-01-01", periods=len(dados), freq="MS")
serie = pd.Series(dados, index=datas)

# Função de suavização exponencial simples
def ses_forecast(series, alpha):
    forecast = [series.iloc[0]]  
    for t in range(1, len(series)):
        f_t = alpha * series.iloc[t-1] + (1 - alpha) * forecast[-1]
        forecast.append(f_t)
    return np.array(forecast)

# Testar diferentes alphas
alphas = [0.7, 0.5, 0.3]
rmse_scores = {}
forecast_series = {}

for alpha in alphas:
    fitted = ses_forecast(serie, alpha)
    rmse = mean_squared_error(serie, fitted)
    rmse_scores[alpha] = rmse
    forecast_series[alpha] = fitted

# Escolher o melhor alpha (menor RMSE)
best_alpha = min(rmse_scores, key=rmse_scores.get)
best_rmse = rmse_scores[best_alpha]

# Previsão para Jan/2025 usando o melhor alpha
# último valor previsto (para Dez/24) + fórmula SES
last_forecast = forecast_series[best_alpha][-1]
last_observed = serie.iloc[-1]
next_forecast = best_alpha * last_observed + (1 - best_alpha) * last_forecast

# Resultados
results = {
    "RMSE_por_alpha": rmse_scores,
    "Melhor_alpha": best_alpha,
    "RMSE_melhor": best_rmse,
    "Previsao_Jan_2025": next_forecast
}

print(f"Segue aqui os resultados: \n{results}")
