const embedForm = document.getElementById("embedForm");
const extractForm = document.getElementById("extractForm");

embedForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new FormData(embedForm);

    const response = await fetch("/embed", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    document.getElementById("embedResult").innerHTML = `
        <div class="result-box">
            <h3>Payload Embedded Successfully</h3>

            <div class="metrics-grid">
                <div class="metric-card">
                    <span>PSNR</span>
                    <strong>${data.psnr}</strong>
                </div>

                <div class="metric-card">
                    <span>SSIM</span>
                    <strong>${data.ssim}</strong>
                </div>
            </div>

            <img src="/static/uploads/${data.stego_image}">

            <a href="/static/uploads/${data.stego_image}" download>
                <button class="download-btn">
                    Download Stego Asset
                </button>
            </a>
        </div>
    `;
});

extractForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new FormData(extractForm);

    const response = await fetch("/extract", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    document.getElementById("extractResult").innerHTML = `
        <div class="result-box">
            <h3>Threat Intelligence Recovered</h3>

            <div class="message-box">
                ${data.message}
            </div>

            <div class="metrics-grid">
                <div class="metric-card">
                    <span>Chi-Square</span>
                    <strong>${data.chi_square}</strong>
                </div>

                <div class="metric-card">
                    <span>P-Value</span>
                    <strong>${data.p_value}</strong>
                </div>
            </div>
        </div>
    `;
});