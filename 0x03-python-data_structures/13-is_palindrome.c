#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to a pointer to the head of the list.
 *
 * Return: 1 if palindrome, 0 otherwise.
 */

int is_palindrome(listint_t **head)
{
listint_t *first = *head, *second = *head;
listint_t *first_end = *head, *reversed_second = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		second = second->next->next;

		if (!second)
		{
			reversed_second = first->next;
			break;
		}
		if (!second->next)
		{
			reversed_second = first->next->next;
			break;
		}
		first = first->next;
	}
	reverse_list(&reversed_second);

	while (reversed_second && first_end)
	{
		if (first_end->n == reversed_second->n)
		{
			reversed_second = reversed_second->next;
			first_end = first_end->next;
		}
		else
		{
			return (0);
		}
	}
	if (!reversed_second)
	{
		return (1);
	}
	return (0);
}


/**
 * reverse_list - Helper function reverses a singly linked list.
 * @head: Pointer to the head of the linked list.
 */

void reverse_list(listint_t **head)
{
listint_t *prev = NULL, *curr = *head, *next = NULL;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	*head = prev;
}
