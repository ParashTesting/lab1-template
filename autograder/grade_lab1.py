import fitz, json, os

def extract_text(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text("text")
    return text.lower()

def grade_lab1(text):
    score = {"part2": 0, "part3": 0, "part4": 0}
    total = 0

    if "hello world from an ide" in text:
        score["part2"] = 2
        total += 2

    if "hello world from the command line" in text:
        score["part3"] = 2
        total += 2

    keywords = ["semicolon", "main method", "static", "private", "string[] args", "system"]
    found = sum(1 for k in keywords if k in text)
    score["part4"] = found
    total += found

    score["total"] = total
    return score

def main():
    pdf = "Lab1.pdf"
    if not os.path.exists(pdf):
        print("❌ Missing Lab1.pdf")
        return

    text = extract_text(pdf)
    result = grade_lab1(text)

    print(f"✅ Total Score: {result['total']} / 10")
    print(json.dumps(result, indent=2))

    with open("results.json", "w") as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()
