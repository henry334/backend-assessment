# Task 1: Product List with Total Value Calculation
#### Objective:
Create a view that displays a list of products along with their prices and quantities. The view should also calculate and display the total value of all products (i.e., the sum of `price * quantity` for each product).

#### Requirements:
1. Model: You are provided with a `Product` model that includes the following fields:
    - **Name**: The name of the product (string).
    - **Price**: The price of the product (decimal).
    - **Quantity**: The quantity of the product in stock (integer).
2. View:
    - Retrieve all `Product` objects from the database.
    - Calculate the total value of all products (i.e., `price * quantity` for each product).
    - Pass the product list and total value to a template for display.
3. Template:
    - Create a template that displays the list of products with their names, prices, and quantities.
    - Below the product list, display the total value of all products.
#### Additional Challenge:
There is an intentional runtime error in the view. The code attempts to access an incorrect field that does not exist in the `Product` model. You must debug and fix this error to ensure the correct value is displayed.

### Deliverables:
- A working `views.py` and `product_list.html` template.