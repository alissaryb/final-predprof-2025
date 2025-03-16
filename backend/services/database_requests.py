from backend.database.models.map import Map
from backend.database.models.modules import Module
from backend.database.models.stations_types import StationType
from backend.database.models.stations import Station
from backend.database.db_session import create_session

from backend.tiles import get_field
from backend.src.api_requests import get_coords
from backend.algorithm import calc_pos


def update_map(matrix: list[list[int]], delete=True, map_id=0) -> None:
    """
    Удаляет старую карту (опционально) и создает новую в базе данных
    :param matrix: двумерный массив, состоящий из высот пикселей
    :param delete: ``True`` по умолчанию
    :param map_id: В базе данных может храниться несколько карт и их настройки. По умолчанию программа работает с картой типа 0.
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
    :param map_id: В базе данных может храниться несколько карт и их настройки. По умолчанию программа работает с картой типа 0.
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
    :param map_id: В базе данных может храниться несколько карт и их настройки. По умолчанию программа работает с картой типа 0.
    :return:
    """
    session = create_session()

    delete_modules(map_id=map_id)

    for module in [module1, module2]:
        new_module = Module(x=module[0], y=module[1], type=module[2], map_id=map_id)
        session.add(new_module)
    session.commit()
    session.close()


def delete_modules(map_id=0) -> None:
    """
    Удаляет старые модули
    :param map_id: В базе данных может храниться несколько карт и их настройки. По умолчанию программа работает с картой типа 0.
    :return:
    """
    session = create_session()

    modules = session.query(Module).where(Module.map_id == map_id).all()
    for i in modules:
        session.delete(i)
    session.commit()
    session.close()


def update_stations(stations: list[tuple[int, int, str]], delete=True, map_id=0) -> None:
    """
    Удаляет старые станции (опционально) и создает новые в базе данных
    :param stations: массив из кортежей (x, y, type), type = ``['cuper', 'engel']``
    :param delete: ``True`` по умолчанию
    :param map_id: В базе данных может храниться несколько карт и их настройки. По умолчанию программа работает с картой типа 0.
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
    :param map_id: В базе данных может храниться несколько карт и их настройки. По умолчанию программа работает с картой типа 0.
    :return:
    """
    session = create_session()

    old = session.query(Station).where(Station.map_id == map_id).all()
    for i in old:
        session.delete(i)
    session.commit()
    session.close()


def update_stations_types(stations_types: dict[str, tuple[float, int]], delete=True, map_id=0) -> None:
    """
    Удаляет старые типы станций (опционально) и создает новые в базе данных
    :param stations_types: словарь (ключ - type) из кортежей (cost, radius), type = ``['cuper', 'engel', ...]`` с информацией о станциях
    :param delete: ``True`` по умолчанию
    :param map_id: В базе данных может храниться несколько карт и их настройки. По умолчанию программа работает с картой типа 0.
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
    :param map_id: В базе данных может храниться несколько карт и их настройки. По умолчанию программа работает с картой типа 0.
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
    :param map_id: В базе данных может храниться несколько карт и их настройки. По умолчанию программа работает с картой типа 0.
    :return:
    """
    matrix = [[0] * 256] * 256

    session = create_session()
    map = session.query(Map).where(Map.map_id == map_id).all()
    for tile in map:
        matrix[tile.x][tile.y] = tile.value
    session.close()

    return matrix


def get_modules(map_id=0) -> dict[str, tuple[int, int]]:
    """
    Возвращает словарь (ключ - type) из кортежей (x, y), type = ``['sender', 'listener']`` с информацией о модулях
    :param map_id: В базе данных может храниться несколько карт и их настройки. По умолчанию программа работает с картой типа 0.
    :return:
    """
    res = {}

    session = create_session()
    modules = session.query(Module).where(Module.map_id == map_id).all()
    for module in modules:
        res[module.type] = (module.x, module.y)
    session.close()

    return res


def get_stations(map_id=0) -> list[tuple[int, int, str, float, int]]:
    """
    Возвращает массив из кортежей (x, y, type, cost, radius), type = ``['cuper', 'engel', ...]`` с информацией о станциях
    :param map_id: В базе данных может храниться несколько карт и их настройки. По умолчанию программа работает с картой типа 0.
    :return:
    """
    res = []

    session = create_session()
    stations = session.query(Station).where(Station.map_id == map_id).all()
    for station in stations:
        res.append((station.x, station.y, station.type, station.cost, station.radius))
    session.close()

    return res


def get_stations_types(map_id=0) -> dict[str, tuple[float, int]]:
    """
    Возвращает словарь (ключ - type) из кортежей (cost, radius), type = ``['cuper', 'engel', ...]`` с информацией о типах станций
    :param stations_types: словарь (ключ - type) из кортежей (cost, radius), type = ``['cuper', 'engel', ...]`` с информацией о станциях
    :param delete: ``True`` по умолчанию
    :param map_id: В базе данных может храниться несколько карт и их настройки. По умолчанию программа работает с картой типа 0.
    :return:
    """
    res = {}

    session = create_session()
    stations_types = session.query(StationType).where(StationType.map_id == map_id).all()
    for station_type in stations_types:
        res[station_type.type] = (station_type.cost, station_type.radius)
    session.close()

    return res


def get_custom_map(modules=False, stations=False, coverage=False, map_id=0) -> list[list[tuple[int, int]]]:
    res = get_map(map_id=map_id)
    matrix = [[(0, 0)] * 256] * 256
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = (0, res[i][j])

    if not modules and not stations:
        return matrix

    if modules:
        modules_data = get_modules(map_id=map_id)
        for key, value in modules_data.items():
            matrix[value[0]][value[1]] = (1, 0)

    if stations:
        stations_data = get_stations(map_id=map_id)
        for station in stations_data:
            matrix[station[0]][station[1]] = (2, station[4])

    if coverage:
        stations_data = get_stations(map_id=map_id)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j][0] == 0:
                    for station in stations_data:
                        dist = ((station[0] - i) ** 2 + (station[1] - j) ** 2) ** 0.5
                        if dist <= station[4]:
                            matrix[i][j] = (3, station[4])
                            break

    return matrix


def fill_database(map_id=0) -> None:
    full_matrix = get_field()
    data = get_coords()

    update_map(full_matrix, map_id=map_id)

    stations_types = {'cuper': (data['price']['cuper'], 32), 'engel': (data['price']['engel'], 64)}
    update_stations_types(stations_types, map_id=map_id)

    update_modules((*data['listener'], 'listener'),
                   (*data['sender'], 'sender'), map_id=map_id)

    stations = calc_pos(full_matrix, data['sender'][0], data['sender'][1], data['listener'][0], data['listener'][1],
                        32, data['price']['cuper'], 64, data['price']['engel'])
    res = []
    for station in stations:
        if station[2] == 0:
            res.append((station[0], station[1], 'cuper'))
        else:
            res.append((station[0], station[1], 'engel'))
    update_stations(res, map_id=map_id)
