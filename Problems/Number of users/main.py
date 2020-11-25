# write your code here
with open("users.json", "r") as f:
    print(len(json.load(f)["users"]))
