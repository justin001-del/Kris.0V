import streamlit as st
import pandas as pd
import numpy as np

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)


if "user_answer" not in st.session_state:
        st.session_state["user_answer"]=""

user_input=""


st.title("Kris.0V")
import random

quotes = [
    "✨ The first step to progress is knowing how you work.",
    "🌀 You don’t need to be perfect — just aware.",
    "🌿 Growth starts where understanding begins.",
    "🔍 Every system begins with self-discovery.",
    "💡 Even chaos has patterns — find yours.",
    "📘 This isn’t just a quiz. It’s a mirror.",
]

quote = random.choice(quotes)
st.markdown( quote)



architect_answers = []
sprinter_answers = []
wanderer_answers = []

st.write("What stresses you the most?")
a1=st.checkbox("(chaos, disorganization, no plan)")
a2=st.checkbox( "(too much structures or boring tasks)")
a3=st.checkbox("(harsh pressure or being forced to do something)")

if a1:
        st.success("done")
        architect_answers.append(a1)
        if a2:
                st.warning("select any one")
                st.stop()
        if a3:
                st.warning("select any one")
                st.stop()
if a2:
        st.success("done")
        sprinter_answers.append(a2)
        if a1:
                st.warning("select any one")
                st.stop()
        if a3:
                st.warning("select any one")
                st.stop()

if a3:
        st.success("done")
        wanderer_answers.append(a3)
        if a2:
                st.warning("select any one")
                st.stop()
        if a1:
                st.warning("select any one")
                st.stop()

st.write("What motivates you deep down?")

b1=st.checkbox("(The satisfaction of clarity and control.)")
b2=st.checkbox("(The rush of urgency and being “in the zone.”)")
b3=st.checkbox("(Doing things my way and feeling good about it.)")

if b1:
        st.success("done")
        architect_answers.append(b1)
        if b2:
                st.warning("select any one")
                st.stop()
        if b3:
                st.warning("select any one")
                st.stop()
if b2:
        st.success("done")
        sprinter_answers.append(b2)
        if b1:
                st.warning("select any one")
                st.stop()
        if b3:
                st.warning("select any one")
                st.stop()

if b3:
        st.success("done")
        wanderer_answers.append(b3)
        if b2:
                st.warning("select any one")
                st.stop()
        if b1:
                st.warning("select any one")
                st.stop()

# Question 3
st.write("what happens if someone is supervising ur work like a teacher behind a student in a exam hall?")  
c1 = st.checkbox("doesn't matter i do it any way")  
c2 = st.checkbox("(suddenly i'm 2x much faster)")  
c3 = st.checkbox("(i feel awkward and wants to work alone )")  

if c1:  
    st.success("done")  
    architect_answers.append(c1)  
    if c2 or c3:  
        st.warning("select any one")  
        st.stop()  
if c2:  
    st.success("done")  
    sprinter_answers.append(c2)  
    if c1 or c3:  
        st.warning("select any one")  
        st.stop()  
if c3:  
    st.success("done")  
    wanderer_answers.append(c3)  
    if c1 or c2:  
        st.warning("select any one")  
        st.stop()  

# Question 4
st.write("You’ve got a task due next week. What do you actually do?")  
d1 = st.checkbox("Plan it out across days and get started calmly.")  
d2 = st.checkbox("(Procrastinate until the last possible moment — then GO GO GO.)")  
d3 = st.checkbox("(Think about doing it, maybe journal about it… then distract yourself. )")  

if d1:  
    st.success("done")  
    architect_answers.append(d1)  
    if d2 or d3:  
        st.warning("select any one")  
        st.stop()  
if d2:  
    st.success("done")  
    sprinter_answers.append(d2)  
    if d1 or d3:  
        st.warning("select any one")  
        st.stop()  
if d3:  
    st.success("done")  
    wanderer_answers.append(d3)  
    if d1 or d2:  
        st.warning("select any one")  
        st.stop()  

# Question 5
st.write("What’s your natural work energy?")  
e1 = st.checkbox("(Consistent & focused when the environment is right.)")  
e2 = st.checkbox("(Random bursts of insane focus under pressure.)")  
e3 = st.checkbox("(I need the vibe — mood, music, comfort — or it ain’t happening)")  

if e1:  
    st.success("done")  
    architect_answers.append(e1)  
    if e2 or e3:  
        st.warning("select any one")  
        st.stop()  
if e2:  
    st.success("done")  
    sprinter_answers.append(e2)  
    if e1 or e3:  
        st.warning("select any one")  
        st.stop()  
if e3:  
    st.success("done")  
    wanderer_answers.append(e3)  
    if e1 or e2:  
        st.warning("select any one")  
        st.stop()  

# Question 6
st.write("You try a new to-do method. What happens?")  
f1 = st.checkbox("(I adapt it into my structured system.)")  
f2 = st.checkbox("(i forgot it unless it's tied to a dead line)")  
f3 = st.checkbox("(I try it if it looks fun or cool… otherwise nope. )")  

if f1:  
    st.success("done")  
    architect_answers.append(f1)  
    if f2 or f3:  
        st.warning("select any one")  
        st.stop()  
