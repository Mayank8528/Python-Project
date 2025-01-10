#include <stdio.h>
#include <stdlib.h>

// Function to display the menu
void displayMenu() {
    printf("\nATM Menu:\n");
    printf("1. Check Balance\n");
    printf("2. Deposit Money\n");
    printf("3. Withdraw Money\n");
    printf("4. Exit\n");
    printf("Select an option: ");
}

// Function to check balance
void checkBalance(float balance) {
    printf("\nYour current balance is: $%.2f\n", balance);
}

// Function to deposit money
void depositMoney(float *balance) {
    float deposit;
    printf("\nEnter amount to deposit: ");
    scanf("%f", &deposit);
    
    if (deposit > 0) {
        *balance += deposit;
        printf("\nSuccessfully deposited $%.2f\n", deposit);
    } else {
        printf("\nInvalid deposit amount.\n");
    }
}

// Function to withdraw money
void withdrawMoney(float *balance) {
    float withdraw;
    printf("\nEnter amount to withdraw: ");
    scanf("%f", &withdraw);
    
    if (withdraw > 0 && withdraw <= *balance) {
        *balance -= withdraw;
        printf("\nSuccessfully withdrew $%.2f\n", withdraw);
    } else if (withdraw > *balance) {
        printf("\nInsufficient funds.\n");
    } else {
        printf("\nInvalid withdrawal amount.\n");
    }
}

int main() {
    float balance = 1000.00;  // Starting balance
    int option;
    
    while (1) {
        displayMenu();
        scanf("%d", &option);

        switch (option) {
            case 1:
                checkBalance(balance);
                break;
            case 2:
                depositMoney(&balance);
                break;
            case 3:
                withdrawMoney(&balance);
                break;
            case 4:
                printf("\nThank you for using our ATM. Goodbye!\n");
                exit(0);
            default:
                printf("\nInvalid option. Please try again.\n");
        }
    }

    return 0;
}