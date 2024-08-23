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

     {"latitude": -6.9196314396038705, "longitude": 107.60702869323114, 
     "name": "Museum Banceuy",
     "address": "3JJ4+4RJ banceuy, Braga, Kec. Sumur Bandung, Kota Bandung, Jawa Barat 40111",
     "image": "https://assets.promediateknologi.id/crop/0x0:0x0/750x500/webp/photo/ayobandung/images-bandung/post/articles/2018/10/19/39388/banceuy.jpg"},

     {"latitude": -6.92000105565769,  "longitude": 107.61767160657425, 
     "name": "Museum Mainan",
     "address": "No., Jl. Sunda No.39, Kb. Pisang, Kec. Sumur Bandung, Kota Bandung, Jawa Barat 40112",
     "image": "https://assets.promediateknologi.id/crop/0x0:0x0/750x500/webp/photo/ayobandung/images-bandung/post/articles/2019/07/07/57016/img_20190707_15406.jpg"},

     {"latitude": -6.927023965504342,   "longitude": 107.62832640558858, 
     "name": "Museum Virajati Seskoad",
     "address": "Jl. Gatot Subroto No.96, Lkr. Sel., Kec. Lengkong, Kota Bandung, Jawa Barat 40263",
     "image": "https://museum.co.id/wp-content/uploads/2020/09/download-2021-08-22T162106.067.jpeg"},

     {"latitude": -6.940516596341998, "longitude": 107.67250289125126, 
     "name": "Museum Nike Ardilla",
     "address": "Komp. Arya Graha, Jl. Aria Utama No.5, Cipamokolan, Kec. Rancasari, Kota Bandung, Jawa Barat 40292",
     "image": "https://lh5.googleusercontent.com/p/AF1QipPXUZ0CLhzq163gHIgKWgEAe5PcmuRpBWkbUE3O=w408-h306-k-no"},

     {"latitude": -6.935605107690772,  "longitude": 107.66225219865223, 
     "name": "Hall Of Fame Jawa Barat - Panggung Inohong",
     "address": "Gedung BAPUSIPDA, Jl. Kawaluyaan Indah IV No.1 Lantai 1, Jatisari, Kec. Buahbatu, Kota Bandung, Jawa Barat 40286",
     "image": "https://lh5.googleusercontent.com/p/AF1QipPK8J6FE5mHNKetznlO2U-tSCdDagwbdmDBf4fv=w408-h306-k-no"},

     {"latitude": -6.85973157131936, "longitude": 107.59417885915715,    
     "name": "Museum Pendidikan Nasional UPI",
     "address": "Jl. Dr. Setiabudi No.229, Isola, Kec. Sukasari, Kota Bandung, Jawa Barat 40154",
     "image": "https://lh5.googleusercontent.com/p/AF1QipMBIctfeE6d8j6-jZ7QL6NvzYuApw71i3KYm-DV=w408-h306-k-no"},

     {"latitude": -6.913356428978398,  "longitude": 107.60810346317106,    
     "name": "Gedung Indonesia Menggugat",
     "address": "JL Perintis Kemerdekaan, No. 5, Babakan Ciamis, Sumurbandung, Babakan Ciamis, Kec. Sumur Bandung, Kota Bandung, Jawa Barat 40117",
     "image": "https://lh5.googleusercontent.com/p/AF1QipMaQKLfzM5hDxLB9ORMHlZToASSYuukGdKE96ja=w408-h272-k-no"},

     {"latitude": -6.893294226461702, "longitude": 107.6185620257531,      
     "name": "Monumen Perjuangan Rakyat Jawa Barat",
     "address": "Jl. Dipati Ukur No.48, Lebakgede, Kecamatan Coblong, Kota Bandung, Jawa Barat 40132",
     "image": "https://lh5.googleusercontent.com/p/AF1QipMxGYh69Md6g6xtTs1JNBCPECMLlUyzzvqLE6l6=w408-h265-k-no"},

    {"latitude": -6.916862623547986,  "longitude": 107.68209543135592,      
     "name": "Bumi Pakarang Sasuhunan",
     "address": "Jl. Pirus Galuh I No.5, Cisaranten Kulon, Kec. Arcamanik, Kota Bandung, Jawa Barat 40293",
     "image": "https://streetviewpixels-pa.googleapis.com/v1/thumbnail?panoid=p0Qi80FAEze8_3PShc-qxQ&cb_client=search.gws-prod.gps&w=408&h=240&yaw=273.6417&pitch=0&thumbfov=100"},

     {"latitude": -6.8992179167488565,   "longitude": 107.60008287179168,      
     "name": "Museum Biofarma",
     "address": "4H2X+6X8, Pasteur, Sukajadi, Bandung City, West Java 40161",
     "image": "https://lh5.googleusercontent.com/p/AF1QipPKgaycqT0smkD8etZc58U4Pdkz78SYwMEY0lf8=w426-h240-k-no"}
     
]

@maps_bp.route('/lokasi')
def lokasi_view():
    return jsonify(lokasi)

@maps_bp.route('/maps')
def maps():
    return render_template('maps.html')





