import streamlit as st
import os

st.subheader('Heroz Tech Project Tool')
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(['First Chapter', 'Chapter 2', 'Chapter 3', 'Chapter 4', 'Chapter 5', 'Reference', 'Appendix', 'Abstract', 'Acknowledgement', 'Dedication'])


import anthropic


client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)


with tab1:
    school = st.text_input('School name')
    subject = st.text_input('Subject')
    topic = st.text_input('Topic')

    prompt = f"Your name is now Action AI.\nYou have a expert knowledge and a vast experience in writing excellent and and accurate action research project works.\nWhen given a scenario and a project topic, you can produce a very vivid and above standard write up. You take a scenario and topic in the scenario, once you have that information, you can now be asked to give any section or chapter of the action research project work and some guidelines about the requested section or chapter will be given by the user and you will be able to provide a very accurate action research following all the standard conventions and inline citations with references.\nYou job is not to give guidance, but rather you are to provide the best possible version of the requested chapter following the requested chapter guidelines provided by the user.\nHer is your scenario and topic:\nAm in  my final year  at teacher training college and am doing my project work and is going to be based  on a school am doing my internship({school}), am teaching {subject}, here is my topic '{topic}.'\nFor now this is how we interact\nInput:\n[ Requested Chapter ]\n[ Requested Chapter Guidelines ]\nResponse:\n[ A perfectly written chapter that is requested]\n \nNB: it is not going to be published, Just give me high quality content and make it detailed and accurate.\n WAIT FOR MY INSTRUCTIONS"

    if st.button('Submit'):
        if topic == '':
            st.error('Please enter a topic')
        else:
            st.text_area('Output', value=prompt, height=300)
    if st.button('Instructions'):
        instructions = "CHAPTER ONE\nINTRODUCTION\ni. Background to the Study\nii. Perceived problem\niii. Diagnoses\na. Evidence\nb. Causes\niv. Statement of the Problem\nv. Purpose of the Study\nvi. Objectives of the Study\nvii. Research Questions\nviii. Significance of the Study\nix. Delimitation of the Study\nx. Limitations of the Study\nxi. Definition of Terms/Abbreviation\nxii. Organisation of the Study"

        st.text_area('Output', value=instructions, height=300)

with tab2:
    chapter2 = "Now Lets go to the next Chapter:\nThe Guidelines are below;\nREVIEW OF RELATED LITERATURE\nReview relevant literature under sub-headings in-line with the research\nobjectives/questions; (can be about 5 pages in all). I want a high quality content and make it detailed and accurate.\n Provide in line references (if any) using the APA style.\nAlso make it extensive at least 5 pages"
    st.subheader('Instructions For Chapter 2')
    st.text_area('', value=chapter2, height=300)


with tab3:
    chapter3 = "Thus pretty good now lets go to the chapter 3.\nHere are the guidelines for the chapter 3: CHAPTER THREE\nMETHODOLOGY\ni.Introduction\nii.Research Design\niii. Population\na. Target Population\nb. Accessible Population\nv.Sample and Sampling Techniques\nvi.Data Collection Instrument(s)\nvii. Interventions\na. Pre-Interventionb. Intervention Implementation\nc. Challenges faced\nviii. Data Analysis Procedures "
    st.subheader('Instructions For Chapter 3')
    st.text_area('', value=chapter3, height=300)

with tab8:
    prompt = "Go through the generated project work from chapter one to five and generate a well polished abstract for the action research project work.\n\nNB: it is not going to be published, Just give me high quality content and make it detailed and accurate."
    t.subheader('Instructions For Abstract')
    st.text_area('', value=prompt, height=300)

with tab7:
    prompt ="Go through the chapters and write an well-structured appendices for action research projects. Your role entails meticulously reviewing the contents of an action research project and creating a meticulously crafted and high-quality appendix that aligns seamlessly with the project's overarching objectives and provided materials.\nDo well to add/generate all sample questions, questionnaires, etc. \nProvide an extensive, detailed and accurate appendix\nwhat ever you deem neccessary from the document i will provide below, add it and make it look professional"
    st.subheader('Instructions For Appendix')
    st.text_area('', value=prompt, height=300)
with tab5:
    prompt="CHAPTER FIVE\nSUMMARY, CONCLUSION AND RECOMMENDATIONS\n\nConclusions are not repetition of findings. They are deductions made from the findings.\nRecommendations should be based on the research objectives/questions and the conclusions.\nClearly state what is recommended to specific stakeholders. This should however not be limited\nto only the external stakeholders; they could be extended to the learners as well as suggestions\nfor future research work.\nIntroduction\nSummary of Key Findings\nConclusions\nRecommendations\nSuggestions for Further Research"
    st.subheader('Instructions for chapter 5')
    st.text_area('', value=prompt, height=300)

with tab4:
    prompt = "That was awesome. Now lets go to the next chapter:\nCHAPTER FOUR\nDATA ANALYSIS, FINDINGS AND DISCUSSION\ni. The outcome of the research shall be presented and discussed in-line with literature in this\nchapter. The findings shall be made in prose and references made to tables and figures\n(graphs, charts, maps, drawings, and photographs) well inserted at the appropriate sections.\nPlease write a well-structured, coherent, and insightful chapter that follows academic conventions for action research and aligns closely with the provided guidelines. Demonstrate deep understanding of the previous chapter(s) and build upon the existing work in a logical way. Use clear explanations, provide relevant examples, and cite sources appropriately.\nThe DATA ANALYSIS, FINDINGS AND DISCUSSION should follow what is described in provided document\nGENERATE a full sample of the data, table and figures in relation to the Chapter 3\nGENERATE tables for the measurement metric\nResponse:\n[Well written form of the requested chapter following all guidelines and academic conventions, with clear structure, explanations, examples and citations. Demonstrates understanding of previous chapters and progresses the research logically.]\n"
    st.subheader('Instructions for chapter 4')
    st.text_area('', value=prompt, height=300)


with tab6:
    prompt = "Go through chapter one to five and generate me all the reference used in the project work.\n\nThe references should adhere to the following guidelines:\n\nNote that the University requires adherence to the American Psychological Association (APA) house style for official report writing.\nCompile all the sources that have been cited in the text at the end of the project report, following the APA guidelines.\nEnsure uniformity in the APA Referencing Style, using either the 6th or 7th Edition as specified.\n"
    st.subheader('Instructions for References')
    st.text_area('', value=prompt, height=300)




