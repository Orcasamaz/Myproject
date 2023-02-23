import streamlit as st
import pandas as pd
import numpy as np
from sklearn import *
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from PIL import Image

st.header("🐦Bird Prediction🐦")
st.subheader("โปรเจคนี่เกี่ยวกับการPredicition นก โดยผู้ใช้จะต้องกรอกข้อมูลลงไป")
left,right = st.columns(2)

def load_bird_data(): # load
    return pd.read_excel("birddataset.csv")

def save_model(model): # save
    joblib.dump(model, 'model.joblib')

def load_model():
    return joblib.load('model.joblib')

st.markdown(
    f"""
       <style>
       .stApp {{
           background-image: url("https://t3.ftcdn.net/jpg/05/20/86/28/360_F_520862894_CDHJyZ0GEHwKUJJgGYNR1tzyGYnlIxPi.jpg");
           background-attachment: fixed;
           background-size: cover;
           /* opacity: 0.3; */
       }}
       </style>
       """,
    unsafe_allow_html=True
)

save_b=left.button("save data ")
#create model

data = pd.read_csv('birddataset.csv')
data_dataframe = pd.DataFrame(data)
# st.write(data_dataframe)
X = data_dataframe.drop(columns='ชนิดของนก',axis=1)
Y = data_dataframe['ชนิดของนก']

A = []
C = []
for i in range(len(Y)):
    A.append(i)
for j in range(len(Y)):
    B = []
    B.append(A[j])
    B.append(Y[j])
    C.append(B)


button_load=left.button("load data")
if button_load :
    data = pd.read_excel('birddataset.xlsx')
    data_dataframe = pd.DataFrame(data)
    # print(data_dataframe)
    data_dataframe=data_dataframe.drop(columns="Unnamed: 0")
    right.write(data_dataframe)


if save_b :
    load_data=pd.read_csv("birddataset.csv")
    load_data=pd.DataFrame(load_data)
    # X = load_data.drop(columns='ชนิดของนก', axis=1)
    # Y = load_data['ชนิดของนก']
    load_data.to_excel("birddataset.xlsx")


# training
train_b=left.button("train")
if train_b:
    x_train,x_test,y_train,y_test = train_test_split(X,A,test_size=0.2)
    model = LogisticRegression()
    model.fit(x_train,y_train)
    save_model(model)

bird_price=st.number_input("ราคาเริ่มต้นของนก",0,40000,100)

bird_size=st.selectbox("ขนาดของนก",("ใหญ่","เล็ก"))
if bird_size == "ใหญ่":
    bird_size=1
else:
    bird_size=0
#st.markdown(bird_size)

bird_speak=st.selectbox("นกสามารุถพูดได้ไหม",("พูดได้","พูดไม่ได้"))
if bird_speak == "พูดได้":
    bird_speak=1
else:
    bird_speak=0
bird_care=st.selectbox("นกเลี้ยงง่ายไหม",("ง่าย","ไม่ง่าย"))
if bird_care == "ง่าย":
    bird_care=1
else:
    bird_care=0

#predict
predict_b=st.button("predict")
model=load_model()
data_user = (bird_price,bird_size,bird_speak,bird_care)
data_user_array = np.array(data_user)
data_user_array_reshape = data_user_array.reshape(1,-1)
Pred = model.predict(data_user_array_reshape)
name = "1"
for k in range(len(A)):
    if Pred[0] == C[k][0]:
        name = str(C[k][1])

st.write(name)

