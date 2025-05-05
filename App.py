from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash

app = Flask(__name__)

# Ma'lumotlar bazasi (bu misolda faqat xotiraga saqlash)
users_db = {}

@app.route('/register', methods=['POST'])
def register():
    # Requestdan ma'lumotlarni olish
    data = request.json
    username = data['username']
    password = data['password']
    
    # Username tekshirish: agar foydalanuvchi mavjud bo'lsa
    if username in users_db:
        return jsonify({"success": False, "message": "Foydalanuvchi allaqachon mavjud!"})
    
    # Parolni xavfsiz saqlash
    hashed_password = generate_password_hash(password)
    
    # Foydalanuvchini ma'lumotlar bazasiga qo'shish
    users_db[username] = hashed_password
    
    return jsonify({"success": True, "message": "Foydalanuvchi ro'yxatdan o'tdi!"})

if __name__ == '__main__':
    app.run(debug=True)
