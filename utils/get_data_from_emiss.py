from io import BytesIO
import requests
import pandas as pd


def get_data_from_emiss(indicator: str, payload: dict, timeout=30) -> pd.DataFrame | None:

    """Получение данных по указанному индикатору."""

    URL = "https://www.fedstat.ru/indicator/data.do"
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0) Gecko/20100101 Firefox/139.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Priority': 'u=0'
    }

    try:
        response = requests.post(
            url=f"{URL}?id={indicator}",
            headers=HEADERS,
            data=payload,
            timeout=timeout
        )

        response.raise_for_status()
        
        excel_bytes = BytesIO(response.content)
        excel_df = pd.read_excel(excel_bytes, engine='xlrd')

        return excel_df

    except requests.Timeout:
        print(f"⏰ Запрос превысил время ожидания {timeout} секунд.")
    except Exception as e:
        print(f"🚨 Произошла ошибка: {e}")

    return None
