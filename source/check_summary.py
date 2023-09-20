from datetime import datetime, timedelta

def last_day_of_month(date) -> datetime:
    if date.month == 12:
        return date.replace(day=31)
    return date.replace(month=date.month + 1, day=1) - timedelta(days=1)

def main() -> None:
    last_day_of_current_month = last_day_of_month(datetime.utcnow())
    print(last_day_of_current_month)


if __name__ == "__main__":
    main()