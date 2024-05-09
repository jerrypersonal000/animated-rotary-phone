import streamlit as st
from collections import deque

def shortest_path_to_range(A, B, C):
    queue = deque([(A, 0, [])])
    visited = set()
    operations = list(range(1, 10))
    max_limit = 10000  # 假设设置一个数值上限

    while queue:
        current, steps, path = queue.popleft()
        
        if B <= current <= C:
            return steps, path
        
        if abs(current) > max_limit:
            continue
        
        for op in operations:
            next_steps = [
                (current + op, f"{current} + {op} = {current + op}"),
                (current - op, f"{current} - {op} = {current - op}"),
                (current * op, f"{current} * {op} = {current * op}"),
                (current // op if op != 0 else None, f"{current} // {op} = {current // op}" if op != 0 else None)
            ]
            for result, desc in next_steps:
                if result is not None and result not in visited and abs(result) <= max_limit:
                    visited.add(result)
                    queue.append((result, steps + 1, path + [desc]))
    
    return -1, []

A = st.number_input("请输入初始值 A: ", step=1)
B = st.number_input("请输入区间下限 B: ", step=1)
C = st.number_input("请输入区间上限 C: ", step=1)

steps, path = shortest_path_to_range(A, B, C)
if steps != -1:
    st.write(f"从 {A} 到区间 [{B}, {C}] 的最短路径需要 {steps} 步")
    st.write("操作步骤如下：")
    for p in path:
        st.write(p)
else:
    st.write(f"没有找到从 {A} 到区间 [{B}, {C}] 的路径。")
