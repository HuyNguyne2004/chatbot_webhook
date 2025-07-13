from database import get_connection

def handle_mealplan_detail(mealplan_name):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT description, benefit
            FROM MealPlanDetails
            WHERE name = ?
        """, mealplan_name)
        row = cursor.fetchone()
        conn.close()

        if row:
            description = row.description or ""
            benefit = row.benefit or ""
            return f"Gói {mealplan_name}: {description}. Lợi ích: {benefit}"
        else:
            return f"Xin lỗi, mình không tìm thấy thông tin cho gói {mealplan_name}."
    except Exception as e:
        return f"Có lỗi xảy ra khi truy xuất dữ liệu: {str(e)}"


def handle_mealplan_suggestion(bmi):
    try:
        bmi = float(bmi)
        conn = get_connection()
        cursor = conn.cursor()

        if bmi < 18.5:
            category = 'tăng cân'
        elif 18.5 <= bmi <= 24.9:
            category = 'duy trì'
        else:
            category = 'giảm cân'

        cursor.execute("""
            SELECT TOP 1 name, description
            FROM MealPlanDetails
            WHERE purpose = ?
        """, category)
        row = cursor.fetchone()
        conn.close()

        if row:
            return f"Dựa vào chỉ số BMI của bạn ({bmi}), mình gợi ý gói '{row.name}': {row.description}"
        else:
            return f"Mình chưa có gợi ý nào cho chỉ số BMI {bmi} hiện tại."

    except ValueError:
        return "Chỉ số BMI bạn nhập không hợp lệ. Vui lòng nhập một con số."
    except Exception as e:
        return f"Có lỗi xảy ra khi đưa ra gợi ý: {str(e)}"
