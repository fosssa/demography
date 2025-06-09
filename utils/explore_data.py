def explore_data(data) -> None:
    # Исследование структуры очищенных данных
    print("📊 ИССЛЕДОВАНИЕ ДАННЫХ")
    print("=" * 50)

    # Основная информация о наборе данных
    print("\n📈 Обзор набора данных:")
    print(f"   Строки: {len(data):,}")
    print(f"   Столбцы: {len(data.columns)}")

    year_columns = [col for col in data.columns if col.isdigit() and len(col) == 4]
    print(f"\n📅 Найдено столбцов с годами: {len(year_columns)}")
    print(f"   Диапазон: {min(year_columns) if year_columns else 'Нет'} - {max(year_columns) if year_columns else 'Нет'}")

    # Проверить пропущенные данные
    missing_data = data.isnull().sum()
    if missing_data.sum() > 0:
        print("\n❌ Пропущенные данные:")
        for col, missing_count in missing_data[missing_data > 0].items():
            missing_pct = (missing_count / len(data)) * 100
            print(f"   {col}: {missing_count:,} ({missing_pct:.1f}%)")
    else:
        print("\n✅ Пропущенные данные не найдены")

    # Показать уникальные значения в категориальных столбцах
    # Определить категориальные столбцы (все, кроме столбцов в формате YYYY)
    categorical_cols = [col for col in data.columns if not (col.isdigit() and len(col) == 4)]
    print("\n📊 Уникальные значения в ключевых столбцах:")
    for col in categorical_cols:
        if col in data.columns:
            unique_count = data[col].nunique()
            print(f"   {col}: {unique_count} уникальных значений")
            if unique_count <= 10:
                print(f"      Значения: {list(data[col].unique())}")
            else:
                print(f"      Образец: {list(data[col].unique()[:5])}...")
