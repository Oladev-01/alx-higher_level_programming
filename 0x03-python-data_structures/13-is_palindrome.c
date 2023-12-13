#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the pointer to the first element of the list
 * Return: 1 if it is a palindrome, 0 if it is not, or -1 for failure
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	int *check;
	int size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		size++;
		slow = slow->next;
	}

	if (fast != NULL)
		slow = slow->next;

	check = malloc((size / 2) * sizeof(int));
	if (check == NULL)
		return (-1);

	for (i = 0; i < size; i++)
	{
		check[i] = slow->n;
		slow = slow->next;
	}

	slow = *head;
	for (i = size - 1; i >= 0; i--)
	{
		if (slow->n != check[i])
		{
			free(check);
			return (0);
		}
		slow = slow->next;
	}

	free(check);
	return (1);
}
