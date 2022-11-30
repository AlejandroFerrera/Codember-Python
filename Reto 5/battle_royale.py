def battle_royale(players: list) -> list:

    kills_counter = 0
    players_copy = players.copy()


    while kills_counter != len(players) - 1:
        
        killing_order = False
        
        for i in range(len(players)):

            if players[i] != 'X' and not killing_order:
                killing_order = True
            else:

                if players[i] == 'X':
                    continue

                players[i] = 'X'
                killing_order = False
                kills_counter += 1
    return players
        






def str_data_to_list(input: str) -> list:
    return input[1:-1].replace('"', '').replace(' ', '').replace('\n', '').split(',')


mecenas = [
    "Gorusuke",
    "DavidFabian",
    "ItziarZG",
    "edy WOLF",
    "MarcosGaPe",
    "Jose Jimenez",
    "Borja ",
    "Jhonathan Izquierdo Higuita",
    "MiLfeR322",
    "Sebastián Espínola",
    "Matias Luna",
    "Imanol Decima",
    "MarcoCasula",
    "MaríaBohórquez",
    "Renan",
    "IvanL'olivier",
    "Shonero",
    "Luichidev",
    "Faviola Narvaez",
    "Christopher Fuentes",
    "Kuro",
    "Juan Pablo Addeo",
    "Sergio Martínez",
    "Fran Enriquez González",
    "Diana",
    "tictools",
    "ConchaAsensio",
    "Emilio_Arreaza",
    "novamix",
    "Tomas Duclos",
    "Elaya",
    "Ignacio Palominos",
    "David C.",
    "Gerardo Felipe Conrado",
    "ElXuri",
    "David Borja Martinez",
    "JaviFelices",
    "CarlesSànchez",
    "Gorusuke",
    "DavidFabian",
    "ItziarZG",
    "edy WOLF",
    "MarcosGaPe",
    "Jose Jimenez",
    "Borja ",
    "Jhonathan Izquierdo Higuita",
    "MiLfeR322",
    "Sebastián Espínola",
    "Matias Luna",
    "Imanol Decima",
    "MarcoCasula",
    "MaríaBohórquez",
    "Renan",
    "IvanL'olivier",
    "Shonero",
    "Luichidev",
    "Faviola Narvaez",
    "Christopher Fuentes",
    "Kuro",
    "Juan Pablo Addeo",
    "Sergio Martínez",
    "Fran Enriquez González",
    "Diana",
    "tictools",
    "ConchaAsensio",
    "Emilio_Arreaza",
    "novamix",
    "Tomas Duclos",
    "Elaya",
    "Ignacio Palominos",
    "David C.",
    "Gerardo Felipe Conrado",
    "ElXuri",
    "David Borja Martinez",
    "JaviFelices",
    "CarlesSànchez",
    "Gorusuke",
    "DavidFabian",
    "ItziarZG",
    "edy WOLF",
    "MarcosGaPe",
    "Jose Jimenez",
    "Borja ",
    "Jhonathan Izquierdo Higuita",
    "MiLfeR322",
    "Sebastián Espínola",
    "Matias Luna",
    "Imanol Decima",
    "MarcoCasula",
    "MaríaBohórquez",
    "Renan",
    "IvanL'olivier",
    "Shonero",
    "Luichidev",
    "Faviola Narvaez",
    "Christopher Fuentes",
    "Kuro",
    "Juan Pablo Addeo",
    "Sergio Martínez",
    "Fran Enriquez González",
    "Diana",
    "tictools",
    "ConchaAsensio",
    "Emilio_Arreaza",
    "novamix",
    "Tomas Duclos",
    "Elaya",
    "Ignacio Palominos",
    "David C.",
    "Gerardo Felipe Conrado",
    "ElXuri",
    "David Borja Martinez",
    "JaviFelices",
    "CarlesSànchez"
]
test = [i for i in range(0, 10)]


print(battle_royale(mecenas))
print(len(mecenas))