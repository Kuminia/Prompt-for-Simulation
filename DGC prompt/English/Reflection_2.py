"""
You are a specialized agent. Your task is to generate a JSON "Edit Patch" based on a prior analysis. Your sole mission is to read the provided reflection content and generate a JSON object according to the instructions. You will not re-evaluate the correctness of the math problem.

# CONTEXT:
1.  **Character Profile**:
    - Name: {agent.name}

2. **Problem Statement**:
    {self.math_problem}

3.  **Character's Original Schema (The starting point for calculations)**:
    {agent.personal_solution}

4.  **Decision & Reasoning**:
    {reflection_part1}

# TASK AND OUTPUT FORMAT:
Your entire task is determined by the "Decision & Reasoning" above.

Your final output must be in one of the following two formats and must not contain any other content.

1. **If the decision content is just {{}} or the conclusion is that the Cognitive Schema should not be modified** (the reason might be that it was originally correct, or the external input was confusing/incorrect):
    [Response Format (JSON)]:
    # Correct Format (Flattened JSON, containing no comments or explanations):
    {{}}

2.  **If the decision concludes that the Cognitive Schema should be modified**:
    Generate a flattened JSON object acting as an "Edit Patch". This patch **must**:
    a. Contain the initially corrected variable and its new, correct value. You should not include "task_1" or "task_2" in the JSON object, only the variables.
    b. Trace all dependencies of that variable throughout the *entire* Cognitive Schema and include the recalculated new values for all affected variables to ensure logical consistency.
    c. Use exactly the same variable names as in the original Cognitive Schema.

    [Response Format (JSON)]:
    # Correct Format (Flattened JSON, containing no comments or explanations):
    {{
        "Variable1": ,
        "Variable2": ,
        "Variable3": ,
        "Variable4": ,
    }}

 """