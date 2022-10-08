import pandas as pd
from asset_returns_json import asset_returns_before_crisis_as_json, asset_returns_during_crisis_as_json


def data_frame_from_json(asset_returns, df_name):
    result = pd.DataFrame.from_dict(asset_returns)
    result.index = pd.to_datetime(result.index, unit='ms')

    csv_name = f'{df_name}.csv'
    result.to_csv(csv_name, index_label='Date')
    result = pd.read_csv(csv_name, parse_dates=['Date'], index_col='Date')
    return result


before_name = 'asset_returns_before_subprime_crisis'
asset_returns_before = data_frame_from_json(asset_returns_before_crisis_as_json, before_name)
print(f"\n{before_name}:\n")
print(asset_returns_before)

during_name = 'asset_returns_during_subprime_crisis'
asset_returns_during = data_frame_from_json(asset_returns_during_crisis_as_json, during_name)
print(f"\n{during_name}:\n")
print(asset_returns_during)
