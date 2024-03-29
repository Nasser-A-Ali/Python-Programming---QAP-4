# DESCRIPTION: Calculates insurance policy information of new customers.
# AUTHOR: Nasser Ali.
# DATE: March 23rd, 2024.


# Imports libraries.
import datetime
import PCL_FormatValues as FV
import os

# Define program constants.
NEXT_POLICY_NUMBER = 1944
BASIC_INSURANCE_RATE = 869.00
ADDITIONAL_CAR_DISCOUNT_RATE = 0.25
EXTRA_LIABILITY_COST = 130.00
GLASS_COVERAGE_COST = 86.00
LOANER_CAR_COVERAGE_COST = 58.00
HST_RATE = 0.15
MONTHLY_PAYMENT_PROCESSING_FEE = 39.99

# Defines values for validations.
PROVINCES = [
    "AB",
    "BC",
    "MB",
    "NB",
    "NL",
    "NS",
    "NT",
    "NU",
    "ON",
    "PE",
    "QC",
    "SK",
    "YT"]
PAYMENT_METHODS = ['Full', 'Monthly', 'Down Pay']


# Define program functions.

# Calculates the insurance premium (premium of all cars + extra costs).
def calculate_insurance_premium(number_of_cars_insured):
    insurance_premium = BASIC_INSURANCE_RATE + \
        (ADDITIONAL_CAR_DISCOUNT_RATE *
         (number_of_cars_insured - 1) * BASIC_INSURANCE_RATE)

    return insurance_premium


def calculate_extra_costs(number_of_cars_insured, extra_liability, glass_coverage, loaner_car):
    total_extra_liability = 0
    total_glass_coverage = 0
    total_loaner_car_coverage = 0

    if extra_liability == 'Y':
        total_extra_liability = number_of_cars_insured * EXTRA_LIABILITY_COST
    if glass_coverage == 'Y':
        total_glass_coverage = number_of_cars_insured * GLASS_COVERAGE_COST
    if loaner_car == 'Y':
        total_loaner_car_coverage = number_of_cars_insured * LOANER_CAR_COVERAGE_COST

    total_extra_costs = total_extra_liability + \
        total_glass_coverage + total_loaner_car_coverage

    return total_extra_costs

# Function to calculate total cost (total premium + HST).


def calculate_total_cost(total_insurance_premium):
    insurance_hst_amount = total_insurance_premium * HST_RATE
    total_cost = total_insurance_premium + insurance_hst_amount

    return total_cost

# Function to calculate the payment amount based on the payment method.


def calculate_payment_amount(total_cost, payment_method, down_payment):
    if payment_method == 'Full':
        payment_amount = total_cost
    elif payment_method == 'Monthly':
        payment_amount = (total_cost + MONTHLY_PAYMENT_PROCESSING_FEE) / 8
    elif payment_method == 'Down Pay':
        total_cost -= down_payment
        payment_amount = (total_cost + MONTHLY_PAYMENT_PROCESSING_FEE) / 8
    return payment_amount

# Function to format claim details


def format_claim_details(claims):
    formatted_claims = ""
    for claim in claims:
        formatted_claims += f"{claim[0]}              {claim[1]
                                                       }        {FV.FDollar2(claim[2]):>9s}\n"

    return formatted_claims


