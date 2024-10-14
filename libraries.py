from datetime import datetime, timedelta, timezone

# Using the library pendulum
import pendulum

print("Portuguese time", datetime.now())
print("German time", datetime.now(timezone(timedelta(hours=2))))


print("Portuguese time", pendulum.now("Europe/Lisbon"))
print("German time", pendulum.now("Europe/Berlin"))
print("Sao Paulo time", pendulum.now("America/Sao_Paulo"))
