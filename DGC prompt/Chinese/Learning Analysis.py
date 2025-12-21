"""
您是一位资深的数学教育专家和学习分析师。请您对这次中学生小组协作学习过程进行深度分析和总结。

[数学题目]:
{game.math_problem}

[标准解答]:
{game.standard_solution}

[完整对话历史]:
{game.dialogue_history}

[学生基本信息]:
"""

# 添加每个学生的基本信息和解答变化
for agent in game.agents:
  summary_prompt += f"""

学生: {agent.name}
数学水平: {agent.math_level.get('overall_ability', '未知') if agent.math_level else '未知'}
发言次数: {len(agent.messages)}
发言轮次: {agent.speaking_history}

解答变化历程:
"""
  
  if hasattr(agent, 'personal_solution_history') and agent.personal_solution_history:
    for i, solution_item in enumerate(agent.personal_solution_history):
      summary_prompt += f"    版本{i+1} (消息#{solution_item['timestamp']}): {solution_item['solution']}\n"
  else:
    summary_prompt += f"    当前解答: {getattr(agent, 'personal_solution', '无')}\n"

summary_prompt += f"""

[分析要求]:
请从以下几个维度进行深入分析和总结：

1. **讨论过程分析**:
   - 整体讨论的逻辑脉络和发展阶段
   - 学生们的协作模式和互动特点
   - 关键转折点和突破性时刻
   - 讨论中出现的主要争议和分歧

2. **个体学习变化**:
   - 每个学生在讨论过程中的表现特点
   - 学生解答的演变轨迹和改进情况
   - 学生对数学概念理解的深化过程
   - 个体学习风格和参与方式的观察

3. **协作学习效果**:
   - 同伴互助对学习的促进作用
   - 不同数学水平学生之间的相互影响
   - 集体智慧的体现和知识建构过程
   - 协作中暴露的问题和改进空间

4. **数学理解评估**:
   - 学生们最终对题目的掌握程度
   - 常见错误类型和认知障碍
   - 数学思维能力的展现
   - 解题策略的多样性和有效性

5. **教学启示**:
   - 这次讨论对教学设计的启发
   - 小组协作学习的优势和局限
   - 个性化学习支持的建议

[输出要求]:
请用中文撰写一份详细的分析报告，结构清晰，论述深入，既要有宏观的整体把握，也要有微观的细节观察。报告应该对教育实践具有指导意义。
"""