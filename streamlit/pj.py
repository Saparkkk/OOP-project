import streamlit as st

# สร้างเว็บแอป
st.title('คำนวณแคลอรี')

# สร้างเมนูในแถบข้าง
menu_option = st.sidebar.radio('เลือกเมนู', ['คำนวณแคลอรี่', 'คำนวณแคลอรี่ของอาหาร'])

# สร้างเว็บแอป ของ คำนวณแคลอรี่
if menu_option == 'คำนวณแคลอรี่':
    st.image('https://www.leancuisine.com.au/wp-content/uploads/2020/12/calories.jpg', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    # สร้างช่องให้ผู้ใช้ป้อนข้อมูล
    weight = st.number_input('น้ำหนัก (กิโลกรัม)', min_value=0.0)
    height = st.number_input('ส่วนสูง (เซนติเมตร)', min_value=0.0)
    age = st.number_input('อายุ (ปี)', min_value=0)

    # รับข้อมูลเพศ
    gender = st.radio('เพศ', ('ชาย', 'หญิง'))

    # รับข้อมูลกิจกรรมที่ทำในแต่ละวัน
    activity_level = st.selectbox('กิจกรรมที่ทำในแต่ละวัน', ['น้อยมาก', 'น้อย', 'ปานกลาง', 'มาก', 'มากมาก'])

    # คำนวณแคลอรีที่ต้องการต่อวัน
    if gender == 'ชาย':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    if activity_level == 'น้อยมาก':
        cal_needed = bmr * 1.2
    elif activity_level == 'น้อย':
        cal_needed = bmr * 1.375
    elif activity_level == 'ปานกลาง':
        cal_needed = bmr * 1.55
    elif activity_level == 'มาก':
        cal_needed = bmr * 1.725
    else:
        cal_needed = bmr * 1.9

    # แสดงผลลัพธ์
    st.write(f'คุณต้องการแคลอรีต่อวัน:  {cal_needed:.2f} ')

# สร้างเว็บแอป ของ คำนวณแคลอรี่ของอาหาร
elif menu_option == 'คำนวณแคลอรี่ของอาหาร':
    # รูปภาพ
    st.image('https://www.usatoday.com/gcdn/media/2022/08/20/USATODAY/usatsports/imageforentry17-ahk.jpg', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    # สร้างช่องให้ผู้ใช้ป้อนข้อมูล
    carbs = st.number_input('คาร์โบไฮเดรต (กรัม)', min_value=0.0)
    fat = st.number_input('ไขมัน (กรัม)', min_value=0.0)
    protein = st.number_input('โปรตีน (กรัม)', min_value=0.0)

    # คำนวณแคลอรี
    calories = 4 * carbs + 9 * fat + 4 * protein

    # แสดงผลลัพธ์
    st.write(f'แคลอรีของอาหารคือ {calories:.2f}')
    
    
def set_background(image_url):
    image_url_str = f'url("{image_url}")'
    css = f"""
    <style>
    .stApp {{
        background-image: {image_url_str};
        background-size: cover;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


##ใช้งานตรงนี้
set_background("https://food-ubc.b-cdn.net/wp-content/uploads/2022/06/AdobeStock_306848967-scaled.jpeg")

