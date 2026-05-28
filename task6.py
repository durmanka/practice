def merge_orders(web_orders, app_orders):
   result = []
   i = 0
   j = 0

   while i < len(web_orders) and j < len(app_orders):
       if web_orders[i]["time"] <= app_orders[j]["time"]:
           result.append(web_orders[i])
           i += 1
       else:
           result.append(app_orders[j])
           j += 1

   while i < len(web_orders):
       result.append(web_orders[i])
       i += 1

   while j < len(app_orders):
       result.append(app_orders[j])
       j += 1

   return result

web_orders = [
   {"id": "W1", "time": "09:00", "item": "Ноутбук"},
   {"id": "W2", "time": "10:30", "item": "Миша"},
   {"id": "W3", "time": "12:00", "item": "Монітор"},
   {"id": "W4", "time": "15:00", "item": "Клавіатура"},
]

app_orders = [
   {"id": "A1", "time": "08:45", "item": "Навушники"},
   {"id": "A2", "time": "10:30", "item": "Веб-камера"},
   {"id": "A3", "time": "13:20", "item": "Принтер"},
]

print("Замовлення з сайту:")
for o in web_orders:
   print(f"  [{o['time']}] {o['id']}: {o['item']}")

print("\nЗамовлення з додатку:")
for o in app_orders:
   print(f"  [{o['time']}] {o['id']}: {o['item']}")

merged = merge_orders(web_orders, app_orders)

print("\nОб'єднаний список:")
for place, o in enumerate(merged, start=1):
   print(f"  {place}. [{o['time']}] {o['id']}: {o['item']}")