# Main program.
while True:
    # Clears the terminal screen.
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome to the One Stop Insurance Company program.")
    print()

    # Gather user input.
    first_name = input("Enter customer's first name: ").title()
    last_name = input("Enter customer's last name: ").title()
    address = input("Enter customer's address: ")
    city = input("Enter customer's city: ").title()

    # Validates province using a list of valid province abbreviations.
    while True:
        user_province = input("Enter customer's province (XX): ").upper()
        if user_province == "":
            print("Data Entry Error - province cannot be empty. Please try again.")
        elif user_province not in PROVINCES:
            print("Data Entry Error - invalid province code.")
        else:
            break

    postal_code = input("Enter customer's postal code: ")
    phone_number = FV.format_phone_number(
        input("Enter customer's phone number: "))
    number_of_cars_insured = int(
        input("Enter number of cars being insured: "))
    extra_liability = input(
        "Include extra liability coverage up to $1,000,000? (Y/N): ").upper()
    glass_coverage = input("Include glass coverage? (Y/N): ").upper()
    loaner_car = input("Include optional loaner car? (Y/N): ").upper()

    # Validates payment method using a list of valid payment methods.
    while True:
        payment_method = input(
            "How would the customer like to pay? (Full/Monthly/Down Pay): ").title()
        if payment_method == "":
            print(
                "Data Entry Error - payment method cannot be empty. Please try again.")
        elif payment_method not in PAYMENT_METHODS:
            print("Data Entry Error - invalid payment method.")
        else:
            break

    if payment_method == 'Down Pay':
        down_payment = float(input("Enter the down payment amount: "))
    else:
        down_payment = 0

    # Previous claims input
    print()
    print("Enter the details of all previous claims for this customer:")
    claims = []
    while True:
        claim_number = input(
            "Enter claim number (type '0' once finished): ")
        if claim_number == '0':
            break
        claim_date = input("Enter claim date (YYYY-MM-DD): ")
        claim_amount = float(input("Enter claim amount: "))
        claims.append([claim_number, claim_date, claim_amount])

    os.system('cls' if os.name == 'nt' else 'clear')

    # Calculate total insurance premium, total cost, and payment amount.
    insurance_premium = calculate_insurance_premium(
        number_of_cars_insured)
    extra_costs = calculate_extra_costs(
        number_of_cars_insured, extra_liability, glass_coverage, loaner_car)
    total_insurance_premium = insurance_premium + extra_costs
    total_cost = calculate_total_cost(total_insurance_premium)

    payment_amount = calculate_payment_amount(
        total_cost, payment_method, down_payment)
    formatted_claims = format_claim_details(claims)

    # Sets dates for invoice and first payment.
    invoice_date = datetime.datetime.today().strftime('%Y-%m-%d')
    first_payment_date = datetime.date.today().replace(day=1) + \
        datetime.timedelta(days=31)

    # Display results.

    print("=============================================")
    print("         One Stop Insurance Company          ")
    print(f"          Invoice Date: {invoice_date}      ")
    print("=============================================")
    print("             Customer information            ")
    print("---------------------------------------------")
    print(f"Name:         {first_name} {last_name}")
    print(f"Address:      {address}")
    print(f"City:         {city}")
    print(f"Province:     {user_province}")
    print(f"Postal Code:  {postal_code}")
    print(f"Phone Number: {phone_number}")
    print("---------------------------------------------")
    print("             Insurance information           ")
    print("---------------------------------------------")
    print(f"Number of cars insured:                     {
          number_of_cars_insured}")
    print(f"Extra liability coverage (Y/N):             {extra_liability}")
    print(f"Glass coverage (Y/N):                       {glass_coverage}")
    print(f"Loaner car coverage (Y/N):                  {loaner_car}")
    print(f"Payment method:                      {payment_method:>8s}")
    print("---------------------------------------------")
    print("              Payment information            ")
    print("---------------------------------------------")
    print(f"Insurance Premium:                  {
          FV.FDollar2(insurance_premium):>9s}")
    print(f"Extra Costs:                        {
          FV.FDollar2(extra_costs):>9s}")
    print(f"Total Insurance Premium:            {
          FV.FDollar2(total_insurance_premium):>9s}")
    print(f"Total Cost:                         {
          FV.FDollar2(total_cost):>9s}")

    if payment_method == 'Full':
        print(f"Payment Due:                        {
              FV.FDollar2(payment_amount):>9s}")
    elif payment_method == 'Monthly':
        print(f"Monthly Payment Processing Fee:        ${
              MONTHLY_PAYMENT_PROCESSING_FEE}")
        print(f"Monthly Payment:                    {
              FV.FDollar2(payment_amount):>9s}")
        print(f"First Payment Due:                 {first_payment_date}")
    elif payment_method == 'Down Pay':
        print(f"Down Payment:                       {
              FV.FDollar2(down_payment):>9s}")
        print(f"Monthly Payment Processing Fee:        ${
              MONTHLY_PAYMENT_PROCESSING_FEE}")
        print(f"Monthly Payment:                    {
              FV.FDollar2(payment_amount):>9s}")
        print(f"First Payment Due:                 {first_payment_date}")

    if len(claims) > 1:
        print("---------------------------------------------")
        print("         Previous Claims Information         ")
        print("---------------------------------------------")
        print("Claim #           Claim Date           Amount")
        print("---------------------------------------------")
        print(formatted_claims)
    print("=============================================")

    # Increments the policy number.
    NEXT_POLICY_NUMBER += 1

    # Checks if user wants to continue using the program.
    programState = input(
        "Would you like to process a new customer? (Y/N): ").upper()
    if programState == "":
        print("Data Entry Error - field cannot be blank. Please try again.")
    elif programState != 'Y' and programState != 'N':
        print("Data Entry Error - choice must be 'Y' or 'N'. Please try again.")

    if programState == 'N':
        break

    print()

# Housekeeping.
os.system('cls' if os.name == 'nt' else 'clear')
print()
print("Thank you for using the One Stop Insurance Company program.")
print("                  Have a great day!                        ")
print()
