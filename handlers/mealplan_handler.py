from database import get_connection

# Bản đồ ánh xạ tên gói người dùng có thể nhập sang ID gói (có thể mở rộng sau)
MEALPLAN_NAME_MAP = {
    "tăng cân cơ bản": 1,
    "giảm cân nhanh": 2,
    "duy trì khỏe mạnh": 3,
    # Thêm các ánh xạ khác nếu có
}

def handle_mealplan_detail(mealplan_name):
    try:
        # Thử ánh xạ tên gói sang ID nếu cần
        mealplan_id = MEALPLAN_NAME_MAP.get(mealplan_name.lower(), mealplan_name)

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT PlanDescription
            FROM MealPlanDetails
            WHERE MealPlanDetailID = ?
        """, mealplan_id)
        row = cursor.fetchone()
        conn.close()

        if row:
            return f"Gói {mealplan_name}: {row.PlanDescription}"
        else:
            return f"Xin lỗi, mình không tìm thấy thông tin cho gói '{mealplan_name}'."

    except Exception as e:
        return f"Có lỗi xảy ra khi truy xuất dữ liệu meal plan: {str(e)}"


def handle_mealplan_suggestion(bmi):
    try:
        bmi = float(bmi)
        if bmi < 18.5:
            bmi_range = 'thiếu cân'
        elif 18.5 <= bmi <= 24.9:
            bmi_range = 'bình thường'
        else:
            bmi_range = 'thừa cân'

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT TOP 1 MealPlanDetailID, PlanDescription
            FROM MealPlanDetails
            WHERE BMIRange = ?
        """, bmi_range)
        row = cursor.fetchone()
        conn.close()

        if row:
            return f"Dựa vào chỉ số BMI của bạn ({bmi}), mình gợi ý gói '{row.MealPlanDetailID}': {row.PlanDescription}"
        else:
            return f"Hiện chưa có gợi ý meal plan cho nhóm BMI '{bmi_range}'."

    except ValueError:
        return "Chỉ số BMI bạn nhập không hợp lệ. Vui lòng nhập một số hợp lệ."
    except Exception as e:
        return f"Có lỗi xảy ra khi đưa ra gợi ý meal plan: {str(e)}"
