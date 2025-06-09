from scipy import stats
from pandas import Series, DataFrame


def calculate_descriptive_statistics(data: Series, type: str) -> dict:

    """Расчет основных статистических показателей"""

    stats_dict = {
        'Тип агрегации': type,
        'Среднее': data.mean(),
        'Медиана': data.median(),
        'Стандартное отклонение': data.std(),
        'Минимум': data.min(),
        'Максимум': data.max(),
        'Размах': data.max() - data.min(),
        'Асимметрия': stats.skew(data),
        'Эксцесс': stats.kurtosis(data),
        'Количество наблюдений': len(data)
    }
    
    return stats_dict


def get_largest_variance(data: DataFrame, n: int = 3) -> list[str]:

    """Получение словаря с наибольшей дисперсией"""

    high_variability = data.nlargest(n, 'Стандартное отклонение')

    res = []
    for idx, row in high_variability.iterrows():
        res.append(f"{row['Тип агрегации']}: σ = {row['Стандартное отклонение']}")

    return res


def get_largest_skewness(data: DataFrame, n: int = 3) -> list[str]:

    """Получение словаря с наибольшей асимметрией"""

    high_skewness = data.nlargest(n, 'Асимметрия')

    res = []
    for idx, row in high_skewness.iterrows():
        skew_desc = "положительная" if row['Асимметрия'] > 0 else "отрицательная"
        res.append(f"{row['Тип агрегации']}: Асимметрия = {row['Асимметрия']} ({skew_desc})")

    return res


def get_largest_kurtosis(data: DataFrame, n: int = 3) -> list[str]:

    """Получение словаря с наибольшим эксцессом"""

    high_kurtosis = data.nlargest(n, 'Эксцесс')

    res = []
    for idx, row in high_kurtosis.iterrows():
        kurt_val = row['Эксцесс']
        kurt_desc = "островершинное" if kurt_val > 0 else "плосковершинное"
        res.append(f"{row['Тип агрегации']}: Эксцесс = {row['Эксцесс']} ({kurt_desc})")

    return res