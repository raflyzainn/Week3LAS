from flask import Blueprint, render_template, jsonify

maps_bp = Blueprint('maps_bp', __name__)

lokasi = [
    {"latitude": -6.971386, "longitude": 107.632456,
     "name": "Telkom University",
     "address": "Jl. Sukabirus No.123, Bandung",
     "image": "https://example.com/telkom.jpg"},
   
    {"latitude": -6.974829, "longitude": 107.636394,
     "name": "Oetomo Hospital",
     "address": "Jl. Telekomunikasi No.1, Bandung",
     "image": "https://example.com/oetomo.jpg"},

     {"latitude": -6.969263, "longitude": 107.628078,
     "name": "TULT",
     "address": "Jl. Telekomunikasi No.1, Bandung",
     "image": "https://example.com/tult.jpg"},

     {"latitude": -6.972476, "longitude": 107.639622,
     "name": "PBB",
     "address": "Jl. Telekomunikasi No.1, Bandung",
     "image": "https://example.com/pbb.jpg"}
]

@maps_bp.route('/lokasi')
def lokasi_view():
    return jsonify(lokasi)

@maps_bp.route('/maps')
def maps():
    return render_template('maps.html')