if f2:  
    st.success("done")  
    sprinter_answers.append(f2)  
    if f1 or f3:  
        st.warning("select any one")  
        st.stop()  
if f3:  
    st.success("done")  
    wanderer_answers.append(f3)  
    if f1 or f2:  
        st.warning("select any one")  
        st.stop()  

# Question 7
st.write("you want to track your progress, you:")  
g1 = st.checkbox("(Use a planner or digital board to track everything.)")  
g2 = st.checkbox("(Just remember the big wins (or scramble when asked).)")  
g3 = st.checkbox("(Track it through creative means — journal, visuals, mood boards. )")  

if g1:  
    st.success("done")  
    architect_answers.append(g1)  
    if g2 or g3:  
        st.warning("select any one")  
        st.stop()  
if g2:  
    st.success("done")  
    sprinter_answers.append(g2)  
    if g1 or g3:  
        st.warning("select any one")  
        st.stop()  
if g3:  
    st.success("done")  
    wanderer_answers.append(g3)  
    if g1 or g2:  
        st.warning("select any one")  
        st.stop()



user_type = ""
if len(architect_answers) > len(sprinter_answers) and len(architect_answers) > len(wanderer_answers):
    user_type = "Architect...(🧱🧠)"
elif len(sprinter_answers) > len(architect_answers) and len(sprinter_answers) > len(wanderer_answers):
    user_type = "Sprinter...(🚀🤍)"
elif len(wanderer_answers) > len(architect_answers) and len(wanderer_answers) > len(sprinter_answers):
    user_type = "Wanderer...(🌙✨)"

elif len(architect_answers) == len(sprinter_answers)> len(wanderer_answers) :
    user_type = "Strategist...(⚡🧠)"
elif len(sprinter_answers) == len(wanderer_answers) > len(architect_answers):
     user_type= "Strom chaser...(🌪️🎧)"
elif len(architect_answers)== len(wanderer_answers)> len(sprinter_answers):
     user_type="Alchemist...(🌀📘)"
elif  len(architect_answers)== len(wanderer_answers)==len(sprinter_answers):
     user_type="Shapeshifter...(🧪🔮)"



st.success(f"You're a {user_type}!")
st.session_state["user answer"]=user_type


df=pd.DataFrame({"user_type":[user_type]})
st.write("hi",user_type)
st.dataframe(df)

csv=df.to_csv(index=False).encode("utf-8")

st.download_button(label="click here to download the result as CSV", data=csv, file_name="quize_result csv", mime="text/csv")



with st.expander("click here to know about your character's trait(Not mandatory)"):
     q=["Architect...(🧱🧠)","Sprinter...(🚀🤍)","Wanderer...(🌙✨)","Strategist...(⚡🧠)","Strom chaser...(🌪️🎧)","Alchemist...(🌀📘)","Shapeshifter...(🧪🔮)"]
     s=st.selectbox("every one have their own pros and cons",q)
     option=q.index(s)

     if option==0:
          st.write(""" 🧱Loves structure, systems, and planning.
                   🧱Gets high on clarity and long-term vision.
                   🧱Deeply focused when the environment is organized
                   🧱Avoids chaos like it’s a plague
                   🧱Thinks in flowcharts, not feelings("practical guru")""")
     elif option==1:
          st.write(""" 🤍Last-minute genius with a turbo brain.
                   🤍Gets bored without urgency.
                   🤍Performs best when the pressure is high.
                   🤍Momentum is short, but powerful.
                   🤍Loves the thrill of the ticking clock.""")
     elif option==2:
          st.write("""🌙intuitive and mood-driven.
                   🌙Works best when inspired.
                   🌙Dislikes rigid systems and external pressure.
                   🌙Deep thinker, often creative and introspective.
                   🌙Prone to wandering… but always returns with treasur""")
          
     elif option==3:
          st.write(""" 🧠Master planner and crisis executor.
                   🧠Loves mixing logic with adrenaline.
                   🧠Can work slow and steady or all-in, depending on the plan.
                   🧠Thrives when strategy meets sprint.
                   🧠Gets annoyed by sloppy randomness""")

     elif option==4:
          st.write("""🌪️intense, wild, magnetic energy.
                   🌪️Loves chaos — finds creativity in the mess.
                   🌪️Deeply emotional but explosively productive.
                   🌪️Unpredictable work patterns.
                   🌪️Cannot be tamed (and kinda likes that)""")

     elif option==5:
          st.write("""📘Organizes with heart, not just logic.
                   📘Turns ideas into tangible, beautiful results.
                   📘Needs emotional connection to structure.
                   📘Peaceful, poetic, and powerful.
                   📘Gets drained by cold, mechanical systems""")
          
     elif option==6:
          st.write("""🧪A little bit of everything.
                   🧪Can shift modes fluidly — sprint, plan, flow.
                   🧪Hard to pin down, easy to admire.
                   🧪Needs freedom and flexibility.
                   🧪Doesn’t “fit in a box” — and never should""")

     
st.divider()
st.markdown(
    "⚠️ **Note:** This quiz is designed for self-reflection, not diagnosis. "
    "Results are based on your current choices — and humans evolve. "
    "Take it as a starting point, not a final label. 🧩"
)