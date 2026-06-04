from fan_class import Fan

try:

    # First Fan Object
    fan1 = Fan(
        speed=Fan.FAST,
        radius=10,
        color="yellow",
        on=True
    )

    # Second Fan Object
    fan2 = Fan(
        speed=Fan.MEDIUM,
        radius=5,
        color="blue",
        on=False
    )

    print("\nFIRST FAN")
    fan1.display_info()

    print("\nSECOND FAN")
    fan2.display_info()

    print("\nOBJECT REPRESENTATION")
    print(fan1)
    print(fan2)

except ValueError as error:
    print(f"Value Error: {error}")

except TypeError as error:
    print(f"Type Error: {error}")

except Exception as error:
    print(f"Unexpected Error: {error}")