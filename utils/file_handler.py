def save(text_):
    with open("data/output.txt", "w", encoding="utf-8") as doc:
        doc.save()
    return "Text saved successfully"
