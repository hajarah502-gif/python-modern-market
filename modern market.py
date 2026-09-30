# ==========================================================
# MAMA MBOGA DIGITAL STALL POS
# Digital POS & End-of-Day Reconciliation Ledger
# ==========================================================


# ----------------------------------------------------------
# FUNCTION 1: Prompt for a valid quantity
# ----------------------------------------------------------

def prompt_quantity(item_name):
    while True:
        try:
            quantity = float(input(f"Enter quantity (kg/bunches) for {item_name}: "))

            if quantity <= 0:
                print("Error: Quantity must exceed 0.0")
            else:
                return quantity

        except ValueError:
            print("Error: Please enter a valid numeric value.")


# ----------------------------------------------------------
# FUNCTION 2: Calculate item price
# ----------------------------------------------------------

def calculate_item_price(item_type, quantity, customer_type="retail"):

    item_type = item_type.lower()
    customer_type = customer_type.lower()

    # ---------------- RETAIL PRICES ----------------
    if customer_type == "retail":

        if item_type == "tomatoes":
            base_price = 3000

            # First 5 kg at normal price
            if quantity <= 5:
                return quantity * base_price

            # Quantity above 5 kg gets 5% discount
            first_five = 5 * base_price
            extra_quantity = quantity - 5
            discounted_price = extra_quantity * base_price * 0.95

            return first_five + discounted_price

        elif item_type == "onions":
            base_price = 2500

            if quantity <= 5:
                return quantity * base_price

            first_five = 5 * base_price
            extra_quantity = quantity - 5
            discounted_price = extra_quantity * base_price * 0.95

            return first_five + discounted_price

        elif item_type == "matooke":
            return quantity * 25000

    # ---------------- WHOLESALE PRICES ----------------
    elif customer_type == "wholesale":

        if item_type == "tomatoes":
            return quantity * 2400

        elif item_type == "onions":
            return quantity * 2000

        elif item_type == "matooke":

            # Wholesale matooke requires at least 3 bunches
            if quantity >= 3:
                return quantity * 20000
            else:
                # Bill at retail price if below 3 bunches
                return quantity * 25000

    # Invalid item
    return 0


# ----------------------------------------------------------
# FUNCTION 3: Apply market levy and packaging
# ----------------------------------------------------------

def apply_market_levy_and_packaging(subtotal, needs_eco_crate=False):

    # 1% market council sanitation levy
    levy = subtotal * 0.01

    # Eco-crate deposit
    crate_deposit = 0

    if needs_eco_crate:
        crate_deposit = 5000

    total = subtotal + levy + crate_deposit

    return total, levy, crate_deposit


# ----------------------------------------------------------
# MAIN PROGRAM
# ----------------------------------------------------------

def main():

    # Session totals
    total_customers = 0
    total_revenue = 0

    highest_customer_name = ""
    highest_customer_bill = 0

    receipt_number = 1

    print("=" * 50)
    print("       MAMA MBOGA DIGITAL STALL POS")
    print("=" * 50)

    # Keep serving customers until cashier says no
    while True:

        # ----------------------------------------------
        # Customer information
        # ----------------------------------------------

        customer_name = input("\nCustomer Name: ").strip()

        while customer_name == "":
            print("Error: Customer name cannot be empty.")
            customer_name = input("Customer Name: ").strip()

        customer_type = input(
            "Customer Type (retail/wholesale): "
        ).strip().lower()

        while customer_type not in ["retail", "wholesale"]:
            print("Error: Please enter retail or wholesale.")
            customer_type = input(
                "Customer Type (retail/wholesale): "
            ).strip().lower()

        # List to store customer's items
        basket = []

        # ----------------------------------------------
        # Add items
        # ----------------------------------------------

        while True:

            item = input(
                "Add Item (tomatoes / onions / matooke / done): "
            ).strip().lower()

            if item == "done":
                break

            if item not in ["tomatoes", "onions", "matooke"]:
                print("Error: Invalid item. Please choose tomatoes, onions, or matooke.")
                continue

            quantity = prompt_quantity(item)

            # Calculate price
            item_total = calculate_item_price(
                item,
                quantity,
                customer_type
            )

            # Determine unit price for display
            if customer_type == "wholesale":

                if item == "tomatoes":
                    unit_price = 2400
                elif item == "onions":
                    unit_price = 2000
                elif item == "matooke":
                    if quantity >= 3:
                        unit_price = 20000
                    else:
                        unit_price = 25000

            else:
                if item == "tomatoes":
                    unit_price = 3000
                elif item == "onions":
                    unit_price = 2500
                else:
                    unit_price = 25000

           