from datetime import date


def main():
    DOB = input ("Input your date of birth in the format 1999-01-27")
    today = date.today()
    age_years = today.year - int(DOB[:4])
    


...


if __name__ == "__main__":
    main()