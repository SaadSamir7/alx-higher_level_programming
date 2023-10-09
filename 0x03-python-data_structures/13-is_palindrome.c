#include "lists.h"

/**
 *is_palindrome - Checks if a singly linked list is a palindrome.
 *@head: Pointer to the head of the linked list.
 *Return: 1 if it is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head;
	listint_t *fast_ptr = *head;
	listint_t *prev = NULL;
	listint_t *temp;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		fast_ptr = fast_ptr->next->next;
		temp = slow_ptr;
		slow_ptr = slow_ptr->next;
		temp->next = prev;
		prev = temp;
	}

	if (fast_ptr != NULL)
		slow_ptr = slow_ptr->next;

	while (prev != NULL && slow_ptr != NULL)
	{
		if (prev->n != slow_ptr->n)
		{
			is_palindrome = 0;
			break;
		}

		prev = prev->next;
		slow_ptr = slow_ptr->next;
	}

	return (is_palindrome);
}
