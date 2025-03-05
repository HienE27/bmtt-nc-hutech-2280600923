from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher  

# Khởi tạo đối tượng Flask
app = Flask(__name__)

# Khởi tạo đối tượng CaesarCipher
caesar_cipher = CaesarCipher()

# Route cho mã hóa Caesar
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    # Kiểm tra xem có các trường cần thiết không
    if 'plain_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing required fields: plain_text or key'}), 400
    
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

# Route cho giải mã Caesar
@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    # Kiểm tra xem có các trường cần thiết không
    if 'cipher_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing required fields: cipher_text or key'}), 400
    
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# Khởi tạo đối tượng VigenereCipher
vigenere_cipher = VigenereCipher()  

# Route cho mã hóa Vigenère
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    # Kiểm tra xem có các trường cần thiết không
    if 'plain_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing required fields: plain_text or key'}), 400
    
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

# Route cho giải mã Vigenère
@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    # Kiểm tra xem có các trường cần thiết không
    if 'cipher_text' not in data or 'key' not in data:
        return jsonify({'error': 'Missing required fields: cipher_text or key'}), 400
    
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# Main function để chạy ứng dụng
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
