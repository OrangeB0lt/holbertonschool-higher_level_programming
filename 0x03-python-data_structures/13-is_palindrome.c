#include "lists.h"

/**
 * is_palindrome - checks if list is a palindrome
 * @head: start of list
 * Return: returns 1 on success, 0 otherwise
 **/

int is_palindrome(listint_t **head)
{
	listint_t *beginning;
	int *storage, index = 0, length = 0;

	beginning = *head;

	while (beginning != NULL)
	{
		beginning = beginning->next;
		length++;
	}
	storage = malloc(sizeof(int) * (length));
	if (storage == NULL)
		return (0);
	index = 0;
	beginning = *head;
	while (storage[index] == storage[length])
	{
		if (index == length || index > length)
		{
			free(storage);
			return (1);
		}
		index++;
		length--;
	}
	free(storage);
	return (0);
}
