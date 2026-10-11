# 2778. Sum of Squares of Special Elements

[LeetCode problem](https://leetcode.com/problems/sum-of-squares-of-special-elements/)

## Approach

An array position is special when it divides the array length `n`. Divisors come in pairs: if `d` divides `n`, then `n // d` also divides `n`.

Check candidate divisors only while `d * d <= n`. For each divisor found, add the squares of the values at both paired positions. The problem uses 1-based positions, so position `p` corresponds to Python index `p - 1`.

When `d` is the square root of `n`, it pairs with itself. The equality check prevents adding that element twice.

## Core Pattern

**Divisor-pair enumeration:** inspect possible factors up to the square root and process each divisor pair together.

## Complexity

- **Time:** `O(√n)`, since at most `√n` candidate divisors are checked.
- **Space:** `O(1)`, using only a few variables.
