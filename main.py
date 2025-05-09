from cash_optimizer.optimizer import find_minimal_exchange

if __name__ == "__main__":
  
    total_value = 19.96
    USdenominations = [0.01, 0.05, 0.10, 0.25, 1, 5, 10, 20, 50, 100]
    payment, change = find_minimal_exchange(USdenominations, total_value)
    
    print(f"Total payment: ${total_value:.2f}")
    print(f"Total exchanges: {len(payment) + len(change)}") 
    print(f"Payment made: {payment} -> Total: ${sum(payment):.2f}")
    print(f"Change given: {change} -> Total: ${sum(change):.2f}") 

