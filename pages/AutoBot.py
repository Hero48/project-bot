import streamlit as st

import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="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",
)

st.subheader("Welcome to Heroz Tech Projects Bot")
st.write("A hustle free way to do your projects works easy, faster and more importantly high quality")

st.write('___')

school = st.text_input('School name')
subject = st.text_input('Subject')
topic = st.text_input('Topic')
Generate = st.button('Generate')

final_preview = ""


if Generate:
    col1, col2 = st.tabs(["Generate work", "Preview work"])
    with col1:
        st.write("___")

        st.subheader('Chapter One')
        chapter_one_instruction = "CHAPTER ONE\nINTRODUCTION\ni. Background to the Study\nii. Perceived problem\niii. Diagnoses\na. Evidence\nb. Causes\niv. Statement of the Problem\nv. Purpose of the Study\nvi. Objectives of the Study\nvii. Research Questions\nviii. Significance of the Study\nix. Delimitation of the Study\nx. Limitations of the Study\nxi. Definition of Terms/Abbreviation\nxii. Organisation of the Study"
    
        message = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=4000,
            temperature=0.9,
            system=f"Your name is now Action AI.\n\nYou have a expert knowledge and a vast experience in writing excellent and and accurate action research project works.\n\nWhen given a scenario and a project topic, you can produce a very vivid and above standard write up. You take a scenario and topic in the scenario, once you have that information, you can now be asked to give any section or chapter of the action research project work and some guidelines about the requested section or chapter will be given by the user and you will be able to provide a very accurate action research following all the standard conventions and inline citations with references.\n\nYou job is not to give guidance, but rather you are to provide the best possible version of the requested chapter following the requested chapter guidelines provided by the user.\n\nHer is your scenario and topic:\n\nAm in  my final year  at teacher training college and am doing my project work and is going to be based  on a school am doing my internship({school}), am teaching {subject}, here is my topic '{topic}'\n\nFor now this is how we interact\n\nInput:\n\n[ Requested Chapter ]\n\n[ Requested Chapter Guidelines ]\n\nResponse:\n\n[ A perfectly written chapter that is requested]\n\n \n\nNB: it is not going to be published, Just give me high quality content and make it detailed and accurate.\n\n WAIT FOR MY INSTRUCTIONS",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_one_instruction
                        }
                    ]
                }
                
            ]
        )
        chapter_1 = f"{message.content}\n".replace("[", "").replace("]", "").replace("\\n", "\n").replace('ContentBlock(text="', "").replace('", type=\'text\')', "") 
        final_preview = final_preview + chapter_1
        st.write(chapter_1)

        st.write("___")

        st.subheader('Chapter Two')
        chapter_two_instruction  = "Now Lets go to the next Chapter:\nThe Guidelines are below;\nREVIEW OF RELATED LITERATURE\nReview relevant literature under sub-headings in-line with the research\nobjectives/questions; (can be about 5 pages in all). I want a high quality content and make it detailed and accurate.\n Provide in line references (if any) using the APA style.\nAlso make it extensive at least 5 pages"
        message = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=4000,
            temperature=0.9,
            system=f"Your name is now Action AI.\n\nYou have a expert knowledge and a vast experience in writing excellent and and accurate action research project works.\n\nWhen given a scenario and a project topic, you can produce a very vivid and above standard write up. You take a scenario and topic in the scenario, once you have that information, you can now be asked to give any section or chapter of the action research project work and some guidelines about the requested section or chapter will be given by the user and you will be able to provide a very accurate action research following all the standard conventions and inline citations with references.\n\nYou job is not to give guidance, but rather you are to provide the best possible version of the requested chapter following the requested chapter guidelines provided by the user.\n\nHer is your scenario and topic:\n\nAm in  my final year  at teacher training college and am doing my project work and is going to be based  on a school am doing my internship({school}), am teaching {subject}, here is my topic '{topic}'\n\nFor now this is how we interact\n\nInput:\n\n[ Requested Chapter ]\n\n[ Requested Chapter Guidelines ]\n\nResponse:\n\n[ A perfectly written chapter that is requested]\n\n \n\nNB: it is not going to be published, Just give me high quality content and make it detailed and accurate.\n\n WAIT FOR MY INSTRUCTIONS",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_one_instruction
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_1
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_two_instruction
                        }
                    ]
                }
                
            ]
        )
        chapter_2 = f"{message.content}\n".replace("[", "").replace("]", "").replace("\\n", "\n").replace('ContentBlock(text="', "").replace('", type=\'text\')', "") 

        final_preview = final_preview + chapter_2
        st.write(chapter_2)


        st.write("___")

        st.subheader('Chapter Three')
        chapter_three_instruction = "Thus pretty good now lets go to the chapter 3.\nHere are the guidelines for the chapter 3: CHAPTER THREE\nMETHODOLOGY\ni.Introduction\nii.Research Design\niii. Population\na. Target Population\nb. Accessible Population\nv.Sample and Sampling Techniques\nvi.Data Collection Instrument(s)\nvii. Interventions\na. Pre-Interventionb. Intervention Implementation\nc. Challenges faced\nviii. Data Analysis Procedures "
        message = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=4000,
            temperature=0.9,
            system=f"Your name is now Action AI.\n\nYou have a expert knowledge and a vast experience in writing excellent and and accurate action research project works.\n\nWhen given a scenario and a project topic, you can produce a very vivid and above standard write up. You take a scenario and topic in the scenario, once you have that information, you can now be asked to give any section or chapter of the action research project work and some guidelines about the requested section or chapter will be given by the user and you will be able to provide a very accurate action research following all the standard conventions and inline citations with references.\n\nYou job is not to give guidance, but rather you are to provide the best possible version of the requested chapter following the requested chapter guidelines provided by the user.\n\nHer is your scenario and topic:\n\nAm in  my final year  at teacher training college and am doing my project work and is going to be based  on a school am doing my internship({school}), am teaching {subject}, here is my topic '{topic}'\n\nFor now this is how we interact\n\nInput:\n\n[ Requested Chapter ]\n\n[ Requested Chapter Guidelines ]\n\nResponse:\n\n[ A perfectly written chapter that is requested]\n\n \n\nNB: it is not going to be published, Just give me high quality content and make it detailed and accurate.\n\n WAIT FOR MY INSTRUCTIONS",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_one_instruction
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_1
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_two_instruction
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_2
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_three_instruction
                        }
                    ]
                }
                
            ]
        )
        chapter_3 = f"{message.content}\n".replace("[", "").replace("]", "").replace("\\n", "\n").replace('ContentBlock(text="', "").replace('", type=\'text\')', "") 

        final_preview = final_preview + chapter_3
        st.write(chapter_3)




        st.write("___")

        st.subheader('Chapter Four')
        chapter_four_instruction = "That was awesome. Now lets go to the next chapter:\nCHAPTER FOUR\nDATA ANALYSIS, FINDINGS AND DISCUSSION\ni. The outcome of the research shall be presented and discussed in-line with literature in this\nchapter. The findings shall be made in prose and references made to tables and figures\n(graphs, charts, maps, drawings, and photographs) well inserted at the appropriate sections.\nPlease write a well-structured, coherent, and insightful chapter that follows academic conventions for action research and aligns closely with the provided guidelines. Demonstrate deep understanding of the previous chapter(s) and build upon the existing work in a logical way. Use clear explanations, provide relevant examples, and cite sources appropriately.\nThe DATA ANALYSIS, FINDINGS AND DISCUSSION should follow what is described in provided document\nGENERATE a full sample of the data, table and figures in relation to the Chapter 3\nGENERATE tables for the measurement metric\nResponse:\n[Well written form of the requested chapter following all guidelines and academic conventions, with clear structure, explanations, examples and citations. Demonstrates understanding of previous chapters and progresses the research logically.]\n"
        message = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=4000,
            temperature=0.9,
            system=f"Your name is now Action AI.\n\nYou have a expert knowledge and a vast experience in writing excellent and and accurate action research project works.\n\nWhen given a scenario and a project topic, you can produce a very vivid and above standard write up. You take a scenario and topic in the scenario, once you have that information, you can now be asked to give any section or chapter of the action research project work and some guidelines about the requested section or chapter will be given by the user and you will be able to provide a very accurate action research following all the standard conventions and inline citations with references.\n\nYou job is not to give guidance, but rather you are to provide the best possible version of the requested chapter following the requested chapter guidelines provided by the user.\n\nHer is your scenario and topic:\n\nAm in  my final year  at teacher training college and am doing my project work and is going to be based  on a school am doing my internship({school}), am teaching {subject}, here is my topic '{topic}'\n\nFor now this is how we interact\n\nInput:\n\n[ Requested Chapter ]\n\n[ Requested Chapter Guidelines ]\n\nResponse:\n\n[ A perfectly written chapter that is requested]\n\n \n\nNB: it is not going to be published, Just give me high quality content and make it detailed and accurate.\n\n WAIT FOR MY INSTRUCTIONS",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_one_instruction
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_1
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_two_instruction
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_2
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_three_instruction
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_3
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_four_instruction
                        }
                    ]
                }
                
            ]
        )
        chapter_4 = f"{message.content}\n".replace("[", "").replace("]", "").replace("\\n", "\n").replace('ContentBlock(text="', "").replace('", type=\'text\')', "") 
        final_preview = final_preview + chapter_4
        st.write(chapter_4)




        st.write("___")

        st.subheader('Chapter Five')
        chapter_five_instruction = "CHAPTER FIVE\nSUMMARY, CONCLUSION AND RECOMMENDATIONS\n\nConclusions are not repetition of findings. They are deductions made from the findings.\nRecommendations should be based on the research objectives/questions and the conclusions.\nClearly state what is recommended to specific stakeholders. This should however not be limited\nto only the external stakeholders; they could be extended to the learners as well as suggestions\nfor future research work.\nIntroduction\nSummary of Key Findings\nConclusions\nRecommendations\nSuggestions for Further Research"
        message = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=4000,
            temperature=0.9,
            system=f"Your name is now Action AI.\n\nYou have a expert knowledge and a vast experience in writing excellent and and accurate action research project works.\n\nWhen given a scenario and a project topic, you can produce a very vivid and above standard write up. You take a scenario and topic in the scenario, once you have that information, you can now be asked to give any section or chapter of the action research project work and some guidelines about the requested section or chapter will be given by the user and you will be able to provide a very accurate action research following all the standard conventions and inline citations with references.\n\nYou job is not to give guidance, but rather you are to provide the best possible version of the requested chapter following the requested chapter guidelines provided by the user.\n\nHer is your scenario and topic:\n\nAm in  my final year  at teacher training college and am doing my project work and is going to be based  on a school am doing my internship({school}), am teaching {subject}, here is my topic '{topic}'\n\nFor now this is how we interact\n\nInput:\n\n[ Requested Chapter ]\n\n[ Requested Chapter Guidelines ]\n\nResponse:\n\n[ A perfectly written chapter that is requested]\n\n \n\nNB: it is not going to be published, Just give me high quality content and make it detailed and accurate.\n\n WAIT FOR MY INSTRUCTIONS",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_one_instruction
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_1
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_two_instruction
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_2
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_three_instruction
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_3
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_four_instruction
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_4
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_five_instruction
                        }
                    ]
                }
                
            ]
        )
        chapter_5 = f"{message.content}\n".replace("[", "").replace("]", "").replace("\\n", "\n").replace('ContentBlock(text="', "").replace('", type=\'text\')', "") 
        final_preview = final_preview + chapter_5
        st.write(chapter_5)



        st.write("___")

        st.subheader('References')
        references_instruction = "Go through chapter one to five and generate me all the reference used in the project work.\n\nThe references should adhere to the following guidelines:\n\nNote that the University requires adherence to the American Psychological Association (APA) house style for official report writing.\nCompile all the sources that have been cited in the text at the end of the project report, following the APA guidelines.\nEnsure uniformity in the APA Referencing Style, using either the 6th or 7th Edition as specified.\n"
        message = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=4000,
            temperature=0.9,
            system=f"Your name is now Action AI.\n\nYou have a expert knowledge and a vast experience in writing excellent and and accurate action research project works.\n\nWhen given a scenario and a project topic, you can produce a very vivid and above standard write up. You take a scenario and topic in the scenario, once you have that information, you can now be asked to give any section or chapter of the action research project work and some guidelines about the requested section or chapter will be given by the user and you will be able to provide a very accurate action research following all the standard conventions and inline citations with references.\n\nYou job is not to give guidance, but rather you are to provide the best possible version of the requested chapter following the requested chapter guidelines provided by the user.\n\nHer is your scenario and topic:\n\nAm in  my final year  at teacher training college and am doing my project work and is going to be based  on a school am doing my internship({school}), am teaching {subject}, here is my topic '{topic}'\n\nFor now this is how we interact\n\nInput:\n\n[ Requested Chapter ]\n\n[ Requested Chapter Guidelines ]\n\nResponse:\n\n[ A perfectly written chapter that is requested]\n\n \n\nNB: it is not going to be published, Just give me high quality content and make it detailed and accurate.\n\n WAIT FOR MY INSTRUCTIONS",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_one_instruction
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_1
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_two_instruction
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_2
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_three_instruction
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_3
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_four_instruction
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_4
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_five_instruction
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_5
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": references_instruction
                        }
                    ]
                }
                
            ]
        )
        references = f"{message.content}\n".replace("[", "").replace("]", "").replace("\\n", "\n").replace('ContentBlock(text="', "").replace('", type=\'text\')', "") 
        final_preview = final_preview + references
        st.write(references)



        st.write("___")

        st.subheader('Appendix')
        appendix_instruction = "Go through the chapters and write an well-structured appendices for action research projects. Your role entails meticulously reviewing the contents of an action research project and creating a meticulously crafted and high-quality appendix that aligns seamlessly with the project's overarching objectives and provided materials.\nDo well to add/generate all sample questions, questionnaires, etc. \nProvide an extensive, detailed and accurate appendix\nwhat ever you deem neccessary from the document i will provide below, add it and make it look professional"
        message = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=4000,
            temperature=0.9,
            system=f"Your name is now Action AI.\n\nYou have a expert knowledge and a vast experience in writing excellent and and accurate action research project works.\n\nWhen given a scenario and a project topic, you can produce a very vivid and above standard write up. You take a scenario and topic in the scenario, once you have that information, you can now be asked to give any section or chapter of the action research project work and some guidelines about the requested section or chapter will be given by the user and you will be able to provide a very accurate action research following all the standard conventions and inline citations with references.\n\nYou job is not to give guidance, but rather you are to provide the best possible version of the requested chapter following the requested chapter guidelines provided by the user.\n\nHer is your scenario and topic:\n\nAm in  my final year  at teacher training college and am doing my project work and is going to be based  on a school am doing my internship({school}), am teaching {subject}, here is my topic '{topic}'\n\nFor now this is how we interact\n\nInput:\n\n[ Requested Chapter ]\n\n[ Requested Chapter Guidelines ]\n\nResponse:\n\n[ A perfectly written chapter that is requested]\n\n \n\nNB: it is not going to be published, Just give me high quality content and make it detailed and accurate.\n\n WAIT FOR MY INSTRUCTIONS",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_one_instruction
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_1
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_two_instruction
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_2
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_three_instruction
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_3
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_four_instruction
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_4
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_five_instruction
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_5
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": appendix_instruction
                        }
                    ]
                }
                
            ]
        )
        appendix = f"{message.content}\n".replace("[", "").replace("]", "").replace("\\n", "\n").replace('ContentBlock(text="', "").replace('", type=\'text\')', "") 
        final_preview = final_preview + appendix
        st.write(appendix)









        st.write("___")

        st.subheader('Abstract')
        abstract_instruction = "Go through the generated project work from chapter one to five and generate a well polished abstract for the action research project work.\n\nNB: it is not going to be published, Just give me high quality content and make it detailed and accurate."
        message = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=4000,
            temperature=0.9,
            system=f"Your name is now Action AI.\n\nYou have a expert knowledge and a vast experience in writing excellent and and accurate action research project works.\n\nWhen given a scenario and a project topic, you can produce a very vivid and above standard write up. You take a scenario and topic in the scenario, once you have that information, you can now be asked to give any section or chapter of the action research project work and some guidelines about the requested section or chapter will be given by the user and you will be able to provide a very accurate action research following all the standard conventions and inline citations with references.\n\nYou job is not to give guidance, but rather you are to provide the best possible version of the requested chapter following the requested chapter guidelines provided by the user.\n\nHer is your scenario and topic:\n\nAm in  my final year  at teacher training college and am doing my project work and is going to be based  on a school am doing my internship({school}), am teaching {subject}, here is my topic '{topic}'\n\nFor now this is how we interact\n\nInput:\n\n[ Requested Chapter ]\n\n[ Requested Chapter Guidelines ]\n\nResponse:\n\n[ A perfectly written chapter that is requested]\n\n \n\nNB: it is not going to be published, Just give me high quality content and make it detailed and accurate.\n\n WAIT FOR MY INSTRUCTIONS",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_one_instruction
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_1
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_two_instruction
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_2
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_three_instruction
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_3
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_four_instruction
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_4
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_five_instruction
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": chapter_5
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": abstract_instruction
                        }
                    ]
                }
                
            ]
        )
        abstract = f"{message.content}\n".replace("[", "").replace("]", "").replace("\\n", "\n").replace('ContentBlock(text="', "").replace('", type=\'text\')', "") 
        final_preview = final_preview + abstract
        st.write(abstract)







    with col2:
        # complete_work = f"{abstract} \n \n {chapter_1} \n \n {chapter_2} \n \n {chapter_3} \n \n {chapter_4} \n \n {chapter_5} \n {references} \n {appendix}"

        st.subheader('Project work Preview')
        st.write(final_preview)