from datetime import datetime, timedelta, timezone

print("Portuguese time", datetime.now())
print("German time", datetime.now(timezone(timedelta(hours=2))))
