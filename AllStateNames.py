"""
Print all State names and their abbreviations
"""
__author__ = 'Gareth'


def main():
    STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                   "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
    for short_state_name in STATE_NAMES:
        print("{:<4} is  {}".format(short_state_name, STATE_NAMES.get(short_state_name)))


if __name__ == "__main__":
    main()
