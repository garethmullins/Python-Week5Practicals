"""
10 Hex colours in a dictionary
"""
__author__ = 'Gareth'


def main():
    HEX_COLOURS = {"aliceblue": "#f0f8ff", "firebrick": "#b22222", "goldenrod": "#daa520", "indianred": "#cd5c5c",
                   "khaki": "#f0e68c", "lawngreen": "#7cfc00", "light": "#eedd82", "lightcoral": "#f08080",
                   "lightgoldenrodyellow": "#fafad2", "mediumaquamarine": "#66cdaa"}

    colour_name = input("Enter the colour's name (no spaces): ").lower()
    while colour_name != "":
        if colour_name in HEX_COLOURS:
            print(colour_name, "is", HEX_COLOURS[colour_name])
        else:
            print("Invalid colour name.")
        colour_name = input("Enter the colour's name: ").lower()


if __name__ == "__main__":
    main()
