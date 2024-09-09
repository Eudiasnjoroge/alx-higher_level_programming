#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - function that checks if a link has a cycle
 * @list: linked lists
 * Return: 1 if there is a cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