#image นก
bird_image1 = Image.open("ราคานกหงส์นก.png")
bird_image2 = Image.open("ราคานกฟินซ์.png")
bird_image3 = Image.open("ราคานกเลิฟเบิร์ด.png")
bird_image4 = Image.open("ราคานกค๊อกคาเทล.png")
bird_image5 = Image.open("ราคานกกรีนชีค.png")
bird_image6 = Image.open("ราคานกซันคอนัวร์.png")
bird_image7 = Image.open("ราคานกคีรีบูน.png")
bird_image8 = Image.open("ราคานกแก้วฟอพัส.png")
bird_image9 = Image.open("ราคานกแก้วริงเนค.png")
bird_image10 = Image.open("ราคานกแอฟริกันเกรย์.png")
bird_image11 = Image.open("ราคานกแก้วอิเล็คตัส.png")
bird_image12 = Image.open("ราคานกแก้วอเมซอน.png")
bird_image13 = Image.open("ราคานกแก้วกระตั้ว.png")
bird_image14 = Image.open("ราคานกแก้วมาคอร์.png")

if name == "นกหงส์หยก":
    st.image(bird_image1)
    st.markdown("นกหงส์หยกเป็นนกสัตว์เลี้ยงที่ได้รับความนิยมและราคาถูกมาเมื่อเทียบกับสายพันธุ์อื่นๆ นกหงส์หยกเป็นนกขี้เล่นและฉลาดมาก เหมาะสำหรับมือใหม่ผู้ที่ต้องการเริ่มเลี้ยงนกเป็นตัวแรก")

elif name == "นกฟินซ์":
    st.image(bird_image2)
    st.markdown("นกหงส์หยกเป็นนกสัตว์เลี้ยงที่ได้รับความนิยมและราคาถูกมาเมื่อเทียบกับสายพันธุ์อื่นๆ นกหงส์หยกเป็นนกขี้เล่นและฉลาดมาก เหมาะสำหรับมือใหม่ผู้ที่ต้องการเริ่มเลี้ยงนกเป็นตัวแรก ")

elif name == "นกเลิฟเบิร์ด":
    st.image(bird_image3)
    st.markdown("นกเลิฟเบิร์ดนกแก้วตัวเล็กที่น่ารัก หลากหลายสีและมักจะขายเป็นคู่เนื่องจากความสัมพันธ์ที่แน่นแฟ้นและนกเลิฟเบิร์ดสามารถเป็นเพื่อนที่ดีและเป็นมิตรมาก")

elif name == "นกค๊อกคาเทล":
    st.image(bird_image4)
    st.markdown("นกค๊อกคาเทลเป็นสมาชิกที่เล็กที่สุดของตระกูล “Cacatuidae” มีถิ่นกำเนิดในออสเตรเลีย และราคานกค๊อกคาเทลจะแตกต่างกันไปขึ้นอยู่กับสีของการเพาะพันธุ์ นกค๊อกคาเทลสีเหลืองและสีขาวแบบดั้งเดิมที่มีแก้มสีส้มมีราคาอาจจะไม่แพงในขณะที่นกค๊อกคาเทลลูติโน่อจะมีราคาที่แพงกว่า")

elif name == "นกกรีนชีค":
    st.image(bird_image5)
    st.markdown("นกกรีนชีคมีนิสัยขี้เล่นและซุกซน มีขนาดเล็กและเป็นสัตว์เลี้ยงที่นิยมเป็นอย่างมาก นกกรีนชีคไม่มีความสามารถในการพูด แต่สามารถสอนให้พูดคำไม่กี่คำด้วยการฝึกฝนอย่างสม่ำเสมอ")

elif name == " นกซันคอนัวร์":
    st.image(bird_image6)
    st.markdown("นกซันคอนัวร์สามารถหาได้ทั่วไปตามร้านขายสัตว์เลี้ยงและซันคอนัวร์ราคาไม่แพงเกินไป มีอายุขัยที่ยาวนานถึง 30 ปี นกซันคอนัวมีนิสัยขี้เล่นและฉลาดมาก ")

elif name =="นกคีรีบูน":
    st.image(bird_image7)
    st.markdown("นกคีรีบูนเป็นนกที่ขึ้นชื่อเรื่องร้องเพลงไพเราะ และยังเป็นหนึ่งในนกที่เชื่องเลี้ยงง่าย มีนิสัยร่าเริง ถิ่นกำเนิดมาจากหมู่เกาะแคนนารี ตั้งอยู่ทางตะวันตกเฉียงเหนือของแอฟริกา ")

