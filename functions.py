def count_bill(rest):

    bills = [100, 50, 10, 5, 1, 0.50, 0.10, 0.050, 0.010]
    bills_quantities = []
        
    for bill in bills:
        quantity = {
            "quantity": rest // bill,
            "bill": bill
        }
        rest = rest % bill
        bills_quantities.append(quantity)
    
    return bills_quantities