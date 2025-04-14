#Assignment 3
# Requisition Management System

Staff members can submit requests through this Python-based requisition management system, which also calculates the overall value and determines the approval status depending on the total cost. The system is made to compute approval or pending status, gather personnel data, and requisition items.

## Properties

- Staff Information Collection: Collecting staff ID, name, and date of requisition.
- Requisition Item Entry: Allowing staff to enter requisition items and their prices.
- Total Calculation: Automatically calculates the total value of the entered requisition items.
- Approval System: Approving requisitions if the total is less than $500, otherwise marks them as pending.
- Approval Reference: Generating an approval reference number for approved requisitions.

## Code Structure

The system is divided into four main functions:

1. staff_info(counter): Collects staff information and generates a unique requisition ID.
2. requisitions_total(counter): Collects requisition items, calculates the total price, and returns the information.
3. requisition_approval(counter): Determines whether the requisition is approved based on the total and generates an approval reference number if approved.
4. display_requisitions(counter): Displays the staff's requisition information, total, status, and approval reference number.

## How to Run the Program

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/requisition-management-system.git
    cd requisition-management-system
    ```

2. Run the Python script:
    ```bash
    python requisition_management.py
    ```

3. Follow the on-screen prompts to enter staff details and requisition items.

## Example of Output

```plaintext
Enter Date : 2024-09-18
Enter Staff ID: 12345
Enter Staff Name: John Doe
Enter Requisition Item Name (or 'done' to finish): Laptop
Enter price for Laptop: 1200
Enter Requisition Item Name (or 'done' to finish): Keyboard
Enter price for Keyboard: 50
Enter Requisition Item Name (or 'done' to finish): done

Printing Requisitions:
Date: 2024-09-18
Requisition ID: 10070
Staff ID: 12345
Date: 2024-09-18
Requisition ID: 10070
Staff Name: John Doe
Total: $1250.0
Status: Pending
Approval Reference Number: N/A
