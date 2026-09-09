from pathlib import Path
import qrcode

root = Path(__file__).parent
url = (root / "site_url.txt").read_text(encoding="utf-8").strip()
img = qrcode.make(url)
img.save(root / "qr_code.png")
print("QR code updated for:", url)
