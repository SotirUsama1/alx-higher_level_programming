#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t** head)
{
    listint_t* prev = *head;
    listint_t* cur = head->next;
    listint_t* temp = head->next->next;

    head->next = NULL;

    while (cur)
    {
        prev = cur;
        cur = temp;
        temp = temp->next;
    }

    *head = cur;
}

/**
* is_palindrome - checks if the list is a palindrome
* @head: pointer to the list head pointer of type node
*
* Return: 1 if palindrome or 0 if not
*/

int is_palindrome(listint_t** head)
{
    
}

#include <stdio.h>
#include <stdlib.h>

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t* head;

    head = NULL;
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 1);
    print_listint(head);

    //if (is_palindrome(&head) == 1)
    //    printf("linked list is a palindrome\n");
    //else
    //    printf("linked list is not a palindrome\n");

    reverse_listint(&head);

    free_listint(head);

    return (0);
}