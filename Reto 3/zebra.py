def zebra(arr: list) -> tuple:

    highest_count = 0
    final_color = ''

    last_color = ''
    next_color = arr[0]
    counter = 1


    for color in arr:

        if (color != next_color or last_color == color):
            counter = 1
        
        counter += 1
        next_color = last_color
        last_color = color

        if counter > highest_count:
            highest_count = counter
            final_color = last_color

    return [highest_count, final_color]

print(zebra(['red', 'blue', 'red', 'blue', 'green']))

    
        
                

