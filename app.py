from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    status = None
    if request.method == 'POST':
        try:
            weight = float(request.form['weight'])
            height = float(request.form['height'])
            bmi = weight / (height ** 2)

            # Xác định tình trạng cơ thể dựa trên BMI
            if bmi < 16:
                status = "Gầy độ III"
            elif 16 <= bmi < 17:
                status = "Gầy độ II"
            elif 17 <= bmi < 18.5:
                status = "Gầy độ I"
            elif 18.5 <= bmi < 25:
                status = "Bình thường"
            elif 25 <= bmi < 30:
                status = "Thừa cân"
            elif 30 <= bmi < 35:
                status = "Béo phì độ I"
            elif 35 <= bmi < 40:
                status = "Béo phì độ II"
            else:
                status = "Béo phì độ III"
        except (ValueError, ZeroDivisionError):
            bmi = "Lỗi: Vui lòng nhập đúng số liệu cho cân nặng và chiều cao."
            status = ""
    
    return render_template('index.html', bmi=bmi, status=status)

if __name__ == '__main__':
    app.run(debug=True, port=5500)
