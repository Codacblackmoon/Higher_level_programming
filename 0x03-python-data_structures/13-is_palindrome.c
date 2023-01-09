#include "list.h"
/**
 * reverse - reverses the second half of the list
 *
 * @h_r: head of the second half
 * Return: no return
 */

void reverse(listint_t **h_r)
{
    listint_t *prv;
    listint_t *crr;
    listint_t *nxt;

    prv = NULL;
    crr = *h_r;

    while (crr != NULL)
    {
        nxt = crr->next;
        crr->next = prv;
        prv = crr;
        crr = nxt;
    }

    *h_r = prv;
}
