text = """
Our data analyst course lasts for six months. 
Students get access to all recorded classes. 
Live classes happen from Monday to Friday. 
Refund requests are accepted within 7 days of purchase. 
Students must complete all assignments before placement.
Eligible students receive minimum 3 interview opportunities.
"""

lines = text.strip().split("\n")

chunks = []

for x in range(0, len(lines), 2):
    chunk = " ".join(lines[x:x+2])
    chunks.append(chunk)

print(chunks)
print("=========================================================================================\n")

for chunk in chunks:
    print("CHUNK:")
    print(chunk)
    print()