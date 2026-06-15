from flask import Flask, render_template, request, jsonify
from core.image_stego.lsb.basic_lsb import embed, extract
from metrics.psnr import calculate_psnr
from metrics.ssim import calculate_ssim
from steganalysis.statistical.chi_square import analyze
import os

app = Flask(__name__)

UPLOAD_FOLDER = "web/static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/embed", methods=["POST"])
def embed_route():
    image = request.files["image"]
    message = request.form["message"]

    input_path = os.path.join(UPLOAD_FOLDER, image.filename)
    output_name = "stego_" + image.filename
    output_path = os.path.join(UPLOAD_FOLDER, output_name)

    image.save(input_path)

    embed(input_path, message, output_path)

    psnr_value = calculate_psnr(input_path, output_path)
    ssim_value = calculate_ssim(input_path, output_path)

    return jsonify({
        "status": "success",
        "stego_image": output_name,
        "psnr": round(psnr_value, 2),
        "ssim": round(ssim_value, 4)
    })

@app.route("/extract", methods=["POST"])
def extract_route():
    image = request.files["image"]

    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(image_path)

    secret_message = extract(image_path)
    analysis = analyze(image_path)

    return jsonify({
        "message": secret_message,
        "chi_square": analysis["chi_square"],
        "p_value": analysis["p_value"]
    })