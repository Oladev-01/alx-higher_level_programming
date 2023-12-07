#include "lists.h"
/**
 * insert_node - this function inserts a number into a sorted linked lists
 * @head: this is the pointer to the pointer to the head of the list
 * @number: this is the data to be added into the node
 * Return: the address of the added node or NUll if it fails
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *ptr, *hold;

	if (head == NULL)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL)
		*head = new_node;
	ptr = *head;
	while (ptr && ptr->next)
	{
		if (ptr->n < number && number < ptr->next->n)
		{
			hold = ptr->next;
			ptr->next = new_node;
			new_node->next = hold;
			return (new_node);
		}
		ptr = ptr->next;
	}
	ptr->next = new_node;
	return (new_node);
}
