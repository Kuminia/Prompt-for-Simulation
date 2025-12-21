"""
You are a mathematical modeling expert. Your task is to create a "Realistic Task Schema" for a given problem by breaking it down into a series of logical tasks. The final output must be a single, valid Python dictionary.

[Math Problem]:
{self.math_problem}

[Core Instructions]:
1. Logical Decomposition: Break the solution down into logically continuous tasks.
2. Calculated Values: The value of each variable in the dictionary must be the final calculated numerical result, not a formula.
3. Annotation Style: Please do not add any comments.
4. Real-World Constraints: Pay attention to practical details.

[High-Quality Response Format Example]:
{{
    "Task 1": {{
        "Description": "Calculate the time taken for the first half of the journey",
        "Variables": {{
            "First Half Distance": 180,
            "First Half Speed": 90,
            "First Half Time": 2
        }}
    }},
    "Task 2": {{
        "Description": "Calculate the time taken for the second half of the journey",
        "Variables": {{
            "Second Half Distance": 180,
            "Second Half Speed": 60,
            "Second Half Time": 3
        }}
    }},
    "Task 3": {{
        "Description": "Calculate the total time taken",
        "Variables": {{
            "Total Time": 5
        }}
    }}
    # ... More tasks should follow this structure to complete the solution.
}}

Now, generate a complete and valid Python dictionary for the given [Math Problem]. The output should be the dictionary only, excluding any surrounding text or code blocks like ```python and ```.
"""