# Module 6 Assignment: Functions and Modular Programming

#We print our starting message for the system
print("=" * 60)
print("TECHRETAIL SALES ANALYSIS SYSTEM")
print("=" * 60)

# Sample quarterly sales data 
# Format: [product_name, category, price, quantity_sold, employee_id]
#This format will help us understand our dictionary, that contains strings, integers, and floats
sales_data = [
    ["Smartphone Pro", "Phones", 899.99, 15, "E101"],
    ["Laptop Ultra", "Computers", 1299.99, 10, "E105"],
    ["Wireless Earbuds", "Audio", 149.99, 30, "E101"],
    ["Smart Watch", "Wearables", 249.99, 12, "E102"],
    ["Gaming Console", "Gaming", 499.99, 8, "E103"],
    ["Bluetooth Speaker", "Audio", 79.99, 25, "E102"],
    ["Tablet Lite", "Computers", 399.99, 18, "E104"],
    ["Digital Camera", "Cameras", 599.99, 5, "E105"],
    ["VR Headset", "Gaming", 299.99, 7, "E103"],
    ["Fitness Tracker", "Wearables", 129.99, 22, "E104"],
    ["Smartphone Plus", "Phones", 699.99, 20, "E101"],
    ["Laptop Basic", "Computers", 899.99, 14, "E105"]
]

# Employee information
# Format: {employee_id: [name, commission_rate]}
#the employee id lets us identify each worker without having to put their names and last names in the list
employees = {
    "E101": ["Alex Johnson", 0.05],
    "E102": ["Sarah Williams", 0.045],
    "E103": ["James Brown", 0.04],
    "E104": ["Lisa Davis", 0.05],
    "E105": ["Michael Wilson", 0.055]
}

#For our Sales Analysis Functions, we define the function and apply the parameters

def calculate_total_sales():
    """
    Calculates the total revenue from all sales.
    
    Returns:
        float: The total sales revenue.
    """
    total = sum(item[2] * item[3] for item in sales_data) #the for loop will keep returning the sales revenue
    return total

def calculate_category_sales(category):
    """
    Calculates the total revenue from sales in a specific product category.
    
    Args:
        category (str): The product category to calculate sales for.
        
    Returns:
        float: The total sales revenue for the specified category.
    """
    total = sum(item[2] * item[3] for item in sales_data if item[1] == category) #this function will calculate each category sale
    return total

def find_best_selling_product():
    """
    Finds the product with the highest total sales revenue.
    
    Returns:
        tuple: (product_name, total_revenue)
    """
    best_product = max(sales_data, key=lambda x: x[2] * x[3])
    return (best_product[0], best_product[2] * best_product[3])

# TODO 2: Commission Calculation Functions

def calculate_employee_commission(employee_id):
    """
    Calculates the commission earned by a specific employee.
    
    Args:
        employee_id (str): The unique identifier of the employee.
        
    Returns:
        float: The commission amount earned.
    """
    if employee_id not in employees:
        return 0.0
    rate = employees[employee_id][1]
    total_sales = sum(item[2] * item[3] for item in sales_data if item[4] == employee_id)
    return total_sales * rate

def calculate_total_commission():
    """
    Calculates total commissions for all employees.
    
    Returns:
        float: Total commission.
    """
    total = sum(calculate_employee_commission(eid) for eid in employees)
    return total

#we define with a function our reports, the sales and the employess

def generate_sales_summary(include_categories=True):
    """
    Generates a formatted sales summary report.
    
    Args:
        include_categories (bool, optional): Whether to include category breakdown.
            Defaults to True.
        
    Returns:
        str: Formatted report string.
    """
    report = "QUARTERLY SALES SUMMARY REPORT\n"
    report += "-" * 40 + "\n"
    total_sales = calculate_total_sales()
    report += f"Total Sales Revenue: ${total_sales:,.2f}\n\n"
    
    if include_categories:
        categories = set(item[1] for item in sales_data)
        report += "Sales by Category:\n"
        for cat in categories:
            report += f"{cat}: ${calculate_category_sales(cat):,.2f}\n"
    
    best_product, best_revenue = find_best_selling_product()
    report += f"\nBest-Selling Product: {best_product} - ${best_revenue:,.2f}\n"
    return report

def generate_employee_report():
    """
    Generates a report showing each employee's sales performance and commission.
    
    Returns:
        str: Formatted employee performance report.
    """
    report = "EMPLOYEE PERFORMANCE REPORT\n" + "-"*40 + "\n"
    for eid, info in employees.items():
        name = info[0]
        commission = calculate_employee_commission(eid)
        total_sales = sum(item[2]*item[3] for item in sales_data if item[4] == eid)
        report += f"{name} - Total Sales: ${total_sales:,.2f}, Commission: ${commission:,.2f}\n"
    return report

# TODO 4: Utility Functions

def get_products_by_category(category):
    """
    Returns all products belonging to a specific category.
    
    Args:
        category (str): The product category to filter by.
        
    Returns:
        list: List of products in the specified category.
    """
    return [item[0] for item in sales_data if item[1] == category]

def calculate_average_sale_price():
    """
    Calculates the average sale price across all transactions.
    
    Returns:
        float: Average sale price.
    """
    total_sales = sum(item[2]*item[3] for item in sales_data)
    total_items = sum(item[3] for item in sales_data)
    return total_sales / total_items if total_items else 0.0

#For our main program, we define with a function

def main():
    print("\nTECHRETAIL QUARTERLY SALES ANALYSIS")
    print("-" * 40)
    
    # we print our total sales
    print("\nTOTAL QUARTERLY SALES:")
    print(f"${calculate_total_sales():,.2f}")
    
    #we also print our sales by category
    print("\nSALES BY CATEGORY:")
    categories = ["Phones", "Computers", "Audio", "Wearables", "Gaming", "Cameras"]
    for cat in categories:
        print(f"{cat}: ${calculate_category_sales(cat):,.2f}")
    
    #we print our best-selling product
    print("\nBEST-SELLING PRODUCT:")
    best_product, revenue = find_best_selling_product()
    print(f"{best_product} - ${revenue:,.2f}")
    
    # we print our employee commissions
    print("\nEMPLOYEE COMMISSIONS:")
    for eid in employees:
        name = employees[eid][0]
        commission = calculate_employee_commission(eid)
        print(f"{name}: ${commission:,.2f}")
    
    # we pring our sales summary report
    print("\nQUARTERLY SALES SUMMARY REPORT:")
    print(generate_sales_summary())
    
    #we print out employee performance report
    print("\nEMPLOYEE PERFORMANCE REPORT:")
    print(generate_employee_report())

#finally, we run the main program with an if statement
if __name__ == "__main__":
    main()