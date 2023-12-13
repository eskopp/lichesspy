""""
 File: api.py
 Package: lichesspy
 Author: ESkopp
 Created: 12/01/2021
 Modified: 03/12/2023
 Version: 6.0.0
"""

import re


def parse_pgn(pgn_string):
    """Parse a PGN string and return a list of games as dictionaries."""
    games = []
    pgn_blocks = _extract_pgn_blocks(pgn_string)
    for pgn_block in pgn_blocks:
        game = _parse_pgn_block(pgn_block)
        games.append(game)
    return games


def _extract_pgn_blocks(pgn_string):
    """Extract PGN blocks from a PGN string."""
    pgn_blocks = re.split(r"\s*\n\n", pgn_string)
    pgn_blocks = [block.strip() for block in pgn_blocks if block.strip()]
    return pgn_blocks


def _parse_pgn_block(pgn_block):
    """Parse a PGN block and return a game as a dictionary."    ""
    game = {}
    tags, moves = pgn_block.split("\n\n", maxsplit=1)
    game["tags"] = _parse_pgn_tags(tags)
    game["moves"] = _parse_pgn_moves(moves)
    return game


def _parse_pgn_tags(tags_string):
    """Parse PGN tags and return a dictionary of tag name-value pairs."""
    tags = {}
    tag_lines = tags_string.split("\n")
    for tag_line in tag_lines:
        if tag_line.strip():
            name, value = tag_line.strip().split(maxsplit=1)
            name = name.strip('["]')
            value = value.strip('["]')
            tags[name] = value
    return tags


def _parse_pgn_moves(moves_string):
    """Parse PGN moves and return a list of moves."""
    moves = moves_string.split()
    return moves
