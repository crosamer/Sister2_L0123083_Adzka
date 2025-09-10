import os

# Folder tempat menyimpan file dummy
OUTPUT_DIR = "files"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_file(filename, size_kb):
    target_size = size_kb * 1024  # konversi KB ke byte
    
    # kerangka HTML dasar
    header = "<html><body>\n"
    footer = "\n</body></html>"
    
    # hitung berapa banyak filler 'x' yang dibutuhkan
    filler_size = target_size - (len(header) + len(footer))
    if filler_size < 0:
        raise ValueError("Ukuran terlalu kecil untuk membuat file HTML")
    
    content = header + ("x" * filler_size) + footer
    
    # simpan file
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w") as f:
        f.write(content)
    print(f"{filename} berhasil dibuat dengan ukuran ~{size_kb}KB")

# daftar ukuran file yang mau dibuat
sizes = [
    (10, "file_10kb.html"),
    (100, "file_100kb.html"),
    (1024, "file_1mb.html"),
    (5 * 1024, "file_5mb.html"),
    (10 * 1024, "file_10mb.html"),
]

# generate semua file
for size, name in sizes:
    generate_file(name, size)
