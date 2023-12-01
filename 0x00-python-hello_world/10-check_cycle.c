#include "lists.h"
/**
 * check_cycle - this function checks for the occurrence of cycled linked lists
 * @list: this is the list to be parsed,
 * i.e the head to the first node of the list
 * Return: 1 for cycle linked list and 0 for linear linked list
*/
int check_cycle(listint_t *list)
{
	listint_t *current;

	current = list;
	while (current != NULL && current->next != NULL)
	{
		current = current->next->next;
		list = list->next;
		if (current == list)
			return (1);
	}
	return (0);
}
