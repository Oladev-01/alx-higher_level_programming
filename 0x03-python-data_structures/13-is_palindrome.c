#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the pointer to the first element of the list
 * Return: 1 if it is a palindrome, 0 if it is not, or -1 for failure
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int a = 0, *check_1, b;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	current = *head;
	while (current != NULL)
	{
		a++;
		current = current->next;
	}
	check_1 = malloc(((a / 2) - 3) * sizeof(int));
	current = *head;
	for (b = 0; b < a / 2; b++)
	{
		check_1[b] = current->n;
		current = current->next;
	}
	if (a % 2 != 0)
		current = current->next;
	b--;
	while (current != NULL)
	{
		if (current->n != check_1[b])
			return (0);
		current = current->next;
		b--;
	}
	return (1);
}
