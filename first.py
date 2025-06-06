import streamlit as st
import pandas as pd
st.title("🕶xujianyang-数字档案")
st.header("🔑 基础信息")
st.subheader("学生ID:NEO-2023-001")
st.markdown('注册时间: :green[2023-10-01 08:30:17]: | 精神状态: ✅ 正常')
st.markdown('当前教室: :green[实训楼301]: | 安全等级: :green[绝密]')
st.header("📊技能矩阵")
c1, c2, c3 = st.columns(3)
c1.metric(label="python", value="95", delta="+2%")
c2.metric(label="java", value="87", delta="-1%")
c3.metric(label="c语言", value='68', delta="-10%", delta_color="off")
st.header("Streamlit 课程进展")
st.progress(33)
import streamlit as st
import pandas as pd
st.header("📜 任务日志")

data={
        '日期': ['2025-03-10', '2025-03-12', '2025-03-15'],
        '任务': ['档案开发', '接口调试', '数据可视化优化'],
        '状态': ['完成', '进行中', '未完成'],
        '难度': ['★★★☆', '★★★★', '★☆☆☆'],
}
index=pd.Series(['0','1','2'],name='序号')
df = pd.DataFrame(data,index=index)
st.dataframe(df)
import streamlit as st
st.title("🔐 最新代码成果")
python_code = '''def matrix_breach():
     while True:
         if detect_vulnerability():
             exploit()
             return "ACCESS GRANTED"
         else:
                stealth_evade()")
'''
st.code(python_code)
st.write('`>> SYSTEM NESSAGE:`下一个任务目标已解锁...')
st.write('`>>TARGET:`课程管理系统')
st.write('`>> COUNTDOWNN:`2025-06-03 15:24:58')