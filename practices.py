import pandas as pd
import numpy as np


def generate_retail_orders(n_orders=100, seed=42):
    np.random.seed(seed)
    timestamps = pd.date_range(start="2025-07-29 09:30", periods=n_orders, freq="1min")
    directions = np.random.choice(["buy", "sell"], size=n_orders)
    quantities = np.random.choice([50, 100, 150], size=n_orders, p=[0.2, 0.3, 0.5])
    types = np.random.choice(["market", "limit"], size=n_orders, p=[0.7, 0.3])
    prices = np.where(types == "limit", np.round(np.random.normal(100, 2, n_orders), 2), None)

    table = pd.DataFrame({
        "timestamps" : timestamps,
        "direction" : directions,
        "quantities" : quantities,
        "types" : types,
        "prices" : prices
    })
    print(table)
    return table
generate_retail_orders()
