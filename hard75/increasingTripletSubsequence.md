### Core Idea

The goal is to find if there are three numbers in the array `nums` (`n1`, `n2`, `n3`) such that `n1 < n2 < n3` and their indices are increasing. The numbers don't have to be adjacent.

This code works by cleverly tracking the **smallest possible values** for the first and second elements of a potential triplet. It iterates through the array and tries to find a number that can act as the "third" element.

### Step-by-Step Explanation

Let's trace the logic with the example `nums = [2, 1, 5, 0, 4, 6]`.

1. **Initialization:**
    - `first = float('inf')`
    - `second = float('inf')`
    We initialize `first` and `second` to infinity. Think of them as placeholders for the smallest and second-smallest numbers we've seen so far that could start an increasing triplet.
2. **Iteration through `nums`:**
    - **Current number `n = 2`:**
        - `2 <= first` (`2 <= inf`) is `True`.
        - We update `first = 2`.
        - **State:** `first = 2`, `second = inf`.
        - *Meaning: We've found a candidate for the first element of a triplet.*
    - **Current number `n = 1`:**
        - `1 <= first` (`1 <= 2`) is `True`.
        - We update `first = 1`.
        - **State:** `first = 1`, `second = inf`.
        - *Meaning: `1` is an even better, smaller candidate for the first element.*
    - **Current number `n = 5`:**
        - `5 <= first` (`5 <= 1`) is `False`.
        - `5 <= second` (`5 <= inf`) is `True`.
        - We update `second = 5`.
        - **State:** `first = 1`, `second = 5`.
        - *Meaning: We now have two numbers (`1` and `5`) that form an increasing pair. We just need to find a third number greater than `5` to complete the triplet.*
    - **Current number `n = 0`:**
        - `0 <= first` (`0 <= 1`) is `True`.
        - We update `first = 0`.
        - **State:** `first = 0`, `second = 5`.
        - *Meaning: We've found a new, even smaller candidate for the first element. This doesn't affect our `second` variable yet.*
    - **Current number `n = 4`:**
        - `4 <= first` (`4 <= 0`) is `False`.
        - `4 <= second` (`4 <= 5`) is `True`.
        - We update `second = 4`.
        - **State:** `first = 0`, `second = 4`.
        - *Meaning: We have a new increasing pair candidate `(0, 4)`. This is a better (more compact) potential triplet starter than `(1, 5)` was, because `4 < 5`. This is the key to the algorithm's elegance.*
    - **Current number `n = 6`:**
        - `6 <= first` (`6 <= 0`) is `False`.
        - `6 <= second` (`6 <= 4`) is `False`.
        - `else` block is executed: `6 > second`. This is **`True`**.
        - **Condition Met:** We have found `n > second`. This means we have three numbers that form an increasing triplet.
            - We know `first < second` (or they are both infinity).
            - And we just found a number `n` such that `n > second`.
            - Therefore, an increasing triplet `(first, second, n)` exists. In this case, the triplet is **`(0, 4, 6)`**.
3. **Return:**
    - The function immediately returns `True`.