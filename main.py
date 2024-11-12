def get_user_choice(question, options):
    while True:
        print(f"\n{question}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        try:
            choice = int(input("Выберите номер из предложенных: "))
            if 1 <= choice <= len(options):
                return choice
            print("Пожалуйста, выберите существующий вариант.")
        except ValueError:
            print("Пожалуйста, введите число.")

def get_movies_database():
    return {
        ('action', 'violent', 'modern', 'long', 'theatrical'): "Джон Уик",
        ('action', 'violent', 'modern', 'short', 'streaming'): "Красное уведомление",
        ('action', 'nonviolent', 'classic', 'long', 'theatrical'): "Миссия невыполнима",
        ('action', 'nonviolent', 'modern', 'short', 'streaming'): "Серый человек",

        ('drama', 'dark', 'modern', 'long', 'theatrical'): "Джокер",
        ('drama', 'dark', 'classic', 'long', 'theatrical'): "Бойцовский клуб",
        ('drama', 'light', 'modern', 'short', 'streaming'): "Король Ричард",
        ('drama', 'light', 'classic', 'long', 'theatrical'): "Форрест Гамп",

        ('comedy', 'dark', 'modern', 'long', 'theatrical'): "Однажды в Голливуде",
        ('comedy', 'dark', 'classic', 'short', 'streaming'): "Большой Лебовски",
        ('comedy', 'light', 'modern', 'short', 'streaming'): "Круэлла",
        ('comedy', 'light', 'classic', 'long', 'theatrical'): "Маска",

        ('scifi', 'complex', 'modern', 'long', 'theatrical'): "Начало",
        ('scifi', 'complex', 'classic', 'long', 'theatrical'): "Матрица",
        ('scifi', 'simple', 'modern', 'short', 'streaming'): "Проект Адам",
        ('scifi', 'simple', 'classic', 'short', 'streaming'): "Назад в будущее",

        ('horror', 'gore', 'modern', 'long', 'theatrical'): "Пила",
        ('horror', 'gore', 'classic', 'short', 'streaming'): "Зловещие мертвецы",
        ('horror', 'psychological', 'modern', 'long', 'theatrical'): "Реинкарнация",
        ('horror', 'psychological', 'classic', 'short', 'streaming'): "Сияние",

        ('thriller', 'mystery', 'modern', 'long', 'theatrical'): "Исчезнувшая",
        ('thriller', 'mystery', 'classic', 'short', 'streaming'): "Молчание ягнят",
        ('thriller', 'crime', 'modern', 'long', 'theatrical'): "Не время умирать",
        ('thriller', 'crime', 'classic', 'short', 'streaming'): "Семь",

        ('fantasy', 'epic', 'modern', 'long', 'theatrical'): "Властелин колец",
        ('fantasy', 'epic', 'classic', 'short', 'streaming'): "Лабиринт",
        ('fantasy', 'urban', 'modern', 'long', 'theatrical'): "Доктор Стрэндж",
        ('fantasy', 'urban', 'classic', 'short', 'streaming'): "Битлджус",

        ('romance', 'drama', 'modern', 'long', 'theatrical'): "Сентябрьские дожди",
        ('romance', 'drama', 'classic', 'short', 'streaming'): "Вторая весна",
        ('romance', 'comedy', 'modern', 'long', 'theatrical'): "Любовь под прикрытием",
        ('romance', 'comedy', 'classic', 'short', 'streaming'): "Невеста из интернета"
    }

def get_subgenre_options(genre):
    options = {
        'action': (["Жестокий экшен", "Лёгкий экшен"], ['violent', 'nonviolent']),
        'drama': (["Мрачная", "Легкая"], ['dark', 'light']),
        'comedy': (["Чёрный юмор", "Обычный юмор"], ['dark', 'light']),
        'scifi': (["Замысловатые", "Лёгкие"], ['complex', 'simple']),
        'horror': (["Сплэттер (кровь, реалистичность)", "Психологический"], ['gore', 'psychological']),
        'thriller': (["Детектив", "Криминал"], ['mystery', 'crime']),
        'fantasy': (["Эпическое фэнтези", "Городское фэнтези"], ['epic', 'urban']),
        'romance': (["Драма", "Комедия"], ['drama', 'comedy'])
    }
    return options.get(genre)

def recommend():
    movies = get_movies_database()
    preferences = []

    genre_options = ["Боевик", "Драма", "Комедия", "Фантастика", "Ужасы", "Триллер", "Фэнтези", "Романтика"]
    genre_map = ['action', 'drama', 'comedy', 'scifi', 'horror', 'thriller', 'fantasy', 'romance']
    genre_choice = get_user_choice("Какой жанр вас интересует?", genre_options)
    selected_genre = genre_map[genre_choice - 1]
    preferences.append(selected_genre)

    subgenre_options, subgenre_map = get_subgenre_options(selected_genre)
    subgenre_choice = get_user_choice("Уточните поджанр:", subgenre_options)
    preferences.append(subgenre_map[subgenre_choice - 1])

    era_options = ["Современное кино (после 2000)", "Классика (до 2000)"]
    era_choice = get_user_choice("Какое время выхода фильма предпочитаете?", era_options)
    preferences.append('modern' if era_choice == 1 else 'classic')

    length_options = ["Длинный (более 2 часов)", "Короткий (менее 2 часов)"]
    length_choice = get_user_choice("Какую длительность фильма предпочитаете?", length_options)
    preferences.append('long' if length_choice == 1 else 'short')

    release_options = ["Кинотеатральный релиз", "Стриминговый релиз"]
    release_choice = get_user_choice("Какой формат выпуска предпочитаете?", release_options)
    preferences.append('theatrical' if release_choice == 1 else 'streaming')

    preferences_tuple = tuple(preferences)
    if preferences_tuple in movies:
        return movies[preferences_tuple]

    best_match = max(movies.keys(),
                     key=lambda k: sum(a == b for a, b in zip(k, preferences_tuple)))
    return movies[best_match]

def main():
    print("Система подбора фильмов")
    recommendation = recommend()
    print(f"\nНа основе ваших предпочтений рекомендуем фильм: {recommendation}")

if __name__ == "__main__":
    main()
