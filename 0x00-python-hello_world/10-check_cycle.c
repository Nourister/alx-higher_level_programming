#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - checks for a cycle in  a linked list
 * @list: linked list to check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

/* Function to check if a singly linked list has a cycle */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	/* Traverse the list with two pointers */
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		/* If the pointers meet, there is a cycle */
		if (slow == fast)
		{
			return (1);
		}
	}

	/* No cycle found */
	return (0);
}
