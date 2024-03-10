import streamlit as st

# สร้างเว็บแอป
st.title('คำนวณแคลอรี')

# สร้างเมนูในแถบข้าง
menu_option = st.sidebar.radio('เลือกเมนู', ['คำนวณแคลอรี่', 'คำนวณแคลอรี่ของอาหาร'])

class CalorieCalculator:
    def __init__(self, weight, height, age, gender, activity_level):
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender
        self.activity_level = activity_level

    def calculate_bmr(self):
        if self.gender == 'ชาย':
            return 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)
        else:
            return 447.593 + (9.247 * self.weight) + (3.098 * self.height) - (4.330 * self.age)

    def calculate_calories_needed(self):
        bmr = self.calculate_bmr()
        if self.activity_level == 'น้อยมาก':
            return bmr * 1.2
        elif self.activity_level == 'น้อย':
            return bmr * 1.375
        elif self.activity_level == 'ปานกลาง':
            return bmr * 1.55
        elif self.activity_level == 'มาก':
            return bmr * 1.725
        else:
            return bmr * 1.9


class FoodCalorieCalculator:
    def __init__(self, carbs, fat, protein):
        self.carbs = carbs
        self.fat = fat
        self.protein = protein

    def calculate_calories(self):
        return 4 * self.carbs + 9 * self.fat + 4 * self.protein


# ใช้งาน CalorieCalculator และ FoodCalorieCalculator
if menu_option == 'คำนวณแคลอรี่':
    # รับข้อมูลจากผู้ใช้
    weight = st.number_input('น้ำหนัก (กิโลกรัม)', min_value=0.0)
    height = st.number_input('ส่วนสูง (เซนติเมตร)', min_value=0.0)
    age = st.number_input('อายุ (ปี)', min_value=0)
    gender = st.radio('เพศ', ('ชาย', 'หญิง'))
    activity_level = st.selectbox('กิจกรรมที่ทำในแต่ละวัน', ['น้อยมาก', 'น้อย', 'ปานกลาง', 'มาก', 'มากมาก'])

    # สร้างอ็อบเจกต์ CalorieCalculator
    calorie_calculator = CalorieCalculator(weight, height, age, gender, activity_level)

    # คำนวณแคลอรี่ที่ต้องการต่อวัน
    cal_needed = calorie_calculator.calculate_calories_needed()

    # แสดงผลลัพธ์
    st.write(f'คุณต้องการแคลอรีต่อวัน:  {cal_needed:.2f} ')

elif menu_option == 'คำนวณแคลอรี่ของอาหาร':
    # รับข้อมูลจากผู้ใช้
    carbs = st.number_input('คาร์โบไฮเดรต (กรัม)', min_value=0.0)
    fat = st.number_input('ไขมัน (กรัม)', min_value=0.0)
    protein = st.number_input('โปรตีน (กรัม)', min_value=0.0)

    # สร้างอ็อบเจกต์ FoodCalorieCalculator
    food_calorie_calculator = FoodCalorieCalculator(carbs, fat, protein)

    # คำนวณแคลอรีของอาหาร
    calories = food_calorie_calculator.calculate_calories()

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

