def obtener_asambleas(spreadsheet_id, sheet_name):
    import pandas as pd
    sheet_name_url_encoded = sheet_name.replace(" ", "%20")
    url = f'https://docs.google.com/spreadsheets/d/{spreadsheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name_url_encoded}'
    df = pd.read_csv(url)
    return df.to_dict(orient='records')

# print(obtener_asambleas('1VKPnJ7fapW2FFVe4rHaoB26HOgzJhDsAgqLNNLcrrGo', 'Cargar Asambleas (respuestas)')[0]["Fecha Asamblea"])

# Este tendria que ir en util

def get_image_id(image):
    # https://drive.google.com/open?id=1guQofGXvcprpJ2kW8QoqeABicAKu1iks
    return image.split("=")[1]

# print(get_image_id('https://drive.google.com/open?id=1guQofGXvcprpJ2kW8QoqeABicAKu1iks')) # 1guQofGXvcprpJ2kW8QoqeABicAKu1iks

def give_format(date):
    y,m,d = date.split("-")

    return f"{d}/{m}/{y}"
print(give_format("2023-10-01")) # 01/10/2023