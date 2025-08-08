from app.tasks import film_analysis, court_cases, csv_report

async def handle_request(questions_file, other_files):
    qtext = (await questions_file.read()).decode("utf-8")

    if "highest grossing films" in qtext.lower():
        return await film_analysis.process(qtext, other_files)

    elif "high court" in qtext.lower():
        return await court_cases.process(qtext, other_files)

    elif any(f.filename.endswith(".csv") for f in other_files):
        return await csv_report.process(qtext, other_files)

    return {"error": "Unknown or unsupported task"}
