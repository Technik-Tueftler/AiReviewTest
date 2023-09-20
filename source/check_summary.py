from datetime import datetime, timedelta

def check_matched_day(current_date: datetime, target_day: int) -> bool:
    last_day_of_current_month = last_day_of_month(current_date)
    if target_day > last_day_of_current_month.day:
        if current_date.day == last_day_of_current_month.day:
            return True
    else:
        if current_date.day == target_day:
            return True
    return False


def last_day_of_month(date) -> datetime:
    if date.month == 12:
        return date.replace(day=31)
    return date.replace(month=date.month + 1, day=1) - timedelta(days=1)

def main() -> None:
    last_day_of_current_month = last_day_of_month(datetime.utcnow())
    print(last_day_of_current_month)



if __name__ == "__main__":
    main()