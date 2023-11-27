#include "lists.h"

/**
 * check_cycle - Check for loops in a linked list.
 * @head: Pointer to the head of the linked list.
 *
 * Return: 1 if a cycle is found, 0 if not.
 */

int check_cycle(listint_t *head)
{
	/* Declare variables - for pointers */
	listint_t *slow_ptr, *fast_ptr;

	/* Check for empty list or a list with only one node */
	if (!head || !head->next)
	{
		return (0);
	}

	/* Initialize pointers: slow and fast */
	slow_ptr = head;
	fast_ptr = head->next;

	/* Iterating through the list */
	while (slow_ptr && fast_ptr && fast_ptr->next)
	{
		/* If pointers meet, a cycle is found */
		if (slow_ptr == fast_ptr)
		{
			return (1);
		}

		/* Move slow pointer by one node */
		slow_ptr = slow_ptr->next;
		/* Move fast pointer by two nodes */
		fast_ptr = fast_ptr->next->next;
	}

	/* In case no cycle found */
	return (0);
}
