from flask import Flask, render_template_string

app = Flask(__name__)

# Diseño HTML, CSS y JS integrado en una sola cadena de texto
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Landing Page - Reloj Digital</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap" rel="stylesheet">
    
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Montserrat', sans-serif;
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #ffffff;
            overflow: hidden;
        }

        .container {
            text-align: center;
            background: rgba(255, 255, 255, 0.05);
            padding: 3rem 4rem;
            border-radius: 20px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
            border: 1px rgba(255, 255, 255, 0.1) solid;
        }

        h1 {
            font-size: 1.5rem;
            font-weight: 300;
            text-transform: uppercase;
            letter-spacing: 4px;
            margin-bottom: 1.5rem;
            color: #00f2fe;
        }

        .clock {
            font-size: 4.5rem;
            font-weight: 700;
            letter-spacing: 2px;
            margin-bottom: 0.5rem;
            text-shadow: 0 0 20px rgba(0, 242, 254, 0.6);
        }

        .date {
            font-size: 1.2rem;
            font-weight: 400;
            color: #a5b1c2;
            letter-spacing: 1px;
        }

        footer {
            position: absolute;
            bottom: 20px;
            font-size: 0.8rem;
            color: rgba(255, 255, 255, 0.4);
            letter-spacing: 1px;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Tiempo Actual</h1>
        <div class="clock" id="clock">00:00:00</div>
        <div class="date" id="date">Cargando fecha...</div>
    </div>

    <footer>© 2026 Landing Page Temporal</footer>

    <script>
        function updateClock() {
            const now = new Date();
            
            // Formatear la hora
            let hours = String(now.getHours()).padStart(2, '0');
            let minutes = String(now.getMinutes()).padStart(2, '0');
            let seconds = String(now.getSeconds()).padStart(2, '0');
            
            document.getElementById('clock').textContent = `${hours}:${minutes}:${seconds}`;
            
            // Formatear la fecha en español
            const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
            let dateString = now.toLocaleDateString('es-ES', options);
            
            // Capitalizar la primera letra del día
            dateString = dateString.charAt(0).toUpperCase() + dateString.slice(1);
            
            document.getElementById('date').textContent = dateString;
        }

        // Ejecutar inmediatamente y luego cada segundo
        updateClock();
        setInterval(updateClock, 1000);
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    # Usamos render_template_string para no necesitar una carpeta /templates
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    # Configurado explícitamente para el puerto 5000
    app.run(debug=True, port=5000)