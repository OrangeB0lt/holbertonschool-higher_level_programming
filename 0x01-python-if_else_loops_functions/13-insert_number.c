#include "lists.h"

/**
 * insert_node - inserts a num into a sort list
 * @head: pointer to list
 * @number: num to add
 * Return: address of the added node otherwise it adds NULL
 **/

listint_t *insert_node(istint_t **head, int number)
{
	listint_t *last, *nexxt, *curr;

	if (head == NULL)
		return (NULL);
	nexxt = malloc(sizeof(listint_t));
	if (nexxt == NULL)
		return (NULL);
	nexxt->n = number;
	last = NULL;
	curr = *head;

	for (; curr != NULL && curr->n < number;)
	{
		last = curr;
		curr = curr->next;
	}
	nexxt->next = curr;

	if (last != NULL)
		last->next = nexxt;
	else
		*head = nexxt;
	return (nexxt);
}
