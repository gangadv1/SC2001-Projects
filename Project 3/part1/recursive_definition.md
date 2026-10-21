
# Part (1): Recursive Definition of P(C)

## Problem Definition

We are given a knapsack with capacity C and n types of objects.

Each object type i has:
- Weight: w_i
- Profit: p_i

There is an unlimited supply of each object type.

Let P(C) represent the maximum total profit obtainable without exceeding the knapsack capacity C.

## Recursive Definition

Base case:

P(0) = 0

For C > 0:

P(C) = max(0, max(p_i + P(C - w_i)))

where the inner maximum considers all object types i satisfying w_i <= C.

## Explanation

For a knapsack of capacity C, we consider every object type whose weight does not exceed C.

If we select object i, we gain profit p_i and reduce the remaining capacity to C - w_i.

The maximum profit obtainable from the remaining capacity is P(C - w_i).

Therefore, the total profit from selecting object i is:

p_i + P(C - w_i)

We evaluate this expression for every object type that fits and select the maximum value.

If no object fits into the remaining capacity, the maximum additional profit is 0.

Since each object type has an unlimited supply, the same object may be selected repeatedly.
