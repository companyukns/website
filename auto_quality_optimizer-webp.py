#!/usr/bin/env python3
import os
import subprocess
import shutil
from PIL import Image
import numpy as np
from skimage.metrics import structural_similarity as ssim

# --- KONFIGURATION ---
SOURCE_FOLDER = 'images'
OUTPUT_FOLDER = 'optimized_images'

# Ziel-SSIM (Structural Similarity). 1.0 = identisch.
# 0.98 ist ein sehr hoher Wert, der "visuell kaum zu unterscheiden" bedeutet.
# Senken Sie den Wert leicht (z.B. auf 0.96), um noch kleinere Dateien zu erhalten.
TARGET_SSIM = 0.98

# Suchbereich für die Qualität.
MIN_QUALITY = 40
MAX_QUALITY = 95

# Kompressionsmethode (0-6). 6 ist am langsamsten, erzeugt aber die kleinsten Dateien.
WEBP_METHOD = 6
# --- ENDE DER KONFIGURATION ---

def is_tool_installed(name):
    """Prüft, ob ein Kommandozeilen-Tool im System-PATH verfügbar ist."""
    return shutil.which(name) is not None

def calculate_ssim(img1_path, img2_path):
    """Berechnet den SSIM-Wert zwischen zwei Bildern."""
    try:
        # Bilder laden und in Graustufen konvertieren (Standard für SSIM)
        img1 = Image.open(img1_path).convert('L')
        img2 = Image.open(img2_path).convert('L')
        
        # Sicherstellen, dass die Bilder die gleiche Größe haben
        if img1.size != img2.size:
            img2 = img2.resize(img1.size, Image.Resampling.LANCZOS)

        img1_arr = np.array(img1)
        img2_arr = np.array(img2)
        
        return ssim(img1_arr, img2_arr, data_range=img2_arr.max() - img2_arr.min())
    except Exception as e:
        print(f"  [Warnung] Konnte SSIM nicht berechnen: {e}")
        return 0

def auto_optimize_images():
    """Findet für jedes Bild die optimale WebP-Qualität und komprimiert es."""
    if not is_tool_installed('cwebp'):
        print("✗ FEHLER: 'cwebp' wurde nicht gefunden. Bitte installieren Sie die WebP-Tools.")
        return

    print(f"✓ 'cwebp' gefunden. Starte automatische Optimierung mit Ziel-SSIM >= {TARGET_SSIM}")

    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    total_savings = 0
    image_count = 0

    for filename in os.listdir(SOURCE_FOLDER):
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        input_path = os.path.join(SOURCE_FOLDER, filename)
        file_root = os.path.splitext(filename)[0]
        output_path = os.path.join(OUTPUT_FOLDER, f"{file_root}.webp")
        temp_path = os.path.join(OUTPUT_FOLDER, 'temp.webp')

        print(f"\nVerarbeite '{filename}'...")

        # --- Binäre Suche nach der optimalen Qualität ---
        low = MIN_QUALITY
        high = MAX_QUALITY
        best_quality = MAX_QUALITY
        
        while low <= high:
            quality = (low + high) // 2
            
            # Temporäre WebP-Datei mit der aktuellen Qualität erstellen
            cmd = ['cwebp', '-q', str(quality), '-m', str(WEBP_METHOD), input_path, '-o', temp_path]
            subprocess.run(cmd, capture_output=True, check=True)
            
            # SSIM-Wert berechnen
            current_ssim = calculate_ssim(input_path, temp_path)
            
            print(f"  -> Teste Qualität {quality}... SSIM: {current_ssim:.4f}", end='\r')

            if current_ssim >= TARGET_SSIM:
                # Qualität ist gut genug, versuchen wir eine niedrigere (kleinere Datei)
                best_quality = quality
                high = quality - 1
            else:
                # Qualität ist zu schlecht, wir brauchen eine höhere
                low = quality + 1
        
        print() # Neue Zeile nach den Tests

        # --- Finale Komprimierung mit der besten gefundenen Qualität ---
        final_cmd = ['cwebp', '-q', str(best_quality), '-m', str(WEBP_METHOD), '-mt', '-sharp_yuv', input_path, '-o', output_path]
        subprocess.run(final_cmd, capture_output=True, check=True)
        
        # Aufräumen
        if os.path.exists(temp_path):
            os.remove(temp_path)

        original_size = os.path.getsize(input_path)
        optimized_size = os.path.getsize(output_path)
        savings = original_size - optimized_size
        total_savings += savings
        image_count += 1

        original_kb = original_size / 1024
        optimized_kb = optimized_size / 1024
        savings_percent = (savings / original_size) * 100 if original_size > 0 else 0

        print(f"✓ Optimal! '{filename}' ({original_kb:.1f} KiB) -> '{os.path.basename(output_path)}' ({optimized_kb:.1f} KiB)")
        print(f"  Beste Qualität gefunden: {best_quality} | Ersparnis: {savings_percent:.1f}%")

    if image_count > 0:
        total_savings_kb = total_savings / 1024
        print("\n--- Zusammenfassung ---")
        print(f"Anzahl optimierter Bilder: {image_count}")
        print(f"Gesamte Dateigrößen-Einsparung: {total_savings_kb:.1f} KiB")
    else:
        print("\nKeine passenden Bilder im Quellordner gefunden.")

if __name__ == "__main__":
    auto_optimize_images()