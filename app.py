@app.route('/result5', methods=['GET', 'POST'])
def result5():
    res = None
    
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        age_str = request.form.get('age', '').strip()

        try:
            age = int(age_str)
            age_togri = 0 <= age <= 120  
        except ValueError:
            age_togri = False

        if '@' in email and age_togri:
            res = [email, age]
        else:
            res = ["Ma'lumotlar noto'g'ri kiritildi"]

    return render_template('result5.html', res=res)
