from flask import Blueprint, render_template, jsonify

maps_bp = Blueprint('maps_bp', __name__)

lokasi = [
    {"latitude": -6.878135872412126, "longitude": 107.58748423039381,
     "name": "Museum Barli",
     "address": "Jl. Prof. Dr. Sutami No.91, Sukarasa, Kec. Sukasari, Kota Bandung, Jawa Barat 40152",
     "image": "https://bolulembang.co.id/wp-content/uploads/2023/01/Menengok-Keindahan-Koleksi-Museum-Barli-Bandung_Img0.jpg?x31789"},

      {"latitude": -6.921596585408139, "longitude": 107.57730866686894,
     "name": "Museum Kebudayaan Tionghoa",
     "address": "Jl. Nana Rohana No.37, Wr. Muncang, Kec. Bandung Kulon, Kota Bandung, Jawa Barat 40211",
     "image": "https://storage.googleapis.com/digo-news/uploads/1674496066.jpg"},

     {"latitude": -6.8514563505372905, "longitude": 107.59618132235902,
     "name": "Museum 3D",
     "address": "4HXW+CF8, Jl. Dr. Setiabudi, Isola, Kec. Sukasari, Kota Bandung, Jawa Barat 40154",
     "image": "https://asset-2.tstatic.net/tribunjabarwiki/foto/bank/images/art-15.jpg"},

     {"latitude": -6.920994876718971, "longitude": 107.61195676719566,
     "name": "Museum Wolff Schoemaker (Preanger)",
     "address": "Jl. Asia Afrika No.81, Braga, Kec. Sumur Bandung, Kota Bandung, Jawa Barat 40112",
     "image": "https://telusuri.id/wp-content/uploads/2021/05/Koleksi-Foto-Bangunan-Karya-Wolff-Schoemaker.jpg"},

     {"latitude": -6.909684820315433, "longitude": 107.60947788155453,
     "name": "Museum Kota Bandung",
     "address": "Jl. Aceh No.47, Babakan Ciamis, Kec. Sumur Bandung, Kota Bandung, Jawa Barat 40117",
     "image": "https://awsimages.detik.net.id/community/media/visual/2018/10/31/1ea73718-9ea2-4fd1-88cf-783fe72ee05b_169.jpeg?w=700&q=90"},

     {"latitude": -6.917336116922969, "longitude": 107.61107567501327,
     "name": "Mandala Wangsit Siliwangi Museum",
     "address": "Jl. Lembong No.38, Braga, Kec. Sumur Bandung, Kota Bandung, Jawa Barat 40111",
     "image": "https://lh5.googleusercontent.com/p/AF1QipPjOqnhdzsSg5APYCjo5XUgCu-s_zQivPKTqouq=w408-h306-k-no"},

     {"latitude": -6.937626118792206, "longitude": 107.60348178349872,
     "name": "Sri Baduga Museum",
     "address": "Jl. BKR No.185, Pelindung Hewan, Kec. Astanaanyar, Kota Bandung, Jawa Barat 40243",
     "image": "https://asset.kompas.com/crops/_Rz_vrPJji7Z7jJdlZlfoZqZxYg=/0x78:1920x1358/780x390/data/photo/2023/03/06/64055c477df26.jpeg"},

     {"latitude": -6.9006685449963, "longitude": 107.62146136735005,
     "name": "Museum Geologi",
     "address": "Jl. Diponegoro No.57, Cihaur Geulis, Kec. Cibeunying Kaler, Kota Bandung, Jawa Barat 40122",
     "image": "https://o-cdn-cas.sirclocdn.com/parenting/images/museum-geologi-bandung.width-800.format-webp.webp"},

     {"latitude": -6.90237406850887, "longitude": 107.61869638703368,
     "name": "Gedung Sate",
     "address": "Jl. Diponegoro No.22, Citarum, Kec. Bandung Wetan, Kota Bandung, Jawa Barat 40115",
     "image": "https://lh5.googleusercontent.com/p/AF1QipNIIoHAulvp9X4zb09N22lwnb717AIweZi2z_c=w408-h272-k-no"},

     {"latitude": -6.921219174780538,  "longitude":  107.6095897155446,
     "name": "Asian African Conference Museum",
     "address": "Jl. Asia Afrika No.65, Braga, Kec. Sumur Bandung, Kota Bandung, Jawa Barat 40111",
     "image": "https://cache2.travelfish.org/b/assets/2015/gallery/thumbR/gallery_sight_thumbR_587_1527552464.jpg"},

      {"latitude": -6.901848471330121,  "longitude": 107.61971171039097, 
     "name": "Museum Pos Indonesia",
     "address": "Cilaki St No.73, Citarum, Bandung Wetan, Bandung City, West Java 40115",
     "image": "https://lh5.googleusercontent.com/p/AF1QipOVg3MjYU7suJGB-SLxbVPea6hmtG8eloW_o-NV=w408-h306-k-no"},

     
]

@maps_bp.route('/lokasi')
def lokasi_view():
    return jsonify(lokasi)

@maps_bp.route('/maps')
def maps():
    return render_template('maps.html')





