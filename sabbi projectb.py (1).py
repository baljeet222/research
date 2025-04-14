class RequisitionSystem:
    def __init__(self):
        self.requisitionID = 10000
        self.staff_info = {}
        self.requisition_items = []

    def collect_staff_info(self):
        print("Printing Staff Information:")
        date = input("Date: ")
        staff_id = input("StaffID: ")
        staff_name = input("Staff name: ")
        self.requisitionID += 1  
        self.staff_info = {
            'date': date,
            'staff_id': staff_id,
            'staff_name': staff_name,
            'requisition_id': self.requisitionID
        }
        print(f"{date}, {staff_id}, {staff_name}, RequisitionID is {self.requisitionID}")

    def collect_requisition_items(self):
        self.requisition_items = []
        for i in range(1, 4):  
            item = input(f"Enter requisition item {i}: ")
            
            price = float(input(f"Enter cost $ for {item}: "))
            total_value =   price
            self.requisition_items.append({
                'item': item,
                
                'price': price,
                'total_value': total_value
            })
        total_cost = sum(item['total_value'] for item in self.requisition_items)
        print(f"Total cost is ${total_cost:.2f}")

    def approve_requisition(self):
        total_value = sum(item['total_value'] for item in self.requisition_items)
        if total_value <= 500:
            print("Approve")
        else:
            print("Pending")

    def display_requisitions(self):
        self.collect_staff_info()
        self.collect_requisition_items()
        self.approve_requisition()
        print("Staff Information:", self.staff_info)
        print("Requisition Items:", self.requisition_items)

if __name__ == "__main__":
    system = RequisitionSystem()
    system.display_requisitions()