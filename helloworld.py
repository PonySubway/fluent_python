import pycountry

# Regional indicator symbols start at 0x1F1E6 (A)
REGIONAL_INDICATOR_A = 0x1F1E6


def country_code_to_flag(country_code):
    """Convert ISO 3166-1 alpha-2 country code to flag emoji"""
    if not country_code or len(country_code) != 2:
        return ""
    # Each letter offset from 'A' gets added to the base
    return "".join(chr(REGIONAL_INDICATOR_A + ord(char) - ord('A')) for char in country_code.upper())


def print_hello_countries():
    """Print hello message with flag emoji for every country in the world"""
    for country in pycountry.countries:
        country_code = country.alpha_2
        flag = country_code_to_flag(country_code)
        print(f"Hello, {country.name} {flag}")


if __name__ == "__main__":
    print_hello_countries()