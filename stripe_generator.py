import sys
import re
import string
import secrets
import stripe
import csv

stripe.api_key = "none"


def main():
    print(api_key())
    coupon_code = create_coupon()
    print(create_promocodes(coupon_code))


def api_key():
    while True:
        stripe.api_key = input("What's your API Key: ")
        if re.search(r"^(sk_|pk_|rk_)[a-zA-Z0-9_]+$", stripe.api_key):
            return "\nAPI KEY IS VALID...\n"
        else:
            sys.exit("Please provide a valid API key")


def create_coupon():
    # Set a random reusable ID for the newly create coupon of length 8
    LENGTH = 8
    generated_id = "".join(
        secrets.choice(string.ascii_letters + string.digits) for _ in range(LENGTH)
    )

    # Intiate the questions to be asked

    print("\n\n\nPROVIDE THE DETAILS FOR YOUR NEW COUPON\n")

    # Ask for the type of the coupon, validate input
    while True:
        input_duration: str = input("What's the type of your coupon: ").lower()
        if input_duration not in ["once", "repeating", "forever"]:
            continue
        else:
            break

    # Ask for the discount percentage of the coupon, validate input
    while True:
        try:
            input_percent: float = float(input(f"What's the % discount: "))
            break
        except ValueError:
            print("Provide an number")
            continue

    # Generate the coupon using the input and random id
    if input_duration in ["once", "forever"]:
        try:
            stripe.Coupon.create(
                id=generated_id,
                duration=input_duration,
                percent_off=input_percent,
            )
        except Exception as e:
            print(f"Failed to create coupon code: {e}")

    # In the case of repeating coupon, ask for repeat cycles
    else:
        while True:
            try:
                input_months: int = int(input(f"For how many months repeating: "))
                break
            except ValueError:
                print("Provide an integer")
                continue
        # Generate the repeating coupon
        try:
            stripe.Coupon.create(
                id=generated_id,
                duration=input_duration,
                duration_in_months=input_months,
                percent_off=input_percent,
            )
        except Exception as e:
            print(f"Failed to create coupon code: {e}")

    # Print when the coupon is created and return coupon code
    print("\n\n\n")
    print(f"Coupon {generated_id} has been generated")
    return generated_id


def create_promocodes(coupon_code):
    # Generate a field name for the final document
    field_name = f"Coupon: {coupon_code}"

    # Intiate the questions to be asked

    print("\n\n\nPROVIDE THE DETAILS FOR YOUR PROMOTION CODES\n")

    # Ask for many promotion codes someone wants to create
    while True:
        try:
            input_times: int = int(
                input(f"How many promotion codes do you want to create: ")
            )
            if input_times > 0:
                break
            else:
                continue
        except ValueError:
            print("Provide an integer")
            continue

    # Ask for the redemption limit of the promotion codes
    while True:
        try:
            input_limit: int = int(input(f"How many times can the code be redeemed: "))
            if input_limit > 0:
                break
            else:
                continue
        except ValueError:
            print("Provide an integer")
            continue

    # Provide a name for the csv
    name = input("Name your output csv file: ")
    if name.endswith(".csv"):
        file_name = name
    else:
        file_name = f"{name}.csv"

    # Wipe CSV if it already exists
    with open(file_name, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=[field_name])
        writer.writeheader()

    # Create CSV file with promotion codes
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer = csv.DictWriter(file, fieldnames=[field_name])

        # If file doesn't exist with header, write header
        if file.tell() == 0:
            writer.writeheader()

        # Generate the promotion codes
        for _ in range(input_times):
            # Set a random reusable ID for the newly create coupon of length 8
            LENGTH = 8
            generated_id = "".join(
                secrets.choice(string.ascii_letters + string.digits)
                for _ in range(LENGTH)
            )

            # Create the promotion code
            try:
                stripe.PromotionCode.create(
                    coupon=coupon_code, code=generated_id, max_redemptions=input_limit
                )
                writer.writerow({field_name: generated_id})
            except Exception as e:
                print(f"Failed to create promotion code: {e}")

    # Return message to confirm successful generation
    print("\n\n\n")
    return f"You've successfully created {input_times} promotion codes for coupon {coupon_code}. You can find all promotion codes in {file_name}"


if __name__ == "__main__":
    main()
