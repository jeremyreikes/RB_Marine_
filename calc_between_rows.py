from geopy.distance import geodesic

def dist_btw_ping(row, row_2):
    if row.id == row_2.id:
        return int(geodesic((row.latitude, row.longitude), (row_2.latitude, row_2.longitude)).miles)
    else:
        return 0

def time_btw_ping(row, row_2):
    if row.id == row_2.id:
        diff= row_2.datetime - row.datetime
        return abs(diff.total_seconds()) / 3600
    else:
        return 0

def lateral_distance(row, row_2):
    if row.id == row_2.id:
        return abs(row_2.latitude - row.latitude)
    else:
        return 0

def vertical_distance(row, row_2):
    if row.id == row_2.id:
        return abs(row_2.longitude - row.longitude)
    else:
        return 0
