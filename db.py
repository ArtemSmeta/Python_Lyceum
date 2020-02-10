def load_db():
    """Загрузить данные.

    Результат: list of dict.

    Сложность: O(1).
    """
    db = [
        {
            "name": "Иванов Иван",
            "birthday": "01/12/2000",
            "height": 170,
            "weight": 70.5,
            "car": True,
            "languages": ["C++", "Python"]
        },
        {
            "name": "Сергеев Сергей",
            "birthday": "01/06/2001",
            "height": 180,
            "weight": 110.4,
            "car": False,
            "languages": ["Pascal", "Delphi"]
        },
        {
            "name": "Николаева Мария",
            "birthday": "14/07/1998",
            "height": 175,
            "weight": 56.9,
            "car": True,
            "languages": ["C#", "C++", "C"]
        },
        {
            "name": "Прудникова Дарья",
            "birthday": "21/11/1994",
            "height": 168,
            "weight": 60.5,
            "car": True,
            "languages": ["C++", "C#", "Python"]
        },
        {
            "name": "Петров Михаил",
            "birthday": "01/06/2001",
            "height": 153,
            "weight": 111.4,
            "car": False,
            "languages": ["Pascal", "Python"]
        },
        {
            "name": "Сидорова Екатерина",
            "birthday": "14/07/1998",
            "height": 190,
            "weight": 75.9,
            "car": True,
            "languages": ["C#", "C"]
        },
        {
            "name": "Пасхалов Петр",
            "birthday": "01/12/1997",
            "height": 160,
            "weight": 72.5,
            "car": True,
            "languages": ["C++", "Python"]
        },
        {
            "name": "Москвин Илья",
            "birthday": "01/06/2003",
            "height": 162,
            "weight": 100.4,
            "car": False,
            "languages": ["Pascal", "Delphi"]
        },
        {
            "name": "Ненашева Ульяна",
            "birthday": "14/07/1988",
            "height": 159,
            "weight": 68.9,
            "car": True,
            "languages": ["C#", "C++", "C"]
        }
    ]

    return db
