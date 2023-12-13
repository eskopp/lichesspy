""""
 File: api.py
 Package: lichesspy
 Author: ESkopp
 Created: 12/01/2021
 Modified: 03/12/2023
 Version: 6.0.0
"""


def users_by_ids(ids, **kwargs):
    """Wrapper for the `POST /api/users <https://github.com/ornicar/lila#post-apiusers-fetch-many-users-by-id>`_ endpoint.
    Returns a generator that splits the IDs into multiple requests as needed.

    Note: Use :data:`~lichesspy.api.users_status` when possible, since it is cheaper and not rate-limited.

    >>> users = lichesspy.api.users_by_ids(['thibault', 'cyanfish'])
    >>> ratings = [u.get('perfs', {}).get('blitz', {}).get('rating') for u in users]
    >>> print(ratings)
    [1617, 1948]
    """
    return _batch(users_by_ids_page, [ids], kwargs, 300)


def users_by_ids_page(ids, **kwargs):
    """Wrapper for the `POST /api/users <https://github.com/ornicar/lila#post-apiusers-fetch-many-users-by-id>`_ endpoint.
    Use :data:`~lichesspy.api.users_by_ids` to avoid manual pagination.
    """
    return _api_post("/api/users", kwargs, ",".join(ids))


def users_status(ids, **kwargs):
    """Wrapper for the `GET /api/users/status <https://github.com/ornicar/lila#get-apiusersstatus-fetch-many-users-online-and-playing-flags>`_ endpoint.
    Returns a generator that makes requests for additional pages as needed.

    Note: This endpoint is cheap and not rate-limited. Use it instead of :data:`~lichesspy.api.users_by_ids` when possible.

    >>> users = lichesspy.api.users_status(['thibault', 'cyanfish'])
    >>> online_count = len([u for u in users if u.get('online')])
    >>> print(online_count)
    1
    """
    return _batch(users_status_page, [ids], kwargs, 40)


def users_status_page(ids, **kwargs):
    """Wrapper for the `GET /api/users/status <https://github.com/ornicar/lila#get-apiusersstatus-fetch-many-users-online-and-playing-flags>`_ endpoint.
    Use :data:`~lichesspy.api.users_status` to avoid manual pagination.
    """
    kwargs["ids"] = ",".join(ids)
    return _api_get("/api/users/status", kwargs)


def user_activity(username, **kwargs):
    """Wrapper for the `GET /api/user/<username>/activity <https://github.com/ornicar/lila#get-apiuserusernameactivity-fetch-recent-user-activity>`_ endpoint."""
    return _api_get("/api/user/{}/activity".format(username), kwargs)


def game(game_id, **kwargs):
    """Wrapper for the `GET /api/game/{id} <https://github.com/ornicar/lila#get-apigameid-fetch-one-game-by-id>`_ endpoint.

    By default, returns a dict representing a JSON game object.
    Use `format=PGN` for a PGN string or `format=PYCHESS` for a `python-chess <https://github.com/niklasf/python-chess>`_ game object.

    >>> game = lichesspy.api.game('Qa7FJNk2')
    >>> print(game['moves'])
    e4 e5 Nf3 Nc6 Bc4 Qf6 d3 h6 ...

    >>> from lichesspy.format import PGN, PYCHESS
    >>> pgn = lichesspy.api.game('Qa7FJNk2', format=PGN)
    >>> print(pgn)
    [Event "Casual rapid game"]
    ...

    >>> game_obj = lichesspy.api.game('Qa7FJNk2', format=PYCHESS)
    >>> print(game_obj.end().board())
    ...
    """
    return _api_get(
        "/game/export/{}".format(game_id),
        kwargs,
        object_type=lichesspy.format.GAME_OBJECT,
    )


def games_by_ids(ids, **kwargs):
    """Wrapper for the `POST /games/export/_ids <https://github.com/ornicar/lila#post-apigames-fetch-many-games-by-id>`_ endpoint.
    Returns a generator that splits the IDs into multiple requests as needed."""
    return _batch(games_by_ids_page, [ids], kwargs, 300)


def games_by_ids_page(ids, **kwargs):
    """Wrapper for the `POST /games/export/_ids <https://github.com/ornicar/lila#post-apigames-fetch-many-games-by-id>`_ endpoint.
    Use :data:`~lichesspy.api.games_by_ids` to avoid manual pagination.
    """
    return _api_post(
        "/games/export/_ids",
        kwargs,
        ",".join(ids),
        object_type=lichesspy.format.GAME_STREAM_OBJECT,
    )


def user_games(username, **kwargs):
    """Wrapper for the `GET /api/user/<username>/games <https://github.com/ornicar/lila#get-apiuserusernamegames-fetch-user-games>`_ endpoint.

    By default, returns a generator that streams game objects.
    Use `format=PGN` for a generator of game PGNs, `format=SINGLE_PGN` for a single PGN string, or `format=PYCHESS` for a generator of `python-chess <https://github.com/niklasf/python-chess>`_ game objects.

    >>> games = lichesspy.api.user_games('cyanfish', max=50, perfType='blitz')
    >>> print(next(games)['moves'])
    e4 e5 Nf3 Nc6 Bc4 Qf6 d3 h6 ...

    >>> from lichesspy.format import PGN, SINGLE_PGN, PYCHESS
    >>> pgns = lichesspy.api.user_games('cyanfish', max=50, format=PGN)
    >>> print(next(pgns))
    [Event "Casual rapid game"]
    ...

    >>> pgn = lichesspy.api.user_games('cyanfish', max=50, format=SINGLE_PGN)
    >>> print(pgn)
    [Event "Casual rapid game"]
    ...

    >>> game_objs = lichesspy.api.user_games('cyanfish', max=50, format=PYCHESS)
    >>> print(next(game_objs).end().board())
    ...
    """
    return _api_get(
        "/api/user/{}/games".format(username),
        kwargs,
        object_type=lichesspy.format.GAME_STREAM_OBJECT,
    )


def team_members(team, **kwargs):
    """Wrapper for the `GET /api/team/{name}/users <https://github.com/ornicar/lila#get-apiteamnamefetch-all-members-of-a-team>`_ endpoint.
    Returns a generator that streams user objects.

    >>> members = lichesspy.api.team_members('coders')
    >>> ratings = [m.get('perfs', {}).get('blitz', {}).get('rating') for m in members]
    >>> print(ratings)
    [1349, 1609, ...]
    """
    return _api_get(
        "/api/team/{}/users".format(team),
        kwargs,
        object_type=lichesspy.format.USER_STREAM_OBJECT,
    )
