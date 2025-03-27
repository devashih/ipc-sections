from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    ipc_sections = ""
    if request.method == "POST":
        incident_description = request.form["incident"]
        
        # Here you can add logic to analyze the incident and return applicable IPC sections
        ipc_sections = analyze_incident(incident_description)
    
    return render_template("index.html", ipc_sections=ipc_sections)

def analyze_incident(description):
    # Placeholder logic for IPC analysis. 
    # Replace this with your own analysis logic.
    if "theft" in description.lower():
        return "Sections applicable: 378 (Theft), 379 (Punishment for Theft)"
    elif "assault" in description.lower():
        return "Sections applicable: 351 (Assault), 352 (Punishment for Assault)"
    else:
        return "No applicable sections found."

if __name__ == "__main__":
    app.run(debug=True)