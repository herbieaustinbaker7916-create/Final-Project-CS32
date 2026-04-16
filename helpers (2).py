def findfood():
    """
    calls a function that requires user input. no input to actual function.
    user inputs rough food item, gets given available options and then chooses
    an available item
    function returns the description of the item from FOoddata.
    """

    import json

    with open('Fooddata.json', 'r') as file:
        fooddata = json.load(file)
    #open dictionary in file
    foods = fooddata["FoundationFoods"]

    #request rough item
    search_term = input("what food are you searching for: ").lower()

    options = []

    #search file for all descriptions that contain rough item, put into a list
    for food in foods:
        if search_term in food["description"].lower():
            options.append(food["description"])
    for i in options:
        print(i)
    #get user to choose the exact description of the item
    while True:
        Act_item = input("Select one of the above: ")
        if Act_item in options:
            break
        else:
            print("Please select a listed item")
            for i in options:
                print(i)

    #when function can change to return exact description
    return(Act_item)


def main():
    test = findfood()

    print(test)

if __name__ == '__main__':
    main()
