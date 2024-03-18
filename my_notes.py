def main():
    # format_function_notes()
    rosharan_seconds_length()


def format_function_notes():
    floating = 0.987654321
    integer = 9
    print("{:<5.2f} {:<5}".format(floating, integer))
    # The format for justifying something you're rounding is justify.round


def rosharan_seconds_length():
    seconds_figure = 69.4252354752
    rosh_year_seconds = 500 * 50 * 20 * seconds_figure
    earth_year_seconds = 365.24219 * 60 * 24 * 60 * 1.1

    print(rosh_year_seconds, "seconds in a rosharan year")

    print(earth_year_seconds, "seconds in an earth year")

    difference = rosh_year_seconds - earth_year_seconds
    print(difference, "more seconds in a rosharan year")
#    print(difference / 60, "minutes")       # divide by seconds
#    print(difference / 60 / 60, "hours")
#    print(difference / 60 / 60 / 24, "days")
#    print(4.6 - 3.5)


main()
