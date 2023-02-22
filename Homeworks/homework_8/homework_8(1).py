import time

def decorate_timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Duration time of function '{func.__name__}'is {end_time - start_time} second.")
        return result
    return wrapper

@decorate_timer
def get_season(date_str):
    data = date_str.split('.')
    day = int(data[0])
    month = int(data[1])
    if month in [3, 4, 5]:
        season = 'Spring'
    elif month in [6, 7, 8]:
        season = 'Summer'
    elif month in [9, 10, 11]:
        season = 'Autumn'
    else:
        season = 'Winter'
    return season

date_str = '22.10'
season = get_season(date_str)
print(season)
