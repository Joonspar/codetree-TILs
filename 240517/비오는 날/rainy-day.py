class Data:
    def __init__(self, date, day, whether):
        self.date = date
        self.day = day
        self.whether = whether

forecast = []
n = int(input())
for _ in range(n):
    x, y, z = input().split()
    forecast.append(Data(x, y, z))

recent = 99999999
idx = -1
for i in range(n):
    new = forecast[i].date.split("-")
    new = "".join(new)
    new = int(new)
    if forecast[i].whether == "Rain" and new < recent: 
        recent = new
        idx = i
        

print(f"{forecast[idx].date} {forecast[idx].day} {forecast[idx].whether}")