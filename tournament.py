#!/usr/bin/env python
# tournament.py -- implementation of a Swiss-system tournament

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("DELETE FROM Matches;")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("DELETE FROM Players;")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    c.execute("SELECT COUNT(*) FROM Players;")
    for row in c:
        return row[0]
    db.commit()
    db.close()


def registerPlayer(name):
    """Adds a player to the tournament database.
      The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
      Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    c = db.cursor()
    c.execute("INSERT INTO players (name) values (%s)", (name, ))
    db.commit()
    db.close()


def playerStandings():
    """Select all from the player standings view that shows a table
of player id, name, wins(in descending order),
and matches played
    """
    db = connect()
    c = db.cursor()
    c.execute("SELECT * FROM playerStandings;")
    rows = c.fetchall()
    db.close()
    return rows
    db.commit()
    db.close()


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    c = db.cursor()
    c.execute("INSERT INTO Matches(winner, loser) VALUES (%s,%s)",
              (winner, loser, ))
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of tuples, each of which contains
      (id1, name1, id2, name2)Id1: the first player's unique id
       name1: the player's name
      id2: the second player's unique id
      name2: the second player's name
    """
    """
    For loops are traditionally used when you have a piece of
     code which you want to repeat a number of times.
     turorials http://www.dotnetperls.com/list-python
     """
    db = connect()
    c = db.cursor()
    pairings = []
    c.execute("SELECT * FROM playerstandings")
    players = c.fetchall()
# Iterate over each of the players and pair them
    for i in range(0, len(players) - 1, 2):
        pairing = (players[i][0], players[i][1],
                   players[i+1][0], players[i+1][1])
# add another element to te end of the list at the end of the loop 
        pairings.append(pairing)
        return pairings
