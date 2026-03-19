class Validators:
    @staticmethod
    def validate_positive_number(value: float):
        try:
            number = float(value)
            if number <= 0:
                raise ValueError("Value must be a positive number.")
            return number
        except ValueError as e:
            raise ValueError(f"Invalid input: {e}")

    @staticmethod
    def validate_non_empty_string(value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Value must be a non-empty string.")
        return value.strip()
    
    @staticmethod
    def validate_order_type(value: str):
        valid_types = ["MARKET", "LIMIT"]
        if value.upper() not in valid_types:
            raise ValueError(f"Order type must be one of {valid_types}.")
        return value.upper()
    
    @staticmethod
    def validate_order_side(value: str):
        valid_sides = ["BUY", "SELL"]
        if value.upper() not in valid_sides:
            raise ValueError(f"Order side must be one of {valid_sides}.")
        return value.upper()
    
    @staticmethod
    def validate_price_limit_for_orders(price: float, min_price: float = 0.01, max_price: float = 1000000.0):
        if price is None or price <= min_price or price > max_price:
            raise ValueError(f"Price must be greater than {min_price} and less than or equal to {max_price} for LIMIT orders.")
        return price
