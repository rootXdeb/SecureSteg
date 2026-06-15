# SecureSteg

## Overview

SecureSteg is a cybersecurity-focused web application that demonstrates how information can be secretly embedded inside digital images using Least Significant Bit (LSB) steganography. The project combines secure data concealment, image quality evaluation, and basic steganalysis techniques within a simple web interface.

Unlike traditional encryption, where the existence of a message is visible, steganography hides the presence of the message itself. SecureSteg allows users to explore both sides of this concept: hiding information and detecting whether an image may contain hidden content.

---

## Problem Statement

In many situations, protecting sensitive information requires more than encryption alone. Encrypted files clearly indicate that protected data exists, which can attract unwanted attention.

The challenge is to securely conceal information within ordinary digital media while maintaining image quality and providing methods to analyze whether hidden data may be present. SecureSteg addresses this challenge by implementing image-based steganography and integrating statistical steganalysis techniques to evaluate suspicious images.

---

## Objectives

The primary objective of SecureSteg is to provide a practical platform for studying and demonstrating steganography concepts in cybersecurity.

The project aims to:

* Hide secret messages inside images using LSB steganography.
* Extract hidden information from stego-images.
* Measure the impact of data embedding on image quality.
* Detect potential hidden content using statistical steganalysis.
* Provide an interactive web-based environment for learning and experimentation.

---

## Key Features

### LSB Image Steganography

Embeds secret text messages into image pixels using the Least Significant Bit technique while preserving the visual appearance of the image.

### Secret Message Extraction

Recovers hidden messages from stego-images accurately and efficiently.

### Image Quality Analysis

Evaluates image distortion after data embedding using:

* PSNR (Peak Signal-to-Noise Ratio)
* SSIM (Structural Similarity Index)

These metrics help determine how closely the stego-image resembles the original image.

### Statistical Steganalysis

Performs Chi-Square analysis on images to identify patterns that may indicate the presence of hidden information.

### Web-Based Interface

Provides a simple dashboard where users can upload images, hide messages, extract data, and view analysis results without requiring command-line interaction.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/rootXdeb/SecureSteg.git
cd SecureSteg
```

### Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Start the Application

```bash
python app.py
```

The application will start on:

```text
http://127.0.0.1:5000
```

### Hide a Secret Message

1. Open the web application.
2. Upload a cover image.
3. Enter the secret message.
4. Click the embed option.
5. Download or view the generated stego-image.
6. Review the PSNR and SSIM values to assess image quality.

### Extract a Hidden Message

1. Upload a stego-image.
2. Run the extraction process.
3. View the recovered secret message.
4. Examine the Chi-Square and p-value results for steganalysis insights.

---

## Educational Value

SecureSteg serves as a practical learning project for students and cybersecurity enthusiasts interested in steganography, digital forensics, covert communication, image analysis, and introductory steganalysis techniques. It demonstrates how hidden communication works while also highlighting methods used to detect concealed information.
