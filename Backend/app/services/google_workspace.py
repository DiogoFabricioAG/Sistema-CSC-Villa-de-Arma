def obtener_datos(spreadsheet_id, sheet_name):
    import pandas as pd
    sheet_name_url_encoded = sheet_name.replace(" ", "%20")
    url = f'https://docs.google.com/spreadsheets/d/{spreadsheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name_url_encoded}'
    df = pd.read_csv(url)
    return df.to_dict(orient='records')

# print(obtener_datos('1zHliU1yGnbmIIG0PcJBeKqr0kPH6FbvMaiASBdeuKUI', 'QuejasOpinionesCSCVilladeArma'))
