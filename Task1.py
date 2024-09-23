class Product:
    _id_counter = 100  # Class-level counter to ensure unique product IDs

    def __init__(self, name, price, category, stockQuantity):
        # Assign a unique productID automatically
        self.productID = Product._id_counter
        Product._id_counter += 1
        
        # Set product attributes
        self.name = name
        self.price = price
        self.category = category
        self.stockQuantity = stockQuantity

    # Method to add new details or initialize product information
    def add_product_details(self, name, price, category, stockQuantity):
        self.name = name
        self.price = price
        self.category = category
        self.stockQuantity = stockQuantity

    # Method to update product details, such as price or stock
    def update_product_details(self, price=None, stockQuantity=None):
        if price is not None:
            self.price = price
        if stockQuantity is not None:
            self.stockQuantity = stockQuantity

    # String representation for easy readability
    def __str__(self):
        return f"Product ID: {self.productID}, Name: {self.name}, Price: ${self.price:.2f}, Category: {self.category}, Stock: {self.stockQuantity}"

# Example usage
eggs = Product("Eggs", 3.99, "Grocery", 200)

# Updating product price and stock
eggs.update_product_details(price=4.50, stockQuantity=180)

print(eggs)
