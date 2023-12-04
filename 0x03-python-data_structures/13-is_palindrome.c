#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to a pointer to the head of the list.
 *
 * Return: 1 if palindrome, 0 otherwise.
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	listint_t *slow = *head, *fast = *head, *prev_slow = *head;
	listint_t *second_half = NULL, *mid_node = NULL;
	int is_palindrome = 1;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next, prev_slow = slow, slow = slow->next;
	}
	if (fast != NULL)
	{
		mid_node = slow, slow = slow->next;
	}
	second_half = slow;
	prev_slow->next = NULL;
	second_half = reverse_list(second_half);
	listint_t *list1 = *head, *list2 = second_half;

	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
		{
			is_palindrome = 0;
			break;
		}
		list1 = list1->next, list2 = list2->next;
	}
	second_half = reverse_list(second_half);

	if (mid_node != NULL)
	{
		prev_slow->next = mid_node, mid_node->next = second_half;
	}
	else
	{
		prev_slow->next = second_half;
	}
	return (is_palindrome);
}


/**
 * reverse_list - Helper function reverses a singly linked list.
 * @head: Pointer to the head of the linked list.
 *
 * Return: Pointer to the head of the reversed list.
 */

listint_t *reverse_list(listint_t *head)
{
listint_t *prev = NULL;
listint_t *curr = head;
listint_t *next = NULL;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	return (prev);
}
