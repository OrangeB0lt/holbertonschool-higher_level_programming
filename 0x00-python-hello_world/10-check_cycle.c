#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list comming in
 * Return: 1 if it cycles, 0 else
 */

int check_cycle(listint_t *list)
{
	listint_t *pointer = list, *checker = list->next;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	while (pointer != NULL &&
	       checker->next != NULL &&
	       checker->next->next != NULL)
	{
		if (pointer == checker)
		{
			return (1);
		}
		pointer = pointer->next;
		if (pointer == NULL)
		{
			return (1);
		}
		checker = checker->next->next;
	}
	return (0);
}
