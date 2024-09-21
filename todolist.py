tasks = []
while True:
    task = input("what is a task for today? If none type 'none' ").strip()
    if task == "none":
        break
    tasks.append(task)
combine = []
for _ in tasks:
    print("when should this task be started? ")
    time = input(f"{_} ")
    combined = time + " " + _
    combine.append(combined)

with open("list.txt","a") as file:
    for _ in combine:
        file.write(f"{_}\n")




