def zebra(colors: list) -> list:

    counter = 1
    highest_count = 0
    highest_color = None
    actual_color = colors[0]

    for i in range(1, len(colors)):

        if colors[i] != actual_color:
            actual_color = colors[i]

            if colors[i - 2] == colors[i] and i >= 2:
                counter += 1
            else:
                counter = 2

        if counter >= highest_count:
            highest_count = counter
            highest_color = actual_color

    return [highest_count, highest_color]

def str_data_to_list(input: str) -> list:
    return input[1:-1].replace('"', '').replace(' ', '').replace('\n', '').split(',')

def main():
    with open("colors.txt") as file:
        str_colors = file.read().strip()
        list_colors = str_data_to_list(str_colors)
        result = zebra(list_colors)
        print(result)

if __name__ == "__main__":
    main()
