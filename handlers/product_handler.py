from database import get_connection

def handle_product_info(product_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT description FROM Products WHERE name = ?", product_name)

    row = cursor.fetchone()
    conn.close()

    if row:
        return f"Sản phẩm {product_name} là: {row.description}"
    else:
        return f"Xin lỗi, tôi không tìm thấy thông tin cho sản phẩm {product_name}."

def handle_product_stock(product_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT stock FROM Products WHERE name = ?", product_name)
    row = cursor.fetchone()
    conn.close()

    if row:
        return f"Sản phẩm {product_name} còn {row.stock} sản phẩm trong kho."
    else:
        return f"Xin lỗi, tôi không tìm thấy thông tin tồn kho cho sản phẩm {product_name}."
