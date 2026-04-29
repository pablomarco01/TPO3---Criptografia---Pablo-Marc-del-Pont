import hashlib

textos = [
    "Juro solemnemente que mis intenciones no son buenas",
    "Juro solemnemente que mis intenciones no son buenas.",
    "Juro solemnemente que mis intenciones no son Buenas",
    "juro solemnemente que mis intenciones no son buenas",
    "Juro solemnemente que mis intenciones no son malas",
]

print("SHA-256 hashes:")
for t in textos:
    h = hashlib.sha256(t.encode()).hexdigest()
    print(f"  [{t[:50]}]")
    print(f"  => {h}\n")