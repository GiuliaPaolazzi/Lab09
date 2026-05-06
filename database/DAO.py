from database.DB_connect import DBConnect
from model.airport import Airports


class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getAllAirports():
        conn = DBConnect.get_connection()
        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM airports"
        cursor.execute(query)

        for row in cursor:
            result.append(Airports(**row))
        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getAllEdgesPesati(x):
        conn = DBConnect.get_connection()
        result = []

        cursor = conn.cursor(dictionary=True)
        query = ("""SELECT LEAST(ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID) AS id1,
         GREATEST( ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID) AS id2, AVG(DISTANCE) AS peso
         FROM flights
         GROUP BY id1,id2
         HAVING peso> %s"""
                 )
        cursor.execute(query)

        for row in cursor:
            result.append((row["id1"],row["id2"],row["peso"]))
        cursor.close()
        conn.close()
        return result


