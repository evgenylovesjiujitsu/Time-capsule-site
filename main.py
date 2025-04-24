from flask import Flask, render_template_string

app = Flask(__name__)

# HTML 
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Мій простий сайт</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
            color: #333;
        }
        header {
            background-color: #4CAF50;
            color: white;
            padding: 20px;
            text-align: center;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        .content {
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        footer {
            text-align: center;
            margin-top: 20px;
            color: #666;
        }
    </style>
</head>
<body>
    <header>
        <h1>Hi, bro!</h1>
    </header>
    
    <div class="content">
        <h2>Про цей сайт:</h2>
        <p>Цей сайт – капсула часу.</p>
        <p>Обіцяю повернутися сюди рівно через 5 років — 25 квітня 2029 року.</p>
        <p>Перевірити, чи став я BJJ Black Belt (а може просто ходжу в качалку і важу 90кг?), чи купив я Tesla (чи може вже щось крутіше?), чи дійшов до Senior Python Engineer (а може й вище?), і чи нарешті закінчилась війна. Буде цікаво порівняти! До зустрічі, майбутній я!</p>
        <p>З любов'ю, Женя.</p>
        <h3>Контакти:</h3>
        <p>Email: doroshbjj@icloud.com</p>
    </div>
    
    <footer>
        <p>&copy; 2025 (Сайт створено з особливим теплом та коханням). Усі права захищені.</p>
    </footer>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True)
