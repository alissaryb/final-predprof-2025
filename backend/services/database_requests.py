from backend.database.models.map import Map
from backend.database.models.modules import Module
from backend.database.models.stations_types import StationType
from backend.database.models.stations import Station
from backend.database.db_session import create_session


def update_map(matrix: list[list[int]], delete=True, map_id=0) -> None:
    """
    Удаляет старую карту (опционально) и создает новую в базе данных
    :param matrix: двумерный массив, состоящий из высот пикселей
    :param delete: ``True`` по умолчанию
    :return:
    """
    session = create_session()

    if delete:
        delete_map(map_id=map_id)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_tile = Map(x=i, y=j, value=matrix[i][j], map_id=map_id)
            session.add(new_tile)
    session.commit()
    session.close()


def delete_map(map_id=0) -> None:
    """
    Удаляет старую карту
    :return:
    """
    session = create_session()

    map = session.query(Map).where(Map.map_id == map_id).all()
    for i in map:
        session.delete(i)
    session.commit()
    session.close()


def update_modules(module1: (int, int, str), module2: (int, int, str), map_id=0) -> None:
    """
    Удаляет старые модули и создает новые в базе данных
    :param module1: кортеж (x, y, type), type = ``['sender', 'listener']``
    :param module2: кортеж (x, y, type), type = ``['sender', 'listener']``
    :return:
    """
    session = create_session()

    modules = session.query(Module).where(Module.map_id == map_id).all()
    for i in modules:
        session.delete(i)
    session.commit()

    for module in [module1, module2]:
        new_module = Module(x=module[0], y=module[1], type=module[2], map_id=map_id)
        session.add(new_module)
    session.commit()
    session.close()


def update_stations(stations: list[tuple[int, int, str]], delete=True, map_id=0) -> None:
    """
    Удаляет старые станции (опционально) и создает новые в базе данных
    :param stations: массив из кортежей (x, y, type), type = ``['cuper', 'engel']``
    :param delete: ``True`` по умолчанию
    :return:
    """
    session = create_session()

    if delete:
        delete_stations(map_id=map_id)

    types = {}
    for type_ in session.query(StationType).where(StationType.map_id == map_id).all():
        types[type_.type] = (type_.cost, type_.radius)

    for station in stations:
        new_station = Station(x=station[0], y=station[1], type=station[2],
                              cost=types[station[2]][0], radius=types[station[2]][1], map_id=map_id)
        session.add(new_station)
    session.commit()
    session.close()


def delete_stations(map_id=0) -> None:
    """
    Удаляет старые станции
    :return:
    """
    session = create_session()

    old = session.query(Station).where(Station.map_id == map_id).all()
    for i in old:
        session.delete(i)
    session.commit()
    session.close()


def update_stations_types(stations_types: dict[str, tuple[int, int]], delete=True, map_id=0) -> None:
    """
    Удаляет старые типы станций (опционально) и создает новые в базе данных
    :param stations_types: словарь (ключ - type) из кортежей (cost, radius), type = ``['cuper', 'egnel', ...]`` с информацией о станциях
    :param delete: ``True`` по умолчанию
    :return:
    """
    session = create_session()

    if delete:
        delete_stations_types(map_id=map_id)

    for key, value in stations_types.items():
        new_type = StationType(type=key, cost=value[0], radius=value[1], map_id=map_id)
        session.add(new_type)
    session.commit()
    session.close()


def delete_stations_types(map_id=0) -> None:
    """
    Удаляет старые типы станций
    :return:
    """
    session = create_session()

    old = session.query(StationType).where(StationType.map_id == map_id).all()
    for i in old:
        session.delete(i)
    session.commit()
    session.close()


def get_map(map_id=0) -> list[list[int]]:
    """
    Возвращает карту с высотами
    :return:
    """
    matrix = [[0] * 16] * 16

    session = create_session()
    map = session.query(Map).where(Map.map_id == map_id).all()
    for tile in map:
        matrix[tile.x][tile.y] = tile.value
    session.close()

    return matrix


def get_modules(map_id=0) -> dict[str, tuple[int, int]]:
    """
    Возвращает словарь (ключ - type) из кортежей (x, y), type = ``['sender', 'listener']`` с информацией о модулях
    :return:
    """
    res = {}

    session = create_session()
    modules = session.query(Module).where(Module.map_id == map_id).all()
    for module in modules:
        res[module.type] = (module.x, module.y)
    session.close()

    return res


def get_stations(map_id=0) -> dict[str, tuple[int, int, str, int, int]]:
    """
    Возвращает массив из кортежей (x, y, type, cost, radius), type = ``['cuper', 'egnel', ...]`` с информацией о станциях
    :return:
    """
    res = []

    session = create_session()
    stations = session.query(Station).where(Station.map_id == map_id).all()
    for station in stations:
        res.append((station.x, station.y, station.type, station.cost, station.radius))
    session.close()

    return res


def get_stations_types(map_id=0) -> dict[str, tuple[int, int]]:
    """
    Возвращает словарь (ключ - type) из кортежей (cost, radius), type = ``['cuper', 'egnel', ...]`` с информацией о типах станций
    :param stations_types: словарь (ключ - type) из кортежей (cost, radius), type = ``['cuper', 'egnel', ...]`` с информацией о станциях
    :param delete: ``True`` по умолчанию
    :return:
    """
    res = {}

    session = create_session()
    stations_types = session.query(StationType).where(StationType.map_id == map_id).all()
    for station_type in stations_types:
        res[station_type.type] = (station_type.cost, station_type.radius)
    session.close()

    return res
