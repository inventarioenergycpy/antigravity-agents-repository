import urllib.request
import zipfile
import shutil
from pathlib import Path

DEST_DIR = Path(r"D:\Usuarios\jidiaz\.gemini\antigravity-ide\scratch\antigravity-agents-repository\scripts")
FFMPEG_EXE = DEST_DIR / "ffmpeg.exe"

def setup():
    if FFMPEG_EXE.exists():
        print(f"[OK] ffmpeg.exe ya existe en: {FFMPEG_EXE}")
        return str(FFMPEG_EXE)
        
    print("Descargando compilación de ffmpeg para Windows...")
    url = "https://github.com/yt-dlp/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
    zip_path = DEST_DIR / "ffmpeg.zip"
    
    urllib.request.urlretrieve(url, zip_path)
    print("Extrayendo ffmpeg.exe...")
    
    with zipfile.ZipFile(zip_path, 'r') as z:
        for member in z.namelist():
            if member.endswith("ffmpeg.exe"):
                with z.open(member) as source, open(FFMPEG_EXE, "wb") as target:
                    shutil.copyfileobj(source, target)
                break
                
    if zip_path.exists():
        zip_path.unlink()
        
    print(f"[OK] ffmpeg.exe listo en: {FFMPEG_EXE}")
    return str(FFMPEG_EXE)

if __name__ == "__main__":
    setup()
