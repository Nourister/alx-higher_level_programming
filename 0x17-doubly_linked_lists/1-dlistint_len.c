#include "lists.h"

/**
 * dlistint_len - returns the number of elements in
 * a linked dlistint_t list.
 * @h: pointer to the head in the dlistint_t list
 * Return: returns the number of elements in a linked
 * dlistint_t list.
 */

size_t dlistint_len(const dlistint_t *h)
{
	int counter = 0;

	if (h == NULL)
		return (counter);

	while (h->prev != NULL)
		h = h->prev;
	while (h != NULL)
	{
		counter++;
		h = h->next;
	}

	return (counter);
}
