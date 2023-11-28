#include "lists.h"
#include <stddef.h>
#include <stdlib.h>


/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The number to insert.
 * Return: A pointer to the new node (Success).
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *new;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (current == NULL || current->n >= number)
	{
		new->next = current;
		*head = new;
		return (new);
	}

	while (current->next && current->next->n < number)
	{
		current = current->next;
	}

	new->next = current->next;
	current->next = new;
	return (new);
}
