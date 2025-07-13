from flask import Flask, request, jsonify
from handlers.product_handler import handle_product_info, handle_product_stock
from handlers.mealplan_handler import handle_mealplan_detail, handle_mealplan_suggestion

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    try:
        req = request.get_json()
        intent = req.get("queryResult", {}).get("intent", {}).get("displayName")
        parameters = req.get("queryResult", {}).get("parameters", {})

        if intent == "ask.product_info":
            product_name = parameters.get("product_name")
            response_text = handle_product_info(product_name)

        elif intent == "ask.product_stock":
            product_name = parameters.get("product_name")
            response_text = handle_product_stock(product_name)

        elif intent == "ask.mealplan_detail":
            mealplan_name = parameters.get("mealplan_name")
            response_text = handle_mealplan_detail(mealplan_name)

        elif intent == "ask.mealplan_suggestion":
            bmi = parameters.get("mealplan_bmi")
            response_text = handle_mealplan_suggestion(bmi)

        else:
            response_text = "Tôi chưa hiểu yêu cầu của bạn. Bạn có thể nói rõ hơn được không?"

    except Exception as e:
        response_text = f"Xin lỗi, đã xảy ra lỗi trong quá trình xử lý: {str(e)}"

    return jsonify({
        "fulfillmentText": response_text
    })