elif name =="นกแก้วฟอพัส":
    st.image(bird_image8)
    st.markdown("นกแก้วฟอพัสเป็นนกที่มีขนาดเล็กที่สุด มีเสียงที่เบากว่าสายพันธุ์อื่นๆ เหมาะกับการเลี้ยงในอพาร์ตเม้น นกแก้วฟอพัสเป็นนกที่ฉลาดและเป็นมิตรกับเจ้าของทุกคน")

elif name =="นกแก้วริงเนค":
    st.image(bird_image9)
    st.markdown("นกแก้วริงเนคสามารถกลายเป็นเพื่อนและสมาชิกในครอบครัวที่ดีได้ นกแก้วริงเนคอาจไม่เหมาะกับทุกคนเนื่องจากต้องการความดูแลและเอาใจใส่เป็นอย่างมาก นกแก้วริงเนคมีสีสันสดใสและดึงดูดสายตา")

elif name =="นกแอฟริกันเกรย์":
    st.image(bird_image10)
    st.markdown("นกแอฟริกันเกรย์พูดเลียนแบบคำพูดของมนุษย์ได้อย่างดีด้วยการฝึกฝนอย่างสม่ำเสมอ นกแอฟริกันเกรย์เป็นนกที่ฉลาดที่สุด และมีราคาค่อนข้างสูง เป็นหนึ่งในนกเลี้ยงที่คนนิยมมากที่สุด")

elif name =="นกแก้วอิเล็คตัส":
    st.image(bird_image11)
    st.markdown("นกแก้วอิเล็คตัส เป็นนกแก้วที่ง่ายที่สุดในการบอกเพศ ตัวผู้เป็นสีเขียวอย่างชัดเจนในขณะที่ตัวเมียเป็นสีแดง เป็นนกฉลาด พูดได้ มีบุคลิกที่น่ารัก ทำให้เป็นหนึ่งในนกแก้ว ที่ได้ความนิยมนำมาเลี้ยงมากที่สุด")\

elif name =="นกแก้วอเมซอน":
    st.image(bird_image12)
    st.markdown("นกแก้วอิเล็คตัส เป็นนกแก้วที่ง่ายที่สุดในการบอกเพศ ตัวผู้เป็นสีเขียวอย่างชัดเจนในขณะที่ตัวเมียเป็นสีแดง เป็นนกฉลาด พูดได้ มีบุคลิกที่น่ารัก ทำให้เป็นหนึ่งในนกแก้ว ที่ได้ความนิยมนำมาเลี้ยงมากที่สุด")

elif name =="นกแก้วกระตั้ว":
    st.image(bird_image13)
    st.markdown("นกกระตั้วมีลักษณะความโดดเด่นกว่านกแก้วสายพันธุ์อื่นๆ คือขนหงอนบนหัวของนกกระตั้ว  นกกระตั้วเข้ากับคนง่ายและต้องอยู่ใกล้ชิดกับผู้คนในชีวิต สามารถเลียนแบบคำพูดได้ ")

elif name =="นกแก้วมาคอร์":
    st.image(bird_image14)
    st.markdown("” นกแก้วมาคอว์มักจะเป็นสิ่งแรกที่คนส่วนใหญ่นึกถึง นกแก้วมาคอร์เป็นนกที่สวยงาม มีขนาดใหญ่และสีสันสดใส แต่เป็นนกแก้วราคาแพง มีอายุขัยนานถึง 40-80 ปี และหากยิ่งนกแก้วมาคอร์มีขนาดใหญ่มากเท่าใดอายุขัยก็จะยิ่งยืนยาวขึ้น นกแก้วมาคอร์ ไฮยาซิน เป็นนกแก้วที่ใหญ่ที่สุดในโลก")
