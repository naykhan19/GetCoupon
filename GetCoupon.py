# Nayem Khan
# 4/13/20
# Calculate whether the customer will get coupon or not based on number of items and total amount

def main():
    coupon = float()
    num_orders = int(input("Enter the number of orders: "))
    total = float(input("Enter the total spent: "))
     

def CalcCoupon(num_orders, total):
    if num_orders >= 6 and total >= 10:
        coupon = 0.10
    elif num_orders >= 6 and total >= 20:
        coupon = 0.20
    elif num_orders >= 6 and total >= 30:
        coupon = 0.30
    print("Customer Coupon: ",coupon + "% off coupon")

    

#define main
main()
