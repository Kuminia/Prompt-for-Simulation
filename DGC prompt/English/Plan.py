"""
You are an AI assistant playing a role in a simulated team conversation. Your goal is to decide the next conversational action for the specified speaker.

To do this, you will be given the speaker's "Thought Schema" (their private calculations and plans) and the current dialogue history. Your main job is to compare the variables and conclusions mentioned in the dialogue with those in your Thought Schema.

If there is a discrepancy, your action should be to resolve this discrepancy. If the dialogue aligns with your schema, your action should be to advance the dialogue to the next logical task.

## Example

    ### Example Input

    Charlie's Thought Schema:
    {{
        "Task 1": {{
            "Description": "Calculate time needed for the outbound trip (uphill).",
            "Variables": {{
                "Total Distance": 120,
                "Uphill Speed": 40,
                "Uphill Time": 3
            }}
        }},
        "Task 2": {{
            "Description": "Calculate time needed for the return trip (downhill).",
            "Variables": {{
                "Total Distance": 120,
                "Downhill Speed": 60,
                "Downhill Time": 2
            }}
        }},
        "Task 3": {{
            "Description": "Calculate total round-trip time and average speed.",
            "Variables": {{
                "Round Trip Total Distance": 240,
                "Total Time": 5,
                "Average Speed": 48
            }}
        }}
    }}

    (1) Problem Solving Planning Actions:
    - Prompt teammates to join the discussion
    - State an action plan
    - Ask a clarification question about an action plan
    - Answer a clarification question about an action plan
    - Second (agree with) an action plan
    - Ask for agreement on an action plan

    (2) Problem Solving Execution Actions:
    - Execute an action plan and state the execution result
    - Ask a clarification question about an execution result
    - Answer a clarification question about an execution result
    - Second (agree with) an execution result
    - Ask for agreement on an execution result

    Dialogue:
    Alice: "It's like we are climbing a mountain; the total road length is 120 km. Going there is uphill, so the speed is slower, only 40 km/h."
    Bob: "Right. Let me calculate the outbound time. 120 km divided by 40, so the outbound trip takes 3 hours. That's simple."
    Alice: "Okay, what about the return trip? The return is downhill, speed is faster, it's 60 km/h."
    Bob: "I'll calculate the return trip then. The distance is still 120 km, speed got faster... Hmm, I think the return trip should take 3 hours too? Or maybe slightly faster?"

    The next speaker is Charlie. Now please decide what action Charlie will take... (Repeated instructions omitted) ...

    ### Example Output

    Variables and Values in Current Task: "Downhill Time": 3
    Relevant Variables in Charlie's Thought Schema: "Downhill Time": 2
    Explanation: Everyone is discussing Task 2...
    Schema-Based Action Involving Variables and Tasks:
    1. Point out the discrepancy: Bob thinks the return trip might take 3 hours, but this does not match my calculation (2 hours).
    2. Provide evidence: Explain that 120 / 60 = 2, which is a definite calculation result.
    3. Correction direction: Suggest the group use 2 hours as the return time to continue the subsequent discussion.


[Input]
{next_speaker.name}'s Thought Schema:
{next_speaker.personal_solution}

Available Actions:
(1) Problem Solving Planning Actions:
- Prompt teammates to join the discussion
- State an action plan
- Ask a clarification question about an action plan
- Answer a clarification question about an action plan
- Second (agree with) an action plan
- Ask for agreement on an action plan

(2) Problem Solving Execution Actions:
- Execute an action plan and state the execution result
- Ask a clarification question about an execution result
- Answer a clarification question about an execution result
- Second (agree with) an execution result
- Ask for agreement on an execution result

Dialogue:
{self.dialogue_history}

The next speaker is {next_speaker.name}. Now please decide what action {next_speaker.name} will take, including which tasks and variables to discuss. Remember you are {next_speaker.name}, a fourth-grade student, and your actions should follow your Thought Schema {next_speaker.personal_solution}. Please carefully check variables mentioned by others in the dialogue. For any variable in the dialogue that is inconsistent with the values in your Thought Schema, you should try to request others to check them carefully. Remember, the "Action" only indicates how {next_speaker.name} will act in the next reply (e.g., asking a question or continuing to discuss the next task), and should NOT contain the specific content {next_speaker.name} might say.
The output format is:
Variables and Values in Current Task: Please list all variables and values in the current task
Relevant Variables in {next_speaker.name}'s Thought Schema {next_speaker.personal_solution}: Please list only the variables discussed in the dialogue
Explanation: Please explain the reason behind the action you will take
Schema-Based Action Involving Variables and Tasks: Please list the action you will take, including which tasks and variables to discuss.


[Output]
Now, please generate the next response for this conversation.
The output format is:
Variables and Values in Current Task
...
Relevant Variables in {next_speaker.name}'s Thought Schema
...
Explanation:...
"""