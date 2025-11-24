import pandas as pd
import numpy as np
import os

# Configurações
np.random.seed(42)
years = np.arange(1950, 2025)

# Configuração EXATA do Mais Frio para o Mais Quente
# Baseado em médias anuais aproximadas
countries_config = [
    # 1. O Mais Frio de todos
    {'country': 'Antarctica Base', 'continent': 'Antarctica',     'base_temp': -25.0}, 
    
    # 2. Frio
    {'country': 'Germany',         'continent': 'Europe',         'base_temp': 9.0},   
    
    # 3. Temperado Frio
    {'country': 'USA',             'continent': 'North America',  'base_temp': 12.0},  
    
    # 4. Temperado Médio (Média da Ásia é puxada para baixo pela Rússia/China norte)
    {'country': 'China',           'continent': 'Asia',           'base_temp': 14.0},  
    
    # 5. Quente
    {'country': 'Australia',       'continent': 'Oceania',        'base_temp': 21.0},  
    
    # 6. Muito Quente
    {'country': 'Brazil',          'continent': 'South America',  'base_temp': 24.0},  
    
    # 7. O Mais Quente
    {'country': 'Nigeria',         'continent': 'Africa',         'base_temp': 26.0}   
]

data = []

print("Gerando dados calibrados: Antártida (Frio) -> África (Quente)...")

for config in countries_config:
    base_temp = config['base_temp']
    continent = config['continent']
    country = config['country']
    
    for year in years:
        # 1. Simulação de CO2 (Igual para todos - atmosfera global)
        progress = (year - 1950)
        co2 = 310 + (progress * 1.5) + (progress**2 * 0.015) + np.random.normal(0, 1)
        
        # 2. Temperatura (Base + Aquecimento Global)
        # Antártida aquece mais rápido (amplificação polar), outros normal
        warming_factor = 2.0 if continent == 'Antarctica' else 1.2
        warming_trend = (progress / 75) * warming_factor
        
        temp = base_temp + warming_trend + np.random.normal(0, 0.3)
        
        # 3. Nível do Mar
        sea_level = (progress * 3.5) + np.random.normal(0, 5)
        
        # 4. Risco
        risk_index = (co2/20) + (temp * 1.5) + (sea_level/10)
        
        data.append({
            'Year': year,
            'Country': country,
            'Continent': continent,
            'Avg_Temperature(°C)': round(temp, 2),
            'CO2_Emissions(Mt)': round(co2, 2),
            'Sea_Level_Rise(mm)': round(sea_level, 2),
            'Climate_Risk_Index': round(risk_index, 2)
        })

df = pd.DataFrame(data)

os.makedirs("data/raw", exist_ok=True)
output_path = "data/raw/Climate_Change_Real_Physics.csv"

df.to_csv(output_path, index=False)
print(f"✅ Sucesso! Arquivo gerado em: {output_path}")