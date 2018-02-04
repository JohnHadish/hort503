Area = ["Bob", "Chris"]
inventory = []
def take(area):
    print("These objects are present", area)
    print("Which item do you want to take?")
    x = input
    if x in area:
        inventory.append(x)
        area.remove(x)
        return
    else:
        print("That item is not present")
        return



take(Area)
