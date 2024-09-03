class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, number):
        print(f"{self.brand} is calling {number}")

    def __str__(self) -> str:
        return f"Brand: {self.brand}, Price: {self.price}"


iphone = Phone("Iphone 10+", 300)
samsung = Phone("Samsung S20", 1400)

print(iphone)
print(samsung)


iphone.call("01001079014")
iphone.call("asdf")

