import datetime


now = datetime.datetime.now()

start_date = input("Enter the start date: ")
end_date = input("Enter the end date: ")

def validate_start_date(start_date) -> str:
    '''
    func have to check start_date and it
    arg: str
    return: str
    '''
    try:
        datetime.datetime.strptime(start_date, '%Y-%m-%d')
        return start_date
    except ValueError:
        start_date = now.strftime('%Y-%m-%d')
        return start_date


def get_result(end_date) -> tuple:
    '''
    func have to check end_date and return new_start_date1 and end_date
    arg: str
    return: tuple
    '''

    new_start_date = validate_start_date(start_date)
    try:
        datetime.datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        end_date = now.strftime('%Y-%m-%d')

    # если дата старта == сегодня, то программе не нужна дата конца
    # ибо данные будут браться за сегодняшний день
    if new_start_date == now.strftime('%Y-%m-%d'):
        end_date = new_start_date
        return new_start_date, end_date
    
    else: return end_date, new_start_date

date = get_result(end_date)

