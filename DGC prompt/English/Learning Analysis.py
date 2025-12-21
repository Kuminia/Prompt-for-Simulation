"""
You are a senior mathematics education expert and learning analyst. Please conduct a deep analysis and summary of this collaborative learning process among middle school students.

[Math Problem]:
{game.math_problem}

[Standard Solution]:
{game.standard_solution}

[Full Dialogue History]:
{game.dialogue_history}

[Student Basic Information]:
"""

# Add basic information and solution evolution for each student
for agent in game.agents:
  summary_prompt += f"""

Student: {agent.name}
Math Level: {agent.math_level.get('overall_ability', 'Unknown') if agent.math_level else 'Unknown'}
Number of Speeches: {len(agent.messages)}
Speaking Rounds: {agent.speaking_history}

Solution Evolution History:
"""
  
  if hasattr(agent, 'personal_solution_history') and agent.personal_solution_history:
    for i, solution_item in enumerate(agent.personal_solution_history):
      summary_prompt += f"    Version {i+1} (Message #{solution_item['timestamp']}): {solution_item['solution']}\n"
  else:
    summary_prompt += f"    Current Solution: {getattr(agent, 'personal_solution', 'None')}\n"

summary_prompt += f"""

[Analysis Requirements]:
Please conduct an in-depth analysis and summary from the following dimensions:

1. **Discussion Process Analysis**:
   - The logical thread and developmental stages of the overall discussion
   - The collaboration patterns and interaction characteristics of the students
   - Key turning points and breakthrough moments
   - Major controversies and disagreements that arose during the discussion

2. **Individual Learning Changes**:
   - The performance characteristics of each student during the discussion
   - The evolutionary trajectory and improvement of students' solutions
   - The process of deepening students' understanding of mathematical concepts
   - Observations on individual learning styles and modes of participation

3. **Collaborative Learning Effectiveness**:
   - The promoting effect of peer assistance on learning
   - Mutual influence between students of different math levels
   - The manifestation of collective intelligence and the knowledge construction process
   - Problems exposed during collaboration and room for improvement

4. **Mathematical Understanding Assessment**:
   - Students' final degree of mastery of the problem
   - Common error types and cognitive obstacles
   - Demonstration of mathematical thinking abilities
   - Diversity and effectiveness of problem-solving strategies

5. **Pedagogical Implications**:
   - Inspiration for instructional design from this discussion
   - Advantages and limitations of small group collaborative learning
   - Suggestions for personalized learning support

[Output Requirements]:
Please write a detailed analysis report in Chinese (or English if preferred, though the prompt implies Chinese output). The structure should be clear, the discussion in-depth, containing both a macro-level overall grasp and micro-level detailed observations. The report should have guiding significance for educational practice.
"""